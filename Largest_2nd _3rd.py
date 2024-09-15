# Largest, 2nd , 3rd

def largest(arr):
    # arr.sort()
    # max = arr[0]
    # for i in arr[1:]:
    #     if i > max:
    #         max = i
    #     else:
    #         continue
    # return max
        
    fmax = smax = tmax = 0
    
    for i in arr:
      if i > fmax:
        tmax = smax
        smax = fmax
        fmax = i
      elif i > smax and i != fmax:
        tmax = smax
        smax = i
      elif i > tmax and i != fmax and i != smax:
        tmax = i
        
    return tmax,smax
        
        
    
    
print(largest([50,2,7,9,6,22,2]))