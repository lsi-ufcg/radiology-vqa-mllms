# Langchain

## Getting Started

Creating and Installing dependencies in virtual environment

`python3.11 -m venv venv`  
`source venv/bin/activate`  
`pip install -r requirements.txt`

Add `LANGCHAIN_API_KEY` in your .env file

## Running app

`python3.11 -u src/script.py <model> >> outputs/output-<model>.txt`

`<model>` can be:

### llama3.2-vision:11b

`ollama pull llama3.2-vision:11b`

### qwen2.5vl:7b

`ollama pull qwen2.5vl:7b`

### gpt-4o

Add `OPENAI_API_KEY` in your .env

### gemini-2.5-pro

Add `GOOGLE_API_KEY` in your .env
