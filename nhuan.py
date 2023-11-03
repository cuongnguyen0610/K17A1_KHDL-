n=int(input("mời nhập vào số năm:"))
if n in (1,3,5,7,8,10,12):
    print("tháng bạn vừa nhập có 31 ngày")
elif n in (4,6,9,11):
    print("tháng bạn vừa nhập có 30 ngày")
elif n==2:
    t=int(input("mời nhập lại năm "))
    if (t%4==0 and t%100!=0) or t%400==0):
        print(f"{t} là năm nhuận")
    else:
        print(f"{t} không pahri năm nhuận")
else:
    print("năm bạn vừa nhập có lỗi")            
