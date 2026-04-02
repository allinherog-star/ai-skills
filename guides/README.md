# Guides Sync Contract

`skills-package/guides` stores GitHub-ready markdown copies of the guides published on the main site.

## Source Of Truth

- Main source: `ai-skills-service/web/content/guides/<locale>/<pillar>/<slug>.md`
- Site rendering: `ai-skills-service/web/src/lib/content/guides.ts`
- Export command: `cd ai-skills-service/web && npm run guides:export -- --locale=zh --pillar=data-insights --slug=douyin-traffic-dashboard-direction-judgment-2026`

## Non-Negotiable Rules

- Do not hand-edit files under `skills-package/guides/<locale>/<pillar>/`.
- Change guide title, summary, cover, links, or body only in `web/content/guides`.
- After any guide content change, rerun the export command so the synced markdown stays aligned.
- Exported markdown rewrites page links to `https://ai-skills.ai/...`.
- Exported guide images are copied into the matching article directory and referenced with relative paths for GitHub compatibility.

## Output Shape

Generated files mirror the site content path, and each article may have a same-name asset directory:

```text
skills-package/guides/<locale>/<pillar>/<slug>.md
skills-package/guides/<locale>/<pillar>/<slug>/
```

Example:

```text
skills-package/guides/zh/data-insights/douyin-traffic-dashboard-direction-judgment-2026.md
skills-package/guides/zh/data-insights/douyin-traffic-dashboard-direction-judgment-2026/
```
