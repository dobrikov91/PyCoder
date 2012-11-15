#!/usr/bin/python
import subprocess
import sys

print "pycoder"

def main(argv=sys.argv):
	if len(sys.argv) == 3:
		s="ffmpeg -i "+sys.argv[1]+" -f mp4 -acodec libfaac -vcodec libx264 -threads 2 -y "+sys.argv[2]
	else:
		s="ffmpeg -i "+sys.argv[1]+" -f mp4 -acodec libfaac -vcodec libx264 -ss "+sys.argv[3]+" -t "+sys.argv[4]+" -threads 2 -y "+sys.argv[2]	

	t = subprocess.Popen(s.split(' '),stderr=subprocess.STDOUT,stdout = subprocess.PIPE)
	out = t.communicate()
	print out
	
if __name__ == "__main__":
    main()
