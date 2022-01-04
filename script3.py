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
		
		
		data=dataSet[11]
		
		export_name ="spin_spin_relaxation_fit"
		title_name=export_name.replace("_"," ")

		print(80*"_"+"\n\nPlotting: ", title_name)
		

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
		fit_range = [None,None]
		fit_plot_range = [None,None]
		
		tau *= 1e-3

		# Fit Equation
		def M_echo(tau, M_sat, T_2, c):
			return M_sat * np.exp(-2 * tau / T_2) + c

		fit_param = [["M_sat", "T_2", "  c"],
		              [4e6, 0.3e3, 0.3e6]]    # Starting values

		#print("x",tau)
		#print("y",max)
		
		popt, pcov =  opt.curve_fit(M_echo, tau[fit_range[0]:fit_range[1]], max[fit_range[0]:fit_range[1]], p0=fit_param[1])
		
		print("\nFit Parameter:")
		print("Param.      Wert          Δ(Fit)")
		for param in fit_param[0]:
			i = fit_param[0].index(param)
			print("{} \t= \t{:.5}".format(param,popt[i])+ (11-len("{:.5}".format(popt[i])))*" "+"± {:.5}".format(np.sqrt(np.diag(pcov))[i]))
		
		# plot
		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(tau, max, '+')
		plt.plot(tau[fit_plot_range[0]:fit_plot_range[1]], M_echo(tau[fit_plot_range[0]:fit_plot_range[1]], *popt))
		plt.xlabel(r'$\tau$ /ms')
		plt.ylabel('Amplitude')
		plt.title('Spin-Spin-Relaxation')
		plt.xlim(0, 5)
		maximize()
		plt.savefig(self.export_folder + export_name + self.export_extension, bbox_inches='tight')
		plt.show()
