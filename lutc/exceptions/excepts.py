sep = "-" * 45 + "\n"
"""
print(sep + "EXCEPTION RAISED AND CAUGHT")
try:
    x = "spam"[99]
except IndexError:
    print("except run IndexError")
finally:
    print("finally run")
print("after run")

print(sep + "NO EXCEPTION RAISED")
try:
    x = "spam"[3]
except IndexError:
    print("except run IndexError")
finally:
    print("finally run")
print("after run")

print(sep + "NO EXCEPTION RAISED WITH ELSE")
try:
    x = "spam"[3]
except IndexError:
    print("except run IndexError")
else:
    print("else run")
finally:
    print("finally run")
print("after run")

print(sep + "EXCEPTION RAISED BUT NOT CAUGHT")
try:
    x = 1 / 0
except IndexError:
    print("except run IndexError")
finally:
    print("finally run")
print("after run")
"""
try:
    1 / 0
except Exception as X:
    print(X)
    saveit = X
print(X)
print(saveit)
