import numpy as np
import math



lookuptable = {}

lookuptable[0]=45.0
lookuptable[1]=26.5650
lookuptable[2]=14.0362
lookuptable[3]=7.1250
lookuptable[4]=3.5763
lookuptable[5]=1.7899
lookuptable[6]=0.8951
lookuptable[7]=0.4476
lookuptable[8]=0.2238
lookuptable[9]=0.1119
lookuptable[10]=0.0230
lookuptable[11]=0.0140
lookuptable[12]=0.0070
lookuptable[13]=0.0035




def cordic(value,  mode):
    z = 0
    if(mode==0):
        x =  0.607252935
        y = 0.0 
    if(mode==1):
        x = 1
        y = value
        
    for i in range(13):
        if(mode==0):
            d = np.sign(value)
        else:
            d = -np.sign(y)

        if(d==0):d = 1
        value -= d*lookuptable[i]

        z -= d*lookuptable[i]

        temp = x
        x -= d * y * 2.0**(-i)
        y +=  d* temp * 2.0**(-i)
        # print("y:",y)
        # print("x:",x)

    if(mode==0):
        print("sin:",y)
        print("cos:",x)
    else:
        print("theta:",z)

cordic(4,1)