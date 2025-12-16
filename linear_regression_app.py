# linear_regression_app.py
import numpy as np
from sklearn.linear_model import LinearRegression
from fastapi import FastAPI
from pydantic import BaseModel

# test change to trigger CI/CD
# test change to trigger CI/CD23456788
# test34567890
#m make dir correct secret key
### 5th testing secret key123=====


# Create FastAPI app
app = FastAPI()

# Dummy training data (y = 2x + 3)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([5, 7, 9, 11, 13])

# Train model
model = LinearRegression()
model.fit(X, y)

class PredictRequest(BaseModel):
    x: float

@app.post("/predict")
def predict(req: PredictRequest):
    prediction = model.predict([[req.x]])[0]
    return {"input": req.x, "prediction": prediction}

