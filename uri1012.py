PI = 3.14159

a, b ,c = raw_input().split()
a = float(a)
b = float(b)
c = float(c)
print "TRIANGULO: %.3f" %(a * c / 2)
print "CIRCULO: %.3f" %(PI * (c * c))
print "TRAPEZIO: %.3f" %(c * ((a+b) / 2))
print "QUADRADO: %.3f" %(b * b)
print "RETANGULO: %.3f" %(a * b)
