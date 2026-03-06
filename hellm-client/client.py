# 

import shutil

width, height = shutil.get_terminal_size()

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


formatted_str = ""
counter = 0
cur_row = ""
for c in lorem:
    
    cur_row += c
    counter += 1
    
    if counter > width / 2:
        counter = 0
        cur_row = cur_row.ljust(width, ' ')
        cur_row += '\n'        
        
        formatted_str += cur_row
        cur_row = ""
        

print(formatted_str)