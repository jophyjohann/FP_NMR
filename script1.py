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
			#mng.full_screen_toggle()
			#os.system('xdotool key alt+F10')

		### Plot all measured datasets (11) and export them for overwiev ###

		for data in dataSet:
			export_name = data['name'][5:6] + "_-_" + data['name'][7:-4]
			name = ("dataSet[" + str(dataSet.index(data)) + "]\n" + export_name).replace("_"," ")
			title_name=export_name.replace("_"," ")

			print(80*"_"+"\n\nPlotting: ", name)
		
			fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
			plt.plot(data['f'], data['re'], '.', label = "real")
			plt.plot(data['f'], data['im'], '.', label = "imaginary")
			plt.title(label=title_name)
			plt.legend()
			plt.savefig(self.export_folder + export_name + self.export_extension, bbox_inches='tight')
			maximize()
			plt.show()