# 처음 내 풀이
# def d(n):
#     if n < 10:
#         return n+n
#     elif n >= 10:
#         return n+ n//10 + n%10
#     elif n >= 100:
#         return n + n//100 + (n-n//100*100)//10 + n%10
#     elif n >= 1000:
#         return n + n//1000 + (n-n//1000*1000)//100 + (n-n//100*100)//10 + n%10
#     elif n == 10000:
#         return 10000 + 1
    
# result = []
# for i in range(1,10001):
#     if d(i) not in result:
#        result.append(d(i))

# for j in range(1,10001):
#     if j not in result:
#         print(j)

# 설명을 보고 푼 풀이
def d(num):
    next = num
    for value in list(str(num)):
        next += int(value)
    return next

natural_num = set(range(1,10001))
generated_num = set()
for count in range(10001):
    generated_num.add(d(count))

self_num = sorted(natural_num - generated_num) 
for i in self_num:
    print(i)
