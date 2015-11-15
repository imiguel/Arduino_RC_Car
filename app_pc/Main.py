# -*- coding: utf-8 -*-
import wx
import methods
import serial


class mainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title="RC Car Controller", size=(700,500))

        #Criar uma barra de menus e sub-menus
        menuBar = wx.MenuBar(0)

        #Sub-menu "Ficheiro"
        fileMenu = wx.Menu()
        btnMenuSair = wx.MenuItem(fileMenu, wx.ID_CLOSE, "Sair") #Botao
        fileMenu.AppendItem(btnMenuSair)
        menuBar.Append(fileMenu, "&Ficheiro")

        #sub-menu "Sobre"
        fileAbout = wx.Menu()
        btnMenuSobre = wx.MenuItem(fileAbout, wx.ID_HELP, "Sobre") #Botao
        fileAbout.AppendItem(btnMenuSobre)
        btnMenuWebsite = wx.MenuItem(fileAbout, wx.ID_HOME, "Pagina oficial") #Botao
        fileAbout.AppendItem(btnMenuWebsite)
        menuBar.Append(fileAbout, "&Sobre")

        #Adiciona a barra de menus
        self.SetMenuBar(menuBar)


        self.label = wx.StaticText(self, label="BOTÕES PARA O LED", pos=(5, 80), style=wx.ALIGN_LEFT)


        ##Coloca os botoes
        buttonOn = wx.Button(self, pos=(20, 100), size=(100,25), id=wx.ID_ANY, label="LED ON")
        buttonOn.Bind(wx.EVT_BUTTON, self.buttonOn_onClick)
        buttonOff = wx.Button(self, pos=(20, 130), size=(100,25), id=wx.ID_ANY, label="LED OFF")
        buttonOff.Bind(wx.EVT_BUTTON, self.buttonOff_onClick)


        #adiciona os metodos aos botoes
        self.Bind(wx.EVT_MENU, self.btnMenuSair_onClick, btnMenuSair)
        self.Bind(wx.EVT_MENU, self.btnMenuSobre_onClick, btnMenuSobre)
        self.Bind(wx.EVT_MENU, self.btnMenuWebSite_onClick, btnMenuWebsite)

        #mostra a janela
        self.Show(True)


    ##Metodos das accoes dos botoes
    def btnMenuSair_onClick(self, event):
        self.Close()

    def btnMenuSobre_onClick(self, event):
        methods.aboutDialogMessage(self)

    def btnMenuWebSite_onClick(self, event):
        methods.openWebPageFromGitHub()

    def buttonOn_onClick(self, event):
        methods.testeDoBotaoOn()

    def buttonOff_onClick(self, event):
        methods.testeDoBotaoOff()



# MAIN
if __name__ == "__main__":
    app = wx.App()
    frame = mainWindow(None, "RC Car Controller")
    app.MainLoop()