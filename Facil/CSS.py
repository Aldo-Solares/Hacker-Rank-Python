
#LINK https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true

import re

for x in range(int(input())):
    text = input()
    matches = re.findall(r"(?<=.)(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})",text)
    if matches:
        for x in matches:
            print(x)
