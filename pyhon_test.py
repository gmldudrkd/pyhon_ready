# code test

# 런타임 구하기
import time
start_time = time.time()

a, b, c = input().split()
var_arr = [a, b, c]
print(len(var_arr))

for i in len(var_arr):
    print(i)

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



# 문자를 10진수 유니코드(Unicode)로
a = ord(input())
# 유니코드를 +1 해서 코드에 해당하는 문자를 출력
print(chr(a+1))

# 단어의 연속 출력
word, r = input().split()
print(word*int(r))

# 연산식
// : 몫구하기
% : 나머지구하기

# 정확도로 반올림한 값(3째자리에서)
print(format(a, ".2f"))
print("%.3f" % round(f1/f2, 3)) > 라운드된 값을 소수점 3째자리까지 노출
print(format(a/b, ".2f")) > 정확도로 소수점 2자리까지 노출

%.숫자f'%노출할입력값
 -> %.숫자f : 표시할 소수점 아래자리수를 정함
 
ex)
 a, b, c = map(int, input().split())
add = a+b+c
aver = round(add/3, 3)
print(add, format("%.2f"%aver))

# 비트연산자
2진수를 왼쪽부터 넣음
<< : *2, >> : %2
print(a << b)
-> a * 2의b승

# 비교연산자
xor : 두값이 다를때만 true
print((a_b and not b_b) or (not a_b and b_b))
not or : 두 값이 모두 false 일때만 true
print(not(a_b or b_b))

# 비트단위 논리연산
~n = -n-1 (tilde, 틸드)
ex) ~5 = -5-1 = -6
 -> ~(0101) = 1010 = -6
비트연산 : int(a) & int(b) => 0101 & 0011 = 0001(3 & 5 = 1)

#3항연산
a if C else b
a : C가 참일때 출력
b : C가 참이 아닐때 출력

'''