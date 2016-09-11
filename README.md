# ManifestedPalletizingLister
Create TimeStamped text files, in DateStamped Pallet Folders, that can be parsed into Manifests, Pallets and Ebay Exchange .csv headers.

Dependencies:<br> Python (Runs on Windows or Linux File Structure)
`import os`
`import datetime`

## OverAll Useage
1: Scan Pallet Number, currently hard coded <b>'StartPallet'</b>. #Will be changed to specific load/manufacturer regex<br>
* New file is created with today's date

2: Scan Summin on the Pallet, currently accepts any alphanumeric string of any length. # Should apply loose regex later<br>
* Create file with current timestamp, then append the "Scan Summin" input with a trailing newline character.<br>

3: Scan pallet number again, indicating end of pallet. Exiting while loop and ending script.

###TODO 
~ Add/Rename '-COMPLETE' to every file that has been ended appropriately. In case several/items are scanned too many times.
* Biggest issue is end user scanning a SKU too many times, messing up quantities, etc...
  * Same can be said for 'missing' a sku as well though.
  * Require same box to be scanned twice before moving on to next box?

~ <strike>Error handling</strike> is pretty smooth. Could use a titch more refining prior to File creation<br>
~ Re order while loop. So that terminal print references the Pallet name once, followed by each additional SKU.<br>
* This is tricky since error handling linux/win `clear`/`cls` whould be convoluted. Find work around.<br>

~ Incorporate regex's for Pallet Number and SKU's.
* Loose enough to be forward compatible, so we aren't editing code when manufacturers change
* specific enough to differentiate between SKU/Pallet# to optimize error handling and file manipulation
* Sidenote: `try/except` user input with regex's from key's in a dictionary file, where values are Fingerhut, Waterford, etc..?
