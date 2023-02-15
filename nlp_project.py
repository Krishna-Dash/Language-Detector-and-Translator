#import statements
from tkinter import *
from langdetect import detect, DetectorFactory, detect_langs
import PyPDF2
from tkinter import filedialog
import tkinter.font as tkFont
from iso639 import languages
from pprint import pprint
import tkinter as tk
from PIL import Image, ImageTk
from googletrans import Translator
from tkinter import ttk
from playsound import playsound
from gtts import gTTS
import tkinter
import customtkinter


#settings
DetectorFactory.seed = 0

def on_resize(event):
    # resize the background image to the size of label
    image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
    # update the image of the label
    l.image = ImageTk.PhotoImage(image)
    l.config(image=l.image)

root = tkinter.Tk()

root.geometry('900x650')

bgimg = Image.open("C:\\Users\\KRISHNA DAS\\Downloads\\aron-visuals-bZZp1PmHI0E-unsplash.jpg") # load the background image
l = tk.Label(root)
l.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
l.bind('<Configure>', on_resize) # on_resize will be executed whenever label l is resized

head = Label(root, text="LANGUAGE DETECTOR",font=('Times', 20,'bold'),bg="#1877F2")
root.configure(bg="#A098BA")

#related to input
input_var=StringVar()
input_Label= Label(root,text='Provide Text Here',font=('times',15,'bold'),bg="#1877F2") #input text
e= Entry(root,textvariable=input_var,font=('times',15,)) #input

#related to input
lang_code=StringVar()
langcode_code= Entry(root,textvariable=lang_code,font=('times',15,)) #input

#Create a Text Box
text= Text(root,width= 30,height=1,font=('times',15,'bold'))
lang_detected= Label(root,text='Language Detected is',font=('times',15,'bold'),bg="#1877F2")

#Create a Text Box
engconvert= Text(root,width= 30,height=1,font=('times',15,'bold'))


#button
def predict():
    input = input_var.get()
    print(detect(input))# console
    language_detected = languages.get(alpha2=detect(input))
    print(language_detected.name) #console
    text.delete(1.0, END)
    text.insert(1.0, language_detected.name)

file=StringVar()
#button
def open_pdf():
   file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files",".pdf"),("All Files",".*")))
   if file:
      #Open the PDF File
      pdf_file= PyPDF2.PdfFileReader(file)
      #Select a Page to read
      page= pdf_file.getPage(0)
      #Get the content of the Page
      content=page.extractText()
      print(detect(content))
      language_detected = languages.get(alpha2=detect(content))
      print(language_detected.name) #console pr print
      text.delete(1.0, END)
      text.insert(1.0, language_detected.name)

#button
def convert_to_eng():
    translator=Translator()
    translated = translator.translate(input_var.get(), src=detect(input_var.get()), dest='en')
    print(translated.text)
    engconvert.delete(1.0, END)
    engconvert.insert(1.0, translated.text)

def convert_to_lang():
    translator=Translator()
    translated = translator.translate(input_var.get(), src=detect(input_var.get()), dest=lang_code.get())
    print(translated.text)
    engconvert.delete(1.0, END)
    engconvert.insert(1.0, translated.text)

def convert_to_audio():
    translator=Translator()
    translated = translator.translate(input_var.get(), src=detect(input_var.get()), dest=lang_code.get())
    print(translated.text)
    #final text
    textfinal=translated.text
    obj = gTTS(text=textfinal, lang= lang_code.get(), slow=False)
    obj.save("exam.mp3")
    playsound("exam.mp3")


#button
def close():
    root.destroy()

#buttons

myButton=customtkinter.CTkButton(master=root,text="Detect Language",corner_radius=10,command=predict,width=150,)
browse=customtkinter.CTkButton(master=root,text="Choose File and Detect",corner_radius=10,command=open_pdf,width=200)
convert=customtkinter.CTkButton(master=root,text="Convert To English",corner_radius=0,command=convert_to_eng,width=200)
converttoanylangauge=customtkinter.CTkButton(master=root,text="Convert To any Language",corner_radius=10,command=convert_to_lang,width=200)
voice=customtkinter.CTkButton(master=root,text="voice",corner_radius=30,command=convert_to_audio)
exit=customtkinter.CTkButton(master=root,text="Exit",corner_radius=30,command=close)

#positioning
head.grid(row=0,column=2,padx= 40,pady=40)
input_Label.grid(row=1,column=1,padx= 50, pady= 20)
e.grid(row=1,column=2,padx= 20, pady= 20)
browse.grid(row=1,column=3,padx= 20, pady= 20)

myButton.grid(row=2,column=2,padx= 20, pady= 20)

lang_detected.grid(row=3,column=1)
text.grid(row=3,column=2)

converttoanylangauge.grid(row=4,column=2)
langcode_code.grid(row=4,column=3)

convert.grid(row=4,column=1,padx=20,pady=20)


engconvert.grid(row=5,column=2,padx= 20, pady= 20)
voice.grid(row=5,column=3)

exit.grid(row=6,column=3)

root.mainloop()


#Questo è il video del nostro progetto---italian
#rafraîchir les villes et les maisons tout en restant écologique---------french
#Questo è il video del nostro progetto---italian
