# code test

#런타임 구하기
import time
start_time = time.time()

a = input()
n = int(a)
print(-n)


end_time = time.time()
print()
print(">> Run time", end_time-start_time)

'''

# 구분값으로 출력(sep)
a, b = input().split(":")
print(a, b, sep=":")

a, b, c = input().split(".")
print(c, b, a, sep="-")

#문자 쪼개기
input_val = input()
print(input_val[0])
print(input_val[1])

#입력 값 글자수 만큼 나눠서 출려
input_val = input()
all_len = int(len(input_val)/2)
set_i = 0
for i in range(all_len):
    print(input_val[set_i:set_i+2])
    set_i += 2


a = input()
n = int(a)
print('%x'%n) #16진수
print('%o'%n) #8진수
'''