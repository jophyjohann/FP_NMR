from dataset_operations import DataSet_Operations
import matplotlib.pyplot as plt
import numpy as np
import os
import scipy.optimize as opt

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
			#mng.full_screen_toggle()
			#os.system('xdotool key alt+F10')
		

		#export_name = dataSet['name'][5:6] + "_-_" + dataSet['name'][7:-4]
		#name = ("dataSet[" + str(dataSet[11]) + "]\n" + export_name).replace("_"," ")
		#title_name=export_name.replace("_"," ")

		#print(80*"_"+"\n\nPlotting: ", name)


		print(dataSet[9]['name'])

		re = dataSet[9]['re']
		im = dataSet[9]['im']
		abs = np.sqrt(re**2 + im**2)
		print(abs.size)   # Laenge des Arrays
		print(abs.size/50)  # Wir haben 50 Messungen bei verschieden Delta t gemacht
		#max = np.amax(abs)
		max = np.zeros(50)  # Array für die maximal Werte bei jeder Messung 
		#print(max)
		
		dt = np.array([4.0, 3.9, 3.8, 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1, 3.0, 2.9, 2.8, 2.7, 2.6, 2.5, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.01]) # Die 50 Delta t werte
		#print(dt.size)
		
		for i in range(50): 
			#print(i) 
			u = 1024*i  # Untere Grenze
			o = 1024*(i+1) # Obere Grenze
			#print(u,o)
			max[i] = np.amax(abs[u:o])
		#print(max)
		
		'''
		# Fit Equation
		def M_echo(dt, M_sat, T_1):
			M = M_sat*(1-np.exp(-dt/T_1))
			return M
		
		Fit_params = [[M_sat, T_1],
		              [4e6, 0.3]]    # Starting values

		popt, pcov =  opt.curve_fit(M_echo, dt, max, p0=Fit_params[1])
		print(popt)
		'''
		
		# plot
		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(dt, max, '+')
		#plt.plot(dt, M_echo(dt, *popt))
		plt.xlabel(r'$\Delta$t /ms')
		plt.ylabel('Amplitude')
		plt.title('Spin-Lattice-Relaxation')
		plt.xlim(0, 4.2)
		maximize()
		plt.show()
		

		
