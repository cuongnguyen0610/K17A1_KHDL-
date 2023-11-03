n = int(input("nhập số phần tử lớn hơn 2:"))
A = []
for i in range(0,n):
	A.append(int(input('phần tử thứ %d:'  %(i+2))))
d = A[1] - A[0]
kt = True;
i = 1;
while (kt == True) and (i<n):
	if A[i] - A[i-1] != d: kt = False
	i = i + 1
	break
if kt == True: print(" Dãy số tạo thành cấp số cộng")
else: print("dãy số không phải tạo thành cấp số cộng")	