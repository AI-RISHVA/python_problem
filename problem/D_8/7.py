#The working hours of Chef’s kitchen are from X pm to Y pm (1 ≤ X < Y ≤ 12).Find the number of hours Chef works.

t= int(input())
for i in range(t):
    x,y = map(int,input().split())
    print(y-x)