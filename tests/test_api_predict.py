import pytest
import pandas as pd
import requests

# Define base URL for the FastAPI application
BASE_URL = "http://127.0.0.1:8000"

# Define sample device specifications
device_specs = {
    "battery_power": 3000,
    "blue": 1,
    "clock_speed": 2.0,
    "dual_sim": 0,
    "fc": 5.0,
    "four_g": 1,
    "int_memory": 64.0,
    "m_dep": 0.4,
    "mobile_wt": 150.0,
    "n_cores": 8.0,
    "pc": 12.0,
    "px_height": 1920.0,
    "px_width": 1080.0,
    "ram": 4.0,
    "sc_h": 5.5,
    "sc_w": 2.5,
    "talk_time": 10.0,
    "three_g": 1,
    "touch_screen": 1,
    "wifi": 1
}


def test_predict_price():
    """
    Test the predict price endpoint.

    Steps:
    1. Define device specifications and device ID.
    2. Send a POST request to the predict price endpoint with the device specifications.
    3. Validate that the response status code is 200 (OK).
    4. Parse the response JSON and validate that it contains the expected fields.
    5. Print the predicted price.
    """
    # Define device ID
    device_id = 1

    # Send POST request to predict price
    response = requests.post(f"{BASE_URL}/predict/{device_id}", json=device_specs)

    # Check if request was successful (status code 200)
    assert response.status_code == 200

    # Parse response JSON
    data = pd.DataFrame(response.json())

    # Validate response fields
    assert "device_id" in data.columns
    assert "predicted_price" in data.columns

    # Print predicted price
    print(f"Predictions\n{data[['device_id', 'predicted_price']].to_markdown()} ")


if __name__ == "__main__":
    pytest.main()
