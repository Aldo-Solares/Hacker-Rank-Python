
#LINK https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true

import re

for x in range(int(input())):
    email = input().split()

    match = re.search(r"<[a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>", email[1])
    if match:
        print(email[0], match.group())