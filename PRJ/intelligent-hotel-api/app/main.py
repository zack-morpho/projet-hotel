from fastapi import FastAPI
from app.routes import availability, optimize, agencies
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Intelligent Hotel Management System",
    description="API FastAPI pour la prédiction de l’occupation et la tarification",
    version="1.0.0"
)
origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "Bienvenue sur l'API RMS.AI ",
        "routes_disponibles": [
            "/predict/availability",
            "/predict/optimal",
            "/predict/agency/{agency_id}"
        ],
        "documentation": "/docs"
    }

app.include_router(availability.router, prefix="/predict")
app.include_router(optimize.router, prefix="/predict")
app.include_router(agencies.router, prefix="/predict")
