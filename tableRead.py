for line in sys.stdin:
	l.append(line)
df=pd.DataFrame(l)
l.columns=['input']
fist=df['input'].str.split('\t',n=1,expand=True)


df['first']=fist[0]
df['second']=fist[1]
df['second']=df['second'].str.strip()
df2=df['first','second']


df2['first']=pd.to_numeric(df2['first'],errors='coerce')
df2['second']=pd.to_numeric(df2['second'],errors='coerce')
