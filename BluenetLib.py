#Bluenet is copyright (C) 2015, KI4JGT
#
#This file is part of Bluenet.
#
#Bluenet is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.
#
#Bluenet is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Bluenet.  If not, see <http://www.gnu.org/licenses/>.

from random import choice
import socket
import json
from os.path import isfile

def id_gen():
	lets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	gid = ""
	while len(gid) < 20:
		gid = gid + choice(lets)
	return gid
	
def beacon(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	sock.sendto(str("Bluenet:%s" % (port,)).encode(), ("<broadcast>", 4601))
	return None
	
def send(ip, port, message):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip, port))
	try:
		sock.sendall(message)
		response = sock.recv(8192)
	finally:
		sock.close()
	if response:
		return response
	else:
		return False

def TryJson(s):
	try:
		results = json.load(s)
	except ValueError:
		return False
	return results

class database():
	
	def __call__(self):
		return 0
	
	def __init__(self):
		self.potpeers = {}
		self.peers = {}
		self.messages = {}
		self.networkhashes = {}
		return None

class settings():
	
	def __call__(self):
		return 0
	
	def __init__(self):
		self.settings = {}
		if isfile("settings.conf"):
			try:
				self.fob = open("settings.conf", "r")
				self.settings = json.loads(self.fob.read().rstrip("\n"))
				self.fob.close()
			except:
				print("Error: Settings file compromised!!!")
		else:
			pass
		
	def retset(self):
		return self.settings
