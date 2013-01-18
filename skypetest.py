import Skype4Py
import time
import pkgutil
import datetime
import json
import sys
import logging
import time
import re
import os
import urllib2
import urllib





skype = Skype4Py.Skype()
skype.FriendlyName = 'Skype4Py_Example'
skype.Attach()
print "Attachment status is " + str(skype.AttachmentStatus)
chats = skype.RecentChats
for chat in chats:
	print chat.Name
