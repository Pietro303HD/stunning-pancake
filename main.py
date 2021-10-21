class Pancake:
  def __init__(self):
    self.stacks = []

  def append(self, stack):
    self.stacks.append(stack)

class InputSelect:
  def __init__(self, options):
    self.options = options

  def input(self):
    for option in options:
      print(f"[0] {option}")

print("Welcome to 'Pancake Simulator 2022'.")
print("What would you like to do?")
