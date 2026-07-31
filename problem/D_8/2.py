# Alice, Bob, and Charlie are bidding for an artifact at an auction. Alice bids A rupees, Bob bids B rupees, and
#  Charlie bids C rupees (where A, B, and C are distinct).According to the rules of the auction, the person who bids the highest amount will win the auction.
#  Determine who will win the auction.

# cook your dish here
t= int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    if a>b and a>c:
        print("Alice")
    elif b>c:
        print("Bob")
    else:
        print("Charlie")