from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")


def class_by_stars(result):
    if result[0]["label"] == "1 star" or result[0]["label"] == "2 stars" :
        status = "negatif" 
    elif result[0]["label"] == "3 stars":
        status = "neutre"
    else :
        status = "positif" 
    return status
 


@app.post("/analyze-review")
def classifier_feedbacks(feedback):
    result = classifier(feedback)
    return {"result": class_by_stars(result)}