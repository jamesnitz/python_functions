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

dollarAmount = 8.69
piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

def coin_star(money):
  while True:
    if money > .25:
      quarters = (money // .25)
      money = money - (quarters * .25)
      money = round(money, 2)
      piggyBank["quarters"] = quarters
    elif money > .10:
      dimes = (money // .10)
      money = money - (dimes * .10)
      piggyBank["dimes"] = dimes
    elif money > .05:
      nickels = (money // .05)
      money = money - (nickels * .05)
      money = round(money, 2)
      piggyBank["nickels"] = nickels
    elif money > .01:
      pennies = (money // .01)
      money = money - (pennies * .01)
      piggyBank["pennies"] = pennies
      break

coin_star(dollarAmount)
