from fastapi import APIRouter

router =APIRouter(prefix="/api/agents",
    tags=["Agents"],)

@router.get("/api/agent")
def agent_call():
    return {
        "status":"calling from agent enpoint"
    }