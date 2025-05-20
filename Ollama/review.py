import requests
import json

def generate_chat_ollama(prompt, model="gemma3:4b"):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": True 
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    full_response = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            if "message" in data and "content" in data["message"]:
                full_response += data["message"]["content"]

    return full_response


if __name__ == "__main__":
    prompt = "Osmisli mi par problema koje bi mogao rijesiti uz pomoc AI-a."
    output = generate_chat_ollama(prompt)
    
    print("Output:\n", output)
    
    with open("ollama_output.txt", "w", encoding="utf-8") as file:
        file.write(output)
    print("\nOutput has been saved to 'ollama_output.txt'")