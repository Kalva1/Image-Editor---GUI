#!/usr/bin/env python
# coding: utf-8

# In[2]:


import PySimpleGUI as sg
from PIL import Image,ImageEnhance,ImageFilter

def window1():
    sg.theme('Dark Blue2')  
    
    layout = [  [sg.Text('Select an image',text_color='white',font='Calibri',size=(40,1))],
                [sg.FileBrowse(),sg.Input(tooltip='Select only an Image File',border_width=5,size=(40,2))],
                 [sg.OK(), sg.Cancel()]] 
 
    
   
     
    window = sg.Window('Image Manipulation', layout) 
    while True:
        event, values = window.read()
        if event=='OK':
            try:
                Image.open(values[0])
            except:
                sg.popup("Please select an Image File")
                window1()  
                
        window.close()
        return values[0]
        
        if event in(None,'Cancel'): 
            window.close() 
            break


def Manipulation(values,photo):
    if(values['transparent']!=''):
        photo.putalpha(int(values['transparent']))     

    if(values['blur']!=''):
        photo =photo.filter(ImageFilter.GaussianBlur(int(values['blur'])/100,))
        
    if(values['color']!=''):
        en=ImageEnhance.Color(photo)
        photo=en.enhance(int(values['color'])/100)
        
    if(values['sharpness']!=''):
        en=ImageEnhance.Sharpness(photo)
        photo=en.enhance(int(values['sharpness'])/100)
    if(values['resize']==''):
        size=.3
        photo= photo.resize( [int(size* s) for s in photo.size] )  
    else:  
        size=int(values['resize'])/100
        photo = photo.resize( [int(size* s) for s in photo.size] )
        
    return photo
        



def Image_Editing(filepath):
    while True:  
        photo = Image.open(filepath)
        z = 0.3
        photox = photo.resize( [int(z * s) for s in photo.size] )
        x,y=photox.size
        photox.save('m.png')
        
        layout=[[sg.Text('Resize'),sg.In(key='resize')],[sg.Text('Grayscale'),sg.In(key='color')],
                [sg.Text('Sharpness'),sg.In(key='sharpness')],
              [sg.Text('Transparency'),sg.In(key="transparent")], [sg.Text('Blur'),sg.In(key='blur')],
               [sg.Frame(title="original image",layout=[[sg.Image(r'm.png')]],
               size=(x+100,y+100))],[sg.OK(),sg.Quit()]]
        
        window = sg.Window('Image Manipulations', layout,size=(x+300,y+300))      
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=='Quit': 
            window.close()
            break
        photo=Manipulation(values, photo)
        Window2(values, photo)
        window.close()
    
def Window2(values,photo):
    x,y=photo.size
    photo.save('m.png')
    layout=[[sg.Frame(title="Manipulated image",layout=[[sg.Image(r'm.png')]],size=(x+300,y+300))],[sg.SaveAs(), sg.Quit()]]
    window = sg.Window('Image Output', layout,size=(y+400,y+400))
    event,values=window.read()
    window.close()


filepath=window1()
Image_Editing(filepath)


# In[ ]:




