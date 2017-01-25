# -*- coding: utf-8 -*-
# filename: index.py
#get/post模块

#导入web，hashlib，receive，send模块
import hashlib
import web
import receive
import send

class Index(object):
    def GET(self):
        try:
            data = web.input()#获取数据（未知用户发送）
            if len(data) == 0:#如果直接用网页访问 len（data）=0
                return "hello, this is index view"
            signature = data.signature #依次提取sig time nonce echostr参数
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "shilei0811" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]#排序列表
            list.sort()
			
            sha1 = hashlib.sha1() #哈希算法
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "index/GET func: hashcode, signature: ", hashcode, signature
			
            if hashcode == signature:#对比数据
                return echostr#验证成功
            else:
                return ""
        except Exception, Argument:
            return Argument
	
    def POST(self):
		try:
			webData = web.data()#获取xml
			print "Handle Post webdata is ", webData #后台打印日志
			recMsg = receive.parse_xml(webData) #调用接收模块，分析XML
			#如果recMsg为receive.Msg类 and recMsg.MsgType方法返回的值为 text 则：
			if isinstance(recMsg,receive.Msg) and recMsg.MsgType == 'text':
				#toUser fromUser反过来 用于返回信息 
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName
				content = "test" #回复用户的文本 这里调用sql
				#sendMsg加入send模块的TextMsg类，并用三个参数初始化
				sendMsg = send.TextMsg(toUser,fromUser,content)
				#print sendMsg
				
				#调用send模块的TextMsg类的send方法，发送xml！
				return sendMsg.send()
			else:
				print "暂不处理"
				return "success"
		except Exception, Argment:
			return Argment
		
		
		
		

	
