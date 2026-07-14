#-------------------1
# Double Rent
#given initial rent X, find the final rent if it gets doubled.
x=int(input())
print (x*2)

#------------------2
# Saving Taxes
# given income X and tax-free limit Y, find the minimum investment needed to avoid tax.
t=int(input())
for i in range(t):
    x, y = map(int, input().split())
    print(x-y)

#-------------------3
# How many unattempted problems
#  out of X total problems, Y are attempted. Find the remaining unattempted problems.
x,y =map(int,input().split())
a = x-y
print(a)

# ---------------4
# Determine the Score (har ek point na 10 point hoy to n point ma ketlo score thy)
#  every xproblem test has total 10 marks. Find the score if N problems are correct.
t = int(input())
for i in range(t):
    x,n = map(int,input().split())
    s = (x//10)*n
    print(s)

#--------------5
# check if a website page exists. If the input ID is 404, it is not found.
x= int(input())

if x==404:
    print('NOT FOUND')
else:
    print('FOUND')