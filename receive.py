# -*- coding:utf-8 -*-
# filename:receive.py
#����΢����Ϣ������xml

#���� xmlģ��
import xml.etree.ElementTree as ET

#����xml����
def parse_xml(web_data):
	xmlData = ET.fromstring(web_data)
	msg_type = xmlData.find('MsgType').text
	#�ж�xml����Ϣ����
	if msg_type == 'text':
		#������ı���Ϣ����xml��ΪTextMsg��
		return TextMsg(xmlData)
	elif msg_type == 'image':
		pass

class Msg(object):#Msg���� init��ʼ��������Ϊ��ȡxml�ڸ���ؼ���Ϣ
	def __init__(self,xmlData):
		self.ToUserName = xmlData.find('ToUserName').text
		self.FromUserName = xmlData.find('FromUserName').text
		self.CreateTime = xmlData.find('CreateTime').text
		self.MsgType = xmlData.find('MsgType').text
		self.MsgId = xmlData.find('MsgId').text

class TextMsg(Msg):#TextMsg��ΪMsg����
	def __init__(self,xmlData):
		#TextMsg�ĳ�ʼ��Ϊ����Msg����ĳ�ʼ��������������Ϊ�˴�������
		#���ı���ϢͼƬ��Ϣ�ȶ����ʼ����ʱ����ÿ����дһ��find
		Msg.__init__(self,xmlData)
		#�����û�������ϢΪUtf-8��Ĭ��Ϊansi
		self.Content = xmlData.find('Content').text.encode("utf-8")
		

# class ImageMsg(msg):
	# def __init__(self, xmlData):
        # Msg.__init__(self, xmlData)
        # self.PicUrl = xmlData.find('PicUrl').text
        # self.MediaId = xmlData.find('MediaId').text	