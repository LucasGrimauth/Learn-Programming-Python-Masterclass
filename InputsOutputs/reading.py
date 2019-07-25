# jabber = open("./text.txt", "r")

# for line in jabber:
#   print(line, end="")

# jabber.close()

# with open("./text.txt", "r") as jabber:
#   for line in jabber:
#     print(line, end="")

with open("./text.txt", "r") as jabber:
  lines = jabber.readlines()
print(lines)

for line in lines:
  print(line, end="")