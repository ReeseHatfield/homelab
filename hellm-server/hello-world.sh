#!/bin/bash

# local test for the server

echo '{"messages":[{"role":"user","content":"hello"}]}' | python3 server.py