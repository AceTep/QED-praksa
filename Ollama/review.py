import requests
import json
from pydantic import BaseModel, ValidationError
from typing import Optional

class Message(BaseModel):
    role: str
    content: str

class ResponseChunk(BaseModel):
    message: Optional[Message] = None

def generate_chat_ollama(prompt, model="gemma3:4b", system_prompt="You are a helpful assistant."):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "stream": True 
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    full_response = ""
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                validated = ResponseChunk(**data)
                if validated.message and validated.message.content:
                    full_response += validated.message.content
            except (json.JSONDecodeError, ValidationError) as e:
                print("Skipping invalid chunk:", e)

    return full_response


if __name__ == "__main__":
    prompt = (
        "I want 3 problems that AI can solve."
        "Every problem needs to be different."
        "For each problem please give me description and simple solution."
        "--"
        "For context: I am student who needs to come up with some problems for my work experience. "
        "Problems need to be related to AI and it should be something that I can solve in 2 weeks."
    )

    system_prompt = (
        "You are an expert AI assistant helping a student brainstorm project ideas. "
        "The student needs three distinct, realistic problems that can be solved using AI, suitable for a "
        "beginner-to-intermediate student to complete within two weeks as part of a work experience program. "
        "For each problem, provide: 1. A clear and simple description of the problem. "
        "2. A basic AI-based solution that can be realistically implemented in that time frame "
        "(e.g., using Python and common libraries). The problems must be different in nature "
        "(e.g., image, text, data), achievable, and educational."
    )

    output = generate_chat_ollama(prompt, system_prompt=system_prompt)
    
    print("Output:\n", output)

    with open("ollama_output.md", "w", encoding="utf-8") as file:
        file.write(output)

    print("\nOutput has been saved to 'ollama_output.md'")
