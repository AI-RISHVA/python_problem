# Given the height of Chef's son (X) and the minimum height required for a roller coaster (H), determine if he is tall enough to ride (meaning X≥H). If he is, print YES; otherwise, print NO.
# Does this core goal make sense to you? If so, what do you think is the first thing we need to do in Python to handle multiple test cases (
# T)


t=int(input())

for i in range(t):
    x,h = map(int,input().split())
    if x>=h:
        print("YES")
    else:
        print("NO")