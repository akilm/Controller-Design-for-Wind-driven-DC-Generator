import math
import matplotlib.pyplot as plt

R = float(input("Enter the Radius : "))
B = float(input("Enter the blade angle : "))
Vw= float(input("Enter the wind speed : "))

def Cp_cal(v):
  ki= (1/(v+0.08*B))-(0.035/(B*B*B+1));
  y =( 0.5176*(116*ki-0.4*B-5)*math.exp(-21*ki))+(0.0068*v);    
  return y      

x=[]
y=[]
i=0.0001

for z in range(5000):
    x.append(i)
    a=Cp_cal(i)
    y.append(a)
    i = i + 0.003
    if(a<0):
      print("the maximum value of TSR for this R and B = ")
      w=i-0.003
      print(w)
      print("the maximum  Rpm of the turbine = ")
      rpm=(w*Vw*30)/(R*3.14)
      print(rpm)
      break;
  

plt.plot(x,y)
plt.xlabel(' Tip speed ratio ')
plt.ylabel(' Cp ')
plt.title(' Cp vs TSR ')
plt.show()



