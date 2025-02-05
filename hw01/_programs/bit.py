"""
File: Bit Maps Solution
Author: Juan Diego Collazos
Date: 1/31/25
"""

from sys import stdin

MAX = 200
SIZE_LINE = 50


bit_map = ''
index = 0
matrix = [[False for _ in range(MAX)] for _ in range(MAX)]
N, M = 0, 0


def quadrants(row_interval, col_interval):
  l_row, r_row = row_interval
  l_col, r_col = col_interval
  md_row, md_col = md(row_interval), md(col_interval)
  return [(l_row, md_row), (md_row, r_row)], [(l_col, md_col), (md_col, r_col)]


def get(i, j):
  return bit_map[i * M + j]


def md(interval):
  l, r = interval
  return ((r + l) >> 1) + (r - l) % 2;


def size(interval):
  return interval[1] - interval[0]


def compress(row_interval, col_interval):
  if size(row_interval) <= 0 or size(col_interval) <= 0:
    ans = []
  elif size(row_interval) == 1 and size(col_interval) == 1:
    ans = [str(get(row_interval[0], col_interval[0]))]
  else:
    ranges_row, ranges_col = quadrants(row_interval, col_interval)
    ans = ['D']
    flag, aux = True, ''

    for row in ranges_row:
      for col in ranges_col:
        q = compress(row, col)
        if len(q) > 0:
          ans.extend(q)
          if not aux: 
            aux = q[0]
          if q[0] != aux:
            flag = False

    if flag and aux != 'D':
      ans = [str(aux)]

  return ans;


def uncompress(row_interval, col_interval):
  global index
  if not (size(row_interval) <= 0 or size(col_interval) <= 0):
    index += 1 
    if bit_map[index] == 'D':
      ranges_row, ranges_col = quadrants(row_interval, col_interval)
      for row in ranges_row:
        for col in ranges_col:
          uncompress(row, col)
    else:
      for i in range(row_interval[0], row_interval[1]):
        for j in range(col_interval[0], col_interval[1]):
          matrix[i][j] = bool(int(bit_map[index])) 


def main():
  global bit_map, index, N, M;

  info = stdin.readline().split();
  while len(info) > 1:
    t, N, M = info[0], int(info[1]), int(info[2])
    
    data = []
    line  = stdin.readline().split()
    while len(line) == 1 and line[0][0] != '#':
      data.append(line[0])
      line = stdin.readline().split()

    bit_map = ''.join(data);

    print("%c %3d %3d" % ('D' if t == 'B' else 'B', N, M))

    if t == 'B':
      ans = compress((0, N), (0, M));
      i = 0;
      while i < len(ans):
        print("%c" %(ans[i]), end='');
        if (i + 1) % SIZE_LINE == 0:
          print()
        i += 1
      if i % SIZE_LINE:
        print()
    else:
      index = -1
      uncompress((0, N), (0, M))
      cnt = 0
      for i in range(N):
        for j in range(M):
          print(1 if matrix[i][j] else 0, end='')
          cnt += 1
          if cnt % SIZE_LINE == 0:
            print()
      if cnt % SIZE_LINE:
        print()

    info = line

main()
