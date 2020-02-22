a=bin(int(input()))
l = list(a)[2:]
c = 0
d = []
a = l.index('1')
for i in range(a,len(l)-1):
	if l[i] == '1':
		c = c + 1
	else:
		d.append(c)
		c = 0
		if '1' not in l[a+1:]:
			break
		i = l[a+1:].index('1')
print(max(d))