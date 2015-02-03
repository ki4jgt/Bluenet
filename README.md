# Bluenet
The goal of Bluenet is to be an open sourced, asymmetrically encrypted, P2P communications platform. Intended services include IM, file transfer, and walkie-talkie. In current, this project is merely a server. I haven't decided in which direction I'm taking it yet.

# Why Bluenet?
The original intended use of this project was as a chat program in a bluetooth mesh network setting, where peers would forward messages to one another. Because of the short distance of bluetooth and development of the B.A.T.M.A.N. routing protocol, 802.11 seemed like a much better alternative. 

# What are you plans?
The aim of this project is to provide secure, authenticated communications to anyone wishing to have them. It is a personal desire of mine to have this project replace cellular network as users bounce from mesh node to mesh node, relaying messages for one another. However, since this project neither has emergency services patched in, nor does it provide real-time communications, I doubt it will get that far. I can dream though.

# What's up with the constant use of Json?
With my initial exposure to MongoDB, Json (Bson) clicked with me. Since then I've dreamed of incorperating Json into all my programming projects. I even had an idea of replacing html with Json (Totally possible ;). Json is a huge part of this project. Messages are formatted in Json. Server responses are formatted in Json. Configuration files are formatted in Json.

# settings.conf
The settings.conf file (which you may create) isn't required for your server to run. Lack of a settings file means that your server will assume default values. That being said, some people prefer customization. For you guys, I have included this feature. As always, the file must be written in a PROPERLY FORMATTED Json dictionary.

VALUE					EXPECTATION							EXPLAINATION
"port"					integer								This is the port your server will be running on. Failure
															to provide a value here will result in a random port
															being chosen.

"_id"					20 Character string					Your network ID is attached to every search or message
															exchange performed on your behalf within the network.
															This is NOT the ID which your messages are sent to. It is
															a feature which makes message delivery within the network
															easier. This option has no practical purpose. It just
															serves as a bit of customization.
