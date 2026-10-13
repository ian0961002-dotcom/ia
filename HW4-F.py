a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
  if a == b == c:
    print("Equilateral")
  elif a == b or a == c or b == c:
    print("Isosceles")
  else:
    print("Scalene")
else:
  print("Invalid")