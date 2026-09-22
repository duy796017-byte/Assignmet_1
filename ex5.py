def Khoiluong(t, p, l):
  print("tổng khối lượng là", (((t*20+p)*32+l)*13.3)//1000, "KG và",(((t*20+p)*32+l)*13.3)%1000 ,"G")
t=float(input("nhập khối lượng (talent):"))
p=float(input("nhập khối lượng (pound):"))
l=float(input("nhập khối lượng (lot):"))
Khoiluong(t, p, l)
