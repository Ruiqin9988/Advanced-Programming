# average of a sum integers ina given range 
limit_str = input ("Range is 1 to input:")
limit_int = int (limit_str)

count_int = 1
sum_int = 0
while count_int <= limit_int:
  sum_int = sum_int + count_int
  count_int= count_int + 1 
average = float(sum_int)/(count_int - 1)

print("The value is ", average)
