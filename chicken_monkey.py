# functions in PYTHON
def create_person(first_name, last_name, age, occupation):
  return {
    "first_name": first_name,
    "last_name": last_name,
    "age": age,
    "occupation": occupation
  }

james = create_person("james", "nitz", 27, "developer")
# numbys = list(range(1, 101))

def chicken_monkey(nums):
  for num in nums:
    if num % 5 == 0 & num % 7 == 0:
      print("ChickenMonkey")
    elif num % 7 == 0:
      print("Monkey")
    elif num % 5 == 0:
      print("chicken")
    else:
      print(num)

# chicken_monkey(numbys)
