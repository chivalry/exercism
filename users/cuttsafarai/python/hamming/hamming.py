def distance(strand_a, strand_b):
	hamming_distance = 0
	if len(strand_a) != len(strand_b):
		raise ValueError("DNA lengths must be equal")
	for nuc_a, nuc_b in zip(strand_a, strand_b):
		if nuc_a != nuc_b:
			hamming_distance += 1
	return hamming_distance

print(distance("GGACGGATTCTG", "AGGACGGATTCT"))
