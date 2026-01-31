from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="NEXA Trading",
    description="NEXA Trading Web App",
    version="1.0.0"
)

# Ruhusu frontend (browser / app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "ok",
        "app": "NEXA Trading",
        "message": "NEXA Trading backend is running successfully"
    }

@app.get("/health")
def health():
    return {"health": "good"}