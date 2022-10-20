m = [1,2,'a',4,5,'6']
s = [x for x in m if isinstance(x, str)]
i = [x for x in m if isinstance(x, int)] 


for x in m:
    if isinstance(x, int):
        i.append(x)
    elif isinstance(x, str):
        s.append(x)
        
print(i)
print(s)