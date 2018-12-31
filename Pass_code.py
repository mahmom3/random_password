import random
def Create_Password():
    i = 0
    password=[]
    pass_length=0
    max_range=0
    inside=["abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ","0123456789","-|@.,?/!~#%^&*(){}[]\=*"]
    pass_length=random.randint(11,23)
    password=[None]*pass_length

    for i in range(0,pass_length):
        ri=random.randint(0,3)
        if ri<2:
            max_range=25
        elif ri<3:
            max_range=9
        else:
            max_range=22
        password[i]=inside[ri][random.randint(0,max_range)]


    j=0
    k=0
    lc=0
    uc=0
    num=0
    schar=0
    for j in range(0,pass_length):
        for k in range(0,4):
            if inside[k].find(password[j])>-1:
                if k==0:
                    lc=1
                    break
                elif k==1:
                    up=1
                    break
                elif k==2:
                    num=1
                    break
                if k==3:
                    schar=1
                    break
    index=0
    pass_string=''
    while pass_length>0:
        pass_string=pass_string + password[index]
        index+=1
        pass_length-=1

    if (lc+up+num+schar)==4:
        print ("The Password is " + pass_string)
    else:
        Create_Password()
Create_Password()
