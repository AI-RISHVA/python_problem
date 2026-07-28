# To find the total chapters, multiply the number of courses, units per course, and chapters per unit (X×Y×Z) for each test case.

# cook your dish here

t= int(input())
for _ in range(t):
    x,y,z = map(int,input().split())
    print(x*y*z)
        