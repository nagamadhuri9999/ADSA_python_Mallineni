from collections import deque

q=deque() 
q.append(10)#enqueu
q.append(20)
q.append(30)
print(q.popleft())#dequeue 
print(q[0])#peek