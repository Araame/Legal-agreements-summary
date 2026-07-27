from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")
 


@app.post("/analyze-review")
def classifier_feedbacks(feedback):
    result = classifier(feedback)
    return {"result": result}