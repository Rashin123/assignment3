Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 29 2018, 20:59:26) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> def hammingDistance(p, q):
	ham = 0
	for x, y in zip(p, q):
		if x != y:
			ham += 1
	return ham

>>> def distanceBetweenPatternAndString(pattern, dna):
	k = len(pattern)
	distance = 0
	for x in dna:
		hamming = k+1
		for i in range(len(x) - k + 1):
			z = hammingDistance(pattern, x[i:i+k])
			if hamming > z:
				hamming = z
		distance += hamming
	return distance

>>> def numberToPattern(x, k):
	if k == 1:
		return numberToSymbol(x)
	return numberToPattern(x // 4, k-1) + numberToSymbol(x % 4)

>>> def numberToSymbol(x):
	if x == 0:
		return "A"
	if x == 1:
		return "C"
	if x == 2:
		return "G"
	if x == 3:
		return "T"

	
>>> def medianString(dna, k):
	distance = len(dna)+1
	median = ""
	for i in range(4**k - 1):
		pattern = numberToPattern(i, k)
		z = distanceBetweenPatternAndString(pattern, dna)
		if distance > z:
			distance = z
			median = pattern
	return median

>>> dna = ["TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT",
"CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA",
"TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT",
"TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA",
"ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG",
"TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA",
"TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC",
"GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA",
"CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG",
"CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG",]
>>> k = 6
>>> print(medianString(dna, k))
CGGCGA
>>> dna = ["CCCTGAATTAACTAGATCGGCCGTTGATAACCATTGGAGTTG",
"CCTACGTCGGTTCCACCCCCCGCGTCGCACTGATAAGAGTAT",
"TAAGAGTGAAAAACAACGGACAATTAGCCGGATGGTTCGAAA",
"AGCCTATGAGAAACACCGCCTTCCTTATATTATCCCGCATTC",
"TGGTGCCAAGTTCATTGCTGTAGATGCCTCTGATAAAGGTGG",
"ACCCCTAGGATGACTTGTTGAAAACACCATATTTCGCCGAAT",
"TCGACGTCAAAAAGGACGGAGTTGACACTATGAGAAGTGTGA",
"AGGGCTTAGTCATCGCCCCTTGGTTGAAAAACTTGGGGCTAG",
"CGGGCATGAGAATTGCTATACTACCACTACCGGTGCGATAAA",
"TCCCTTAAGAGATGCCAGTGAAAATACATTATGGGACAGATA"]
>>> k = 6
>>> print(medianString(dna, k))
TGAAAA
>>> 
