import requests
from dossier import Dossier
from abuseipdb import AbuseIPDB
from ipvoid import IPVoid
from xforce import XForce
from virustotal import VirusTotal

class IPrep:
	def __init__(self, ip):
		self.__ip = ip
		self.__dossier = Dossier(self.__ip)
		self.__abuse = AbuseIPDB(self.__ip)
		self.__ipvoid = IPVoid(self.__ip)
		self.__xforce = XForce(self.__ip)
		self.__virustotal = VirusTotal(self.__ip)
		self.__tornode = True if self.__ip in requests.get('https://check.torproject.org/torbulkexitlist').text else False

	def getIP(self) -> str:
		return self.__ip

	def getAbuseIPDB(self) -> AbuseIPDB:
		return self.__abuse

	def getIPVoid(self) -> IPVoid:
		return self.__ipvoid
	
	def getXForce(self) -> XForce:
		return self.__xforce
	
	def getVirusTotal(self) -> VirusTotal:
		return self.__virustotal

	def getWhois(self) -> Dossier:
		return self.__dossier

	def isTorNode(self) -> bool:
		return self.__tornode

	def __str__(self):
		output = str(self.__ip)
		output += '\n' + 'WHOIS'
		output += '\n' + str(self.__dossier)
		output += '\n\n' + 'Reputation'
		output += '\n' + '•\tAbuseIPDB: ' + str(self.__abuse) + ('' if not self.__abuse.isWhitelisted() else '\tATTENZIONE! Questo IP risulta in whitelist.')
		output += '\n' + '•\tIPVoid: ' + str(self.__ipvoid)
		output += '\n' + '•\tIBM X-Force: ' + str(self.__xforce)
		output += '\n' + '•\tVirusTotal: ' + str(self.__virustotal)
		output += ('\n\n' + self.getIP() + ' è un nodo di uscita Tor.') if self.isTorNode() else ''
		output += ('\n\n' + self.__abuse.str_category()) if self.__abuse.getCategory() is not None else ''
		return output