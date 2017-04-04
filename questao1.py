Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=0
def imprima(x,y):
  print(x)
  if x == y:
    return ""
  else:
    return imprima(x+1,y)
y=int(input("informe y :"))
print(imprima(x,y))
