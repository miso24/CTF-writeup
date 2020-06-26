from pwn import *

arr = [1, 10, 3, 2, 5, 9, 8, 7, 4, 6]

p = remote('2020.redpwnc.tf', 31039)

for i in range(len(arr) - 1):
  for j in range(len(arr) - i - 1):
    if arr[j] > arr[j + 1]:
      p.sendline(str(j))
      arr[j], arr[j + 1] = arr[j + 1], arr[j]
p.sendline(str(10))

print(p.readall().decode())
