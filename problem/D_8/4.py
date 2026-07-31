# For the upcoming semester, the admins of your university decided to keep a total of X seats 
# for the MATH-1 course. A student interest survey was conducted by the admins, and it was found that Y students
#  were interested in taking up the MATH-1 course.Find the minimum number of extra seats that the admins need to add to the
#  MATH-1 course to make sure that every student who is interested in taking the course is able to do so

# cook your dish here
t= int(input())
for i in range(t):
    x,y = map(int,input().split())
    if y>x:
        print(y-x)
    else:
        print(0)