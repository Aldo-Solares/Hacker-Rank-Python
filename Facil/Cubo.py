
#LINK https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true

from collections import deque

def verificar(blocks):
    blocks = deque(blocks)
    top = float('inf')
    
    while blocks:
        if blocks[0] >= blocks[-1] and blocks[0] <= top:
            top = blocks.popleft()
        elif blocks[-1] <= top:
            top = blocks.pop()
        else:
            return "No"
    
    return "Yes"

test = int(input())
for _ in range(test):
    n = int(input())
    blocks = list(map(int, input().split()))
    print(verificar(blocks))
