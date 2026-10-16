text=str(input())


K=0
currentlen=0


for i in text:
	if i!=' ' and i!=',' and i!='.':
		currentlen+=1
	else:
		K=max(K,currentlen)
		currentlen=0

albt=sorted('qwertyuiopasdfghjklzxcvbnm')
albt+=albt
Albt=sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
Albt+=Albt

nia=0 # number of the character in alphabet
newtext=''
for i in text:
	if i in albt:
		for char in range(26):
			if str(i)==str(albt[char]):
				nia=char
		newtext+=albt[nia+K]
	elif i in Albt:
		for char in range(26):
                        if str(i)==str(Albt[char]):
                                nia=char
		newtext+=Albt[nia+K]
	else:
		newtext+=i
	nia=0

print(K)
print(text)
print(newtext)
