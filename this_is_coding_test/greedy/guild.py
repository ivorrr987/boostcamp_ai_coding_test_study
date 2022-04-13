# '이코테' (p.311)
# '모험가 길드'

# 첫째줄에 모험가의 수 N
# 둘째줄에 N명의 모험가. 공백으로 구분하고 각 모험가의 공포도로 표현됨.

# 각 모험가는 자신의 공포도와 같은 숫자의 길드원으로 이루어진 길드에 들어가야만 함.
# 예를 들어 공포도 3인 모험가는 자신 포함 최소 3명으로 이루어진 길드에 들어가야 함.

# 이런 식으로 길드를 구성할 때 만들어질 수 있는 최대의 길드 수를 구하는 프로그램을 작성.
# 몇명의 모험가는 마을에 남아 있어도 됨.

def solution(input):
    # input은 \n을 포함한 문자열.(입력이 두개의 줄에 걸쳐 이루어지므로)
    input = input.split("\n")
    n = int(input[0])
    fears = list(map(int, input[1].split(' ')))
    fears = sorted(fears, reverse=True)

    i = 0
    cnt = 0
    while i<len(fears):
        i += fears[i]
        cnt += 1
    return cnt

if __name__ == '__main__':
    input1 = '5\n2 3 1 2 2'
    print(solution(input1))
