import math

point_str = input("Enter the lead in points: ")
point_remaining_int = int(point_str)

lead_calculation_float = float(point_remaining_int - 3)

has_ball_str = input("Does the lead team have the ball (Yes or No)")

if has_ball_str == 'Yes':
  lead_calculation_float = lead_calculation_float + 0.5
else:
  lead_calculation_float = lead_calculation_float - 0.5
  
if lead_calculation_float < 0:
  lead_calculation_float = 0
  
lead_calculation_float = lead_calculation_float ** 2

second_remaining_int = int(input("Enter the number of second remaining: "))

if lead_calculation_float > second_remaining_int:
  print("Lead is safe")
else:
  print("Lead is not safe")
