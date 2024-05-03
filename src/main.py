from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
import pandas as pd
import pickle, uvicorn, os

app = FastAPI()

# Define filepath for ml_components.pkl
ML_COMPONENTS_FILEPATH = os.path.join("assets", "ml", "ml_components.pkl")

# Load machine learning model and other components
with open(ML_COMPONENTS_FILEPATH, "rb") as file:
    ml_components = pickle.load(file)

# preprocessor = ml_components["preprocessor"]
pipeline = ml_components["pipeline"]


class DeviceSpecs(BaseModel):
    """
    Device specifications.

    - battery_power: Total energy a battery can store in one time measured in mAh
    - blue: Has Bluetooth or not (0 for False, 1 for True)
    - clock_speed: The speed at which the microprocessor executes instructions
    - dual_sim: Has dual sim support or not (0 for False, 1 for True)
    - fc: Front Camera megapixels
    - four_g: Has 4G or not (0 for False, 1 for True)
    - int_memory: Internal Memory in Gigabytes
    - m_dep: Mobile Depth in cm
    - mobile_wt: Weight of mobile phone
    - n_cores: Number of cores of the processor
    - pc: Primary Camera megapixels
    - px_height: Pixel Resolution Height
    - px_width: Pixel Resolution Width
    - ram: Random Access Memory in Megabytes
    - sc_h: Screen Height of mobile in cm
    - sc_w: Screen Width of mobile in cm
    - talk_time: longest time that a single battery charge will last when you are
    - three_g: Has 3G or not (0 for False, 1 for True)
    - touch_screen: Has touch screen or not (0 for False, 1 for True)
    - wifi: Has wifi or not (0 for False, 1 for True)
    """

    battery_power: float
    blue: int
    clock_speed: float
    dual_sim: int
    fc: float
    four_g: int
    int_memory: float
    m_dep: float
    mobile_wt: float
    n_cores: float
    pc: float
    px_height: float
    px_width: float
    ram: float
    sc_h: float
    sc_w: float
    talk_time: float
    three_g: int
    touch_screen: int
    wifi: int

    @validator("blue", "dual_sim", "four_g", "three_g", "touch_screen", "wifi")
    def validate_boolean(cls, v):
        # Ensure the values are either 0 or 1
        if v not in (0, 1):
            raise ValueError("Value must be 0 or 1")
        return v


@app.post("/predict/{device_id}")
async def predict_price(device_id: int, specs: DeviceSpecs):
    """
    Predict the price of a device based on its specifications.

    Args:
        device_id (int): The ID of the device.
        specs (DeviceSpecs): The device specifications.

    Returns:
        dict: A dictionary containing the input data and predicted price.
    """
    try:
        # Preprocess the data
        data = pd.DataFrame([{"device_id": device_id, **specs.dict()}])

        # Predict price
        data["predicted_price"] = pipeline.predict(data)

        print(f"\n{data.to_markdown()}\n")

        # Return input data and predicted price
        return data.to_dict("records")
    except Exception as e:
        print(f"{e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
