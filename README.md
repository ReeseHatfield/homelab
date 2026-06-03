# Homelab
This is my homelab setup

# Setup 

## Local Network
- Set a static LAN IP (DHCP reservation) on  router
- Assign homelab MAC address to a fixed IP
- Install and configure SSH on homelab
- Install `openssh-server`
- Forward external port (I used 2222) → internal port 22 (SSH port) on router


For external network SSH access, you will also need to setup dynamic DNS on the server for a consistent SSH hostname.

I used [DuckDNS](https://www.duckdns.org/)

Once you sign up with DuckDNS. Grab the token they generate

On your server, you will need to:
```bash
git clone git@github.com:ReeseHatfield/homelab.git
cd homelab
touch token.txt
```

Put your token as the only content of `token.txt`

You can test that is is working by `./duck.sh` and check the `duck.log` file in this directory.

You will have to configure this `duck.sh` file to run automatically every so often. You can set this up automatically by running `./setup-cron.sh`

If done correctly, you should be able to SSH into the homelab with

```bash
ssh -p [PORT] [USER]@[SUBDOMAIN].duckdns.org
```

## RDP
For full RDP desktop access (my homelab ships gnome <3), you'll need to setup Remmina.
You'll to install `remmina` and `xrdp`
Assuming all the keys are in the right places, run the `rdp/setup-remmina.sh`.
Once that is working, you can RDP in via `./rdp/rdp.sh`.

Make sure you have the ssh private key as `$HOME/.ssh/homelab-rpc`

## HELLM
Homelab Enabled LLM

- Ollama wrapper via custom SSH RPC
```bash 
python3 hellm-client/client.py
```
Will provide a chat interface, with all computation offloaded to the server
