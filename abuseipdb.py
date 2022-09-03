from typing import Set
import requests
from os import environ

CATEGORIES = {
	1: 'DNS Compromise',
	2: 'DNS Poisoning',
	3: 'Fraud Orders',
	4: 'DDoS Attack',
	5: 'FTP Brute-Force',
	6: 'Ping of Death',
	7: 'Phishing',
	8: 'Fraud VoIP',
	9: 'Open Proxy',
	10: 'Web Spam',
	11: 'Email Spam',
	12: 'Blog Spam',
	13: 'VPN IP',
	14: 'Port Scan',
	15: 'Hacking',
	16: 'SQL Injection',
	17: 'Spoofing',
	18: 'Brute-Force',
	19: 'Bad Web Bot',
	20: 'Exploited Host',
	21: 'Web App Attack',
	22: 'SSH abuse',
	23: 'IoT Targeted'
}

class AbuseIPDB:
	def __init__(self, ip):
		__URL = 'https://api.abuseipdb.com/api/v2/check?maxAgeInDays=90&verbose'
		__headers = {
			#export ABUSE_TOKEN=token
			'Key': environ.get('ABUSE_TOKEN'),
			'Accept': 'application/json',
		}

		__params = {
			'ipAddress': ip,
		}

		__query = requests.get(__URL, headers=__headers, params=__params).json().get('data')
		self.__score = __query.get('abuseConfidenceScore')
		self.__category = {CATEGORIES.get(y) for x in __query.get('reports') for y in x.get('categories')}
		self.__whitelisted = bool(__query.get('isWhitelisted'))

	def getScore(self) -> int:
		return self.__score

	def getCategory(self) -> set:
		return self.__category

	def str_category(self) -> str:
		if len(self.__category) > 0:
			output = 'L\'IP è stato classificato come: '
			for i in self.__category:
				output += ('\n' + '•\t' + str(i)) if i is not None else ''
		
			return output
		else:
			return ''

	def isWhitelisted(self) -> bool:
		return self.__whitelisted

	def __str__(self):
		return str(self.__score) + '%'