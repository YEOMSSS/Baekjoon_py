'''
문제
The Department of Computer Engineering at Sharif University of Technology
has recently initiated a professional education program known as Micromasters.
This program offers a set of courses designed to empower students with specialized knowledge
and skills in various domains of computer science and engineering.
As an incentive to promote the program,
the department has introduced a referral system wherein individuals
who refer other students to the Micromasters program receive a $10\%$ discount
for each referred student on their own course registrations.

Mina is a talented student who is passionate about spreading the benefits of the Micromasters program.
With each referral, Mina’s list of discounts grows,
and now the following question arises: given the number of students who are referred by Mina,
how many courses can she enroll in for free?

입력
The input consists of a single line containing a single integer $n$ ($0 \le n \le 1000$),
which represents the number of students that Mina has referred.

출력
Print a single line, containing the number of courses Mina can enroll in for free using the discounts.

예제 입력 1 
5
예제 출력 1 
0
예제 입력 2 
18
예제 출력 2 
1
'''
# 250515
# 10%를 내림으로 출력하라는 거지? 맞지?

students = int(input())

print(students // 10)
# // 를 사용해 내림을 해준다.
# 입력 범위가 양수니까 int()를 써서 버려도 된다.