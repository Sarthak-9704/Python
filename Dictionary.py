D={"roll":10, "name":"sarthak"}
print(D["roll"])

D["Marks"]= 99
print(D)

up={"name":"jayani", "roll":1}
D.update(up)
print(D)
# del D["name"]

# print(D)

D.popitem()

# k1={1,2,3}
# v1={"sar"}

# d=dict.fromkeys(k1,v1)
print(D)