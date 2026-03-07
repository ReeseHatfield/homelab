
import shutil
import json
import subprocess
import sys

from enum import Enum, StrEnum, auto
from typing import Dict, List, Literal
from pathlib import Path

# I dont wanna import this as a module bc this should exist as a separate script for now
sys.path.append(str(Path(__file__).resolve().parent.parent / "ssh-as-rpc"))
from ssh_rpc import run

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

EMPTY_CONTEXT: Context = {
    "messages": []
}


class Role(StrEnum):
    USER = auto()
    ASSISTANT = auto()
    
    

def build_msg(role: Role, txt: str) -> Message:
    message: Message = {
        "role": role.value,
        "content": txt
    }
    
    return message



def append_msg(ctx: Context, msg: Message) -> Context:
    
    ctx["messages"].append(msg)
    
    return ctx


def main() -> None:
    
    ctx: Context = EMPTY_CONTEXT.copy()

    print(json.dumps(ctx))
    print()
    print()

    ctx = append_msg(ctx, build_msg(Role.USER, "How is the weather?"))
    ctx = append_msg(ctx, build_msg(Role.ASSISTANT, "it is cloudy"))
    ctx = append_msg(ctx, build_msg(Role.USER, "What was my first message?"))
    
    
    server_reply = run("HELLM", json.dumps(ctx))
    
    response: Message = json.loads(server_reply)
    append_msg(ctx, response)
    
    print(json.dumps(ctx))


if __name__ == "__main__":
    main()
