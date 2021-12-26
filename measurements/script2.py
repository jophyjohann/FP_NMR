import matplotlib.pyplot as plt
import numpy as np

'''
#10 measurements at 45.5MHz from tau_1=25µs to 925µs
name="mess_2_45.5Mhz.txt"
im, re, t = np.loadtxt(name, unpack=True, skiprows=3)
abs = im + re


FT_name = name.replace(".txt","_FT.txt")
ft_im, ft_re, ft_f = np.loadtxt(FT_name, unpack=True, skiprows=3)
ft_abs = ft_im + ft_re

plt.plot(ft_f, ft_abs, '-')
plt.title(FT_name[7:-4])
plt.show()


plt.plot(t, abs, '-')
plt.title(name[7:-4])
plt.show()
'''

#50 measurements at 45.5MHz from tau_1=25µs to 4925µs
name="mess_3_45.5Mhz.txt"
re, im, t = np.loadtxt(name, unpack=True, skiprows=4)
abs = im + re

'''
FT_name = name.replace(".txt","_FT.txt")
ft_im, ft_re, ft_f = np.loadtxt(FT_name, unpack=True, skiprows=3)
ft_abs = ft_im + ft_re

plt.plot(ft_f, ft_abs, '-')
plt.title(FT_name[7:-4])
plt.show()
'''

plt.plot(t, abs, '-')
plt.title(name[7:-4])
plt.show()
