
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
                return 'Starting Brave'
                
            elif 'InternetExplorer'  in text:
                os.system('start microsoftedge')
                return 'Starting MicrosoftEdge'
            else:
                
                return "I don't understand it please tell properly what to open ? \N{thinking face}"
        
        elif 'search' in text:
            text = text [1:]
            text = ''.join([str(elem) for elem in text])
            webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' %text)
            return f'searching {text[-1]} on google \N{Globe with Meridians}'
        else:
            return "Unable to do task \N{Disappointed face}"
            
             
                
