#!/bin/bash


TOKEN=$(cat /home/rhatfield/forge/homelab/token.txt)
DOMAIN="reese-lab"
URL="https://www.duckdns.org/update?domains=$DOMAIN&token=$TOKEN&ip="

curl -k -o duck.log -s -K - <<< "url=$URL"
