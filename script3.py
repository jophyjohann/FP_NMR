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


		print(dataSet[11]['name'])

		re = dataSet[11]['re']
		im = dataSet[11]['im']
		abs = np.sqrt(re**2 + im**2)
		#print(abs.size)   # Laenge des Arrays
		#print(abs.size/50)  # Wir haben 50 Messungen bei verschieden tau gemacht
		#max = np.amax(abs)
		max = np.zeros(50)  # Array für die maximal Werte bei jeder Messung 
		#print(max)
		tau = np.linspace(25, 4925) # Die 50 tau werte
		for i in range(50): 
			#print(i) 
			u = 512*i  # Untere Grenze
			o = 512*(i+1) # Obere Grenze
			#print(u,o)
			max[i] = np.amax(abs[u:o])
		#print(max)
		
		plot_range=[None,None]
		fit_range = [10,-10]
		fit_plot_range = [10,-10]
		
		max *= 1e-6

		# Fit Equation
		def M_echo2(tau, M_sat, T_2):
			return M_sat * np.exp(-2 * tau / T_2)

		def M_echo(tau, M_sat, T_2):
			M = M_sat * np.exp(tau)*2
			return M
		
		Fit_params = [["M_sat", "T_2"],
		              [4, 0.3]]    # Starting values

		#print("x",tau)
		#print("y",max)
		
		popt, pcov =  opt.curve_fit(M_echo, tau[fit_range[0]:fit_range[1]], max[fit_range[0]:fit_range[1]], p0=Fit_params[1])
		print(popt)
		
		# plot
		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(tau, max, '+')
		plt.plot(tau[fit_plot_range[0]:fit_plot_range[1]], M_echo(tau[fit_plot_range[0]:fit_plot_range[1]], *popt))
		plt.xlabel(r'$\tau$ /$\mu$s')
		plt.ylabel('Amplitude')
		plt.title('Spin-Spin-Relaxation')
		plt.xlim(0, 5000)
		maximize()
		plt.show()

		
