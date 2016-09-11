import os
import datetime

cwd = os.getcwd()
opj = os.path.join

folderWithTodaysDate = opj(cwd, str(datetime.date.today().strftime('X%m.X%d.20%y').replace('X0', '').replace('X', '')))
currentTimeStampFile = str(datetime.datetime.now().strftime('%I.%M.%S %p'))+'.txt' #Create txt file with timestamp name. Change for .csv, etc...?

def PalletizeInput():
	#Add another input here for scanning barcode that's clear text corresponds to "Let's Start Palletizing", "Let's start Counting", "Let's stop palletizing", etc...
		scanPalletNumber = raw_input('\nPallet Number: ')

		if str(scanPalletNumber) == 'StartPallet': # change later for specific Pallet Number regex (Company specific of general for forward compatibility)

			#folderWithTodaysDate = os.path.join(cwd, str(datetime.date.today().strftime('X%m.X%d.20%y').replace('X0', '').replace('X', '')))
			if os.path.exists(folderWithTodaysDate) == True: #If file w/ today's date exists, then continue the script.
				pass
			else: #else create the directory with read/write/exe permissions.
				os.makedirs(folderWithTodaysDate, 0o666) #read/write permissions for creating files inside python created folder. For Win & Linux.

			#File name should also be appended with 'COMPLETE' after timestamp when script is completely/exited properly (scan pallet number again?)
			
			createFileInDateDirectory = str(opj(folderWithTodaysDate, currentTimeStampFile)) 
			while True:
				try:
					print("\nLast Scanned SKU: " + str(scanSkusOnPallet))
				except UnboundLocalError:
					continue
				finally:
					print('Current Pallet Number: ' + str(scanPalletNumber))
					scanSkusOnPallet = raw_input('Scan Summin: ')
					with open(createFileInDateDirectory, 'a') as f:
						f.write(scanSkusOnPallet + '\n')
						f.close()
						if str(scanPalletNumber) == str(scanSkusOnPallet):
							#rename file name =+ filename + 'Finished'
							break
						else:
							pass
		else:
			print('Put Error Handling Here') # try/except would reformat entire script, elif statements for later loads/manufacturers?
			print("You didn't scan a valid pallet number")

PalletizeInput()

#TODO
#Find a way to select previous [dynamic] timestamped file OR create simple GUI for manually slecting which pallets to read/parse for manifesting/listing
#Or should I just code for selecting all datestamp*-COMPLETE.txt files from 'todays' date folder. If another .txt is needed take function input.

"""
def OpenPalletFile():
	with open(currentTimeStampFile, 'r') as f:
		print(f.readlines())

OpenPalletFile()
"""