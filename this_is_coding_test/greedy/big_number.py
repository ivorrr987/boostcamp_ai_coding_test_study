# '이것이 코딩 테스트다' p92
# '큰 수의 법칙' 

# 주어진 수들을 M번 더하여 가장 큰 수를 만들어야 함.
# 하지만 배열의 특정 인덱스에 해당하는 수가 연속해 K번 초과하여 더해질 수는 없음.

# 첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어짐.
# 각 자연수는 공백으로 구분.
# 둘째 줄에 N개의 자연수가 주어짐. 
# 각 자연수는 공백으로 구분하고 각 자연수는 1 이상 10000 이하의 수로 주어짐.
# K<=M

# 책의 방식대로 짠 solution 함수.
def solution():
    n, m, k = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    
    numbers = sorted(numbers)
    max1 = numbers[-1]
    max2 = numbers[-2]

    return (m // (k+1)) * (k * max1 + max2) + (m % (k+1)) * max1

# notion의 test cases를 활용하기 위해 짠 solution 함수.
# 만약 수작업으로 case를 넣어보는게 아닌, notion의 test case table을 활용하려면 코테 연습문제를 풀어볼 때 아래처럼 test.py의 test_by_cases 코드를 고려해서 짜야함.
def solution2(input):
    input = input.split("\n")
    input[0] = input[0].split()
    input[1] = input[1].split()
    n, m, k = list(map(int, input[0]))
    numbers = list(map(int, input[1]))

    numbers = sorted(numbers)
    max1 = numbers[-1]
    max2 = numbers[-2]

    return (m // (k+1)) * (k * max1 + max2) + (m % (k+1)) * max1

