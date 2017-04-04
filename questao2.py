Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> global x
x=0
def soma(n):
  global x
  x+=n
  if n == 0:
    return x
  else:
    return soma(n-1)

print(soma(6))
