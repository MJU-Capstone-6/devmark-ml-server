from pydantic import BaseModel


class PredictParam(BaseModel):
    title: str
