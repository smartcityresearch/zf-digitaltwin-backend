from fastapi import APIRouter
from modules import data_processing

router = APIRouter()

@router.post("/waterqualitysub/{table_name}")
async def water_quality_sub(table_name: str, data: dict):
    return data_processing.process_water_quality_sub(table_name, data)

@router.post("/waterlevelsub/{table_name}")
async def water_level_sub(table_name: str, data: dict):
    return data_processing.process_water_level_sub(table_name, data)

@router.post("/motorsub/{table_name}")
async def motor_sub(table_name: str, data: dict):
    return data_processing.process_motor_sub(table_name, data)