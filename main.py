class Stack:
  # Holds a value;
  def __init__(self, value):

class Pancake:
  # Contains multiple stacks;
  def __init__(self):
    self.stacks = []

  def append(self, stack):
    self.stacks.append(stack)

class InputSelect:
  # Selection menu using input();
  def __init__(self, options):
    self.options = options

  def input(self):
    for option in self.options:
      index = self.options.index(option)
      print(f"[{index}] {option}")

    index = int(input("=> "))
    return self.options[index], index


pancakeSelect = InputSelect(["Create a new pancake.", "Import already existing pancake."])

print("Welcome to 'Pancake Simulator 2022'.")
print("What would you like to do?")
pancakeSelect.input()
