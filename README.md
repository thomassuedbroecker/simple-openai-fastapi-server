# Simple OpenAI FastAPI server

This code example is a [`FastAPI`](https://fastapi.tiangolo.com/) server that contains multiple API endpoints for interacting with an [`OpenAI`](https://openai.com/) model. 

* [Related blog post](https://suedbroecker.net/2023/11/23/how-to-create-a-fastapi-server-to-use-openai-models/)

## The objective is to provide three main endpoints

* One endpoint is to send a simple text to Open AI and return the result.
* One endpoint to send a preconfigured prompt to Open AI. The preconfigured prompt contains a context and a question as parameters. These parameters will be replaced by the provided values of the endpoint invocation and sent to Open AI. The response will be provided as the return value of the endpoint.
* One endpoint is to upload a file and question as parameters for Open AI.
 
## Overview

* It uses [`HTTPBasic authentication`](https://en.wikipedia.org/wiki/Basic_access_authentication) for security. 
* It defines endpoints for `health status`, fetching simple text from [`OpenAI`](https://openai.com/), fetching text with a prompt from `OpenAI`, and uploading a file as context for the question to get a response from `OpenAI`. 
The code also includes `OpenAPI` configuration for the `Swagger UI`. 
* It uses custom modules for environment variables, response and payload definition, and AI access. 
* Finally, it runs the FastAPI application using [`uvicorn`](https://www.uvicorn.org/) on localhost port 8080.

_Clone the project to your local computer:_

```sh
git clone https://github.com/thomassuedbroecker/simple-openai-server-fastapi.git
```

![](/images/2023-11-22_fastapi-01.gif)

_Note:_ 

  * You can find additional information, on how to create a pipeline in the related project: “How to use and set up `Watsonx.ai` in the simple pipeline project”: https://github.com/thomassuedbroecker/simple-qa-pipeline. We reuse code and concepts from that pipeline project.
  * You can also use the Online editor (github.**dev**) to edit files: `https://github.dev/thomassuedbroecker/simple-openai-server-fastapi`.

_Content_

* [1. Setup of the Windows Machine](#1-setup-windows-machine)
* [2. Setup of the Python environment](#2-setup-the-python-environment)
* [3. Configure and start the `simple-openai-server` FastAPI server](#3-configure-and-start-the-simple-openai-server-fastapi-server)
* [4. Get your own OpenAI access](#4-get-your-own-openai-access)

## 1. Setup of the Windows Machine

### 1.1 Install Python

Please follow the link for the installation [Download Python for Windows](https://www.python.org/downloads/windows/).
_Note:_ Additional resources, how to [Set virtual environment for Python](https://suedbroecker.net/2023/05/23/set-a-virtual-environment-for-python/).

### 1.2 Install virtual environment

Follow the steps in [set up a virtual environment for Python](https://suedbroecker.net/2023/05/23/set-a-virtual-environment-for-python/)

_Note:_ To add the `path variable` please open in your Windows search bar `Edit environment variables for your account`.
 
### 1.3 Ensure you can use PowerShell on Windows

Please follow the link for the installation oder verification [Learn Microsoft Powershell](https://learn.microsoft.com/en-us/powershell/scripting/windows-powershell/starting-windows-powershell?view=powershell-7.3)

### 1.4 Install VSCode

Please follow the link for the installation of [`VSCode`](https://code.visualstudio.com/)

### 1.5 Install GitBash

Please follow the link for the installation of [`How to install GitBash`](https://www.educative.io/answers/how-to-install-git-bash-in-windows)

## 2. Setup of the Python environment

### 2.1 Create a virtual Python environment

* Windows with GitBash terminal.

```sh
cd code
python3.10 -m venv env3.10
source ./env3.10/Scripts/activate
```

* Mac and Linux terminal.

```sh
cd code
python3.10 -m venv env3.10
source ./env3.10/bin/activate
```

### 2.2. Install the needed Python libraries 

```sh
# Linux
#source ./env3.10/bin/activate 
# Windows
source ./env3.10/Scripts/activate 
python3 -m pip install --upgrade pip
python3 -m pip install "fastapi[all]"
python3 -m pip install requests
python3 -m pip install pydantic
python3 -m pip install openai
python3 -m pip install typing
python3 -m pip install beautifulsoup4
python3 -m pip install --upgrade openai
python3 -m pip freeze > requirements.txt 
```

## 3. Configure and start the `simple-openai-server` FastAPI server

### 3.1 Create the environment file

* Set a new user and password.

```sh
cat .env_template > .env
```
* Content

```sh
# APP
export APP_USER=admin
export APP_APIKEY=admin

# OpenAI
export OPENAI_KEY=YOUR_KEY
export OPENAI_MODEL=gpt-3.5-turbo-1106
export PROMPT="Document:\n\n<<CONTEXT>>\n\nQuestion:\n\n<<QUESTION>>\n\nAnswer:\n\n"
```

### 3.2 Start the `simple-openai-server` FastAPI server

* Windows 

```sh
cd code
source ./env3.10/Scripts/activate 
source .env
python3 simple-openai-server.py
```

* Linux

```sh
cd code
source ./env3.10/bin/activate 
source .env
python3 simple-openai-server.py
```

### 3.3 Open a browser and enter the following URL

```sh
http://localhost:8080/docs
```

### 3.4 Invoke FastAPI server endpoints by using the curl commands

* Access FastAPIserver `/`

```sh
export URL=http://localhost:8080
curl -X GET \
  "${URL}/" \
  -H "Content-Type: application/json" 
```

* Using REST GET to invoke the `health` endpoint

```sh
export URL=http://localhost:8080
export USER=admin
export PASSWORD=thomas
export REST_API_PATH=health
curl -u ${USER}:${PASSWORD} -X GET "${URL}/${REST_API_PATH}"
```

* Using REST POST to invoke the `get_openai_text_with_prompt` endpoint.

```sh
export URL=http://localhost:8080
export USER=admin
export PASSWORD=thomas
export CONTEXT="My name is Thomas."
export QUESTION="What is my name?"
export REST_API_PATH=get_openai_text_with_prompt

curl -u ${USER}:${PASSWORD} -X POST "${URL}/${REST_API_PATH}/" -H "Content-Type: application/json" -d "{\"context\":\"${CONTEXT}\",\"question\":\"${QUESTION}\"}"
```

## 4. Get your own OpenAI access

### 4.1 Register your account

_Note:_ Keep in mind `OpenAI` has a kind of prepaid model.

* [OpenAI](https://openai.com/blog/openai-api)
* [OpenAI Pricing](https://openai.com/pricing)

## 5. Additional notes

* [Files](https://fastapi.tiangolo.com/tutorial/request-files/)

