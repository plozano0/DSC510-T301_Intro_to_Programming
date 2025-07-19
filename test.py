# pip install pywin32
import win32com.client
outlook = win32com.client.Dispatch("Outlook.Application")
# call the outlook variable through debug mode
outlook