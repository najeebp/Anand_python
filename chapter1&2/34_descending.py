def descendind(a):
	freequency={}
	l=[]
	for q in a:
		freequency[q]=freequency.get(q,0)+1
	l.append(freequency)
	print l[0]
#	b=freequency.sort(key=lambda x=freequency.values())
#	print b
#	c=b.sort()
#	print c
	print freequency
	k=[]
	r=[4,7,5,8]
	print freequency.values().sort()
descendind('asian paintssssssss apex')
