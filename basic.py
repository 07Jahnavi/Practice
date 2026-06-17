# l=[2,3,1,5]
# ele=float('-inf')

# i=0
# while(i<=len(l)-1):
#     if(l[i]>ele):
#         ele=l[i]
#     i+=1
# print(ele)
# ele2=float('-inf')
# i=0
# while(i<=len(l)-1):
#     if(l[i]>ele2 and l[i]!=ele):
#         ele2=l[i]
#     i+=1
# print(ele2)



l=[2,3,1,5]
ele1=float('-inf')
ele2=float('-inf')

i=0
while(i<=len(l)-1):
    if(l[i]>ele1):
        ele2=ele1
        ele1=l[i]
    elif(l[i]!=ele1 and l[i]>ele2):
        ele2=l[i]
    i+=1
print(f"first is {ele1} and second is {ele2}")

hey 
