from langchain_huggingface import HuggingFaceEndpoint
from openai import OpenAI

def get_llm():

    # llm = ChatOpenAI(temperature=0, model='ruslandev/llama-3-8b-gpt-4o-ru1.0-gguf', base_url="http://localhost:1234/v1", api_key="lm-studio")
    # Load the model from Hugging Face Hub
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

    llm = HuggingFaceEndpoint(
        repo_id=repo_id,
        model_kwargs={
            "max_length": 200  # Set your intended max_length here
        },
        temperature=0.5,
        verbose=True,
        timeout=60
    )

    return llm