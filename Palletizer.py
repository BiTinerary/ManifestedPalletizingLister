import os
import datetime

def PalletizeInput():
		scanPalletNumber = raw_input('\nPallet Number: ')

		if str(scanPalletNumber) == 'StartPallet': # change later for specific Pallet Number regex (Company specific of general for forward compatibility)
			cwd = os.getcwd()
			folderWithTodaysDate = cwd + '%s%s' % ('/', str(datetime.date.today().strftime('X%m.X%d.20%y').replace('X0', '').replace('X', ''))) # raise try/else/exception handling if datestamp file already exists!!@!@!
			os.makedirs(folderWithTodaysDate, 0o666)
			while True:
				scanSkusOnPallet = raw_input('\nScan Summin: ')
				currentTimeStamp = str(datetime.datetime.now().strftime('%I.%M%p'))+'.txt'
				with open(str(folderWithTodaysDate +'/'+ currentTimeStamp), 'w') as f:
					f.write(scanSkusOnPallet)
					f.close()
					#print str(cwd + "/" +currentTimeStamp)
					print (str(folderWithTodaysDate +'/'+ currentTimeStamp))
					#os.rename(str(cwd + '/' + currentTimeStamp), str(folderWithTodaysDate + currentTimeStamp))
				#with open
		else:
			print('Put Error Handling Here') # try/except would reformat entire script, elif statements for later loads/manufacturers?
			print("You didn't scan a valid pallet number")

PalletizeInput()