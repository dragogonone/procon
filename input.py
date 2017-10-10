### 一行n列
#2 4 5 7
#  例１ それぞれ別の変数にいれる
a, b, c, d = (int(i) for i in input().split())
# a=2 b=4 c=5 d =7

# 1行n列リスト
n = int(input())
inp = [int(_) for _ in input().split()]
# a = [2, 4, 5, 6]

# n行一列
n = int(input())
inp = [int(input()) for i in range(n)]
# t = [22, 14, 45]

#　n行m列
n = int(input())
inp = [[int(_) for _ in input().split()] for i in range(n)]

# n行m列　順番をふる
n = int(input())
inp = []
for i in range(N):
    x, y = map(int, input().split())
    inp.append((i, x, y))
# inp = ((0,3,5),(1,2,7),(2,6,89))