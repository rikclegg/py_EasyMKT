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
