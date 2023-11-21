from pydantic import BaseModel
from typing import List

#############################
### Sub type specifictions

class BasicResult(BaseModel):
    result: str

class BasicTextResult(BaseModel):
    result: str

class BasicFileResult(BaseModel):
    result: str
    filename: str

class Result(BaseModel):
    result: List[dict]

class Status (BaseModel):
    status: bool

#############################
### Responses

#########################
# Example return value
#{
#  "status":"OK"
#}
class Health(BaseModel):
    status: str


#########################
# Example return value
#{
#  "openai_config":"{ "APIKEY":"APIKEY", "NEXT_KEY":"NEXT_VALUE"}"
#  "validation": true
#}
class Get_openai_config(BaseModel):
    openai_config: dict
    validation: bool

#########################
# Example return value
#{
#  "text": {
#    "result": "text"
#  },
#  "validation": {
#    "status": true
#  }
#}
class Get_openai_text(BaseModel):
    text: BasicTextResult # uses sub type 'BasicTextResult'
    validation: Status

####################################
# Example return value
#{
#  "text": {
#    "result": "text_string",
#    "filename": "filename_string"
#  },
#  "validation": {
#    "status": true
#  }
#}
class Get_openai_text_file(BaseModel):
    text: BasicFileResult # uses sub type 'BasicFileResult'
    validation: Status

