import json

from pathlib import Path
# {
#   "USER": "reesehatfield",
#   "DUCK_DNS_SUBDOMAIN": "reese-lab",
#   "SSH_PORT": "2222",
#   "FUNCS": {
#     "HELLM": {
#       "COMMAND": "python3 ~/homelab/hellm-server/server.py"
#     }
#   }
# }
def run():
    
    
    cur_file_path = Path(__file__).resolve()
    cur_dir = cur_file_path.parent
    
    
    conf_file_path = cur_dir.parent  / "RPC_CONFIG.json"
    
    with open(conf_file_path, 'r') as f:
        conf = json.load(f)
    
    
    
    print(conf)


# todo delete me later
if __name__ == "__main__":
    run()