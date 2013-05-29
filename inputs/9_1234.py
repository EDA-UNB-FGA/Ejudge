inputs = raw_input()
[a, b] = inputs.split()

a = int(a)
b = int(b)
c = a + b

if c < 10:
	print c
else:
	print '0'
