#! /usr/bin/python3
import socket
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "irc.freenode.net" # Server
channel = "#newchan" # Channel
botnick = 'bits'
adminname = 'brute4s99'
exitcode = 'bye ' + botnick

ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send(bytes("USER "+botnick+" "+botnick+" "+botnick+" "+botnick+"\n","UTF-8")) #We are basically filling out a form with this line and saying to set all the fields to the bot nickname.
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # assign the nick to the bot


q=[]
    
# CONNECTED SUCCESSFULLY 
def joinchan(chan):
    ircsock.send(bytes('JOIN '+chan+'\n','UTF-8'))
    ircmsg=''
    while ircmsg.find('End of /NAMES list.')==-1:   # KEEP PRINTING(for debugging only) TILL YOU GET LIST OF ALL MEMBERS!
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)

def ping(): # respond to server Pings.
    ircsock.send(bytes("PONG :pingis\n", "UTF-8"))

def sendmsg(msg, target=channel): # sends messages to the target.
    ircsock.send(bytes("PRIVMSG "+ target +" :"+ msg +"\n", "UTF-8"))
def commandmode():
    while 1:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)
        if ircmsg.find("PING :") != -1:
                ping()
        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!',1)[0][1:]
            message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
        if message == '!' and name not in q:
            q.append(name)
        if message =='next':
            if len(q)==0:
                sendmsg('Everyone is happy and calm.')
            else:
                sendmsg(q.pop(0)+' will ask the Question now')
                if len(q)!=0:
                    sendmsg(q[0]+' is next.')
        if message == '#stop' and name.lower()==adminname.lower():
            if len(q)!=0:
                sendmsg('There still are '+str(len(q))+' people left in q')
            return                
        if '<eof>' in message  or '<eom>' in message :
            q.remove(name)
        if message == 'showq':
            for i in q: sendmsg(i,name)




def main(): 
    joinchan(channel)
    print ("Connection successful! Now showing messages !!!")
    while 1:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)
        if ircmsg.find("PING :") != -1:
                ping()
        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!',1)[0][1:]
            message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
        
        
        if (message.lower()).find(botnick) != -1:   # TAlking to me, maybe ?
            if len(message.split()) == 2:
                if message.split()[0] not in ('stop','bye','goobye') and message.split()[1] not in ('stop','bye','goobye','.',','):
                    sendmsg("Hello " + name + "!")
        if message == '!' and name not in q:
            q.append(name)
        if message =='#oye' and name.lower()==adminname.lower():
            commandmode()
        if message == '<eof>' or message == '<eom>':
            q.remove(name)
        if message == 'showq':
            for i in q: sendmsg(i,name)

        if name.lower() == adminname.lower() and message.rstrip() == exitcode:
            sendmsg("oh...okay. :'(")
            ircsock.send(bytes("QUIT \n", "UTF-8"))
            return  
        print(name)
        print(message)            
print("Let's do this !")
main()