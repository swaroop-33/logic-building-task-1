u="admin"
p="1234"
iu="admin"
ip="1234"
print("Login Successful" if iu==u and ip==p else "Invalid Credentials")

m=[45,78,90,33,60]
pc=0
fc=0
for x in m:
    pc+=x>=50
    fc+=x<50
print(pc,fc)

n=[" Alice ","bob"," CHARLIE "]
c=[x.strip().lower() for x in n]
print(c)

msg=["Hi","Welcome to the platform","OK"]
for x in msg:
    l=len(x)
    print(l,"FLAG" if l>10 else "")

log=["INFO","ERROR","WARNING","ERROR"]
e=0
for x in log:
    e+=x=="ERROR"
print(e)
