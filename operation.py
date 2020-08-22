
import os
import webbrowser

class Task:
    
    def __init__(self):
        pass
    def do(self, text: str):
        text = text.lower()
        text = text.split()
        if ('open' in text or 'run' in text  or 'start' in text):
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
                
            elif 'Internet Explorer'  in text :
                os.system('start microsoftedge')
                return 'Starting MicrosoftEdge'

            elif 'vscode'  in text or 'visual studio code'  in text :
                os.system('start code')
                return 'Starting visual studio code'

            elif 'my computer' in text or 'this pc' in text or 'explorer' in text:
                os.system('start explorer')
                return 'Starting explorer'
            
            elif 'map' in text:
                webbrowser.open_new_tab('https://www.google.com/maps' )

            else:
                return "I don't understand it please tell properly what to open ? \N{thinking face}"
        
        else:
            text = text [1:]
            text = ''.join([str(elem) for elem in text])
            webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' %text)
            return f'searching {text} on google \N{Globe with Meridians}'
            
             
                
