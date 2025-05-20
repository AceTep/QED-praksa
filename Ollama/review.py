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

    # Čitaj liniju po liniju (stream)
    full_response = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            if "message" in data and "content" in data["message"]:
                full_response += data["message"]["content"]

    return full_response


if __name__ == "__main__":
    prompt = "Napiši kratki opis Gemma 3 modela i kako se koristi u Ollami."
    output = generate_chat_ollama(prompt)
    print("Output:\n", output)
