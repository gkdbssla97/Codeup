N = input()
size = len(N)
#print(size)
N = int(N)

pick = []
for i in range(size):
    pick.append(str(N % 10))
    N = N // 10
print("".join(pick))