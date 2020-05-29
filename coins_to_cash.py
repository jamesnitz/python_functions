def calc_dollars(**coins):
  total = 0
  for key, value in coins.items():
    if key == 'pennies':
      penny_total = value / 100
      total += penny_total
    elif key == 'nickels':
      nickel_total = value / 20
      total += nickel_total
    elif key == 'dimes':
      dime_total = value / 10
      total += dime_total
    elif key == 'quarters':
      quarter_total = value / 4
      total += quarter_total
  print(total)

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)