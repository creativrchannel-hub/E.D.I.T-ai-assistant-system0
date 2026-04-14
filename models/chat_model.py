import requests

def run_chat(prompt):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "gemma:3",
        "prompt": prompt,
        "stream": False
    })
    return res.json()["response"]
