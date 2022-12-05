'''
# CHANGE LOG
- Blink control (half on, half off)
- Time control (3.5secs per seq)
- A dictonary controls the blink and frecuency 
- Add counter until complete 20 reps.
'''
#ASIGNA ALTA PRIORIDAD DE EJECUCION DE PROCESOS EN WINDOWS
import psutil, os, platform
p = psutil.Process(os.getpid())

if platform.system() == 'Darwin' or platform.system() == 'Linux':
    p.nice(20)
else:
    p.nice(psutil.HIGH_PRIORITY_CLASS)



from decimal import *
import sys
from tkinter import *  
from PIL import ImageTk,Image  
import time
import threading

from datetime import timedelta
from datetime import datetime
import random

from pyOpenBCI import OpenBCICyton
from pylsl import StreamInfo, StreamOutlet
import numpy as np

root = Tk()  

root.title("Adquisición de Datos EEG")
root.configure(bg='black')
root.attributes('-fullscreen', True)

#Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# screen_width = 800
# screen_height = 600
#Print the screen size
print("Screen width:", screen_width) 
print("Screen height:", screen_height)


# CV_W=300
# CV_H=300
# canvas = Canvas(root, width = CV_W, height = CV_H,bg='black') 
# canvas = Canvas(root, width = screen_width, height = screen_height,bg='black') 
canvas = Canvas(root, width = screen_width, height = screen_height, bd=0, highlightthickness=0, relief='ridge',bg = 'black') # delete canvas contour
canvas.pack() # put the canvas in some window position  




img1 = ImageTk.PhotoImage(Image.open("BLANCO.png"))  #5Hz
img2 = ImageTk.PhotoImage(Image.open("ROJO.png"))  #9Hz  
img3 = ImageTk.PhotoImage(Image.open("GRIS.png"))  #13Hz
img4 = ImageTk.PhotoImage(Image.open("VERDE.png"))  #17Hz
img5 = ImageTk.PhotoImage(Image.open("DRAW.png"))  # 3.5 sec

def Frecuencias(frecuencia_1,frecuencia_2,frecuencia_3,frecuencia_4):

    '''
    Esta funcion recepta el valor de las frecuencias, que se quieren usar para los estimulos visuales,
     y las asigna a la correspondiente figura de acuerdo al orden determinado

     Se pueden asiganar hasta 5 frecuencias

     Cabe recalcar que al usar un monitor para mostrar los estimulo, estos estimulos deben ser seteados a frecuencias que sea divisores
     enteros de la tasa de refresco del monitor

    '''
    periodos = [Decimal(1/frecuencia_1),Decimal(1/frecuencia_2),Decimal(1/frecuencia_3),Decimal(1/frecuencia_4)]

    dcblue={'tag':'blue','x':screen_width-110,'y':(screen_height/2),'img':img1,'t':periodos[0]} #5hz
    dcred={'tag':'red','x':screen_width/2,'y':110,'img':img2,'t':periodos[1]}#9hz
    dcyellow={'tag':'yellow','x':110,'y':(screen_height/2),'img':img3,'t':periodos[2]}#13hz
    dcgreen={'tag':'green','x':(screen_width/2),'y':screen_height-110,'img':img4,'t':periodos[3]}#17hz

    ls_seqs=[dcblue,dcred,dcyellow,dcgreen]

    return ls_seqs

# PARAMETRIZAR NUMERO DE REPETICIONES PARA COLOCAR EN UN FOR 


def begin():
    '''Esta funcion marca el inicio de la secuencia
    muestra la imagen base durante 3.5 segundos
    '''

    canvas.delete("all")
    canvas.create_image((screen_width/2),(screen_height/2),anchor=CENTER,image=img5,tags='base')
    root.update()
    #print (20*">"+" Begin")
    time.sleep(3.5)
    clean()
# the images arer added or reduced in 110 px because the center position cuts the image (221x221) in the middle 




def end():
    canvas.create_image(screen_width-110,(screen_height/2), anchor=CENTER,image=img1,tags='blue')
    canvas.create_image((screen_width/2),110, anchor=CENTER,image=img2,tags='red')
    canvas.create_image(110,(screen_height/2), anchor=CENTER,image=img3,tags='yellow')
    canvas.create_image((screen_width/2),screen_height-110, anchor=CENTER,image=img4,tags='green')
    canvas.create_image((screen_width/2),(screen_height/2),anchor=CENTER,image=img5,tags='base')
    root.update()
    print (20*"<"+" End")
    time.sleep(3.5)
    clean()



def clean():
    canvas.delete("all") # delete by tag
    root.update()
    #print (20*"*"+" All figs deleted ")


    
