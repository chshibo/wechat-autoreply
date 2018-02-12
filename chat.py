import sys
import itchat
from time import gmtime, strftime

STATUS = ""


@itchat.msg_register(itchat.content.TEXT)
def handle_content(msg):
    user = msg['FromUserName']
    user_info = itchat.search_friends(userName=user)
    f = open('msg.list', 'a+')
    f.write("User: " + user_info['NickName'] + " Alias:" + user_info['Alias'] +
            " Sends you a text message: " + msg['Text'] + " @ " +
            strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    f.close()
    return "您的信息我已收到。由于我正在" + STATUS + "，将稍后回复。急事致电:+17348469266 (您的消息我已储存于本地，故无法撤回）"


@itchat.msg_register(itchat.content.PICTURE)
def handle_content(msg):
    user = msg['FromUserName']
    user_info = itchat.search_friends(userName=user)
    f = open('msg.list', 'a+')
    f.write("User: " + user_info['NickName'] + " Alias:" + user_info['Alias'] +
            " Sends you a picture message: @ " +
            strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    f.close()
    return "您的图片我已收到。由于我正在" + STATUS + "，将稍后回复。急事致电:+17348469266"


@itchat.msg_register(itchat.content.RECORDING)
def handle_content(msg):
    user = msg['FromUserName']
    user_info = itchat.search_friends(userName=user)
    f = open('msg.list', 'a+')
    f.write("User: " + user_info['NickName'] + " Alias:" + user_info['Alias'] +
            " Sends you a recording message: " + " @ " +
            strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    f.close()
    return "您的语音已收到。由于我正在" + STATUS + "，将稍后回复。急事致电:+17348469266"


@itchat.msg_register(itchat.content.CARD)
def handle_content(msg):
    user = msg['FromUserName']
    user_info = itchat.search_friends(userName=user)
    f = open('msg.list', 'a+')
    f.write("User: " + user_info['NickName'] + " Alias:" + user_info['Alias'] +
            " Sends you a card message:  @ " +
            strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    f.close()
    return "您的信息我已收到。由于我正在" + STATUS + "，将稍后回复。急事致电:+17348469266"


if __name__ == "__main__":
    STATUS = sys.argv[1]
    itchat.auto_login(hotReload=True)
    itchat.run()
