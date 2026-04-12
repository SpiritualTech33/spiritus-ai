# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Cada entrada es un commit
Aqui uso un sistema de SnapShot. Tomo una foto del repo antes de hacer los cambios y los guardo en memoria de ClaudeCode o Gemini. Despues les digo que compare la repo despues del commit y registre los cambios en el Changelog

---

## [0.0.2] — 2026-04-11 — Visual Sanctuary

> *Sophia begins to see her own reflection.*

### Changed
- **Refined Landing Page (`docs/index.html`)** — Redesigned for a minimalist, "soul-oriented" aesthetic using deep blacks and gold accents.
- **Narrative Flow Update** — Reorganized the landing page to follow the path: SpiritusAI (Vision) → Sophia (Intelligence) → SophiaEngine (Source).
- **Integrated Visuals** — Added high-quality project images for the SpiritusAI logo, Sophia Aura, and Sophia Engine.
- **Interactive Aesthetics** — Implemented an ambient particle system and scroll-reveal transitions to enhance the user experience.

### Removed
- **Redundant Prototypes** — Deleted older HTML versions and local image assets (`docs/prototype/`, `docs/sophia_image.jpg`, etc.) to favor GitHub-hosted assets.
- **Local Assets** — Removed local `favicon.svg` and `sophia_image.jpg` as the project transition to centralized image hosting.

---

## [0.0.1] — 2026-04-11 — The Separation

> *The vault deserved its own home.*

### Added
- New `README.md` — introduces spiritus-ai as a multi-model platform (Sophia, Nous, Logos), links to SophiaEngine repo, includes project images
- `CHANGELOG.md` — this file, tracking the project from day one

### Changed
- **SophiaEngine moved to independent repository** — the vault is now at [github.com/SpiritualTech33/SophiaEngine](https://github.com/SpiritualTech33/SophiaEngine), no longer nested inside spiritus-ai
- `CORPUS_PATH` updated from `./SophiaEngine` to `../SophiaEngine` in `.env` and `.env.example`
- `.gitignore` cleaned — removed SophiaEngine-specific entries
- `9 Phase Plan.md` updated — all SophiaEngine references now reflect the independent repo architecture, GitHub Action rewritten as cross-repo dispatch

### Architecture Decision
SophiaEngine (knowledge) and spiritus-ai (application) are now two separate repos. The vault grows independently. The RAG pipeline reads from it via `CORPUS_PATH`. Clean separation of concerns — the library got its own building.

