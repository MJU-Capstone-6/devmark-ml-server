from pathlib import Path

import joblib
from fastapi import FastAPI

import __main__

from .models import PredictParam
from .tokenizer.kkma_tokenizer import kkma_tokenizer

app = FastAPI()

setattr(__main__, "kkma_tokenizer", kkma_tokenizer)
model_path = Path.cwd() / "model"
loaded_model = joblib.load(f"{model_path}/KCNB.pkl")
loaded_vectorizer = joblib.load(f"{model_path}/KCNB_Vec.pkl")


@app.post("/")
async def predict_category(param: PredictParam):
    sentence_counts = loaded_vectorizer.transform([param.title])
    category = loaded_model.predict(sentence_counts)
    return {"category": category[0]}
