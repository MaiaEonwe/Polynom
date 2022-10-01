
import math,re
#f(x)=5x**3+5x**2+12x+5
def polynom_check(x,y):
    a=re.findall("-?\d\w\**\d|-?\d\w|-?\d",x)
    b=re.findall("\+|\-",x)
    print(a)
    print(b)
    el_sayi=len(a)
    us_sayi=0
    index=0
    index1=0
    index2=0
    us1=0
    c=[]
    us_bul=[]
    for i in a:
        c.append(re.findall("^-?\d+",i))
        us_bul.append(re.findall("\**\d+$|\w$",i))
    for x in us_bul:
        for v in x:
            index2+=1
            if "**" in v:
                us_bul[index2-1]=[v.replace("**","")]
        for h in x:
            index1+=1
            if h == "x":
                us_bul[index1-1]=[1]
        for r in x:
            us1+=1
            filter=re.findall("^-?\d+$",r)
            for t in filter:
                if r == t:
                    us_bul[us1-1]=[r.replace(t,"0")]
        for u in us_bul:
            us_sayi+=1
    print(us_bul)
    #print(us_bul)
    #print(c)
    #print(d)
    def polynom(x,y):
        def power_and_baskat(x,y):
            islem1=0
            islem2=0
            powerv=[]
            baskat=[]
            ind1=0
            ind2=0
            indx1=1
            indx2=0
            y=int(y) 
            for g in us_bul:
                for powerv1 in g:
                    powerv.append(powerv1)
            for k in c:
                for baskats in k:
                    baskat.append(baskats) 
            def polyn_islem(y):
                y=int(y)
                ind1=0
                ind2=0
                indx1=0
                islem=0
                if "-" in baskat[0]:
                    islem+=int(baskat[ind1])*(pow(y,int(powerv[ind2])))
                    ind1+=1
                    ind2+=1
                for kalan_is in range(0,el_sayi):
                    if b[indx1] =="+":
                        islem+=int(baskat[ind1])*pow(y,int(powerv[ind2]))
                        ind1+=1
                        ind2+=1
                        indx1+=1
                    elif b[indx1]=="-":
                        islem-=int(baskat[ind1])*pow(y,int(powerv[ind2]))
                        print(type(islem))
                        print(type(baskat))
                        print(type(powerv))
                        ind1+=1
                        ind2+=1
                        indx1+=1
                    if indx1==len(b)-1:
                        pass
                print(islem)
            print(baskat)
            print(powerv)
            polyn_islem(y)
        power_and_baskat(x,y)
    polynom(x,y)
polynom_check("+5x**2 + 2x - 5",5)

    
