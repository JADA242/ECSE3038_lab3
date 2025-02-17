from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List, Optional

app = FastAPI()

tanks = {}

class Tank(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    location: str
    lat: float
    long: float

class TankUpdate(BaseModel):
    location: Optional[str] = None
    lat: Optional[float] = None
    long: Optional[float] = None

@app.get("/tank", response_model=List[Tank])
async def get_tanks():
    return list(tanks.values())

@app.get("/tank/{tank_id}", response_model=Tank)
async def get_tank(tank_id: UUID):
    tank = tanks.get(tank_id)
    if not tank:
        raise HTTPException(status_code=404, detail="Tank not found")
    return tank

@app.post("/tank", status_code=201)
async def create_tank(tank_request: Tank):
    tank_id = uuid4()
    tank = tank_request.model_copy(update={"id": tank_id})
    tanks[tank_id] = tank
    return JSONResponse(content=jsonable_encoder(tank), status_code=201)

@app.patch("/tank/{tank_id}", response_model=Tank)
async def update_tank(tank_id: UUID, tank_update: TankUpdate):
    if tank_id not in tanks:
        raise HTTPException(status_code=404, detail="Tank not found")

    existing_tank = tanks[tank_id]
    update_data = tank_update.model_dump(exclude_unset=True)  

    if not update_data:
        raise HTTPException(status_code=400, detail="At least one field must be provided for update")

    updated_tank = existing_tank.model_copy(update=update_data)  
    tanks[tank_id] = updated_tank  

    return updated_tank

@app.delete("/tank/{tank_id}", status_code=204)
async def delete_tank(tank_id: UUID):
    if tank_id not in tanks:
        raise HTTPException(status_code=404, detail="Tank not found")
    del tanks[tank_id]
    return
