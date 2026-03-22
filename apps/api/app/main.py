from fastapi import FastAPI

# Application FastAPI minimale.
# Ce fichier servira de point d'entrée principal pour l'API web.
app = FastAPI(
    title="stock-quant-oop-gui API",
    version="0.1.0",
)

@app.get("/api/v1/health")
def health() -> dict:
    """
    Endpoint de santé minimal.
    Le GUI s'en servira pour vérifier que l'API répond.
    """
    return {
        "status": "ok",
        "service": "stock-quant-oop-gui-api",
    }
