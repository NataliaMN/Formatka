
"""
Created on Wed Mar 22 15:42:24 2023

@author: Natalia
"""

import tkinter as tk
from tkinter.messagebox import showinfo
import numpy as np
import pandas as pd 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class MainWindow(tk.Tk):
    def __init__(self,):
        super().__init__()
        
        # i, k, l - liczby podtrzebne w dalszej czesci do aktualizacji danych na wykresach
        self.i = 1
        self.k = 1
        self.l = 101
        
        self.title('SUPER TYTUL')
        self.geometry('500x400')
        
       
        self.label = tk.Label(self, text='Duży NAPIS', font=("Arial", 35))
        
        # pozycja napisu
        self.label.place(x=430,y=0)
        
        # utworzenie figury, ktora bedzie zawierac nasze wykresy 
        # i umieszczenie jej na obiekcie figure_canva na naszym GUI
        self.figure = Figure(figsize=(10, 4), dpi=100)
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)
        
        # dodanie narzedzia do nawigacji po wykresach
        NavigationToolbar2Tk(self.figure_canvas, self)
        
        # przywolanie funkcji Plot w celu narysowania wykresow
        self.Plot()
        
        # utworzenie trzech przyciskow do aktualizacji wykresow
        # command laczy przycisk z funkcja, ktora zostanie wykonana po
        # prycisnieciu guzika
        self.button_updateax1 = tk.Button(self,  text ="update1", height= 2, width=20)
        self.button_updateax2 = tk.Button(self,  text ="update2", height= 2, width=20, command = self.UpdatePlot2)
        self.button_updateax3 = tk.Button(self,  text ="update3", height= 2, width=20, command = self.UpdatePlot3)
        
        # wybranie pozycji dla figury i przyciskow
        self.figure_canvas.get_tk_widget().place(x=0,y=60)
        self.button_updateax1.place(x=100,y=450)
        self.button_updateax2.place(x=430,y=450)
        self.button_updateax3.place(x=770,y=450)
   
    def Plot(self):
  
        # dodanie pierwszego wykresu
        ax1 = self.figure.add_subplot(1,3,1)
        
        X1 = np.linspace(5, 20, 30)
        
        ax1.plot(X1, X1 * X1 / 100)
        ax1.set_title('Tytul')
        ax1.set_ylabel('y')
        ax1.set_xlabel('x')
        
        
        # dodanie drugiego wykresu 
        self.ax2 = self.figure.add_subplot(1,3,2)
        self.ax2.set_title('Tytul2')
        self.ax2.set_ylabel('y')
        self.ax2.set_xlabel('x')
        
        self.y2List = np.array([] ) 
        new_y = self.ImportDataCSV("dlugi_losowy",self.k,self.l)
        self.line2, = self.ax2.plot(new_y)
               
        # dodanie trzeciego wykresu
        self.ax3 = self.figure.add_subplot(1,3,3)
        self.ax3.set_title('Tytul3')
        self.ax3.set_ylabel('y')
        self.ax3.set_xlabel('x')
        
        yList = self.ImportData(self.i)
        self.line, = self.ax3.plot(yList)
        
        # rysowanie wykresow
        self.figure_canvas.draw()  
        
        # wybranie odstepu miedzy wykresami
        self.figure.tight_layout(pad=1.0)
     
            
    def ImportData(self,i):
        #  pobieranie danych z kolejnych plikow xlsx i przypisywanie ich do
        #  zmiennej dane
        title = "losowe"+str(i)+".xlsx"
        dane = pd.read_excel(title, header=None)
        dane = np.array(dane)
        return dane 
    
    def ImportDataCSV(self,title,k,l):
        tekst = title
        title = str(tekst)+".csv"
        dane_csv = np.genfromtxt(title, delimiter=';')
        dane_csv = np.array(dane_csv)
        dane_csv = dane_csv[k:l]
        
        return dane_csv 
    
    def UpdatePlot2(self):
        # zwiekszanie liczby k i l w celu prezentacji kolejnych danych z tego
        #  samego pliku z danymi 
        # dane sa aktualizowane poprzez self.line2.set_ydata()
        self.k = self.k+4
        self.l = self.l+4
        new_y = self.ImportDataCSV("dlugi_losowy",self.k,self.l)
        self.line2.set_ydata(new_y)
        self.figure_canvas.draw()  
    
    def UpdatePlot3(self):
        # zwiekszenie liczby i w celu prezentacji danych z kolejnego pliku
        self.i = self.i+1
        yList = self.ImportData(self.i)
        self.line.set_ydata(yList)
        self.figure_canvas.draw()  
      
