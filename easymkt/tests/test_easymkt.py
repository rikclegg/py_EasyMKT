'''
Created on 01 Dec 2018

@author: RCLEGG2@BLOOMBERG.NET
'''

import unittest
import time
from easymkt import easymkt 
from easymkt.notification import Notification

class TestEasyMKT(unittest.TestCase):

    def process_notification(self,notification):

        if notification.category == Notification.NotificationCategory.MKTDATA:
            if notification.type == Notification.NotificationType.NEW or notification.type == Notification.NotificationType.UPDATE: 
                print("EasyMKT Notification MKTDATA -> NEW/UPDATE")
        

    def test_start_easymkt_does_not_fail(self):

        raised = False
        
        try:
            pass
            emkt = easymkt.EasyMKT()
            emkt.add_field("LAST_PRICE")
            sec = emkt.add_security("BBHBEAT Index")
            sec.add_notification_handler(self.process_notification)
            emkt.start()
            
            time.sleep(5)
            
        except Exception as e:
            print("Error: " + str(e))
            raised=True
        
        self.assertFalse(raised)


    def test_external_request_non_blocking(self):
        
        raised = False

        try:
            emkt = easymkt.EasyMKT()
            emkt.start()
            
            req = emkt.create_request("ReferenceDataRequest")
            
            req.append("securities", "IBM US Equity")

            req.append("fields", "PX_LAST")

            self.pending_result=True
            
            emkt.send_request(req, self.message_handler)
            
        except BaseException as e:
            print("Error: " + str(e))
            raised=True
            
        self.pending_result=True
        
        while self.pending_result:
            pass
            
        self.assertFalse(raised)


    def message_handler(self,msg,partial):
        print (msg)
        if not partial:
            self.pending_result=False
        
        
    def test_external_request_blocking(self):
        
        raised = False

        msg = None
        
        try:
            emkt = easymkt.EasyMKT()
            emkt.start()
            
            req = emkt.create_request("ReferenceDataRequest")
            
            req.append("securities", "IBM US Equity")

            req.append("fields", "PX_LAST")

            msg = emkt.send_request(req)

            pxlast = msg.getElement("securityData").getValue(0).getElement("fieldData").getElement("PX_LAST").getValue()
            print(pxlast)
            
        except BaseException as e:
            print("Error: " + str(e))
            raised=True
            
           
        print(msg)
        
        self.assertFalse(raised)
