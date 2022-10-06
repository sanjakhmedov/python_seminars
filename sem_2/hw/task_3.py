n = int(input('enter the number: '))

nums = list()

for i in range(1, n + 1):
    a = round((1 + 1/i) ** i)
    nums.append(a)

print(nums)
nums_sum = sum(nums)
print(nums_sum)
