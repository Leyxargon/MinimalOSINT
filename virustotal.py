import requests
from os import environ

class VirusTotal:
	def __init__(self, ip):
		__BASE_URL = 'https://www.virustotal.com/api/v3/ip_addresses/'

		#export VT_TOKEN=token
		headers = {'x-apikey': environ.get('VT_TOKEN')}
		self.__score = requests.get(__BASE_URL + ip, headers=headers).json().get('data').get('attributes').get('last_analysis_stats')

	def getScore(self):
		return self.__score

	def __str__(self):
		return str(self.__score.get('malicious')) + '/' + str(self.__score.get('harmless') + self.__score.get('malicious') + self.__score.get('suspicious') + self.__score.get('undetected'))