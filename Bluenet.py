#!/usr/bin/env python3

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

#Testing github

from platform import system
from os import system as command
import threading
import socketserver
import json
from BluenetLib import *
from time import sleep

version = "15.2 Alpha"

if system() == "Linux" or "Darwin":
	command("clear")
if system == "Windows":
	command("cls")

database = database()
settings = settings().retset()

port = 0
netid = ""
ping = True

if "port" in settings:
	port = settings["port"]
if "_id" in settings:
	netid = settings["_id"]
if "ping" in settings:
	ping = settings["ping"]
if "start" in settings:
	for entry in settings["start"]:
		database.potpeers.append(entry)
if netid == "":
	netid = id_gen()
	
if ping == True:
	beacon(port)

class BroadcastServer(socketserver.BaseRequestHandler):
	
	def handle(self):
		data = self.request[0].strip().decode()
		socket = self.request[1]
		if data[:8] == "Bluenet:":
			print("Ping From: " + self.client_address[0] + ":" + data[8:])

class BroadcastThreaded(socketserver.ThreadingMixIn, socketserver.UDPServer):
	pass

class BluenetServer(socketserver.BaseRequestHandler):
	
	def handle(self):
		self.test = False
		self.data = self.request.recv(8192).decode()
		print(self.data)
		if self.data == "status":
			self.request.sendall(json.dumps({"_id":netid, "peers":database.peers}).encode())
			self.test = True
		if self.data[:8] == "request:":
			self.peer = send(self.client_address, self.data[8:], "status".encode())
			self.peer = TryJson(self.peer)
			if len(database.peers) < 10:
				if self.peer != False and len(self.peer) != 1:
					if "_id" in self.peer:
						if self.peer["_id"] not in database.peers and len(self.peer["_id"] == 20 and isinstance(self.peer["_id"], str):
							database.peers.append({self.peer["_id"]:{"internet":{"ip":self.client_address, "port":self.data[8:]}}})
							print("Database: " + self.peer["_id"] + " added.")
							self.request.sendall(str("OK:" + netid).encode())
							self.test = True
			else:
				self.request.sendall(json.dumps(database.peers).encode())
				
		if self.test == False:
			#Send "Not Correctly Formatted"
			self.request.sendall("NCF".encode())
			
class BluenetThreaded(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
		
if __name__ == "__main__":
	server = BluenetThreaded(("", port), BluenetServer)
	broadcast = BroadcastThreaded(("", 4601), BroadcastServer)
	print("Server Port: " + str(server.server_address[1]))
	print("Network ID: " + netid + "\n")
	thread = threading.Thread(target=server.serve_forever)
	broadcast = threading.Thread(target=broadcast.serve_forever)
	thread.daemon = False
	broadcast.daemon = False
	thread.start()
	broadcast.start()
	print("Bluenet Server v.%s Running!!!\n============================================" % (version,))
