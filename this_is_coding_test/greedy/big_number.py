# '이것이 코딩 테스트다' p92

# 주어진 수들을 M번 더하여 가장 큰 수를 만들어야 함.
# 하지만 배열의 특정 인덱스에 해당하는 수가 연속해 K번 초과하여 더해질 수는 없음.

# 첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어짐.
# 각 자연수는 공백으로 구분.
# 둘째 줄에 N개의 자연수가 주어짐. 
# 각 자연수는 공백으로 구분하고 각 자연수는 1 이상 10000 이하의 수로 주어짐.
# K<=M



def solution():
    n, m, k = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    if len(numbers) != n:
        raise Exception("n개의 자연수를 입력해야 합니다")
    elif min(numbers) < 1:
        raise Exception("자연수를 입력해야 합니다.")
    
    numbers = sorted(numbers)
    max1 = numbers[-1]
    max2 = numbers[-2]

    return (m // (k+1)) * (k * max1 + max2) + (m % (k+1)) * max1



print(solution())
