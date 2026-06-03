#!/bin/bash

# abs path of this scripts directory hack
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PROFILE_FILE="$HOME/.local/share/remmina/homelab_rdp_ssh.remmina"

if [ ! -f "$PROFILE_FILE" ]; then
    echo "Profile not found. Running setup..."
    # this should always work, regardless of calling directory
    bash "$SCRIPT_DIR/setup-remmina.sh"
fi

echo "Launching Remmina with profile: $PROFILE_FILE"
remmina -c "$PROFILE_FILE" &