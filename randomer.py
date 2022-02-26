from random import choice
from string import ascii_letters
from sys import argv
from os import system,name

system('cls' if name == 'nt' else 'clear')

banner = '''
\033[31m
 ███████████                            █████                                                                    
░░███░░░░░███                          ░░███                                                                     
 ░███    ░███   ██████   ████████    ███████   ██████  █████████████    ██████  ████████     ████████  █████ ████
 ░██████████   ░░░░░███ ░░███░░███  ███░░███  ███░░███░░███░░███░░███  ███░░███░░███░░███   ░░███░░███░░███ ░███ 
 ░███░░░░░███   ███████  ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███████  ░███ ░░░     ░███ ░███ ░███ ░███ 
 ░███    ░███  ███░░███  ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███░░░   ░███         ░███ ░███ ░███ ░███ 
 █████   █████░░████████ ████ █████░░████████░░██████  █████░███ █████░░██████  █████     ██ ░███████  ░░███████ 
░░░░░   ░░░░░  ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░  ░░░░░     ░░  ░███░░░    ░░░░░███ 
                                                                                             ░███       ███ ░███ 
                                                                                             █████     ░░██████  
                                                                                            ░░░░░       ░░░░░░  
\033[0m by Ahmet Yigit AYDENIZ

'''

about = '''
randomer.py

is a program that you can make adjustable sized files
with any extension you want in seconds.Lets talk about
the interface,when you run it with no extra argumants 
it will need to show this screen but if you want to make
a big mp4 file to test your code or you want to make some
fake files and making honeypots for security on your server
or pc 

usage :

>> python3 randomer.py   <file_you_want_to_generate>    <file_size>

(you need to type the size as byte but you can make it kb,mb or gb by editing the code)

thats it , you can make everyfile you want like this

\033[31m!!! please don't use this python project for bad purposes I am not responsible for what you done with this code !!!\033[0m

'''

if len(argv) <= 1:

	print(banner + about)

else:

	def generate_big_random_letters(filename,size):
	
		#for zettabytes (don't try this at home seriously)
		#n = size*1024**7
		
		#for for uhm exabytes (bro,stop...)
		#n = size*1024**6
		
		#for petabytes (bro !)
		#n = size*1024**5
		
		#for terabytes .d (you need to think about a little I think)
		#n = size*1024**4
		
		#for selecting as gb
		#n = size*1024**3
		
		#for selecting as mb
		#n = size*1024**2
		
		#for selecting as kb
		#n = size*1024
		
		n = size #as byte

		chars = ''.join([choice(ascii_letters) for i in range(n)]) 

		with open(filename, 'w',1) as f:
			f.write(chars)
		pass
	print(banner)
	print('generating...\n')

	filename = argv[1]

	size = int(argv[2])

	toolbar_width = 40

	def progress(percent=0, width=40):
		
		left = width * percent // 100
		right = width - left
		tags = '█' * left
		spaces = ' ' * right
		percents = f"{percent:.0f}%"
		
		print('\r[', tags, spaces, ']', percents, sep='', end='', flush=True)

	for x in range(101):
	
		progress(x)
		generate_big_random_letters(filename,size)
		
		
	print('\n'+'\n'+'done!!!'+'\n')
	system('Get-Item ' + getcwd + filename if os.name == 'nt' else 'stat '+filename)
	print('\n')
	exit()
