a=1
j=7
n1=n2=0
while a<=100:
	if a<10:
		if a%7==0 :
			a=a+1
			continue
		print(a)
		a=a+1
	elif a<100:
		if a%7==0 :
			a=a+1
			continue
		n1=a%10
		n2=(a/10)%10
		if n1==7:
			a=a+1
			continue
		if n2==7:
			a=a+1
			continue
		if a/10==7:
			a=a+1
			continue
		print (a)
		a=a+1
	else:
		print (a)
		a=a+1
#print ("end go ...")