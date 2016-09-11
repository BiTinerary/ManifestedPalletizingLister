# ManifestedPalletizingLister
Create TimeStamped text files, in DateStamped Pallet Folders, that can be parsed into Manifests, Pallets and Ebay Exchange .csv headers.

## OverAll Useage
~ Scan Pallet Number, currently hard coded <b>'StartPallet'</b>. #Will be changed to specific load/manufacturer regex<br>
* New file is created with today's date
~ Scan Summin on the Pallet, currently accepts any alphanumeric string of any length. # Should apply loose regex later<br>
* Create file with current timestamp, then append the "Scan Summin" input with a trailing newline character.<br>

###TODO 

~ <strike>Error Handling</strike> is pretty smooth. Could use a titch more refining prior to File creation<br>
~ Re order while loop. So that terminal print references the Pallet name once, followed by each additional SKU.<br>
* This is tricky since error handling linux/win `clear`/`cls` whould be convoluted. Find work around.
~ Incorporate regex's for Pallet Number and SKU's.
* Loose enough to be forward compatible, so we aren't editing code when manufacturers change
* specific enough to differentiate between SKU/Pallet# to optimize error handling and file manipulation
* Sidenote: Determine regex's from key's in a dictionary file where values are Fingerhut, Waterford, etc..?
