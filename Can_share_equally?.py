a,b = map(int,input().split())
if a%2 == 0 and b%2 == 0:
    print("YES")
elif (a%2 == 0 or b%2 == 0) and (a > 0 and b > 0):
    print("YES")
else:
    print("NO")