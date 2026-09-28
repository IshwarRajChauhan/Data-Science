import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 11)
y = x**2


#FINCTIONAL METHOD

#------------------------------------------------------

#plt.plot(x,y)   #plot(x-axis,y-axis)
#plt.xlabel('X Label')    #name x axis
#plt.ylabel('Y Label')    #name y axis
#plt.title('Title')       #name the graph

#------------------------------------------------------


# plt.subplot(1,2,1)
# plt.plot(x,y,'r-')
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("y = x²")

# plt.subplot(1,2,2)
# plt.plot(y,x,'b')
# plt.xlabel("Y")
# plt.ylabel("X")
# plt.title("x vs y")


# plt.show()




#------------------------------------------------------


#OBJECT ORIENTED METHOD
#------------------------------------------------------


# fig = plt.figure(figsize=(10, 4))
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y)
# axes.set_xlabel('X Label')
# axes.set_ylabel('Y Label')
# plt.show()


#------------------------------------------------------

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x,y)
axes1.set_title('Larger Plot')
axes2.plot(y, x)
axes2.set_title('Smaller Plot')
plt.show()




















