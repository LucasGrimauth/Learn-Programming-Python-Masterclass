def lasagna1():
  def lasagna2():
    def lasagna3():
      z = " even more lasagna"
      print("In lasagna3, locals are {}".format(locals()))
      return z

    y = " more lasagna" + x
    y += lasagna3()
    print("In lasagna2, locals are {}".format(locals()))
    return y
  
  x = "lasagna"
  x += lasagna2()
  print("In lasagna1, locals are {}".format(locals()))
  return x

print(lasagna1())