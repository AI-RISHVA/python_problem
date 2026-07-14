# Dog Binary hears frequencies from (67) Hz to (45,000) Hz (inclusive). Given a command frequency \(X\), determine if Binary can hear the command.Input:\(T\): Number of test cases.(x): The command frequency in Hertz.
# cook your dish here
t = int(input())
for i in range(t):
    x = int(input())
    if 67 <=x<=45000:
        print("YES")
    else:
        print("NO")

# Chef and his friends want to join a puzzle hunt. The event requires teams of 6 to 8 people. If Chef's team has \(N\) people, are they eligible to participate?
n = int(input())

if n>=6 and n <= 8:
    print("Yes")
else:
    print("No")

# given the heights of Alice (\(X\) cm) and Bob (\(Y\) cm), determine who is taller. It is guaranteed that \(X \neq Y\).Input: Two integers \(X\) and \(Y\).Output: Print A if Alice is taller, otherwise print B.Logic / Pseudo-codetextIf X > Y:
#     Print "A"
# Else:
#     Print "B"
# Use code with caution.If you need help writing this in a specific programming language like Python, C++, or Java, let me know!Who is taller! Practice Problem in 500 difficulty ratingCharlie measured the heights of Alice and Bob, and got to know that Alice's height is X X X centimeters and Bob's height is Y Y Y ...CodeChefShow all    
# cook your dish here
t =int(input())
for i in range(t):
    x,y = map(int,input().split())
    if x>y:
        print("A")
    else:
        print("B")

# Chef has \(N\) notes of Rs. \(2000\). Since Rs. \(2000\) notes are banned, how many Rs. \(500\) notes does he need to pay the same amount CodeChef Practice?Would you like me to help you solve this problem with the mathematical formula or write a program/algorithm for it?
# cook your dish here
n = int(input())

print(4 * n)

# Given \(N\) chocolates, determine if they can be divided equally between two people without breaking any chocolate
# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    if n%2 ==0:
        print("Yes")
    else:
        print("No")