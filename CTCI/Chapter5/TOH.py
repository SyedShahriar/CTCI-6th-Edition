def TOH(n,A,C,B):

	if n==1:
		print "Move Disk 1 from "+ A + " to " + C
		return

	TOH(n-1,A,B,C)

	print "Move Disk " + str(n) + " from " + A + " to " + C

	TOH(n-1,B,C,A)
	
if __name__ == '__main__':
	print TOH(3,"A","C","B")

