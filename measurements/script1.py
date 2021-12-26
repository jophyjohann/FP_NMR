import matplotlib.pyplot as plt
import numpy as np


'''
#45.3MHz
name="mess_1_45.3Mhz.txt"
re, im, t = np.loadtxt(name, unpack=True, skiprows=3)
abs = im + re

FT_name = name.replace(".txt","_FT.txt")
FT_re, FT_im, FT_f = np.loadtxt(FT_name, unpack=True, skiprows=3)
FT_abs = FT_im + FT_re
FT_f *= 1000

plt.plot(t, abs, '-')
plt.title(name[7:-4])
plt.show()

plt.plot(FT_f, FT_abs, '-')
plt.title(FT_name[7:-4])
plt.show()


#45.4MHz
name="mess_1_45.4Mhz.txt"
re, im, t = np.loadtxt(name, unpack=True, skiprows=3)
abs = im + re

FT_name = name.replace(".txt","_FT.txt")
FT_re, FT_im, FT_f = np.loadtxt(FT_name, unpack=True, skiprows=3)
FT_abs = FT_im + FT_re
FT_f *= 1000

plt.plot(t, abs, '-')
plt.title(name[7:-4])
plt.show()

plt.plot(FT_f, FT_abs, '-')
plt.title(FT_name[7:-4])
plt.show()

'''

#45.5MHz
name="mess_1_45.5Mhz.txt"
re, im, t = np.loadtxt(name, unpack=True, skiprows=3)
abs = im + re

FT_name = name.replace(".txt","_FT.txt")
FT_re, FT_im, FT_f = np.loadtxt(FT_name, unpack=True, skiprows=3)
FT_abs = FT_im + FT_re
FT_f *= 1000

plt.plot(t, abs, '-')
plt.title(name[7:-4])
#plt.show()

plt.plot(FT_f, FT_abs, '-')
plt.title(FT_name[7:-4])
#plt.show()

# calc the local B field inside the sample
f=45.5e6
omega=2*np.pi*f
h_red=1.054571635e-34
#g=1.16
g=0.3

mu_N=5.0507837461e-27
gamma=g * mu_N / h_red

B=omega / gamma

print(B)

'''
#45.6MHz
name="mess_1_45.6Mhz.txt"
re, im, t = np.loadtxt(name, unpack=True, skiprows=3)
abs = im + re

FT_name = name.replace(".txt","_FT.txt")
FT_re, FT_im, FT_f = np.loadtxt(FT_name, unpack=True, skiprows=3)
FT_abs = FT_im + FT_re
FT_f *= 1000

plt.plot(t, abs, '-')
plt.title(name[7:-4])
plt.show()

plt.plot(FT_f, FT_abs, '-')
plt.title(FT_name[7:-4])
plt.show()


#45.7MHz
name="mess_1_45.7Mhz.txt"
re, im, t = np.loadtxt(name, unpack=True, skiprows=3)
abs = im + re

FT_name = name.replace(".txt","_FT.txt")
FT_re, FT_im, FT_f = np.loadtxt(FT_name, unpack=True, skiprows=3)
FT_abs = FT_im + FT_re
FT_f *= 1000

plt.plot(t, abs, '-')
plt.title(name[7:-4])
plt.show()

plt.plot(FT_f, FT_abs, '-')
plt.title(FT_name[7:-4])
plt.show()
'''
