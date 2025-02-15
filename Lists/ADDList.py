a=[1,32,3]
a.append(4)
print(a)

s=["LA" ,"ams" ,3]
print(len(s))
s.append(True)
print(s)
print(len(s))

#insert

s.insert(1,"WOW")
print(s)
print(len(s))

#extend
q=[1,2,3]
w=[6,7,8]
print(len(q))
q.extend(w)
print(q)
print(len(q))

w.extend(q)
print(w)
print(len(w))