# Langchain

## Supported models

- GPT 4o
- Gemini 2.5 Pro
- Qwen 2.5 VL
- Llama 3.2 Vision
- Llava

> Some models require API Keys

## Getting Started

Create a virtual environment  
`python3.11 -m venv venv`

Activate it  
`source venv/bin/activate`

Install dependencies  
`pip install -r requirements.txt`

Add `LANGCHAIN_API_KEY` in your .env file

## Getting access to the models

**GPT 4o**: Add `OPENAI_API_KEY` in your .env  
**Gemini 2.5 Pro**: Add `GOOGLE_API_KEY` in your .env  
**Qwen 2.5 VL**: `ollama pull qwen2.5vl:7b`  
**Llama 3.2 Vision**: `ollama pull llama3.2-vision:11b`  
**Llava**: `ollama pull llava:13b`

## Running the App

`python3.11 -u src/script.py <model> >> outputs/output-<model>.txt`

Where `<model>` variable must be one of the following options:

llama3.2-vision:11b  
qwen2.5vl:7b  
gpt-4o  
gemini-2.5-pro
