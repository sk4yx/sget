##################################################################################################################
#            /$$       /$$   /$$                                                                         /$$     #
#           | $$      | $$  | $$                                                                        | $$     #
#   /$$$$$$$| $$   /$$| $$  | $$ /$$   /$$ /$$   /$$                      /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$   #
#  /$$_____/| $$  /$$/| $$$$$$$$| $$  | $$|  $$ /$$/       /$$$$$$       /$$_____/ /$$__  $$ /$$__  $$|_  $$_/   #
# |  $$$$$$ | $$$$$$/ |_____  $$| $$  | $$ \  $$$$/       |______/      |  $$$$$$ | $$  \ $$| $$$$$$$$  | $$     #
#  \____  $$| $$_  $$       | $$| $$  | $$  >$$  $$                      \____  $$| $$  | $$| $$_____/  | $$ /$$ #
#  /$$$$$$$/| $$ \  $$      | $$|  $$$$$$$ /$$/\  $$                     /$$$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/ #
# |_______/ |__/  \__/      |__/ \____  $$|__/  \__/                    |_______/  \____  $$ \_______/   \___/   #
#                                /$$  | $$                                         /$$  \ $$                     #
#                               |  $$$$$$/                                        |  $$$$$$/                     #
#                                \______/                                          \______/                      #
##################################################################################################################

import requests
import argparse

description = '''
A command made in python to download files
'''
parser = argparse.ArgumentParser(description=description)
parser.add_argument('--url', '-u')
parser.add_argument('--name', '-n')

args = parser.parse_args()

if args.url == None:
	print("usage: sget.py [-h] [--url URL] [--name NAME]")
else:
	url = args.url
	try:
		response = requests.get(url)

		params = url.split("/")
		params2 = len(params)-1

		name = params[params2]

		while True:
			if name == '':
				params2 = params2-1
				name = params[params2]
			else:
				break

		if args.name == None:
			with open(name, 'wb') as file:
				file.write(response.content)
		else:
			try:
				with open(args.name, 'wb') as file:
					file.write(response.content)
			except:
				with open('invalid', 'wb') as file:
					file.write(response.content)

		print('sget: '+url+' successfully downloaded')
		

	except:
		print("sget: error invalid url '"+url+"'")
