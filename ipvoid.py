import requests
from bs4 import BeautifulSoup
import re

class IPVoid:
	def __init__(self, ip):
		__BASE_URL = 'https://www.ipvoid.com/ip-blacklist-check/'
		__payload = {'ip': ip}
		self.__score = int(BeautifulSoup(requests.post(__BASE_URL, data = __payload).text, 'html.parser').find('span', {'class':'label'}, string=re.compile('/106')).text.replace('/106', ''))

	def getScore(self) -> int:
		return self.__score

	def __str__(self):
		return str(self.__score) + '/106'