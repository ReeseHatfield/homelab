#!/bin/bash

REMMINA_DIR="$HOME/.local/share/remmina"
PROFILE_FILE="$REMMINA_DIR/homelab_rdp_ssh.remmina"

mkdir -p "$REMMINA_DIR"

# ensure perms
chmod 600 "$HOME/.ssh/homelab-rpc"
chmod 700 "$HOME/.ssh"

cat << EOF > "$PROFILE_FILE"
[remmina]
server=localhost:3389
clientname=
username=reesehatfield
password=
domain=
protocol=RDP
group=Homelab
name=Homelab RDP
save_password=0
security=
resolution_mode=2
width=1920
height=1080
colordepth=32
viewmode=1

# SSH Tunnel Settings
ssh_tunnel_loopback=0
ssh_tunnel_enabled=1
ssh_tunnel_server=reese-lab.duckdns.org:2222
ssh_tunnel_username=reesehatfield
ssh_tunnel_auth=1
ssh_tunnel_privatekey=$HOME/.ssh/homelab-rpc
EOF

echo "Remmina profile successfully updated at $PROFILE_FILE"