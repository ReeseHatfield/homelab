#!/bin/bash

# Define paths and profile name
REMMINA_DIR="$HOME/.local/share/remmina"
PROFILE_FILE="$REMMINA_DIR/homelab_rdp_ssh.remmina"

mkdir -p "$REMMINA_DIR"

# reminna needs a profil config to be scriptable
cat << 'EOF' > "$PROFILE_FILE"
[remmina]
server=127.0.0.1:33389
clientname=
username=reesehatfield
password=
domain=
protocol=RDP
group=Homelab
name=Homelab RDP via SSH Tunnel
save_password=0
security=
resolution_mode=2
width=1920
height=1080
colordepth=32
viewmode=1

# SSH Tunnel Settings
ssh_tunnel_loopback=1
ssh_tunnel_enabled=1
ssh_tunnel_server=reese-lab.duckdns.org:2222
ssh_tunnel_username=reesehatfield
ssh_tunnel_auth=0
EOF

echo "Remmina profile created at $PROFILE_FILE"
echo "remmina -c $PROFILE_FILE"