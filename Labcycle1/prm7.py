y={"e":5,"a":1,"f":6,"b":2,"d":4,"c":3}
l=list(y.items())
l.sort()
print("Ascending oreder",l)
l=list(y.items())
l.sort(reverse=True)
print("Descending order",l)
dict=dict(l)
print("Dictionary",dict)