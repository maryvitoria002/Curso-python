# n = int(input())
# lista = list(map(int, input().split()))
# count = 0

# for i in range (n-2):
#     if lista[i] == 1 and lista [i+1] == 0 and lista[i+2] == 0:
#         count += 1
# print(count)

n = int(input())
lista = str(input())

print(lista.count('1 0 0'))