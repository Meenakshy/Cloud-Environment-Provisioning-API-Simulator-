from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from sqlmodel import Session, select
from app.models import Environment
from app.schemas import EnvironmentCreate, EnvironmentRead
from app.database import get_session
import asyncio

router = APIRouter(prefix="/environments", tags=["Environments"])

async def simulate_provisioning(env_id: int, session: Session):
    await asyncio.sleep(5)
    env = session.get(Environment, env_id)
    if env:
        env.status = "active"
        session.add(env)
        session.commit()

@router.post("/", response_model=EnvironmentRead)
async def create_environment(
    data: EnvironmentCreate,
    background_tasks: BackgroundTasks,
    session: Session = Depends(get_session)
):
    env = Environment(**data.dict())
    session.add(env)
    session.commit()
    session.refresh(env)
    background_tasks.add_task(simulate_provisioning, env.id, session)
    return env

@router.get("/", response_model=list[EnvironmentRead])
async def list_environments(session: Session = Depends(get_session)):
    envs = session.exec(select(Environment)).all()
    return envs

@router.get("/{env_id}", response_model=EnvironmentRead)
async def get_environment(env_id: int, session: Session = Depends(get_session)):
    env = session.get(Environment, env_id)
    if not env:
        raise HTTPException(status_code=404, detail="Environment not found")
    return env

@router.delete("/{env_id}")
async def delete_environment(env_id: int, session: Session = Depends(get_session)):
    env = session.get(Environment, env_id)
    if not env:
        raise HTTPException(status_code=404, detail="Environment not found")
    session.delete(env)
    session.commit()
    return {"message": f"Environment {env_id} deleted"}
