import equations as eq

print("Enter province as 2 digit code in lowercase")


prov = input("Enter your province: ")

amount = input("Enter the sale amount: ")



if prov == "bc":
    print(eq.bc(amount) + float(amount))

if prov == "ab":
    print(eq.ab(amount) + float(amount))
    
if prov == "sk":
    print(eq.sk(amount) + float(amount))

if prov == "mn":
    print(eq.mn(amount) + float(amount))

if prov == "on":
    print(eq.on(amount) + float(amount))

if prov == "qc":
    print(eq.qc(amount) + float(amount))  

if prov == "nl":
    print(eq.nl(amount) + float(amount)) 

if prov == "pei":
    print(eq.pei(amount) + float(amount)) 

if prov == "ns":
    print(eq.ns(amount) + float(amount))

if prov == "nb":
    print(eq.nb(amount) + float(amount))

if prov == "nu":
    print(eq.nu(amount) + float(amount))

if prov == "yt":
    print(eq.yt(amount) + float(amount))

if prov == "nt":
    print(eq.nt(amount) + float(amount))