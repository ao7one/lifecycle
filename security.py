# Get known CVE's with fixes and convert to JSON

import pandas

url = "https://www14.software.ibm.com/webapp/set2/flrt/doc?page=aparCSV"
timeout = 5.0

csv=pandas.read_csv(url)
print(csv)
#dict_from_csv=pandas.read_csv(url, header=None, index_col=0).to_dict()
#print(dict_from_csv)

