sub = 0
for num in range(1, 101):
    if num % 10 == 3:
        continue
    sub += num
print(sub)