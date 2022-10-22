src = not False and True or False and not True
src = True and True or False and False
src = True or False # 1+0=1
result = True  # TODO подставить результат выражения

print(src == result)