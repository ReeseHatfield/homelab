#!/bin/bash

# local test for the server

echo "Running ollama example with context"

context=$(cat <<'EOF'
{
    "messages": [
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "I am well, thank you! How can I help you today?"},
        {"role": "user", "content": "What's the weather like in Fairborn, OH?"}
    ]
}
EOF
)

echo $context | python3 ../server.py 