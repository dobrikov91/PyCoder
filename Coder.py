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

		origw = ""
		origh = ""		

		out = subprocess.Popen(["ffmpeg","-i",infile], stderr = subprocess.STDOUT, stdout = subprocess.PIPE)
		for i in iter(out.stdout.readline, ""):
			k = i.find("DAR")		
			if k > -1:
				j = k + 4				
				while i[j].isdigit():				
					origw = origw + i[j]
					j = j + 1
				j = j + 1
				while i[j].isdigit():				
					origh = origh + i[j]
					j = j + 1
		origasp = float(origw)/float(origh)
		
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
			asp = float(width)/float(height)
			if asp < origasp:
				height = str(int(float(width) / float(origw) * float(origh)))	
			else:
				width = str(int(float(height) / float(origh) * float(origw)))
			s = s + ["-s",width+'x'+height]
		
		print s
		s = s + [outfile]		
		print subprocess.Popen(s, stderr = subprocess.STDOUT, stdout = subprocess.PIPE).communicate()		
	
if __name__ == "__main__":
    main()
