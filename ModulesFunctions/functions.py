def python_food():
  print("pandas and dogs")


def center_text(*args, sep=" ", end="\n", file=None, flush=False):
  text = "" 
  for arg in args:
    text += str(arg) + sep
  left_margin = (70 - len(text)) // 2
  print(" " * left_margin, text, end=end, file=file, flush=flush)

center_text("first", "second", 3, 4, "pandas")
