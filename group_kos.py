#!usr/bin/env python

__author__ = "Kevin Chan"
__maintainer__ = "Kevin Chan"
__email__ = "kevchan1@alumni.ubc.ca"

"""
Script to group KO identifiers into higher categories in a summary table.
"""

import argparse
import pandas as pd
import os
from collections import defaultdict

def listDirNoHidden(indir):
	return [f for f in os.listdir(indir) if not f.startswith(".")]

def getArgs():
	parser = argparse.ArgumentParser(description = "Group KO identifiers into higher categories.")
	parser.add_argument("-k", "--ko-table", required = True, help = "KEGG Orthology csv generated from the KEGG-to-anvio script.")
	parser.add_argument("-o", "--outpath", default = ".", help = "Path to output file.")
	parser.add_argument("-g", "--gene-calls-dir", required = True, help = "Directory containing gene calls exported from An'vio.")
	args = parser.parse_args()
	return args

def getKOList(gene_calls_file):
	df = pd.read_table(gene_calls_file)
	return df["KeggGhostKoala (ACCESSION)"].tolist()

def deletePaths(s):
	l = s.split(" ")
	del l[0]
	del l[-1]
	return " ".join(l)

def formatKOTable(ko_table):
	df = pd.read_table(ko_table, sep = ",")
	df = df.set_index("accession")
	df["Category3"].apply(lambda x: deletePaths(x))
	return df

def getMatches(df, l):
	dd = {}
	dd = defaultdict(lambda: 0, dd)
	# this will take a while...
	for ko in l:
		for i, row in df.iterrows():
			if ko == i:
				for v in row.values:
					dd[v] += 1
	return dd

def getCategories(df):
	cat1 = df["Category1"].unique()
	cat2 = df["Category2"].unique()
	cat3 = df["Category3"].unique()
	cat4 = df["description"].unique()
	return cat1, cat2, cat3, cat4

def main():
	args = getArgs()
	KO_TABLE = args.ko_table
	OUTPATH = args.outpath
	GENE_CALLS_DIR = args.gene_calls_dir
	gene_calls_files = [f for f in listDirNoHidden(GENE_CALLS_DIR) if os.path.isfile(os.path.join(GENE_CALLS_DIR, f))]
	df = formatKOTable(KO_TABLE)
	categories = df.columns.values
	for category in categories:
		print "on category %s" % category
		outfile = open(os.path.join(OUTPATH, "kegg_" + category + ".txt"), "w")
		outfile.write("kegg_category\t" + "\t".join(os.path.splitext(f)[0] for f in gene_calls_files) + "\n")
		cols = df[category].unique()
		ko_list = None
		for col in cols:
			print "on column %s" % col
			outfile.write(col + "\t")
			for f in gene_calls_files:
				print "working on file %s" % f
				FULL_PATH = os.path.join(GENE_CALLS_DIR, f)
				if ko_list is None:
					ko_list = getKOList(FULL_PATH)
				all_ko_counts = getMatches(df, ko_list)
				outfile.write(all_ko_counts[col] + "\t")
				print "finished writing for file %s" % f 
			outfile.write("\n")

if __name__ == "__main__":
	main()