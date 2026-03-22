# stock-quant-oop-gui

Frontend web + API pour piloter le moteur `stock-quant-oop`.

## Objectifs
- rendre les pipelines plus user friendly
- exposer une Web API stable
- permettre un GUI pour refresh, diagnostics, coverage et backtests

## Architecture
- `apps/api`: backend FastAPI
- `apps/web`: frontend web
- `docs`: documentation produit et technique
- `infra`: déploiement local / reverse proxy

## Dépendance principale
Ce projet consomme le moteur quant depuis le repo source `stock-quant-oop`.
