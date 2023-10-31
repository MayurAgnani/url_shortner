1:1  chat

send message POST

v1/send_message

{

    sender:
    reciver:
    message:
    timestamp:
}


get_message GET

v1/messages/{reciver}/{sender}


user 1 - 1,2,3
user 2 - 4,5,6

user1/user2 = 1,2,3


#Scaling
for high thoughput
caching
sepearte read ans write server
