

#!/usr/bin/env python3
import sys
import json
import time
import subprocess
import requests

# this relies on the client storing all the context, 
# but I think its a better model anyway
# This is stateless model, kinda just faking RPC

# idk why it defaults to this port
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"

# just kill it regardless
subprocess.run(["pkill", "ollama"], check=False)

# if this fails, it should be fine
ollama = subprocess.Popen(
    ["ollama", "serve"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)


# this needs a second, but sometimes more idk
time.sleep(1)


req = json.load(sys.stdin)
r = requests.post(
    OLLAMA_URL,
    json={
        "model": req.get("model", "llama3"),
        "messages": req["messages"],
        "stream": False
    }
)

resp = r.json()

print(resp)

sys.stdout.write(json.dumps(resp["message"]) + "\n")
sys.stdout.flush()

# kill without checking PID
subprocess.run(["pkill", "ollama"], check=False)