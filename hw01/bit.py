"""
File: Bit Maps Solution
Author: Juan Diego Collazos
Date: 1/24/25
"""
from sys import stdin

MAX = 200
SIZE_LINE = 50

bit_map = ''
index = 0
matrix = [[0 for _ in range(MAX)] for _ in range(MAX)]
type_bitmap = {'B' : 'D', 'D' : 'B'}
N, M = 0, 0;

def quadrants(row_interval, col_interval):
  l_row, r_row = row_interval
  l_col, r_col = col_interval
  md_row, md_col = md(row_interval), md(col_interval)
  return [(l_row, md_row), (md_row, r_row)], [(l_col, md_col), (md_col, r_col)]

def get(i, j):
  return int(bit_map[i * M + j])

def md(interval):
  l, r = interval
  return ((r + l) >> 1) + (r - l) % 2;

def size(interval):
  return interval[1] - interval[0]

def fi_compress(row_interval, col_interval):
  if size(row_interval) <= 0 or size(col_interval) <= 0:
    ans = []
  elif size(row_interval) == 1 and size(col_interval) == 1:
    ans = [str(matrix[row_interval[0]][col_interval[0]])]
  else:
    ranges_row, ranges_col = quadrants(row_interval, col_interval)
    ans = ['D']
    flag, aux = True, ''
    for row in ranges_row:
      for col in ranges_col:
        q = fi_compress(row, col)
        if len(q) > 0:
          ans.extend(q)
          if not aux: 
            aux = q[0]
          if q[0] != aux:
            flag = False

    if flag and aux != 'D':
      ans = [str(aux)]

  return ans;

def fi_uncompress(row_interval, col_interval):
  global index
  if not (size(row_interval) <= 0 or size(col_interval) <= 0):
    index += 1
    if bit_map[index] == 'D':
      ranges_row, ranges_col = quadrants(row_interval, col_interval)
      for row in ranges_row:
        for col in ranges_col:
          fi_uncompress(row, col)
    else:
      for i in range(row_interval[0], row_interval[1]):
        for j in range(col_interval[0], col_interval[1]):
          matrix[i][j] = int(bit_map[index])


def main():
  global bit_map, index, N, M;
  info = stdin.readline().split();
  while len(info) > 1:
    t, N, M = info[0], int(info[1]), int(info[2]);
    print("%c %3d %3d" %(type_bitmap[t], N, M))

    if t == 'B':
      n = N * M
      i = j = k = 0
      while k < n:
        row = stdin.readline().strip()
        for bit in row:
          matrix[i][j] = bit
          k += 1; j += 1
          if j == M:
            j = 0; i += 1
      
      ans = fi_compress((0, N), (0, M))

      i = 0
      while i < len(ans):
        print("%c" %(ans[i]), end='')
        if (i + 1) % SIZE_LINE == 0:
          print()
        i += 1
      if i % SIZE_LINE:
        print()

    else:
      bit_map = stdin.readline().strip()

      index = -1
      fi_uncompress((0, N), (0, M))

      cnt = 0
      for i in range(N):
        for j in range(M):
          print(matrix[i][j], end='')
          if (cnt + 1) % SIZE_LINE == 0:
            print()
          cnt += 1
      if cnt % SIZE_LINE:
        print()

    info = stdin.readline().split();

main()