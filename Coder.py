#!/usr/bin/python
import subprocess
import sys

print "pycoder"

def main(argv=sys.argv):
	if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
		print "Enter the two parameters - the names of the input and output files"
		print "sample - Pycoder.py \"In file.ogg\" \"Out file.mp4\""
		print ""
		print "You can also make a piece of video encoding"
		print "To do this, after the main parameters to specify the start time and the duration of the fragment"
		print "sample - Pycoder.py \"In file.ogg\" \"Out file.mp4\" 00:01:15 00:00:20"
	else:
		if len(sys.argv) == 3:
			s = ["ffmpeg",
			"-i",sys.argv[1],
			"-f","mp4",
			"-acodec","libfaac",
			"-vcodec","libx264",
			"-threads","2",
			"-y",
			sys.argv[2]]		
		#	s="ffmpeg$-i$"+sys.argv[1]+"$-f$mp4$-acodec$libfaac$-vcodec$libx264$-threads$2$-y$\""+sys.argv[2]+"\""
		else:
			s = ["ffmpeg",
			"-i",sys.argv[1],
			"-f","mp4",
			"-acodec","libfaac",
			"-vcodec","libx264",
			"-ss",sys.argv[3],
			"-t",sys.argv[4],
			"-threads","2",
			"-y",
			sys.argv[2]]		
		#	s="ffmpeg$-i$"+sys.argv[1]+"$-f$mp4$-acodec$libfaac$-vcodec$libx264$-ss$"+sys.argv[3]+"$-t$"+sys.argv[4]+"$-threads 2$-y$"+sys.argv[2]	
		#print s
		t = subprocess.Popen(s,stderr=subprocess.STDOUT,stdout = subprocess.PIPE)
		out = t.communicate()
		print out
	
if __name__ == "__main__":
    main()
