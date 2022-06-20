import sys.argv

url = sys.argv[1]
wlist = sys.argv[2]
subdom = open(wlist, "r")


for sd in subdom:
	if sd[0] == '/':
		print(f"{url}{sd}")
	else:
		continue
