# hef took an examination two times. In the first attempt, he scored 
# X marks while in the second attempt he scored 
# Y marks. According to the rules of the examination, the best score out of the two attempts will be considered as the final score.

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x>y:
        print(x)
    else:
        print(y)