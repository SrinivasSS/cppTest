def exp(num):
	return 2.7**num
def eveodd(num):
	return num%2==0
s=["This is a string"]
nums=[1,24,5,0,9,11,6,12,13,15]
print "Exponenttial of nums using map():", map(exp,nums) #Maps a function to an iterable item
print "Even odd of nums using filter():", filter(eveodd, nums) #Returns value only is condition met
print "String Reversal lambda expr:", map(lambda s:s[::-1],s)



