
import shutil
import json
import subprocess

from enum import Enum, StrEnum, auto
from typing import Dict, List, Literal


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


Message = Dict[Literal["role", "content"], str]

Context = List[Message] 


class Role(StrEnum):
    USER = auto()
    ASSISTANT = auto()
    
    

def build_msg(role: Role, txt: str) -> Message:
    message: Message = {
        "role": role.value,
        "content": txt
    }
    
    return message



def append_message(ctx: Context, msg: Message) -> Context:
    
    ctx["messages"].append(msg)
    
    return ctx


def main() -> None:
    
    ctx: Context = {
        "messages": []
    }

    
    print(json.dumps(ctx))
    print()
    print()

    ctx = append_message(ctx, build_msg(Role.USER, "How is the weather?"))
    ctx = append_message(ctx, build_msg(Role.ASSISTANT, "it is cloudy"))
    ctx = append_message(ctx, build_msg(Role.USER, "Give me an approximation for the square root of 2"))
    # super cursed, will eventually be an ssh call
    result = subprocess.run(
        ["sudo", "python3", "../hellm-server/server.py"],
        input=json.dumps(ctx),
        capture_output=True,
        text=True,
        check=True
    )
    
    response: Message = json.loads(result.stdout)
    append_message(ctx, response)
    
    print(json.dumps(ctx))


if __name__ == "__main__":
    main()
# lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# print_message(lorem, align=Justify.LEFT)
