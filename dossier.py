from ipwhois import IPWhois

class Dossier:
	def __init__(self, ip):
		query = IPWhois(ip).lookup_whois()
		self.__netrange = query.get('nets')[0].get('range')
		self.__cidr = query.get('nets')[0].get('cidr')
		self.__netname = query.get('nets')[0].get('name')
		self.__nethandle = query.get('nets')[0].get('handle')
		self.__description = query.get('asn_description')
		self.__country = query.get('asn_country_code')

	def getNetRange(self):
		return self.__netrange

	def getCIDR(self):
		return self.__cidr

	def getNetName(self):
		return self.__netname
	
	def getNetHandle(self):
		return self.__nethandle

	def getDescription(self):
		return self.__description

	def getCountry(self):
		return self.__country

	def __str__(self):
		output = 'NetRange: ' + str(self.__netrange) if self.__netrange is not None else ''
		output += '\n' + 'CIDR: ' + str(self.__cidr) if self.__cidr is not None else ''
		output += '\n' + 'NetName: ' + str(self.__netname) if self.__netname is not None else ''
		output += '\n' + 'NetHandle: ' + str(self.__nethandle) if self.__nethandle is not None else ''
		output += '\n' + 'Description: ' + str(self.__description) if self.__description is not None else ''
		output += '\n' + 'Country: ' + str(self.__country) if self.__country is not None else ''
		return output