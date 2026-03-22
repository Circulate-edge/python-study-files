count = 0
for num in range(1, 101):
    if num % 7 == 0 or '7' in str(num):
        count += 1
        print(num,"拍手")
print("拍手了",count,"次")