from fastapi import FastAPI
from app.database import init_db
from app.routes import environments

app = FastAPI(title="Cloud Environment Provisioning API (Simulator)")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(environments.router)

@app.get("/health")
def health_check():
    return {"status": "OK"}
