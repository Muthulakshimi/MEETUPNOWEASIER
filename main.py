import os
import eel

from tkinter import filedialog, Tk, messagebox
import os
import apis_caller as tb
the_l=list()
eel.init('web')



@eel.expose                         # Expose this function to Javascript
def button_handler_py(name_user,email_user,desc_user):
    #print("Javascript name_user : {}".format(name_user))
    #print("Javascript email_user : {}".format(email_user))
    #print("Javascript desc_user : {}".format(desc_user))
    #print("Javascript password {}".format(mpass))
    the_t={"Name":name_user,"Email":email_user,"Description":desc_user}
    the_l.insert(0,the_t)


@eel.expose
def getFile ():
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1) # without that it wil go behind all others apps
    file = filedialog.askopenfilename(parent=root,
     initialdir=os.getcwd(),
     title = "Ouvrez un fichier pickle",
     filetypes = (
       ("images","*.jpeg"),
       ("all files","*.*")
     )
    )
    #print(file)
    f=file.replace('\\','/')
    #print(f)
    the_path={"Path":f}
    the_l.append(the_path)
@eel.expose
def selected_apis(dict_type):
  the_l.append(dict_type)
  print(the_l)
  tb.boss_the(f'{the_l[0].get("Name")}\n{the_l[0].get("Email")}\n{the_l[0].get("Description")}',the_l[1].get("Path",'Error'))
  
  'C:/Users/grant/OneDrive/Pictures/Screenshots/Screenshot 2022-06-05 101023.png'

eel.start('index.html', size=(800, 800) )    # Start



    






