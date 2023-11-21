from openai import OpenAI
from .load_env import load_openai_env
from fastapi.exceptions import ResponseValidationError

def get_simple_text(text):
    
    openai_env, verification_key = load_openai_env()
    print(f"*** DEBUG (get_simple_text): {openai_env} {verification_key}")

    if (verification_key == True):

        print(f"*** DEBUG (verification): {text} : {verification_key} ")
        message = text
        try:
            # https://github.com/openai/openai-python
            client = OpenAI(
                        # defaults to os.environ.get("OPENAI_API_KEY")
                        api_key=openai_env["OPENAI_KEY"]
                    )
            
            completion = client.chat.completions.create(
                model = openai_env["OPENAI_MODEL"],
                #response_format={ "type": "json_object" },
                messages = [{"role":"user",
                            "content": message}]              
            )
            response = str(completion.choices[0].message.content)
            print(f"*** DEBUG ( response): Detail: {response} - All: {completion}")
            verification = True
        
        except Exception as e:
             error = {"Exception": e }                  
             response = str(error)
             verification = False
             return response, {"status":verification}        
    else:
        print(f"*** DEBUG (False) get simple key: {verification_key} ")
        response = "OpenAI is not configured"
        verification = False
    print(f"DEBUG: {response}")
    return response, {"status":verification} 

def get_text_with_prompt(context, question):
    
    openai_env, verification_key = load_openai_env()
    print(f"*** DEBUG (get_simple_text): {openai_env} {verification_key}")
    
    prompt_context_replace_template="<<CONTEXT>>"
    prompt_question_replace_template="<<QUESTION>>"

    if ( verification_key == True):
        
        # Build final prompt
        # 1. Load prompt.template
        prompt = openai_env["OPENAI_PROMPT"]
        # 2. Replace in prompt.template the <<CONTEXT>> with the value of the 
        #    input from the input parameter `context` and save it to the variable 
        #    'input_txt'.
        input_txt = prompt.replace(prompt_context_replace_template,context)
        # 3. Replace in 'input_txt' the <<QUESTION>> with the value of the 
        #    input from the input parameter `question` and and save it to the variable 
        #    'final_prompt'.
        final_prompt = input_txt.replace(prompt_question_replace_template,question)
        
        print(f"*** DEBUG: {final_prompt} : {verification_key} ")
        
        try:
            # https://github.com/openai/openai-python
            # 1. Create an OpenAI client with authenication.
            client = OpenAI(
                        # defaults to os.environ.get("OPENAI_API_KEY")
                        api_key=openai_env["OPENAI_KEY"]
                    )
            
            # 2. Invoke OpenAI with the 'final_prompt'
            completion = client.chat.completions.create(
                model = openai_env["OPENAI_MODEL"],
                #response_format={ "type": "json_object" },
                messages = [{"role":"user",
                            "content": final_prompt}]              
            )
            print(f"*** DEBUG completion : {completion}")

            
            # 3. Extract the result and save it as response as a return value.
            response = str(completion.choices[0].message.content)
            print(f"*** DEBUG response : {response}")

            
            verification = True
        
        except Exception as e:
             error = {"Exception": e }                  
             response = str(error)
             verification = False
             return response, {"status":verification}        
    else:
        print(f"*** DEBUG (False) get simple key: {verification_key} ")
        response = "OpenAI is not configured"
        verification = False
    
    print(f"DEBUG: {response}")
    return response, {"status":verification} 