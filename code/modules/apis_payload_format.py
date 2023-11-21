from pydantic import BaseModel, ValidationError
import json
from fastapi import UploadFile

class Openai_simple_text(BaseModel):
    text: str

class Openai_simple_prompt(BaseModel):
    question: str

class Openai_question(BaseModel):
    question: str
    # context_file: UploadFile
    
