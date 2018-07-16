def stairs(n):
	
	if n<=3: return n

	a=1
	b=2
	c=3

	for i in range(4,n+1):
		val = a + b + c
		a=b
		b=c
		c=val

	return val


if __name__ == "__main__":

	print stairs(100000)