def magicIndex(A,start,end):

	if end>=start:
		mid = (start+end)//2
		if A[mid]==mid: return mid

		if A[mid]>mid: return magicIndex(A,0,mid-1)
		elif A[mid]<mid: return magicIndex(A,mid+1,end)

if __name__ == '__main__':
	print magicIndex([0,1,3,5,7,8,9,10],0,7)