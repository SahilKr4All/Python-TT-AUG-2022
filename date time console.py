Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from datetime import datetime
dt = datetime.now()
dt.strftime("%d/%m/%y")
'23/08/22'
dt.strftime("%d/%m/%y,%p")
'23/08/22,PM'
dt.strftime("%d/%m/%y,%a")
'23/08/22,Tue'
dt.strftime("%H:%M:%S,%p")
'15:41:49,PM'
# 24 hour clock
dt.strftime("%I:%M:%S,%p")
'03:41:49,PM'
#12 Hour clock format
