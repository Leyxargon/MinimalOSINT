import requests
from os import environ

class XForce:
	def __init__(self, ip):
		__BASE_URL = 'https://exchange.xforce.ibmcloud.com/api/ipr/'
		
		__headers = {'Accept': 'application/json'}
		#export IBM_TOKEN=token
		#export IBM_PASSWD=password
		__auth = (environ.get('IBM_TOKEN'), environ.get('IBM_PASSWD'))
		self.__score = requests.get(__BASE_URL + ip, headers=__headers, auth=__auth).json().get('score')

	def getScore(self):
		return self.__score

	def __str__(self):
		return str(self.__score)