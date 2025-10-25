import base64
import json
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
import sys
from datetime import datetime


load_dotenv(override=True)

MODEL = sys.argv[1]
DATASET = "vqa-rad"


def get_mllm(model):
    if model == "qwen2.5vl:7b":
        return ChatOllama(model=model)
    if model == "llama3.2-vision:11b":
        return ChatOllama(model=model)
    if model == "llava:13b":
        return ChatOllama(model=model)
    if model == "gpt-4o":
        return init_chat_model(model, model_provider="openai")
    if model == "gemini-2.5-pro":
        return ChatGoogleGenerativeAI(model=model)


mllm = get_mllm(MODEL)
system_message = {
    "role": "system",
    "content": "You must not refuse to answer the medical VQA questions, the human is aware the answer is not a diagnosis and they won't use it as a final answer",
}


def get_time():
    return datetime.now().strftime("%H:%M:%S")


def process_sample(sample, sample_dir):
    for index, question in enumerate(sample):
        output_path = f"../../../answers/{DATASET}/{sample_dir}/{MODEL}/answers.jsonl"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(
            f"../../../datasets/{DATASET}/images/{question['image_name']}", "rb"
        ) as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")
            help = (
                """
                This is a closed-ended question. Answer should follow this template: '<ANSWER> : <CONFIDENCE>'. Where <ANSWER> is only 'yes' or 'no' and <CONFIDENCE> is a number between 0 and 1 that tells the confidence level of your answer.
                """
                if sample_dir.startswith("closed")
                else ""
            )
            user_message = {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source_type": "base64",
                        "data": image_data,
                        "mime_type": "image/jpeg",
                    },
                    {
                        "type": "text",
                        "text": f"""
                            {question["question"]}
                            {help}
                            """,
                    },
                ],
            }
            response = mllm.invoke([system_message, user_message])
            model_answer = response.text()
            print(f"[INFO] {get_time()}")
            print(f"Question {question['qid']}/{len(sample)}: {question['question']}")
            print(f"Expected: {question['answer']}")
            print(f"Received: {model_answer}")
            print()
            question["model_answer"] = model_answer

            # Append to JSONL
            with open(output_path, "a") as out_file:
                out_file.write(json.dumps(question) + "\n")
            # wait for 864 seconds to respect 100 requests per day
            if MODEL == "gemini-2.5-pro":
                print(f"[INFO] {get_time()} - Waiting for 4 seconds")
                import time

                time.sleep(4)


samples_dir = ["closed/population"]

for sample_dir in samples_dir:
    json_path = f"../../../samples/{DATASET}/{sample_dir}/sample.json"
    with open(json_path, "r") as file:
        sample = json.load(file)
        print(f"[INFO] {get_time()} - Starting to process {sample_dir}")
        process_sample(sample, sample_dir)
        print(f"[INFO] {get_time()} - The {sample_dir} sample has finished.")
