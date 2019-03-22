import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox
import os
root=Tk()
root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('TechMates')
frame.config(background='light blue')
label = Label(frame, text="TechMates",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="/home/seidu/PROJECT/project/demo.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)



def hel():
   os.System(register.py)

def Contri():
   tkinter.messagebox.showinfo("Contributors","\n Prince Ashong\n Boamah Marry \nJim Etornam Odo \n Festus Kwame Awumey\nXornam Egbetorke\n")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Face Recognition Attendance System\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')
                                    
   

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="About",menu=subm1)
subm1.add_command(label="Tools",command=anotherWin)
subm1.add_command(label="Contributors",command=Contri)



def exitt():
   import sys;sys.exit()

  
def web():
   capture =cv2.VideoCapture(0)
   while True:
      ret,root=capture.read()
      gray = cv2.cvtColor(root, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',root)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   capture.release()
   cv2.destroyAllWindows()

def webrec():
   capture =cv2.VideoCapture(0)
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample1.avi',fourcc,11.0,(640,480))
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      op.write(frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   op.release()
   capture.release()
   cv2.destroyAllWindows()   

def webdet():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          
           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

       
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   capture.release()
   cv2.destroyAllWindows()
 
def webdetRec():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample2.avi',fourcc,9.0,(640,480))

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          

           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
       op.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   op.release()      
   capture.release()
   cv2.destroyAllWindows()

   
def alert():
   mixer.init()
   alert=mixer.Sound('beep-07.wav')
   alert.play()
   time.sleep(0.1)
   alert.play()   
   
def blink():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
   blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')

   while True:
      ret, frame = capture.read()
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray)

      for (x,y,w,h) in faces:
         print(x,y,w,h)
         font = cv2.FONT_HERSHEY_COMPLEX
         cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]

         eyes = eye_cascade.detectMultiScale(roi_gray)
         for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

         blink = blink_cascade.detectMultiScale(roi_gray)
         for(eyx,eyy,eyw,eyh) in blink:
            cv2.rectangle(roi_color,(eyx,eyy),(eyx+eyw,eyy+eyh),(255,255,0),2)
            alert()
            img_item = "my-image.png"
            cv2.imwrite(img_item, roi_color)

            color = (225, 200, 100)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
          break
         
  
   capture.release()
   cv2.destroyAllWindows()

   
but1=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=web,text='Open Cam',font=('helvetica 15 bold'))
but1.place(x=5,y=104)

but2=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webrec,text='Open Cam & Record',font=('helvetica 15 bold'))
but2.place(x=5,y=176)

but3=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webdet,text='Open Cam & Detect',font=('helvetica 15 bold'))
but3.place(x=5,y=250)

but4=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webdetRec,text='Detect & Record',font=('helvetica 15 bold'))
but4.place(x=5,y=322)

but5=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=blink,text='Detect Eye Blink & Record With Sound',font=('helvetica 15 bold'))
but5.place(x=5,y=400)

but5=Button(frame,padx=5,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but5.place(x=210,y=478)


root.mainloop()

