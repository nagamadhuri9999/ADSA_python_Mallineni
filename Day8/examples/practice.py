# for i in range(10,0,-1):
#     print(i)
# i=20
# while i>10:
#     print(i-10)
#     i-=1
   
def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
count(10)


    
    