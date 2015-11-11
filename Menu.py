# -*- coding: utf-8 -*-
import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title="RC Car Controller", size=(700,500))


        self.Show(True)



#Mostra no ecra
app = wx.App(False)
frame = MainWindow(None, "RC Car Controller")
app.MainLoop()