import importlib.util
import json
import os
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[2]
EXPECTED_TIMEOUT_SECONDS = 15
NETWORK_RUNNER_PATHS = [
    "skills-catalog/packages/bilibili-sentiment-dashboard/scripts/run.py",
    "skills-catalog/packages/douyin-hotlist-overall/scripts/run.py",
    "skills-catalog/packages/douyin-kol-search/scripts/run.py",
    "skills-catalog/packages/douyin-realtime-hot-rise/scripts/run.py",
    "skills-catalog/packages/douyin-sentiment-dashboard/scripts/run.py",
    "skills-catalog/packages/douyin-traffic-dashboard/scripts/run.py",
    "skills-catalog/packages/kuaishou-sentiment-dashboard/scripts/run.py",
    "skills-catalog/packages/xhs-sentiment-dashboard/scripts/run.py",
]


class DummyResponse:
    def __init__(self, payload):
        self._payload = payload

    def read(self):
        return json.dumps(self._payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


def load_runner_module(relative_path: str):
    module_path = REPO_ROOT / relative_path
    module_name = relative_path.replace("/", "_").replace(".", "_")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class RunnerSecurityTests(unittest.TestCase):
    def test_network_runners_use_explicit_timeout(self):
        for relative_path in NETWORK_RUNNER_PATHS:
            with self.subTest(runner=relative_path):
                module = load_runner_module(relative_path)
                with patch.dict(os.environ, {"AISKILLS_API_KEY": "test-api-key"}, clear=False):
                    with patch.object(
                        module.urllib.request,
                        "urlopen",
                        return_value=DummyResponse({"success": True, "data": {"result": []}}),
                    ) as mock_urlopen:
                        with patch("builtins.print"):
                            module.request_json("POST", "/api/test", {"ping": True})

                self.assertEqual(
                    mock_urlopen.call_args.kwargs.get("timeout"),
                    EXPECTED_TIMEOUT_SECONDS,
                    f"{relative_path} should set an explicit network timeout",
                )

    def test_network_runners_convert_url_errors_to_structured_failures(self):
        for relative_path in NETWORK_RUNNER_PATHS:
            with self.subTest(runner=relative_path):
                module = load_runner_module(relative_path)
                with patch.dict(os.environ, {"AISKILLS_API_KEY": "test-api-key"}, clear=False):
                    with patch.object(
                        module.urllib.request,
                        "urlopen",
                        side_effect=urllib.error.URLError("connection refused"),
                    ):
                        with patch("builtins.print") as mock_print:
                            caught = None
                            try:
                                module.request_json("POST", "/api/test", {"ping": True})
                            except BaseException as exc:  # noqa: BLE001
                                caught = exc

                self.assertIsInstance(
                    caught,
                    SystemExit,
                    f"{relative_path} should exit cleanly on network errors",
                )
                self.assertEqual(getattr(caught, "code", None), 1)
                self.assertTrue(mock_print.called, f"{relative_path} should print a structured error payload")
                printed_payload = mock_print.call_args.args[0]
                parsed = json.loads(printed_payload)
                self.assertEqual(parsed["success"], False)
                self.assertEqual(parsed["error"]["code"], "NETWORK_ERROR")


if __name__ == "__main__":
    unittest.main()
