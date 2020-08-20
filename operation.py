
import os
import webbrowser

class Task:
    
    def __init__(self):
        pass
    def do(self, text: str):
        text = text.lower()
        text = text.split()
        if 'open' in text:
            if 'notepad' in text:
                os.system('start notepad')
                return 'Starting Notepad'
            elif 'chrome' in text:
                os.system('start chrome')
                return 'Starting Chrome'
            elif 'vlc' in text:
                os.system('start vlc')
                return 'Starting vlc'
            elif 'word' in text:
                os.system('start winword')
                return 'Starting Word'
            elif 'excel' in text:
                os.system('start excel')
                return 'Starting excel'
            elif 'powerpoint' in text:
                os.system('start powerpnt')
                return 'Starting powerpoint'
            elif 'brave' in text:
                os.system('start brave')
                return
            elif 'InternetExplorer'  in text:
                os.system('start microsoftedge')
                return
            else:
                return "I don't understand it please tell properly "
        
        elif 'search' in text:
            webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' %text[-1])
            return f'searching {text[-1]} on google '
             
                
