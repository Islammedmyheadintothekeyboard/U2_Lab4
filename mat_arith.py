# There is no need to import SAMPLE_MATRICES
# Donovan Farley-Freeman
# 10/3/24
# Creating functions to add and multiply matrices



def mat_sum(m1, m2):
  m1m = len(m1)
  m1n = len(m1[0])
  m2m = len(m2)
  m2n = len(m2[0])
  mn1 = str(m1m) + str(m1n)
  mn2 = str(m2m) + str(m2n)
  if mn1 == mn2:
    new = [[0]*m1m for i in range(m1n)]
    for row in range(m1m):
      for column in range(m1n):
        new[row][column] = (m1[row][column]+m2[row][column])
    return new
  else:
    return "no solution"



def mat_mul(m1, m2):
  m1m = len(m1)
  m1n = len(m1[0])
  m2m = len(m2)
  m2n = len(m1[0])
  if m1n == m2m:
    new = [[0]*m1m for i in range(m2n)]
    for row in range(m1m):
      for column in range(m2n):
        solution = 0
        for i in range(idk):
          solution += tempsol
  else:
    return "no solution"