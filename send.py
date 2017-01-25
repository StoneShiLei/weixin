# -*- coding: utf-8 -*-
# filename: send.py
#������Ϣ���ܣ���Ҫ���͵���Ϣд��xml

#����timeģ�� Ϊ�˼���ʱ���
import time

#����sendģ���TextMsg��
class TextMsg(object):
	#ʹ��3����ֵ��ʼ������
	#__dictΪ˽�з������ⲿ���ɷ���
	#dict()�������½�һ���ֵ䣬�����ֵ�����Ϊ__dict����
	def __init__(self,toUserName,fromUserName,content):
		self.__dict = dict()
		#��ʼ��ʱΪ�ֵ���Ӽ�ֵ��
		self.__dict['ToUserName'] = toUserName
		self.__dict['FromUserName'] = fromUserName
		#���ʱ�����΢��xmlʱ���ʽΪ����int
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['Content'] = content
	
	#����send����
	def send(self):
		#���뻨����Ϊformat��ʽ��
		#textΪ�̶��ı�������Ҫ���ģ�ֱ��д��
		#ע��ʱ����ĸ�ʽ
		XmlForm = """
		<xml>
			<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
			<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
			<CreateTime>{CreateTime}</CreateTime>
			<MsgType><![CDATA[text]]></MsgType>
			<Content><![CDATA[{Content}]]></Content>
		</xml>
		"""
		
		#**self.__dict �ؼ��ֲ���  ������һ���ֵ�
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