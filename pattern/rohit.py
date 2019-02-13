import numpy as np

n = int(input())
# arr = np.array([[n for x in range()]]) 
arr = np.add(np.zeros((n,n),dtype=np.int8),n)
for i in range(1,int((n+1)/2)+1):
    arr[i:n-i,i:n-i] = np.add(arr[i:n-i,i:n-i],-1)
print('\n'.join(' '.join(str(cell) for cell in row) for row in arr))
