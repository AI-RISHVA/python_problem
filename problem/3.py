# "If Chef attends MasterChef's cooking classes for \(X\) weeks at a cost of \(Y\) coins per week, what is the total amount he must pay?"You can easily calculate the total by multiplying the number of weeks by the cost per week: \(X \times Y\).
t = int(input())
for i in range(t):
    x, y = map(int , input().split())
    print(x*y)

# Chef and Chefina want to equalize their incomes by donating the difference. If Chef earns \(X\) and Chefina earns \(Y\) (with \(Y > X\)), how much should they donate to charity?
# cook your dish here
t = int(input())
for i in range(t):
    x,y = map(int,(input()).split())
    print(y-x)

# Chef's secret agent will reveal information to him after \(K\) weeks. If \(X\) days have already passed, find the number of remaining days Chef must wait.Would you like me to help you write the formula or the complete logic in C++/Python to solve this problem?
t =int(input())
for i in range(t):
    k,x =map(int, input().split())
    print(    (7*k)-x)

# Chef's body temperature is measured as \(X\) °F. A person has a fever if temperature is strictly greater than \(98\) °F. Output YES if Chef has a fever, and NO otherwise.
# cook your dish here
t = int(input())
for i in range(t):
    x = int(input())
    if x > 98:
        print("YES")
    else:
        print("NO")

#  car rental costs Rs 10 per km, with a minimum daily charge for 300 km. If the car is driven X km in a day, what is the total cost?
t =int(input())
for i in range(t):
    x =int(input())
    print(max(300,x)*10)