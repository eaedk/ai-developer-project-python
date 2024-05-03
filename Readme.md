# Devices Price Prediction API

This API predicts the price range of a mobile device based on its specifications. [Go to the deployed API](https://huggingface.co/spaces/eaedk/DevicesPricePredictionAPI)

This README section provides an overview of the repository structure, details about the machine learning part, setup instructions, and information on interacting with the API and running tests.

## Repository Tree

```
.
├── Readme.md
├── assets
│   ├── data
│   ├── img
│   └── ml
│       └── ml_components.pkl
├── command.txt
├── notebooks
│   └── ML_Step_By_Step_AI_Developer.ipynb
├── requirements.txt
├── requirements_from_colab.txt
├── src
│   └── main.py
└── tests
    └── test_api_predict.py

8 directories, 8 files
```

## Machine Learning Part

The machine learning part of this project was conducted using a Jupyter Notebook located in the `notebooks` directory. The notebook `test.ipynb` contains the following details:

- **Best Model**: Linear Regression achieved the best result.
- **Optimal Parameters**: The best parameters for the Linear Regression model are:
  - `classifier__C`: 200
  - `classifier__max_iter`: 300
  - `preprocessor__numerical__num_imputer__strategy`: 'mean'
- **Dataset Split**: 80% of the training dataset was used for training the model.
- **Performance Metrics**:
  - Accuracy: 97.75%
  - F1-score: 0.977

The machine learning model was serialized using pickle and saved as `ml_components.pkl` in the `assets/ml` directory.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/devices-price-prediction-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd devices-price-prediction-api
   ```

3. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - Windows:

     ```bash
     venv\Scripts\activate
     ```

   - macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Ensure you have the necessary ML components file (`ml_components.pkl`) in the `assets/ml` directory.

2. Start the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

   The application will start running on `http://localhost:8000`.

## Interacting with the API

- **Predict Price Endpoint**:
  - **Endpoint**: `/predict/{device_id}`
  - **Method**: POST
  - **Description**: Predicts the price range of a device based on its specifications.
  - **Request Body**:
    ```json
    {
        "battery_power": 2000,
        "blue": 1,
        "clock_speed": 2.5,
        ...
    }
    ```
  - **Response**:
    ```json
    [
      {
        "device_id": 1,
        "predicted_price": 2
      }
    ]
    ```

Replace `{device_id}` with the ID of the device you want to predict the price for.

## Testing

To ensure the correctness of the API functionality, tests are provided using `pytest`. Follow these steps to run the tests:

1. Open a terminal.

2. Navigate to the project directory.

3. Activate the virtual environment (if not already activated).

4. Run the following command to execute the tests:

   ```bash
   pytest tests/test_api_predict.py
   ```

   This command will run the tests defined in `tests/test_api_predict.py`.

   Ensure that the FastAPI application is running before executing the tests with `pytest`.

## Documentation

For detailed documentation of the API endpoints, navigate to `http://localhost:8000/docs` when the application is running.
