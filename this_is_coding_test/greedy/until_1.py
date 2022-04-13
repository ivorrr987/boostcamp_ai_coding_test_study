# '이코테' p99
# '1이 될 때까지'

# 어떠한 수 N에 대해 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
# 1. N = N-1
# 2. N / K (only when N % K == 0)
# N이 1이 될때까지 두 과정 중 하나를 수행할 때 과정을 수행하는 최소 횟수를 구하여라.

# 2 <= N <= 100000, 2 <= K <= 100000
# N,K가 공백으로 구분되어 자연수로 주어짐.
# 이때 항상 N > K

def solution():
    n, k = list(map(int, input().split()))
    cnt = 0

    while n > 1:
        if n % k == 0:
            cnt += 1
            n = n // k
            # print(f"n={n}, cnt={cnt}")
        else:
            cnt += n % k
            n -= n % k
            # print(f"n={n}, cnt={cnt}")

    return cnt
def solution2(input):
    n, k = list(map(int, input.split()))

    cnt=0
    while n > 1:
        if n >= k:
            if n % k == 0:
                cnt += 1
                n = n // k
                # print(f"n={n}, cnt={cnt}")
            else:
                cnt += n % k
                n -= n % k
                # print(f"n={n}, cnt={cnt}")
        else:
            cnt += 1
            n -= 1

    return cnt

if __name__ == '__main__':
    print("hello")
    input1 = '25 5'
    print(solution2(input1))