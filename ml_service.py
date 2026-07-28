from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel, Field, ValidationError, field_validator
from functools import lru_cache


# Implementing singleton for caching the get_pipeline object once 
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Pipeline(metaclass=SingletonMeta):
    @staticmethod
    @lru_cache(maxsize=1)
    def get_pipeline():
        return pipeline("text-classification",model="nlptown/bert-base-multilingual-uncased-sentiment",)
        



class ReviewModel(BaseModel):
    content : str 


    @field_validator("content", mode="after")
    @classmethod
    def validate_review_content(cls, content : str):
        if not isinstance(content, str):
            raise ValidationError("Review content must be a string !")
        if content == "":
            raise ValidationError("Review content cannot be empty !")
        if len(content) > 50 :
            raise ValidationError("Review content cannot contain more than 50 caracters !")
        if len(content) < 20 :
            raise ValidationError("Review content cannot be under 20 caracters !")

        return content


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
        



