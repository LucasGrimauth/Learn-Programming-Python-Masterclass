import shelve

with shelve.open("ShelfTest") as fruit:
  fruit["orange"] = "a sweet, orange, citrus fruit"
  fruit["apple"] = "red and round"
  fruit["grape"] = "a small, sweet fruit growing in bunches"

  print(fruit["apple"])
  print(fruit["grape"])