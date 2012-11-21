#!/usr/bin/python
import subprocess
import sys
import re

def main(argv=sys.argv):
	if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
		for line in open('help','r'):
  			print line,		
	else:
		infile = sys.argv[1]
		outfile = sys.argv[2]
		st = ""
		length = ""
		height = ""
		width = ""

		a = ""
		b = ""		
	
		#get origin aspect.. but for what?	
		out = subprocess.Popen(["ffmpeg","-i",infile], stderr = subprocess.STDOUT, stdout = subprocess.PIPE)
		for i in iter(out.stdout.readline, ""):
			k = i.find("DAR")		
			if k > -1:
				j = k + 4				
				while i[j].isdigit():				
					a = a + i[j]
					j = j + 1
				j = j + 1
				while i[j].isdigit():				
					b = b + i[j]
					j = j + 1
		print "aspect = " + a + ':' + b
				
		s = ["ffmpeg",
		"-i", infile,
		"-f", "mp4",
		"-acodec", "libfaac",
		"-vcodec", "libx264",
		"-threads", "2",
		"-y"]
		
		for i in sys.argv :
			if re.match("\d\d:\d\d:\d\d", i):	
				if st == "" :
					st = i
				else:
					length = i

		for i in sys.argv :
			if i.isdigit() :	
				if width == "" :
					width = i
				else:
					height = i

		if st != "" and length != "":		
			s = s + ["-ss", st, "-t", length]
		
		if width != "" and height != "":
			s = s + ["-s",width+'x'+height]

		s = s + [outfile]		
		t = subprocess.Popen(s, stderr = subprocess.STDOUT, stdout = subprocess.PIPE)
		out = t.communicate()
		print out
	
if __name__ == "__main__":
    main()
