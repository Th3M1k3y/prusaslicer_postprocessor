#!/usr/bin/python
s_from_min = 0
s_from_max = 255

s_to_min = 0.0
s_to_max = 1.0

decimals = 5


import sys, re
if __name__ == '__main__':
    filename = sys.argv[1]
        
    output_file = open(filename, encoding='utf-8')            
    lines = output_file.readlines()
    output_file.close()
        
    output_file = open(filename, "r+")
    output_file.seek(0)                       
    output_file.truncate()
    for line in lines:
        if "M106" in line:            
            S = re.search(r'S(\d{1,3})', line)
            speed = f'S{round((float(S[0][1:]) - float(s_from_min)) * (float(s_to_max) - float(s_to_min)) / (float(s_from_max) - float(s_from_min)) + float(s_to_min),decimals)}'
            line = re.sub(r'S\d+', speed, line, flags=re.MULTILINE)
        output_file.write(line)
    output_file.close()
