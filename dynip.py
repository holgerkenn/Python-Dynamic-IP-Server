#!/usr/bin/env python3

import os
import smtplib
import sys
import json
import socket
import time
import cgi, cgitb


def DoMail(message:str):
        fromaddr = "<source e-mail address>"
        toaddr  = "<destination e-mail address>"
        # Add the From: and To: headers at the start!
        msg = ("From: %s\r\nTo: %s\r\n" % (fromaddr, toaddr))
        msg = msg + "Subject: DynDNS Message\r\n\r\n"
        msg = msg + message
        msg = msg + "\r\n"
        server = smtplib.SMTP('<your favorite e-mail server that works without auth, e.g., localhost>')
        server.starttls()
        server.sendmail(fromaddr, toaddr, msg)
        server.quit()


def Main():
        log = open("/tmp/dyndnslog","a");
        result = {'success':'true'};
        print (time.asctime(time.localtime()),':',file=log,end='')
        form = cgi.FieldStorage()
        formip = form.getvalue('ip')
        formuser = form.getvalue('user')
        formpass = form.getvalue('pass')
        formhost = form.getvalue('host')
        message= "entry: " + formip + ","+ formuser + ","+ formpass+ ","+ formhost
        print (message,file=log)
        DoMail(message)
        log.close()
        print ('Content-Type: text/html\n\n')
        print ('<html><body>OK</body></html>')

if __name__ == '__main__':
        Main()
