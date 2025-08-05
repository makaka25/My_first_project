print('OOOOOH')
print('egdv')
h=input()
sum1=''
f=''
el_lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
el_upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
g=''
s=[]

for r in h:
    if r.isalpha():
        f+=r
    else:  
        total=len(f)
        for t in f:
            if t in el_lower:
                t=el_lower[(el_lower.index(t)+total)%26]
            else:
                t=el_upper[(el_upper.index(t)+total)%26]
            sum1+=t
        sum1+=r
        f=''
    g+=sum1
    sum1=''
g+=sum1    
                  
print(s)
print(g)