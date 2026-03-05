# Homelab
This is my homelab setup

## Setup 

The first thing you will need to do is setup dynamic DNS on the server for a consistent SSH hostname.

I used [DuckDNS](https://www.duckdns.org/)

Once you sign up with DuckDNS. Grab the token they generate

On your server, you will need to:
```bash
git clone git@github.com:ReeseHatfield/homelab.git
cd homelab
touch token.txt
```

Put your token as the only ocntent of `token.txt`

You can test that is is working by `./duck.sh` and check the `duck.log` file in this directory.

You will have to configure this `duck.sh` file to run automatically every so often. You can set this up automatically by running `./setup-cron.sh`

