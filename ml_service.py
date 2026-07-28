from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel, Field
from functools import lru_cache

app = FastAPI()

@lru_cache(maxsize=1)
def get_pipeline():
    classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")
    return classifier


# class ReviewModel(BaseModel):
#     content : str = Field(min_length=20, max_length=50)

def class_by_stars(result):
    if result[0]["label"] == "1 star" or result[0]["label"] == "2 stars" :
        status = "negatif" 
    elif result[0]["label"] == "3 stars":
        status = "neutre"
    else :
        status = "positif" 
    return status

def is_urgent_or_not(status):
    if status == 'positif' or status == 'neutre':
        is_urgent = False
    else :
        is_urgent = True
    return {"is_urgent" : is_urgent}
        


@app.post("/analyze-review")
def classifier_feedbacks(feedback):
        classifier = get_pipeline()
        result = classifier(feedback)
        status = class_by_stars(result)
        return {"result": class_by_stars(result),"is_urgent": is_urgent_or_not(status)}
