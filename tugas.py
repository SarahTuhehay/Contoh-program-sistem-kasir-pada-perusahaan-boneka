#Sarah Tuhehay_202351009
#Rianti Tomatala_202351005

boneka = int(input("Masukan jumlah boneka: "))
if boneka <=12:
    print("Harga perboneka Rp 20000\n ")
    print("Total", boneka * 20000)
elif boneka <=24:
    print("Harga perboneka Rp 19.500\n")
    print("Total", boneka * 19500)
elif boneka <=50:
    print("Harga perboneka Rp 18000\n")
    print("Total", boneka * 18000)
else:
    print("Harga perboneka Rp 17000\n")
    print("Total", boneka * 17000) 
    
print("Terimakasih sudah berbelanja")