#!/bin/bash

# local test for the server

echo "Running ollama hello world example"

echo '{"messages":[{"role":"user","content":"hello"}]}' | python3 ../server.py