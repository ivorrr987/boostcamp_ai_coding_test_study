# '이것이 코딩테스트다' p96
# '카드 게임'

# 숫자가 쓰인 카드들이 N x M 형태로 놓여있다. N은 행의 개수, M은 열의 개수.
# 행을 먼저 선택.
# 해당 행에서 가장 숫자가 낮은 카드가 선택됨.
# 이러한 규칙을 감안했을 때 가장 높은 카드를 뽑을 수 있는 알고리즘을 만들어라.

# N, M이 공백으로 구분되어 입력됨.
# 1<=N, M<=100
# 둘째줄부터 N+1번째 줄까지(N개 줄에 걸쳐) 각 카드의 숫자가 입력됨.
# 각 숫자는 1 이상, 10000 이하

# 게임의 룰에 맞게 선택된 숫자가 출력됨.

def solution():
    n, m = list(map(int, input().split()))
    rows = [list(map(int, input().split())) for row in range(n)]
    nums = [min(row) for row in rows]

    return max(nums)

def solution2(input):
    input = input.split("\n")
    input[0] = input[0].split()
    n, m = list(map(int, input[0]))
    rows = [list(map(int, row.split())) for row in input[1:]]
    nums = [min(row) for row in rows]

    return max(nums)
