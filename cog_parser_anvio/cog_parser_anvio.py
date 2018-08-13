#!usr/bin/env python2

import argparse

"""
taken from http://clovr.org/docs/clusters-of-orthologous-groups-cogs/
i had to write these out manually. might be a better way to keep these updated
"""
lower_categories = {
	"D": "Cell cycle control, cell division, chromosome partitioning",
	"M": "Cell wall/membrane/envelope biogenesis",
	"N": "Cell motility",
	"O": "Post-translational modification, protein turnover, and chaperones",
	"T": "Signal transduction mechanisms",
	"U": "Intracellular trafficking, secretion, and vesicular transport",
	"V": "Defense mechanisms",
	"W": "Extracellular structures",
	"Y": "Nuclear structure",
	"Z": "Cytoskeleton",
	"A": "RNA processing and modification",
	"B": "Chromatin structure and dynamics",
	"J": "Translation, ribosomal structure and biogenesis",
	"K": "Transcription",
	"L": "Replication, recombination and repair",
	"C": "Energy production and conversion",
	"E": "Amino acid transport and metabolism",
	"F": "Nucleotide transport and metabolism",
	"G": "Carbohydrate transport and metabolism",
	"H": "Coenzyme transport and metabolism",
	"I": "Lipid transport and metabolism",
	"P": "Inorganic ion transport and metabolism",
	"Q": "Secondary metabolites biosynthesis, transport, and catabolism",
	"R": "General function prediction only",
	"S": "Function unknown"
}

higher_categories = {
	"D": "CELLULAR PROCESSES AND SIGNALING",
	"M": "CELLULAR PROCESSES AND SIGNALING",
	"N": "CELLULAR PROCESSES AND SIGNALING",
	"O": "CELLULAR PROCESSES AND SIGNALING",
	"T": "CELLULAR PROCESSES AND SIGNALING",
	"U": "CELLULAR PROCESSES AND SIGNALING",
	"V": "CELLULAR PROCESSES AND SIGNALING",
	"W": "CELLULAR PROCESSES AND SIGNALING",
	"Y": "CELLULAR PROCESSES AND SIGNALING",
	"Z": "CELLULAR PROCESSES AND SIGNALING",
	"A": "INFORMATION STORAGE AND PROCESSING",
	"B": "INFORMATION STORAGE AND PROCESSING",
	"J": "INFORMATION STORAGE AND PROCESSING",
	"K": "INFORMATION STORAGE AND PROCESSING",
	"L": "INFORMATION STORAGE AND PROCESSING",
	"C": "METABOLISM",
	"E": "METABOLISM",
	"F": "METABOLISM",
	"G": "METABOLISM",
	"H": "METABOLISM",
	"I": "METABOLISM",
	"P": "METABOLISM",
	"Q": "METABOLISM",
	"R": "POORLY CHARACTERIZED",
	"S": "POORLY CHARACTERIZED"
}

def getArgs():
	parser = argparse.ArgumentParser(description="Creates a table of descriptive COG categories from single letter entries in gene_calls.txt after running anvi-run-ncbi-cogs.")
	parser.add_argument("-d", "--input-dir", help="Directory containing gene calls of interest.")
	parser.add_argument("-o", "--output-dir", default=".", help="Output directory. Default: current working directory.")
	args = parser.parse_args()
	return args

def main():
	args = getArgs()
	IN_DIR = args.input_dir
	OUT_DIR = args.output_dir
	print "input directory is: " + IN_DIR
	print "output directory is: " + OUT_DIR

	

if __name__ == "__main__":
	main()
