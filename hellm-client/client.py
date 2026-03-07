
import shutil
import json

from enum import Enum
from typing import Dict, List, Literal


# context=$(cat <<'EOF'
# {
#     "messages": [
#         {"role": "user", "content": "Hello, how are you?"},
#         {"role": "assistant", "content": "I am well, thank you! How can I help you today?"},
#         {"role": "user", "content": "What's the weather like in Fairborn, OH?"}
#     ]
# }
# EOF
# )

# type should mirror above bash
Context = List[Dict[Literal["role", "content"], str]] 
messages: Context = {
    "messages": [
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "I am well, thank you! How can I help you today?"},
        {"role": "user", "content": "What's the weather like in Fairborn, OH?"}
    ]
}

json_str = json.dumps(messages)


print(json_str)

class Justify(Enum):
    LEFT = 1
    RIGHT = 2

def print_message(text: str, align: Justify):
    
    
    width, _ = shutil.get_terminal_size()

    formatted_str = ""
    counter = 0
    cur_row = ""
        
    for c in text:
        
        cur_row += c
        counter += 1
        
        if counter > width / 2:
            counter = 0
            
            if align == Justify.LEFT:
                cur_row = cur_row.rjust(width, ' ')
            elif align == Justify.RIGHT:
                cur_row = cur_row.ljust(width, ' ')
                
                
            cur_row += '\n'        
            
            formatted_str += cur_row
            cur_row = ""
            
            
    print(formatted_str)


# lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# print_message(lorem, align=Justify.LEFT)
