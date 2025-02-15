a=[1,2,3,4,5]
a.remove(3)
print(a)
print(len(a))

#if more than one specific value remove() remove first one
s=[10,11,11,11,13]
s.remove(11)
print(s)
print(len(s))

#pop specific index

p=["afa","apu","vai"]
p.pop(0)
print(p)


#if do not specify the index remove last item
n=[4,5,8]
n.pop()
print(n)


#del keyword remove specific

m=["s",12,23.4]
print(m)
del m[0]
print(m)
del m
#print(m)

c=[12,213.3,32434]
print(c)
c.clear()
print(c) #list still remain ,but it has no content