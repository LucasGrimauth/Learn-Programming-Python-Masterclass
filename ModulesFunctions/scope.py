def fact(n):
  result = 1
  if n > 1:
    for f in range(2, n+1):
      result *= f
  return result

def recfact(n):
  if n <= 1:
    return 1
  else:
    return n * recfact(n-1)

for i in range(10):
  print(i, recfact(i))