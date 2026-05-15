from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect
)

from app.services.websocket_manager import manager

router = APIRouter(
    tags=["Live Tracking"]
)

@router.websocket("/ws/live-tracking")
async def websocket_endpoint(
    websocket: WebSocket
):

    await manager.connect(websocket)

    try:

        while True:

            data = await websocket.receive_json()

            await manager.broadcast(data)

    except WebSocketDisconnect:

        manager.disconnect(websocket)