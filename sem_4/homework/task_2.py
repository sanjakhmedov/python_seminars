def find_prime_nums(num):
    pr_fact = []
    di = 2
    while num > 1:
        if num % di == 0:
            pr_fact.append(di)
            num /= di
        else:
            di += 1
    return pr_fact


res = find_prime_nums(int(input("Enter the number: ")))
print(res)
