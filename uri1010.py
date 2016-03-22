cod1, nro1, value1 = raw_input().split()
cod2, nro2, value2 = raw_input().split()

cod1 = int(cod1)
cod2 = int(cod2)
nro1 = int(nro1)
nro2 = int(nro2)
value1 = float(value1)
value2 = float(value2)

print "VALOR A PAGAR: R$ %.2f" %((nro1 * value1) + (nro2 * value2))

