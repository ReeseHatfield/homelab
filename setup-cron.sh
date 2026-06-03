#!/bin/bash

DUCK="$(pwd)/duck.sh"

if [ ! -f "$DUCK" ]; then

    echo "could not find duck.sh in cwd"
    exit 1
fi


(crontab -l 2>/dev/null; echo "*/5 * * * * $DUCK >/dev/null 2>&1") | crontab -

echo "Installed new cron job"
echo "Will update duckdns ip every 5 minutes"