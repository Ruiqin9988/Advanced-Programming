import math

percent_float = float(input("what is your percentage? :"))
print("Total score: ", percent_float)

if 90 <= percent_float < 100:
  print("You received an A")
elif 80 <= percent_float < 90:
  print("You received an B")
elif 70 <= percent_float < 80:
  print("You received an C")
elif 60 <= percent_float < 70:
  print("You received an D")
else:
  print("oops, not good as well")
