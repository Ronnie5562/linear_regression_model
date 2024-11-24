import pickle
import pandas as pd
from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from summative.linear_regression import merge_files

# Initialize FastAPI app
app = FastAPI(
    title="Calories Prediction API",
    description="API to predict calories burned during exercise",
    version="0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = None

# Function to reassemble the model on startup
@app.on_event("startup")
def reassemble_model():
    global model
    try:
        print("Reassembling model...")
        # Merge the model chunks
        merge_files.merge_files(
            "prediction.pkl",
            "summative/linear_regression/model_split"
        )
        print("Model reassembled successfully.")
    except FileNotFoundError:
        print("Model chunks not found. Skipping reassembly.")
        exit()
    except Exception as e:
        print(f"An error occurred while reassembling the model: {e}")
        exit()

    # Load the model once after reassembly
    with open('prediction.pkl', 'rb') as file:
        model = pickle.load(file)
        print("Model loaded successfully.")


# Define the CaloriesPrediction class (Pydantic model)
class CaloriesPrediction(BaseModel):
    Gender: Literal["Male", "Female"] = Field(..., description="Gender of the person")
    Age: int = Field(..., gt=0, lt=150, description="Age of the person")
    Heart_Rate: float = Field(..., gt=0, lt=500, description="Heart rate of the person")
    Body_Temp: float = Field(..., gt=10, lt=50, description="Body temperature of the person")
    Height: float = Field(..., gt=0, lt=3, description="Height in meters")
    Weight: float = Field(..., gt=0, lt=500, description="Weight in kilograms")
    Duration: float = Field(..., gt=0, lt=300, description="Duration in minutes")

    def calculate_bmi_x_duration(self):
        bmi = self.Weight / (self.Height ** 2)
        bmi_x_duration = bmi * self.Duration
        return bmi_x_duration


@app.post("/predict/")
async def predict(data: CaloriesPrediction):
    if model is None:
        return {
            "error": "Model not loaded properly. Please try again later."
        }

    bmi_x_duration = data.calculate_bmi_x_duration()

    input_features = {
        "Gender": int(data.Gender == "Male"),
        "Age": data.Age,
        "Heart_Rate": data.Heart_Rate,
        "Body_Temp": data.Body_Temp,
        "BMI_x_Duration": bmi_x_duration
    }

    features = pd.DataFrame([input_features])
    prediction = model.predict(features)

    return {"predicted_calories": prediction[0]}
