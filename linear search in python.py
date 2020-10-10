def linearSearch(arr,item):
    arr1=[]
    flag=False
    for i in range(len(arr)):
        if arr[i]==item:
            flag=True
            arr1.append(i)
    
    if flag==True:
        for i in arr1:
            print(f"{item} Found in Index {i}")
    else:
        print("element not found")
   

arr=[6,8,5,5,0,3,2,7]
print(arr)
item=int(input("Enter Element You Want To Search: "))
linearSearch(arr,item)
