
def knapsack(val, wt, cap):
    
    index = list(range(len(val)))#[0,1,2]
    
    ratio = [v/w for v,w in zip(val,wt)]#[5,6,4]
    
    index.sort(key = lambda x: ratio[x], reverse=True)  #sorting [1,0,2]
    
    max_value=0
    
    frac = [0]*len(val)
    
    for i in index:
        if wt[i]<=cap:
            
            frac[i] = 1
            max_value+=val[i]
            cap-=wt[i]
        else:
            frac[i]= cap/wt[i]
            max_value+=val[i]*cap/wt[i]
            break
    return max_value
            
print("Enter values for a weight: ")
val = [int(x) for x in input().split()]
print("Enter weights: ")
wt =[int(x) for x in input().split()]
capacity = int(input("Enter a capacity of a bag: "))

print(knapsack(val, wt, capacity))


