import os
import datetime

def PalletizeInput():
		scanPalletNumber = raw_input('\nPallet Number: ')

		if str(scanPalletNumber) == 'StartPallet': # change later for specific Pallet Number regex (Company specific of general for forward compatibility)
			cwd = os.getcwd()
			folderWithTodaysDate = os.makedirs(cwd + '%s%s' % ('/', str(datetime.date.today().strftime('X%m.X%d.20%y').replace('X0', '')))) # raise try/else/exception handling if datestamp file already exists!!@!@!
			while True:
				scanSkusOnPallet = raw_input('\nScan Summin: ')
				#with open
		else:
			print('Put Error Handling Here') # try/except would reformat entire script, elif statements for later loads/manufacturers?
			print("You didn't scan a valid pallet number")

PalletizeInput()