def python_food():
  print("pandas and dogs")


def center_text(*args, sep=" "):
  text = "" 
  for arg in args:
    text += str(arg) + sep
  left_margin = (70 - len(text)) // 2
  return " " * left_margin + text

print(center_text("first", "second", 3, 4, "pandas"))
