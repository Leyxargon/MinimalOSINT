import requests
from dossier import Dossier

class IPgeo:
	def __init__(self, ip):
		self.__ip = ip
		
		__url = 'https://ipapi.co/{}/json/'.format(self.__ip)
		__query = requests.get(__url).json()

		self.__country = __query.get('country_name')
		self.__countryCode = __query.get('country_code')
		self.__city = __query.get('city')
		self.__region = __query.get('region')

	def getIP(self):
		return self.__ip

	def getCountry(self):
		return self.__country

	def getCountryCode(self):
		return self.__countryCode

	def getCity(self):
		return self.__city

	def getRegion(self):
		return self.__region

	def __str__(self):
		output = str(self.getIP())
		output += '\n\n' + 'WHOIS' + '\n' + str(Dossier(self.getIP()))
		output += '\n\n' + 'L\'IP risulta geolocalizzato come segue: '
		output += str(self.getCity()) + ', ' + str(self.getRegion()) + ' (' + str(self.getCountry()) + ')'

		return output