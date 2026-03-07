import json
import subprocess

from pathlib import Path


def run(rpc_func: str, rpc_input):
    
    
    cur_file_path = Path(__file__).resolve()
    cur_dir = cur_file_path.parent
    conf_file_path = cur_dir.parent  / "RPC_CONFIG.json"
    
    CONF = None
    with open(conf_file_path, 'r') as f:
        CONF = json.load(f)
    
    
    result = subprocess.run(
        ["ssh", "-p", f"{CONF['SSH_PORT']}", f"{CONF['USER']}@{CONF['DUCK_DNS_SUBDOMAIN']}.duckdns.org", CONF['FUNCS'][rpc_func]['COMMAND']],
        input=rpc_input,
        capture_output=True,
        text=True,
        check=True
    )

    
    return result.stdout
