# Chef wants to host a party with a total of 
# N people.However, the party hall has a capacity of 
# X people. Find whether Chef can host the party.

# cook your dish here
t= int(input())
for i in range(t):
    n,x = map(int,input().split())
    if n>x:
        print("no")
    else:
        print("yes")