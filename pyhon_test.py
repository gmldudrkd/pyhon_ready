# code test

# 런타임 구하기
import time
start_time = time.time()

# 초기화
all_width = [[0 for i in range(10)] for j in range(10)]

# 좌표생성
for x in range(10):
    data = list(map(int, input().split()))
    for y in range(10):
        all_width[x][y] = data[y]

end_route = "N"
s_x = s_y = 1
all_width[s_x][s_y] = 9

no_route = ""
x_t = y_t = 0
while end_route != "Y":
    x_t = y_t = 0
    if all_width[s_x][s_y+1] == 1:
        x_t = s_x+1
        y_t = s_y
    else:
        x_t = s_x
        y_t = s_y+1

    if all_width[x_t][y_t] == 2:
        all_width[x_t][y_t] = 9
        end_route = "Y"
    elif all_width[x_t][y_t] == 1:
        all_width[x_t][y_t] = 1
        end_route = "Y"
    else:
        all_width[x_t][y_t] = 9
        s_x = x_t
        s_y = y_t

# 출력
for ii in range(10):
    for jj in range(10):
        print(all_width[ii][jj], end=" ")
    print()


end_time = time.time()
print()
print(">> Run time", end_time-start_time)

''' 

# 구분값으로 출력(sep)a, b = input().split(":")
print(a, b, sep=":")
hj
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

# 3항연산
a if C else b
a : C가 참일때 출력
b : C가 참이 아닐때 출력

# elseif 문
if input_score >= 90:
elif input_score >= 70:

# 알파벳함수
ord('a') : a를 숫자로 
print(chr(alpha_st), end=' ') : alpha_st를 뒤에 공백잇게 문자열로 출력

#16진수 곱셈
n = int(input(),16)
for i in range(1,16):
    print('%X*%X=%X'%(n,i,n*i),sep='')
    
# 빛의표현(저장공간의 계산)
input_rgb = input().split(" ")
val_h = int(input_rgb[0])
val_b = int(input_rgb[1])
val_c = int(input_rgb[2])
-- (val_h * val_b * val_c) > bit
val_mb = (val_h * val_b * val_c)/8/1024/1024
print(format(val_mb, ".2f")+" MB")

8 bit(비트)           = 1byte(바이트)     # 8bit=1Byte
1024 Byte(210 byte) = 1KB(킬로 바이트)  # 1024Byte=1KB
1024 KB(210 KB)      = 1MB(메가 바이트)
1024 MB(210 MB)     = 1GB(기가 바이트)
1024 GB(210 GB)      = 1TB(테라 바이트)

# 반복문 시작~끝값 정하기
for i in range(1, input_number+1):

# 공백을 두고 한줄로 출력 > 반복문으로
print(all_student[ii], end=" ")

# 반복문 뒤에서부터 출력
for ii in range(len(all_student)-1, -1, -1):

# 입력값 정수형 리스트로 저장
data = list(map(int, input().split()))

# 바둑판 리스트컴프리헨션
- 기본 :  a = [0 for i in range(20)]
badok = [[0 for i in range(20)] for j in range(20)]


# 코드업 바둑판 10자 뒤집기 6096
badok_arr = [[0 for i in range(19)] for j in range(19)]
# 입력 값 바둑판 생성
for a in range(19):
    data = list(map(int, input().split()))
    for b in range(len(data)):
        badok_arr[a][b] = data[b]

input_chk = int(input())
for change_n in range(input_chk):
    get_num = input().split()
    get_i = int(get_num[0])-1
    get_j = int(get_num[1])-1

    for i in range(19):
        if badok_arr[get_i][i] == 1:
            badok_arr[get_i][i] = 0
        else:
            badok_arr[get_i][i] = 1
    for i in range(19):
        if badok_arr[i][get_j] == 1:
            badok_arr[i][get_j] = 0
        else:
            badok_arr[i][get_j] = 1
            
# 코드업 설탕과자 뽑기 6067
x_a, y_a = map(int, input().split())
all_width = [[0 for i in range(y_a)] for j in range(x_a)]


for_num = int(input())
for a in range(for_num):
    l, d, x, y = map(int, input().split())
    # 가로
    if d == 0:
        for ld in range(l):
            all_width[x-1][y-1+ld] = 1
    else:
        # 세로
        for pt in range(l):
            all_width[x-1+pt][y-1] = 1


for ii in range(x_a):
    for jj in range(y_a):
        print(all_width[ii][jj], end=" ")
    print()


# 출력
for ii in range(19):
    for jj in range(19):
        print(badok_arr[ii][jj], end=" ")
    print()
'''