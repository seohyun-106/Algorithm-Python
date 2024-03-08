T = int(input())
for _ in range(T):
    str = list(input())
    stack = []
    vps = True

    while str:
        tmp = str.pop()

        if tmp == ')':
            stack.append(tmp)
        else:
            if stack:
                stack.pop()
            else:
                vps = False
                break

    if not vps:
        print("NO")
    else:
        if stack:
            print("NO")
        else:
            print("YES")
