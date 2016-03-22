a, b ,c = raw_input().split()
a = int(a)
b = int(b)
c = int(c)

maior = (a+b+abs(a-b)) / 2

if (c>maior):
	print "%i eh o maior" %c
else:
	print "%i eh o maior" %maior