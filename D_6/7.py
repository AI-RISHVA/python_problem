# There are G girl and B boy students at IIT (BHU) such that B > G.
# If ICM were a team game where teams could only be of size 2, having exactly 1 girl student and 1 boy student,
# what would be the minimum number of boy students from IIT (BHU) who would not be able to participate?

# cook your dish here
t= int(input())
for i in range(t):
    g,b=map(int,input().split())
    print(b-g)