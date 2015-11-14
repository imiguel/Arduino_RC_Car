# -*- coding: utf-8 -*-
import wx
import methods


class mainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title="RC Car Controler", size=(700,500))

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
        dialog = wx.MessageDialog(self, "Programa para controlar RC Car\n \nDesenvolvido por: Miguel Rosa\n \n \n \nTodos os direitos reservados\n \n \nMértola 2016", "RC Car Controller - Sobre")
        dialog.ShowModal()#Mostra a caixa de dialogo
        dialog.Destroy() #destroi a caixa de dialogo

    def btnMenuWebSite_onClick(self, event):
        methods.openWebPageFromGitHub()



# MAIN
if __name__ == "__main__":
    app = wx.App(False)
    frame = mainWindow(None, "RC Car Controller")
    app.MainLoop()