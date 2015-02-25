d ={}

with open("data/19.data", 'r', encoding="UTF-8") as inf:
    for st in inf:
        s = st.strip()
        if s in d:
            d[s] += 1
        else:
            d.update({s: 0})

m = max(d.values())
res = sorted([k for k,v in d.items() if v==m])

for r in res:
    print (r, end=", ")

