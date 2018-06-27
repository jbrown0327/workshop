'''
Transcribes DNA strands to RNA format
'''

while 1:
	dna = ["C", "G", "T", "A"]
	for n in input("Enter DNA strand: "):
		if n == "G":
			trans = "C"
		elif n == "C":
			trans = "G"
		elif n == "T":
			trans = "A"
		elif n == "A":
			trans = "U"
		else:
			print("%s" % n + " not a DNA strand. Use G, C, T, or A")

		if n in dna:
			print(n + " " + trans)