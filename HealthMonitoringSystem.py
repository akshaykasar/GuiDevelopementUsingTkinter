# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:38:17 2020

@author: Akshay
"""

from biosppy.signals import ecg
from tkinter import*
import random 
import time
from tkinter.filedialog import askopenfilename 
import pandas as pd
import scipy
import scipy.io
import scipy.fftpack
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
from matplotlib.figure import Figure 
from scipy import fftpack
import numpy as np


def createWindow(NewWindow):
    NewWindow.geometry("1600x700+0+0")
    NewWindow.title("Health Monitoring System System")
    

    Tops = Frame(NewWindow, width =1600,height=50 ,bg="powder blue" ,relief=SUNKEN)
    Tops.pack(side=TOP,fill='x')
    #===============================Time=======================================================
    localtime=time.asctime(time.localtime(time.time())) #datetimeFunction 
    #===============================Info============================================
    lblinfo=Label(Tops, font=('arial',50,'bold'),text="Health Monitoring System" ,fg="steel Blue",bd=10,anchor='n')
    lblinfo.pack(anchor='center')
    
    lblinfo2=Label(Tops, font=('arial',30,'bold'),text="EEE Department, IIT Guwahati" ,fg="steel Blue",bd=10,anchor='w')
    lblinfo2.pack(anchor='center')
    
    lblDateTime=Label(Tops, font=('arial',20,'bold'),text=localtime ,fg="steel Blue",bd=10,anchor='w')
    lblDateTime.pack(anchor='center')
    
    # upBtn=Button(root,bd=8,fg="Steel Blue",font=('arial',30,'bold'),
    #         text="Upload ECG Signal",bg="powder blue",command=getdata).pack(pady=50)

    # btnExit=Button(root,bd=8, fg="Steel Blue",font=('arial',30,'bold'),
    #                 text="Exit Application", bg="powder blue", command = qExit).pack(pady=30)
    
    lblinfo4=Label(NewWindow, font=('arial',20,'bold'),text="Project Guide- Prof-S.Dandapat" ,fg="dark Blue",bd=10,anchor='w')
    lblinfo4.pack(side=BOTTOM)
    
    lblinfo3=Label(NewWindow, font=('arial',20,'bold'),text="Developed by - Akshay Kasar" ,fg="dark Blue",bd=10,anchor='w')
    lblinfo3.pack(side=BOTTOM)
          
def MagandAngle(fftdb,fftangle):
    Magnitude.set(fftdb[freq.get()])
    Angle.set(fftangle[freq.get()])  
    
    


def hamming():
    
    hamWindow=Toplevel(root)
    createWindow(hamWindow)

    samfreq=fs.get()
    out= ecg.ecg(signal=df, sampling_rate=samfreq, show=True)
    
    # ts (array) – Signal time axis reference (seconds).
    # filtered (array) – Filtered ECG signal.
    # rpeaks (array) – R-peak location indices.
    # templates_ts (array) – Templates time axis reference (seconds).
    # templates (array) – Extracted heartbeat templates.
    # heart_rate_ts (array) – Heart rate time axis reference (seconds).
    # heart_rate (array) – Instantaneous heart rate (bpm).
    
    ts=out[0]
    filtered=out[1]
    rpeaks=out[2]
    period=rpeaks[2]-rpeaks[1]
    plt.plot(df)
    #getting spectrum 
    ham=np.hamming(period)
    spedata=ham*filtered[0:period]
    
    spedft=fftpack.fft(spedata)
    magnitude=np.abs(spedft)
    ph=np.angle(spedft,deg=True)
    f=np.linspace(0,samfreq,len(spedft))
    
    frame5=Frame(hamWindow )
    frame5.pack(fill='x')
    
    
    
    fig = Figure(figsize = (5, 3), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(f,magnitude)
    plot1.set_xlabel('frequency')
    plot1.set_ylabel('Magnitude')
    plot1.set_xlim=(0,period)
    canvas = FigureCanvasTkAgg(fig, master = frame5)
    canvas.draw() 
    canvas.get_tk_widget().grid(row=0,column=0)
    
    btnExit6=Button(frame5, fg="Steel Blue",font=('arial',15,'bold'),
    text="Back", bg="powder blue", command =lambda: qExit(hamWindow)).grid(row=0,column=1,padx=30,pady=30)

def hanning():
    
    hanWindow=Toplevel(root)
    createWindow(hanWindow)

    samfreq=fs.get()
    out= ecg.ecg(signal=df, sampling_rate=samfreq, show=True)
    
    # ts (array) – Signal time axis reference (seconds).
    # filtered (array) – Filtered ECG signal.
    # rpeaks (array) – R-peak location indices.
    # templates_ts (array) – Templates time axis reference (seconds).
    # templates (array) – Extracted heartbeat templates.
    # heart_rate_ts (array) – Heart rate time axis reference (seconds).
    # heart_rate (array) – Instantaneous heart rate (bpm).
    
    ts=out[0]
    filtered=out[1]
    rpeaks=out[2]
    period=rpeaks[2]-rpeaks[1]
    plt.plot(df)
    #getting spectrum 
    han=np.hanning(period)
    spedata=han*filtered[0:period]
    
    spedft=fftpack.fft(spedata)
    magnitude=np.abs(spedft)
    ph=np.angle(spedft,deg=True)
    f=np.linspace(0,samfreq,len(spedft))
    
    frame5=Frame(hanWindow )
    frame5.pack(fill='x')
    
    
    
    fig = Figure(figsize = (5, 3), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(f,magnitude)
    plot1.set_xlabel('frequency')
    plot1.set_ylabel('Magnitude')
    plot1.set_xlim=(0,period)
    canvas = FigureCanvasTkAgg(fig, master = frame5)
    canvas.draw() 
    canvas.get_tk_widget().grid(row=0,column=0)
    
    btnExit6=Button(frame5, fg="Steel Blue",font=('arial',15,'bold'),
    text="Back", bg="powder blue", command =lambda: qExit(hanWindow)).grid(row=0,column=1,padx=30,pady=30)

def bartlet():
    
    barWindow=Toplevel(root)
    createWindow(barWindow)

    samfreq=fs.get()
    out= ecg.ecg(signal=df, sampling_rate=samfreq, show=True)
    
    # ts (array) – Signal time axis reference (seconds).
    # filtered (array) – Filtered ECG signal.
    # rpeaks (array) – R-peak location indices.
    # templates_ts (array) – Templates time axis reference (seconds).
    # templates (array) – Extracted heartbeat templates.
    # heart_rate_ts (array) – Heart rate time axis reference (seconds).
    # heart_rate (array) – Instantaneous heart rate (bpm).
    
    ts=out[0]
    filtered=out[1]
    rpeaks=out[2]
    period=rpeaks[2]-rpeaks[1]
    plt.plot(df)
    #getting spectrum 
    bar=np.bartlett(period)
    spedata=bar*filtered[0:period]
    
    spedft=fftpack.fft(spedata)
    magnitude=np.abs(spedft)
    ph=np.angle(spedft,deg=True)
    f=np.linspace(0,samfreq,len(spedft))
    
    frame5=Frame(barWindow )
    frame5.pack(fill='x')
    
    
    
    fig = Figure(figsize = (5, 3), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(f,magnitude)
    plot1.set_xlabel('frequency')
    plot1.set_ylabel('Magnitude')
    plot1.set_xlim=(0,period)
    canvas = FigureCanvasTkAgg(fig, master = frame5)
    canvas.draw() 
    canvas.get_tk_widget().grid(row=0,column=0)
    
    btnExit6=Button(frame5, fg="Steel Blue",font=('arial',15,'bold'),
    text="Back", bg="powder blue", command =lambda: qExit(barWindow)).grid(row=0,column=1,padx=30,pady=30)
    

def wintech():
    wnwindow=Toplevel(root)
    createWindow(wnwindow)
    
    ham=Button(wnwindow, fg="Steel Blue",font=('arial',15,'bold'),
    text="Hamming Window", bg="powder blue" ,command=hamming).pack(pady=10)
    
    han=Button(wnwindow, fg="Steel Blue",font=('arial',15,'bold'),
    text="Hanning Window", bg="powder blue" ,command=hanning).pack(pady=10)
    
    bart=Button(wnwindow, fg="Steel Blue",font=('arial',15,'bold'),
    text="Bartlet Window", bg="powder blue" ,command=bartlet).pack(pady=10)
    
    btnExit5=Button(wnwindow, fg="Steel Blue",font=('arial',15,'bold'),
    text="Back", bg="powder blue", command =lambda: qExit(wnwindow)).pack(pady=30)
    
    
    
    
    wnwindow.mainloop()

def calHR():
    hrwindow=Toplevel(root)
    createWindow(hrwindow)
    
    samfreq=fs.get()
    out= ecg.ecg(signal=df, sampling_rate=samfreq, show=True)
    
    heartratearr=out[6]
    heartratets=out[5]
    heartrate=np.mean(heartratearr)
    global hr
    hr=StringVar()
    hr.set(str(heartrate))
    frame3=Frame(hrwindow)
    frame3.pack(fill='x')
    
    fig = Figure(figsize = (5, 3), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(heartratets,heartratearr)
    plot1.set_xlabel('time')
    plot1.set_ylabel('heartrate')
    canvas = FigureCanvasTkAgg(fig, master = frame3)
    canvas.draw() 
    canvas.get_tk_widget().grid(row=0,column=0)
   
    frame4=Frame(frame3)
    
   
    hrlbl=Label(frame4,fg="Steel Blue",font=('arial',15,'bold'),text="Avg Heart Rate").pack(pady=5,padx=30)
   
    heartOut=Entry(frame4,font=('arial',15,'bold'),textvariable=hr)
    heartOut.pack(padx=30,pady=5) 
   
    btnExit4=Button(frame4, fg="Steel Blue",font=('arial',15,'bold'),
    text="Back", bg="powder blue", command =lambda: qExit(hrwindow)).pack(padx=30,pady=30)
    
    frame4.grid(row=0,column=1)
    
    hrwindow.mainloop()    

def showSpectrum():
    
    speWindow=Toplevel(root)
    createWindow(speWindow)

    samfreq=fs.get()
    out= ecg.ecg(signal=df, sampling_rate=samfreq, show=True)
    
    # ts (array) – Signal time axis reference (seconds).
    # filtered (array) – Filtered ECG signal.
    # rpeaks (array) – R-peak location indices.
    # templates_ts (array) – Templates time axis reference (seconds).
    # templates (array) – Extracted heartbeat templates.
    # heart_rate_ts (array) – Heart rate time axis reference (seconds).
    # heart_rate (array) – Instantaneous heart rate (bpm).
    
    ts=out[0]
    filtered=out[1]
    rpeaks=out[2]
    period=rpeaks[2]-rpeaks[1]
    plt.plot(df)
    #getting spectrum 
    spedata=filtered[0:period]
    
    spedft=fftpack.fft(spedata)
    magnitude=np.abs(spedft)
    ph=np.angle(spedft,deg=True)
    f=np.linspace(0,samfreq,len(spedft))
    
    frame1=Frame(speWindow )
    frame1.pack(fill='x')
    
    
    
    
    lblMag=Label(frame1, font=('arial',15,'bold'),text="Magnitude Spectrum" ,fg="dark Blue",bd=10,anchor='w')
    lblMag.grid(row=0,column=0)
    
    fig = Figure(figsize = (5, 3), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(f,magnitude)
    plot1.set_xlabel('frequency')
    plot1.set_ylabel('Magnitude')
    plot1.set_xlim=(0,period)
    canvas = FigureCanvasTkAgg(fig, master = frame1)
    canvas.draw() 
    canvas.get_tk_widget().grid(row=1,column=0)
    
    
    frame2 = Frame(frame1 ,relief=SUNKEN)
    frame2.grid(row=1,column=1,padx=50)
    
    lbl1=Label(frame2, font=('arial',15,'bold'),text="Enter Frequency" ,fg="black",bd=10,anchor='w')
    lbl1.pack(side=TOP)
    

    global Magnitude
    global Angle
    global freq
    
    freq=IntVar()
    Magnitude=StringVar()
    Angle=StringVar() 
    
    freqEntry=Entry(frame2,font=('arial',15,'bold'), textvariable=freq ,bd=10, insertwidth=4,
                   bg="white")
    freqEntry.pack(pady=15)
    
    freqBtn=Button(frame2,bd=8,fg="Steel Blue",font=('arial',15,'bold'),
    text="Find Magnitude and Angle",bg="powder blue", command=lambda :MagandAngle(magnitude,ph)).pack(pady=15)
    
    magOut=Entry(frame2,font=('arial',15,'bold'),textvariable=Magnitude ,bd=10, insertwidth=4,
                   bg="white",justify='right')
    magOut.pack(pady=10)
    
    AngOut=Entry(frame2,font=('arial',15,'bold'),textvariable=Angle ,bd=10, insertwidth=4,
                   bg="white")
    AngOut.pack()

    
    btnExit3=Button(frame1,bd=8, fg="Steel Blue",font=('arial',15,'bold'),
    text="Back", bg="powder blue", command =lambda: qExit(speWindow)).grid(row=0,column=1)
    
    
    lblAng=Label(frame1, font=('arial',15,'bold'),text="Phase Spectrum" ,fg="dark Blue",bd=10,anchor='w')
    lblAng.grid(row=0,column=2)
    
    
    fig2 = Figure(figsize = (5, 3), dpi = 100)
    plot2 = fig2.add_subplot(111)
    plot2.plot(f,ph)
    plot2.set_xlabel('freuency')
    plot2.set_ylabel("Angle in degrees")
    plot2.set_xlim(0,period)
    canvas2 = FigureCanvasTkAgg(fig2, master = frame1)
    canvas2.draw() 
    canvas2.get_tk_widget().grid( row=1,column=2)
    
    
    # fig, ax = plt.subplots()
    # ax.plot(f,magnitude)
    # ax.set_xlabel('frequency')
    # ax.set_ylabel(' Magnitude')
    # ax.set_xlim(0,period)
    
    # fig2, ax2 = plt.subplots()
    # ax2.plot(f,ph)
    # ax2.set_xlabel('frequency')
    # ax2.set_ylabel(' Angle in degress')
    # ax2.set_xlim(0,period)    
        
    speWindow.mainloop()  

def getdata():
    
    
    global df
    name = askopenfilename(filetypes=[('CSV', '*.csv',), ('Excel', ('*.xls', '*.xlsx')),('WAV','*.wav'),('MP3','*.mp3')])
    if name:
        if name.endswith('.csv'):
            df=pd.read_csv(name)
        else:
            df=pd.read_excel(name)
    
    N=df.shape[1]
    df=(df.values).reshape(N)
    df=df-np.mean(df)
    UploadWindow=Toplevel(root)
    createWindow(UploadWindow)
      
    
    
    global fs
    fs=IntVar()

    fslbl=Label(UploadWindow, text="Enter sampling frequency",font=('arial',15,'bold')).pack(pady=10)
    
    fsentry=Entry(UploadWindow,textvariable=fs).pack(pady=10)
    
    speBtn=Button(UploadWindow,fg="Steel Blue",font=('arial',15,'bold'),
    text="Show Spectrum",bg="powder blue",command=showSpectrum).pack(pady=10)
    
    hrBtn=Button(UploadWindow,fg="Steel Blue",font=('arial',15,'bold'),
    text="Calculate Heart rate",bg="powder blue",command=calHR).pack(pady=10)
    
    wnBtn=Button(UploadWindow,fg="Steel Blue",font=('arial',15,'bold'),
    text="Apply Window Technique",bg="powder blue",command=wintech).pack(pady=10)
    
    btnExit2=Button(UploadWindow, fg="Steel Blue",font=('arial',15,'bold'),
    text="Back To Home", bg="powder blue", command =lambda: qExit(UploadWindow)).pack(pady=10)
    
    UploadWindow.mainloop()
    

def qExit(window):
    window.destroy();        
    

   

root=Tk()
createWindow(root)


upBtn=Button(root,bd=8,fg="Steel Blue",font=('arial',30,'bold'),
text="Upload ECG Signal",bg="powder blue",command=getdata).pack(pady=50)

btnExit=Button(root,bd=8, fg="Steel Blue",font=('arial',30,'bold'),
text="Exit Application", bg="powder blue", command =lambda: qExit(root)).pack(pady=30)



root.mainloop()
