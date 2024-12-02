a, b, c, d = map(int, input().split())
for i in range(c, d + 1):
    print(f'   {i}', end='')
print()
st = a
for i in range(a, b + 1):
    if i // 10 == 0:
        print(st, end='  ')
    else:
        print(st, end=' ')
    for j in range(c, d + 1):

        print(i * j, end=' ')
        if i * j // 10 == 0:
            print('  ', end='')
        else:
            print(' ', end='')
    print()
    st += 1
