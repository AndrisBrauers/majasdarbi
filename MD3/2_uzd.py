m = [1,2,'a',4,5,'6']
i = []
s = []

for x in m:
    if isinstance(x, int):
        i.append(x)
    elif isinstance(x, str):
        s.append(x)
        
print(i)
print(s)