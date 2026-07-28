
# Chef wants to give a burger party to all his N friends i.e. he wants to buy one burger for each of his friends.
# The cost of each burger is X rupees while Chef has a total of K rupees.Determine whether he has enough money to buy a burger for each of his friends or not.


t= int(input())
for _ in range(t):
    n,x,k = map(int,input().split())
    if n*x<=k:
        print("yes")
    else:
        print("no")