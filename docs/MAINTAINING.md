# Maintaining the visual GitHub profile

The profile is published from `README.md` in the `m-qazi99` repository. GitHub renders linked images and disclosures; it does not run the portfolio's interactive JavaScript.

```bash
python scripts/build_visual.py
```

The build generates the original visual assets and calls `build_showcase.py` last. To regenerate only v2.1 project cards:

```bash
python scripts/build_showcase.py
```

Update `content/live-projects.json` for product versions and review descriptions. Keep public slugs consistent with the portfolio and catalog. `content/search-attribution.md` provides accessible factual text. SVG cards include meaningful alternative text and link to the real live products; source buttons link to code and contribution guides.

Do not publish fake activity, proficiency percentages or technology claims. Existing résumé, experience and skill categories are preserved. Before publishing, check each product/card link and verify the resulting README in GitHub.
