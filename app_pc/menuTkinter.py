# -*- coding: utf-8 -*-
import wx
import methods
import serial


class mainWindow(wx.Frame):
    def __init__(self, parent, title):

        windowWidth = 500
        windowHeight = 700

        wx.Frame.__init__(self, parent, title="RC Car Controller", size=(windowHeight,windowWidth))

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


        #Labels
        labelTextoMovimento = wx.StaticText(self, label="Movimento", pos=(36, 50), style=wx.ALIGN_CENTER)
        labelTextoOpcoes = wx.StaticText(self, label="OPÇÕES", pos=(550, 50), style=wx.ALIGN_CENTER)
        labelLigarLuzes = wx.StaticText(self, label="Ligar as Luzes (frente)", pos=(400, 120), style=wx.ALIGN_CENTER)

        #Definicoes das fontes das labels
        fontToLabelTextoMovimento = wx.Font(26, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        fontToLabelTextoOpcoes = wx.Font(26, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        fontToLabelLigarLuzes = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        labelTextoMovimento.SetFont(fontToLabelTextoMovimento)
        labelTextoOpcoes.SetFont(fontToLabelTextoOpcoes)
        labelLigarLuzes.SetFont(fontToLabelLigarLuzes)

        ##ESTES 4 botoes ESTAO CERTOS!!!
        buttonMoveUP = wx.Button(self, pos=(85, 100), size=(45, 45), id=wx.ID_ANY, label="UP")
        buttonMoveDOWN = wx.Button(self, pos=(85, 150), size=(45, 45), id=wx.ID_ANY, label="DOWN")
        buttonMoveLEFT = wx.Button(self, pos=(35, 150), size=(45, 45), id=wx.ID_ANY, label="LEFT")
        buttonMoveUP = wx.Button(self, pos=(135, 150), size=(45, 45), id=wx.ID_ANY, label="RIGHT")
        buttonCarLightsOn = wx.Button(self, pos=(430, 140), size=(30, 30), id=wx.ID_ANY, label="ON") #FALTA A ACCAO PARA O BOTAO
        buttonCarLightsOff = wx.Button(self, pos=(470, 140), size=(30, 30), id=wx.ID_ANY, label="OFF") #FALTA A ACCAO PARA O BOTAO


        #adiciona os metodos aos botoes
        self.Bind(wx.EVT_MENU, self.btnMenuSair_onClick, btnMenuSair)
        self.Bind(wx.EVT_MENU, self.btnMenuSobre_onClick, btnMenuSobre)
        self.Bind(wx.EVT_MENU, self.btnMenuWebSite_onClick, btnMenuWebsite)
        #buttonOn.Bind(wx.EVT_BUTTON, self.buttonOn_onClick)

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



# MAIN
if __name__ == "__main__":
    app = wx.App()
    frame = mainWindow(None, "RC Car Controller")
    app.MainLoop()