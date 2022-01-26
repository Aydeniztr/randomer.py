import random
import string
import time
import sys

def generate_big_random_letters(filename,size):

	chars = ''.join([random.choice(string.ascii_letters) for i in range(size)]) 

	with open(filename, 'w') as f:
		f.write(chars)
	pass

print('generating...')

filename = sys.argv[1]

size = int(sys.argv[2])

toolbar_width = 40

# setup toolbar
sys.stdout.write("|%s|" % (" " * toolbar_width))

sys.stdout.flush()

sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for x in range(toolbar_width):
	
	time.sleep(0.1) # do real work here
	
	generate_big_random_letters(filename,size)
	
	# update the bar
	
	sys.stdout.write("█")
	
	sys.stdout.flush()

sys.stdout.write("|\n") # this ends the progress bar

print('done!!!')	
	
exit()