s=str(input()).split(' ')
s1=''
for i in s[::-1]:
	s1+=i[::-1]+' '
print(s1)
