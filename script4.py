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
		
		data=dataSet[9]
		
		export_name ="spin_lattice_relaxation_fit"
		
		title_name=export_name.replace("_"," ")

		print(80*"_"+"\n\nPlotting: ", title_name)
		

		re = data['re']
		im = data['im']
		abs = np.sqrt(re**2 + im**2)
		#print(abs.size)   # Laenge des Arrays
		#print(abs.size/50)  # Wir haben 50 Messungen bei verschieden Delta t gemacht
		#max = np.amax(abs)
		max = np.zeros(50)  # Array für die maximal Werte bei jeder Messung 
		
		dt = np.array([4.0, 3.9, 3.8, 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1, 3.0, 2.9, 2.8, 2.7, 2.6, 2.5, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.01]) # Die 50 Delta t werte
		
		for i in range(50): 
			#print(i) 
			u = 1024*i  # Untere Grenze
			o = 1024*(i+1) # Obere Grenze
			max[i] = np.amax(abs[u:o])
		
		# Fit Equation
		def M_echo(dt, M_sat, T_1, c):
			M = M_sat*(1-np.exp(-(dt)/T_1))  + c
			return M
		
		plot_range=[None,None]
		fit_range = [None,None]
		fit_plot_range = [None,None]
		

		fit_param = [["M_sat", "T_1", "  c"],
		              [1.5e6, 0.3, 0.59e6]]    # Starting values

		popt, pcov =  opt.curve_fit(M_echo, dt[fit_range[0]:fit_range[1]], max[fit_range[0]:fit_range[1]], p0=fit_param[1])
		
		
		print("\nFit Parameter:")
		print("Param.      Wert          Δ(Fit)")
		for param in fit_param[0]:
			i = fit_param[0].index(param)
			print("{} \t= \t{:.5} \t± {:.4}".format(param,popt[i],np.sqrt(np.diag(pcov))[i]))
		
		
		# plot
		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(dt, max, '+')
		plt.plot(dt[fit_plot_range[0]:fit_plot_range[1]], M_echo(dt[fit_plot_range[0]:fit_plot_range[1]], *popt))
		plt.xlabel(r'$\Delta$t /ms')
		plt.ylabel('Amplitude')
		plt.title('Spin-Lattice-Relaxation')
		plt.xlim(0, 4.2)
		maximize()
		plt.savefig(self.export_folder + export_name + self.export_extension, bbox_inches='tight')
		plt.show()
