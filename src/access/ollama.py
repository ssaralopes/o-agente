import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"


def ask_ollama(message, system_prompt=None):
    """
    Envia uma mensagem para o modelo Llama através do Ollama
    e retorna a resposta gerada.
    """

    messages = []

    if system_prompt:
        messages.append({
            "role": "system",
            "content": system_prompt
        })

    messages.append({
        "role": "user",
        "content": message
    })

    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data["message"]["content"]
