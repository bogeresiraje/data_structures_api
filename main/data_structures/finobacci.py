

def fino(n):  
   if n <= 1:  
       return n  
   else:  
       return(fino(n-1) + fino(n-2))


def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n-1)