
url = input("[+] Enter Target URL: ")
subdom = open("subdom.txt", "r")


for sd in subdom:
	if sd[0] == '/':
		print(f"{url}{sd}")
	else:
		continue
