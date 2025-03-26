
#LINK https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true

import re

s = input().strip()

match = re.search(r'([a-zA-Z0-9])\1', s)
if match:
    print(match.group(1))
else:
    print(-1)