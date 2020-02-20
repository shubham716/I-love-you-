
n=s=0
p=input('Enter your name:-')
q=input("Enter your partner name:-")
print()
if(n==0):
	for i in p:n=n+1
	for i in q:s=s+1
	t=p+' '*(10-n)
	v=q+' '*(10-s)
	print('  *  *   *  *  ')
	print('*      *      *')
	for j in[t,v]:print(f'*   {j}*')
	for i in [1,2,4]:print(' '*i+'*'+' '*(13-2*i)+'*')
	print('       *')
	
