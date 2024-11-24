# Calories Burnt Prediction APP

This project focuses on predicting calories burned during physical activities using machine learning models and a user-friendly API interface. Leveraging a dataset of human activity data, I built and evaluated three predictive models: Linear Regression, Random Forest, and Decision Tree Regressor. Each model was trained to capture the relationship between activity features (e.g., heart rate, body temperature, BMI x duration) and the calories burned.

The application is powered by FastAPI, providing a robust and scalable API for real-time predictions. Users can input their activity data, and the API returns calorie predictions based on the trained models. This combination of machine learning and a modern web framework ensures a seamless and efficient experience.

## My Mission
Empowering individuals to lead healthier lifestyles by harnessing the power of technology and data-driven insights. Through innovative solutions and a commitment to wellness, I strive to make health improvement accessible, personalized, and actionable for everyone.

## Data Source
The dataset was gotten from kaggle datasets, [click here](https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos)

## How to Run the Project

### **1. Clone the Repository**

```bash
git https://github.com/Ronnie5562/linear_regression_model.git
cd linear_regression_model
```

### **2. Install Dependencies**
- Ensure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

### **3. Start the FastAPI Server**
- Run the following command from the project root:
python run.py


### **4. Access the API**
- API Documentation: <http://127.0.0.1:8000/docs>
- Interactive API Testing: <http://127.0.0.1:8000/redoc>

### **5. Run the Frontend App**:
- Change directory into the flutter App and run these commands:
```bash
cd FlutterApp/calories_app
flutter pub get
flutter run
```

## Technologies Used
- FastAPI for backend API services.
- Python for model development and API integration.
- Flutter for the mobile frontend.
- Machine Learning Models: Linear Regression, Random Forest, and Decision Trees.

## Deployed URL
- **Swagger Documentation**: https://calories-burnt-predicton-cf22bad3d3d6.herokuapp.com/docs
- **Redoc Documentation**: https://calories-burnt-predicton-cf22bad3d3d6.herokuapp.com/redoc

## Demo Video
- ### [Watch here](https://www.youtube.com/watch?v=FVuaQnsyDKw)

# Author

## [`Abimbola Ronald`](https://www.linkedin.com/in/abimbola-ronald-977299224/)