from fastapi import FastAPI
from ml_service import ReviewModel, Pipeline, class_by_stars, is_urgent_or_not
from pydantic import ValidationError


app = FastAPI()


@app.post("/analyze-review")
def classifier_feedbacks(feedback : ReviewModel ):
    try:
        classifier = Pipeline.get_pipeline()
        result = classifier(feedback.content)
        status = class_by_stars(result)
        return {"result" : result , "result": class_by_stars(result),"is_urgent": is_urgent_or_not(status)}
    except ValidationError as e:
        return  {"error": e}


if __name__ == "__main__":
    classifier_feedbacks(feedback)
