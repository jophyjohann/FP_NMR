import glob, os
import numpy as np

class DataSet_Operations:
	def __init__(self):
		self.folder_name="measurements/"
		self.file_extension=".txt"

		self.this_file = __name__ + ".py"
		self.working_path = os.getcwd()

		#automatically inserted dataset_files:
		self.dataset_files = ["mess_1_45.7Mhz_FT.txt",
										 "mess_1_45.6Mhz.txt",
										 "mess_1_45.6Mhz_FT.txt",
										 "mess_1_45.5Mhz.txt",
										 "mess_1_45.5Mhz_FT.txt",
										 "mess_1_45.4Mhz.txt",
										 "mess_1_45.4Mhz_FT.txt",
										 "mess_1_45.3Mhz.txt",
										 "mess_1_45.3Mhz_FT.txt",
										 "mess_4_45.5mhz_spin_lattice2.txt",
										 "mess_4_45.5mhz_spin_lattice.txt",
										 "mess_3_45.5Mhz.txt",
										 "mess_2_45.5mhz.txt",
										 "mess_1_45.7Mhz.txt",
										 ]
		#end of automatically inserted dataset_files


	def datasets_change_comma_to_dot(self):
		for filename in self.dataset_files:
			#print(filename)
			file =  open(self.folder_name + filename,"r")
			data =file.read().replace(",", ".")
			file = open(self.folder_name + filename,"w")
			file.write(data)
			file.close()


	def insert_dataset_files(self):
		os.chdir(self.folder_name)
		new_filenames = glob.glob("*" + self.file_extension)
		os.chdir(self.working_path)

		filename_list = '['
		for file in new_filenames:
			filename_list += '"' + file + '",\n										 '
		filename_list += ']'
		filename_list.replace(",\n										 ]","]")
		filename_list += "\n"

		file = open(self.this_file,"r")
		data = file.read()
		file = open(self.this_file,"w")
		start_string = "		#automatically inserted dataset_files:"
		stop_string = "		#end of automatically inserted dataset_files"
		additional_string = "\n		self.dataset_files = "
		dataset_spot=data[data.find(start_string):data.find(stop_string)] + stop_string
		file.write(data.replace(dataset_spot, start_string + additional_string + filename_list + stop_string))
		file.close()


	def import_dataset_measurements(self):
		self.dataSet = [None] * len(self.dataset_files)
		for i in range(len(self.dataset_files)):
			self.dataSet[i] = {
        	'name': self.dataset_files[i],
					're': np.loadtxt(self.folder_name + self.dataset_files[i], unpack=True, comments="#", usecols=(0), delimiter="\t"),
        	'im': np.loadtxt(self.folder_name + self.dataset_files[i], unpack=True, comments="#", usecols=(1), delimiter="\t"),
        	'f': np.loadtxt(self.folder_name + self.dataset_files[i], unpack=True, comments="#", usecols=(2), delimiter="\t"),
    			}
