def rechenArt():
  print("1: +\n2: -\n3: /\n4: *\n\n")
  z = input("Welche Rechenart? ")
  if int(z) == 1:
    add()
  elif int(z) == 2:
    sub()
  elif int(z) == 3:
    div()
  elif int(z) == 4:
    mul()
  else:
    print("\nExit")


def add():
  a = input("\nGebe den ersten Wert an: ")
  b = input("Gebe den zweiten Wert an: ")
  c = int(a) + int(b)
  print(f"= {c}")


def sub():
  a = input("Gebe den ersten Wert an: ")
  b = input("Gebe den zweiten Wert an: ")
  c = int(a) - int(b)
  print(f"= {c}")


def div():
  a = input("Gebe den ersten Wert an: ")
  b = input("Gebe den zweiten Wert an: ")
  c = int(a) / int(b)
  print(f"= {c}")


def mul():
  a = input("Gebe den ersten Wert an: ")
  b = input("Gebe den zweiten Wert an: ")
  c = int(a) * int(b)
  print(f"= {c}")


print("This code is by SimplePyCode\n\nCalculator v1.0\n\n")
rechenArt()