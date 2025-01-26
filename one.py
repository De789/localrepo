# numbers=range(1,11)
# res=list(filter(lambda x:x%2,numbers))
# print(res),

d="Maheshshhsh"
new={}
for x in d:
    if x not in new.keys():
        new[x]=1
    else:
        new[x]+=1
print(new)
for k,v in new.items():
    print(f"{k} occured in {v} times")
