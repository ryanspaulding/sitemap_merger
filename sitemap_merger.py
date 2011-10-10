#!/usr/bin/env python

# take in two sitemap.xml files and merge them to make one super sitemap.xml file 
# to rul them all 


import getopt, sys

def usage():
	print "Usage: sitemap_merger.py --sitemap=sitemap.xml --sitemap2=sitemap2.xml"
	print " --sitemap, -s	sitemap.xml this is the one that will be writen out too"
	print " --sitemap2, -t	sitemap2.xml this is the file that will be added to sitemap.xml"
	print " --verbose, -v 	add verbose output"
	print " --help, -h 	print this message"
	sys.exit(0)

def merge(sitemap, sitemap2, verbose):
	tempsitemap = "/tmp/sitemap.xml"
	if verbose:
		print "sitemap file: %s" %(sitemap) 
		print "sitemap2 file: %s" %(sitemap2)
		print "lets get merging...." 

	tempfile = file(tempsitemap, "w")
	sitemap_handle = file(sitemap, "rw")
	sitemap2_handle = file(sitemap2, "r")

	for line in sitemap_handle:
		if line == "</urlset>\n":
			if verbose:
				print "found line: %s" %(line)
			continue
		tempfile.write(line)

	# only need to do this one time
	tempfile.write("<url>\n") # this is a total hack

	for line2 in sitemap2_handle:
		if 'xml-stylesheet' in line2:
			continue
		if 'sitemap-generator-url' in line2:
			continue
		if 'urlset xmlns' in line2:
			continue
		if 'generated-on' in line2:
			continue

		tempfile.write(line2)

	tempfile.close()
	sitemap_handle.close()
	sitemap2_handle.close()

	# now finish the job and overwrite sitemap

if __name__ == '__main__':
	try:
        	opts, args = getopt.getopt(sys.argv[1:], "hs:t:v", ["help", "sitemap=", "sitemap2=", "verbose"])
    	except getopt.GetoptError, err:
        	# print help information and exit:
        	print str(err) # will print something like "option -a not recognized"
        	usage()
        	sys.exit(2)

	sitemap = None
	sitemap2 = None
    	verbose = False
    	for o, a in opts:
        	if o in ("-v", "--verbose"):
            		verbose = True
        	elif o in ("-h", "--help"):
            		usage()
        	elif o in ("-s", "--sitemap"):
            		sitemap = a
			if verbose:
				print "sitemap file: %s" %(sitemap) 
        	elif o in ("-t", "--sitemap2"):
            		sitemap2 = a
			if verbose:
				print "sitemap2 file: %s" %(sitemap2) 
        	else:
            		assert False, "unhandled option"

	if sitemap == None or sitemap2 == None:
		print "sitemap and sitemap2 required!"
		usage()
	else:
		merge(sitemap, sitemap2, verbose)
