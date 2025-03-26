
#LINK https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

n = int(input())

student_marks = {}

for x in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

resultado = ((student_marks[query_name][0]+ student_marks[query_name][1]+ 
            student_marks[query_name][2])/3)
            
print(f"{resultado:.2f}")