# def sequence(**kwargs):
def sequence(tag,x,y,img,t):
    '''Esta funcion se encarga de realizar el parpadeo de la imagen recibida a la frecuencida determinada 
    en la funcion Frecuencias

    recibe los atributos que acompañan a la etiqueta con la que está asocidad la imagen a mostrar
    '''
    t_b_on = datetime.now() - start_time
    print('+ {} ON time elapsed (hh:mm:ss.ms) {}'.format(tag,t_b_on))

    if (t_b_on>=d):
        diff = t_b_on
        print('+ {} ON time elapsed (hh:mm:ss.ms) {}'.format(tag,t_b_on))
        return diff

    #limpia la pantalla
    canvas.delete("all")

    t_b_on = datetime.now() - start_time
    print('+ {} ON time elapsed (hh:mm:ss.ms) {}'.format(tag,t_b_on))

    if (t_b_on>=d):
        diff = t_b_on
        print('+ {} ON time elapsed (hh:mm:ss.ms) {}'.format(tag,t_b_on))
        return diff

    #primera parte del periodo de la imagen (se muestra la imagen):
    canvas.create_image(x,y,anchor=CENTER,image=img,tags=tag)
    root.update()
    
    t_b_on = datetime.now() - start_time
    print('+ {} ON time elapsed (hh:mm:ss.ms) {}'.format(tag,t_b_on))

    if (t_b_on>=d):
       diff = t_b_on
       print('+ {} ON time elapsed (hh:mm:ss.ms) {}'.format(tag,t_b_on))
       return diff 
    
    time.sleep(float(Decimal(t/2)))


    t_b_on = datetime.now() - start_time

    if (t_b_on>=d):
       diff = t_b_on
       print('+ {} ON time elapsed (hh:mm:ss.ms) {}'.format(tag,t_b_on))
       return diff 
    



    canvas.delete(tag)
    root.update()
    t_b_off = datetime.now() - start_time
    print('- {} OFF time elapsed (hh:mm:ss.ms) {}'.format(tag,t_b_off))

    if (t_b_off>=d):
        diff = t_b_off
        print('+ {} OFF time elapsed (hh:mm:ss.ms) {}'.format(tag,t_b_off))
        return diff

    time.sleep(float(Decimal(t/2)))

    t_b_off = datetime.now() - start_time
    print('- {} OFF time elapsed (hh:mm:ss.ms) {}'.format(tag,t_b_off))

    if (t_b_off>=d):
        diff = t_b_off
        print('+ {} OFF time elapsed (hh:mm:ss.ms) {}'.format(tag,t_b_off))
        return diff


    canvas.delete("all")

    diff = datetime.now() - start_time

    return diff

        


#dcblue={'tag':'blue','x':screen_width-110,'y':(screen_height/2),'img':img1,'t':100} #5hz
#dcred={'tag':'red','x':screen_width/2,'y':110,'img':img2,'t':55.5555555555556}#9hz
#dcyellow={'tag':'yellow','x':110,'y':(screen_height/2),'img':img3,'t':38.4615384615384615}#13hz
#dcgreen={'tag':'green','x':(screen_width/2),'y':screen_height-110,'img':img4,'t':29.4117647058824}#17hz

#ls_seqs=[dcblue,dcred,dcyellow,dcgreen]

# begin()
# d = timedelta(seconds=3,microseconds=500000 )
# start_time = datetime.now()
# time_elapsed = datetime.now() - start_time
# while time_elapsed<=d:
#     time_elapsed = datetime.now() - start_time
#     sequence(**dcred)
# end()





cnt=0
hora_inicio=datetime.now()
print(hora_inicio)

ls_seqs = Frecuencias(5,8,12,15)

while (cnt<100): #para que se repitan 20 veces cada uno de los estimulos visuales
    begin()
    random.shuffle(ls_seqs) #random 
    for i in ls_seqs:
        d = timedelta( seconds=3, microseconds=499999 )
        start_time = datetime.now()

        time_elapsed = datetime.now() - start_time
        while time_elapsed<d:
            time_elapsed = datetime.now() - start_time
            time_elapsed = sequence(**i)
            #time_elapsed = datetime.now() - start_time
            
        cnt+=1
        # clean()


tiempo_pasado = datetime.now() - hora_inicio
print (tiempo_pasado)
end()




def closeWindow(event):
    root.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing



#------------------------------ Streaming de datos EEG


def lsl_streamers(sample):
      outlet_eeg.push_sample(np.array(sample.channels_data)*SCALE_FACTOR_EEG)
      outlet_aux.push_sample(np.array(sample.aux_data)*SCALE_FACTOR_AUX)

def grabacionEEG():


    SCALE_FACTOR_EEG = (4500000)/24/(2**23-1) #uV/count
    SCALE_FACTOR_AUX = 0.002 / (2**4)


    print("Creating LSL stream for EEG. \nName: OpenBCIEEG\nID: OpenBCItestEEG\n")

    info_eeg = StreamInfo('OpenBCIEEG', 'EEG', 16, 250, 'float32', 'OpenBCItestEEG')

    print("Creating LSL stream for AUX. \nName: OpenBCIAUX\nID: OpenBCItestEEG\n")

    info_aux = StreamInfo('OpenBCIAUX', 'AUX', 3, 250, 'float32', 'OpenBCItestAUX')

    outlet_eeg = StreamOutlet(info_eeg)
    outlet_aux = StreamOutlet(info_aux)

    board = OpenBCICyton(port='COM5', daisy=True)

    board.start_stream(lsl_streamers)


#def 

root.bind('<Escape>', closeWindow)
root.mainloop() 
