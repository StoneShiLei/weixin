# -*- coding:utf-8 -*-
# filename:receive.py
#接收微信信息，解析xml

#导入 xml模块
import xml.etree.ElementTree as ET

#解析xml函数
def parse_xml(web_data):
	xmlData = ET.fromstring(web_data)
	msg_type = xmlData.find('MsgType').text
	#判定xml的消息类型
	if msg_type == 'text':
		#如果是文本消息，将xml设为TextMsg类
		return TextMsg(xmlData)
	elif msg_type == 'image':
		pass

class Msg(object):#Msg超类 init初始化，代码为获取xml内各项关键信息
	def __init__(self,xmlData):
		self.ToUserName = xmlData.find('ToUserName').text
		self.FromUserName = xmlData.find('FromUserName').text
		self.CreateTime = xmlData.find('CreateTime').text
		self.MsgType = xmlData.find('MsgType').text
		self.MsgId = xmlData.find('MsgId').text

class TextMsg(Msg):#TextMsg类为Msg子类
	def __init__(self,xmlData):
		#TextMsg的初始化为调用Msg超类的初始化，这种做法是为了代码重用
		#将文本信息图片信息等对象初始化的时候不用每个都写一遍find
		Msg.__init__(self,xmlData)
		#解码用户发送信息为Utf-8，默认为ansi
		self.Content = xmlData.find('Content').text.encode("utf-8")
		

# class ImageMsg(msg):
	# def __init__(self, xmlData):
        # Msg.__init__(self, xmlData)
        # self.PicUrl = xmlData.find('PicUrl').text
        # self.MediaId = xmlData.find('MediaId').text	