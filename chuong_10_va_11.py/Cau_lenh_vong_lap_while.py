# Cau lenh vong lap while
n = 10
while n > 2:#True
    print(f"chay vong lap {n}")
    n = n - 1 

#Vong lap while cung ho tro: break, continue va else
#Break
n = 10
while n > 2:#True
    print(f"chay vong lap {n}")
    n = n - 1 
    if n == 6:
        break 

#Continue
n = 10
while n > 2:
    n = n - 1 
    if n == 6:
        continue
    print(f"chay vong lap {n}")

#Else
n = 10
while n > 2:#True
    print(f"chay vong lap {n}")
    n = n - 1 
    if n == 6:
        break
else:
    print("chay cau lenh else")


n = 10
while n > 2:
    print(f"chay vong lap {n}")
    n = n - 1
    if n == 6:
        continue
else:
    print("chay cau lenh else")
#Tim so nguyen to lon nhat nho hon hoac bang 20
n = 20
while True:
    for i in range(1,n):
        if n%i==0 and i!=1 and i!=n:
            print("so nay khong phai so nguyen to")
            break
    else:
        break

    if n < 1:
        break        

print(f"day la so nguyen to")  


n = int(input("nhap gia tri nguyen "))