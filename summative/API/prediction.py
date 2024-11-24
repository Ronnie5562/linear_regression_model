import pickle
import pandas as pd
from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware


with open('../linear_regression/prediction.pkl', 'rb') as file:
    model = pickle.load(file)


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


class CaloriesPrediction(BaseModel):
    Gender: Literal["Male", "Female"] = Field(...)
    Age: int = Field(..., gt=0, lt=150)
    Heart_Rate: float = Field(..., gt=0, lt=500)
    Body_Temp: float = Field(..., gt=10, lt=50)
    Height: float = Field(..., gt=0, lt=3, description="Height in meters")
    Weight: float = Field(..., gt=0, lt=500, description="Weight in kilograms")
    Duration: float = Field(..., gt=0, lt=300, description="Duration in minutes")

    def calculate_bmi_x_duration(self):
        bmi = self.Weight / (self.Height ** 2)
        bmi_x_duration = bmi * self.Duration
        return bmi_x_duration


@app.post("/predict/")
async def predict(data: CaloriesPrediction):
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

# Run the API with the command below:
# uvicorn prediction:app --reload
