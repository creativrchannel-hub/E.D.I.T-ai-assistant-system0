import requests

def summarize(text):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "gemma:3",
        "prompt": f"Summarize:\n{text}",
        "stream": False
    })
    return res.json()["response"]
