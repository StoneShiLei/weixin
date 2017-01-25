# -*- coding: utf-8 -*-
# filename: index.py
#get/postģ��

#����web��hashlib��receive��sendģ��
import hashlib
import web
import receive
import send

class Index(object):
    def GET(self):
        try:
            data = web.input()#��ȡ���ݣ�δ֪�û����ͣ�
            if len(data) == 0:#���ֱ������ҳ���� len��data��=0
                return "hello, this is index view"
            signature = data.signature #������ȡsig time nonce echostr����
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "shilei0811" #�밴�չ���ƽ̨����\������������Ϣ��д

            list = [token, timestamp, nonce]#�����б�
            list.sort()
			
            sha1 = hashlib.sha1() #��ϣ�㷨
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "index/GET func: hashcode, signature: ", hashcode, signature
			
            if hashcode == signature:#�Ա�����
                return echostr#��֤�ɹ�
            else:
                return ""
        except Exception, Argument:
            return Argument
	
    def POST(self):
		try:
			webData = web.data()#��ȡxml
			print "Handle Post webdata is ", webData #��̨��ӡ��־
			recMsg = receive.parse_xml(webData) #���ý���ģ�飬����XML
			#���recMsgΪreceive.Msg�� and recMsg.MsgType�������ص�ֵΪ text ��
			if isinstance(recMsg,receive.Msg) and recMsg.MsgType == 'text':
				#toUser fromUser������ ���ڷ�����Ϣ 
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName
				content = "test" #�ظ��û����ı� �������sql
				#sendMsg����sendģ���TextMsg�࣬��������������ʼ��
				sendMsg = send.TextMsg(toUser,fromUser,content)
				#print sendMsg
				
				#����sendģ���TextMsg���send����������xml��
				return sendMsg.send()
			else:
				print "�ݲ�����"
				return "success"
		except Exception, Argment:
			return Argment
		
		
		
		

	
