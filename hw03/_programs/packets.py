from sys import stdin

N = 6

def greedy(order):
  ans = 0
  ans += order[0]
  ans += order[1]
  order[-1]  

def main():
  order = list(map(int, stdin.readline().split()))
  while sum(order) != 0:
    order.reverse()
    print(greedy(order))
    order = list(map(int, stdin.readline().split()))
