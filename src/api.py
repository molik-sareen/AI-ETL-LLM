from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/predict/{value}")
def predict(value: float):
    import pickle
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    prediction = model.predict([[value]])
    return {"prediction": prediction[0]}

