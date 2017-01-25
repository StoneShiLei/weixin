# -*- coding: utf-8 -*-
# filename: send.py
#发送信息功能，将要发送的信息写入xml

#导入time模块 为了加入时间戳
import time

#定义send模块的TextMsg类
class TextMsg(object):
	#使用3个数值初始化对象
	#__dict为私有方法，外部不可访问
	#dict()函数会新建一个字典，将新字典设置为__dict方法
	def __init__(self,toUserName,fromUserName,content):
		self.__dict = dict()
		#初始化时为字典添加键值对
		self.__dict['ToUserName'] = toUserName
		self.__dict['FromUserName'] = fromUserName
		#添加时间戳，微信xml时间格式为整形int
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['Content'] = content
	
	#定义send方法
	def send(self):
		#加入花括号为format格式化
		#text为固定文本，不需要更改，直接写好
		#注意时间戳的格式
		XmlForm = """
		<xml>
			<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
			<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
			<CreateTime>{CreateTime}</CreateTime>
			<MsgType><![CDATA[text]]></MsgType>
			<Content><![CDATA[{Content}]]></Content>
		</xml>
		"""
		
		#**self.__dict 关键字参数  导入了一个字典
		return XmlForm.format(**self.__dict)
		
# class ImageMsg(Msg):
    # def __init__(self, toUserName, fromUserName, mediaId):
        # self.__dict = dict()
        # self.__dict['ToUserName'] = toUserName
        # self.__dict['FromUserName'] = fromUserName
        # self.__dict['CreateTime'] = int(time.time())
        # self.__dict['MediaId'] = mediaId
    # def send(self):
        # XmlForm = """
        # <xml>
        # <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        # <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        # <CreateTime>{CreateTime}</CreateTime>
        # <MsgType><![CDATA[image]]></MsgType>
        # <Image>
        # <MediaId><![CDATA[{MediaId}]]></MediaId>
        # </Image>
        # </xml>
        # """
        # return XmlForm.format(**self.__dict)