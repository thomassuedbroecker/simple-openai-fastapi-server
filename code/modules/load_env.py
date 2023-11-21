import os

# Application environment variables
def load_apikey_env():
    if (os.environ.get("APP_USER") == None):
            USER = "admin"
    else:
            USER = os.environ.get("APP_USER")
    
    if (os.environ.get("APP_APIKEY") == None):
            APIKEY = "apikey"
    else:
            APIKEY = os.environ.get("APP_APIKEY")
    
    if ((USER=="admin") or 
        (APIKEY=="apikey")):
            authenicationStatus = False
    else:
            authenicationStatus = True
    
    authenicationJSON = { "USER": USER,
                          "APIKEY":APIKEY
                        }
    print(authenicationJSON)

    return authenicationJSON, authenicationStatus

# OpenAI environment variables
def load_openai_env():
    
    if (os.environ.get("OPENAI_KEY") == None) or (os.environ.get("OPENAI_KEY") == "YOUR_KEY") :
            OPENAI_KEY = "NO_KEY"
    else:
            OPENAI_KEY = os.environ.get("OPENAI_KEY")
    
    if (os.environ.get("OPENAI_MODEL") == None) or (os.environ.get("OPENAI_MODEL") == "YOUR_MODEL") :
            OPENAI_MODEL = "NO_MODEL"
    else:
            OPENAI_MODEL = os.environ.get("OPENAI_MODEL")

    if (os.environ.get("OPENAI_PROMPT") == None) or (os.environ.get("OPENAI_PROMPT") == "YOUR_MODEL") :
            OPENAI_PROMPT = "NO_PROM"
    else:
            OPENAI_PROMPT = os.environ.get("OPENAI_PROMPT")
    
    
    if (OPENAI_KEY=="NO_KEY" or 
        OPENAI_MODEL=="NO_MODEL" or 
        OPENAI_PROMPT=="NO_PROMPT"):
            openaiStatus = False
    else:
            openaiStatus = True

    
    openaiJSON = { "OPENAI_KEY":OPENAI_KEY,
                   "OPENAI_MODEL":OPENAI_MODEL,
                   "OPENAI_PROMPT":OPENAI_PROMPT
                 }
    
    print(openaiJSON)

    return openaiJSON, openaiStatus