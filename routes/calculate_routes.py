from fastapi import APIRouter,Depends
from modules.models import SimulationInput, ROFiltrationRequest, SoilContaminationRequest
from modules.calculation import calculate_ro_filtration, calculate_soil_contamination
from modules import data_processing
from modules.ml_models import load_soil_module

# Load the machine learning model and scaler
soil_model, soil_scaler = load_soil_module()
router = APIRouter()

@router.post("/calculate")
async def calculate_simulation(input_data: SimulationInput):
    """
    Calculate the sum of the input data
    :param input_data: SimulationInput
    :return: Dictionary with the calculated sum
    """
    return calculate_simulation(input_data)

@router.post("/calculate_ro_filtration")
def calculate_ro_filtration_pass(params: ROFiltrationRequest):
    """
    Calculate the reverse osmosis filtration based on the input parameters
    :param params: ROFiltrationRequest
    :return: Dictionary with the calculated reverse osmosis filtration
    """
    return calculate_ro_filtration(params)

@router.get("/predict_voltage/{soil_quantity}")
async def predict_voltage(soil_quantity: int):
    """
    Predict voltage based on soil quantity.

    Args:
        soil_quantity (int): The quantity of soil.

    Returns:
        dict: The predicted voltage.
    """
    return data_processing.voltage_calculation(soil_quantity)

@router.post("/calculate_soil_contamination")
def calculate_soil_contamination_pass(params: SoilContaminationRequest, soil_model=soil_model, soil_scaler=soil_scaler):
    """
    Calculate the soil contamination based on the input parameters
    :param params: SoilContaminationRequest
    :param soil_model: The loaded machine learning model for soil contamination
    :param soil_scaler: The scaler used for preprocessing soil data
    :return: Dictionary with the calculated soil contamination
    """
    return calculate_soil_contamination(params, soil_model, soil_scaler)
