print "Hello World!"
## Test
c = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
d = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,]

## Assignment
e = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7,1,6,9,3,9,9,3,7,5,1,0,5,8,2,0,9,7,4,9,4,4,5,9,2]
f = [2,7,1,8,2,8,1,8,2,8,4,5,9,0,4,5,2,3,5,3,6,0,2,8,7,4,7,1,3,5,2,6,6,2,4,9,7,7,5,7,2,4,7,0,9,3,6,9,9,9,5,9,5,7,4,9,6,6,9,6,7,6,2,7]

## General case
a = [1,2,3,4]
b = [3,4]

def li_to_num(a):
    m = len(a)
    res = 0
    for i in range(m-1,-1,-1):
        res = res + a[i]*10**(m-1-i)
    return res

def num_to_li(a):
    ret = a
    out = []
    while ret:
        temp = ret%10
        out.append(temp)
        ret = ret/10
    out.reverse()
    return out

def kara(a,b):
    if len(a) == 1 or len(b) == 1:
        return li_to_num(a) * li_to_num(b)
    
    n = len(a)
    i = n/2
    m = len(b)
    j = m/2
    
    kara_a = li_to_num(a)
    kara_b = li_to_num(b)
    
    k_a = kara_a/10**(i)
    k_b = kara_a%10**(i)
    k_c = kara_b/10**(j)
    k_d = kara_b%10**(j)
    
    k_ac = kara(a[0:i], b[0:j])
    k_bd = kara(a[i:len(a)], b[j:len(b)])
    #k_ad_bc = kara(num_to_li(k_a+k_b), num_to_li(k_c+k_d)) - k_ac - k_bd
    k_ad = kara(a[0:i], b[j:len(b)])
    k_bc = kara(a[i:len(a)], b[0:j])
    
    #res = k_ac*10**(i+j) + k_ad_bc*10**(max(i,j)) + k_bd
    res = k_ac*10**(i+j) + k_ad*10**(i) + k_bc*10**(j) + k_bd
    return res

result = kara(e,f)
result = num_to_li(result)
res = ''
for element in result:
    res = res+str(element)
print res
