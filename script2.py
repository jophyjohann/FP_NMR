from dataset_operations import DataSet_Operations
import matplotlib.pyplot as plt
import numpy as np
import os

class run:
	def __init__(self):
		self.dat = DataSet_Operations()
		self.dat.import_dataset_measurements()

		self.export_folder = "export/script" + __name__[-1] + "/"
		self.export_extension = ".pdf"


	def main(self):
		dataSet = self.dat.dataSet
		
		def maximize():
			'''maximizes the matplotlib plot window'''
			mng = plt.get_current_fig_manager()
			mng.resize(*mng.window.maxsize())
		
		print("script2.py is running!")

		#45.5MHz
		### Plot ... ###
		
		dataSet_No = 0   
		data = dataSet[dataSet_No]
		name = data['name'][24:-20]
		
		print(50*"_"+"\n\nPlotting: ", name.replace("_"," "))
		#abs = im + re

		#FT_name = name.replace(".txt","_FT.txt")
		#FT_re, FT_im, FT_f = np.loadtxt(FT_name, unpack=True, skiprows=3)
		#FT_abs = FT_im + FT_re
		#FT_f *= 1000

		#plt.plot(t, abs, '-')
		#plt.title(name[7:-4])
		#plt.show()

		#plt.plot(FT_f, FT_abs, '-')
		#plt.title(FT_name[7:-4])
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