
#LINK https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
#NOTE Todo el codigo va en la parte predeterminada del ejercicio

largo = len(string)
stuart, kevin = 0,0
for x in range(largo):
    if string[x] in "AEIOU":
        kevin+=largo-x
    else:
        stuart+=largo-x

print(f"Stuart {stuart}" if stuart>kevin else f"Kevin {kevin}" if kevin>stuart else "Draw")