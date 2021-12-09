import  tkinter as tk
from tkinter import ttk
from tkinter.constants import END
from typing_extensions import IntVar


################crate window#####################
window = tk.Tk()
window.geometry('500x350')
window.title('Registr')
        
###############get user and add to file(regester.text)#######################
def get_values():
    #lbl_name.getvar(1,END)
    with open('Registrs.txt','a') as f:
        f.write(f'\nName: {name_entry.get()}\nFamilename: {familename_entry.get()}\
                \nGender: {gender_entry.get()}\nE-Mail: {email_entry.get()}\
                \nPhone: {phone_entry.get()}\n')

##########################delete all data in the frame (new butten)#####################
def dell_forms():
    name_entry.delete(0,END)
    familename_entry.delete(0,END)
    gender_entry.delete(0,END)
    email_entry.delete(0,END)
    phone_entry.delete(0,END)


##################### Label fur Help ##################
label_rigester = tk.Label(master=window,text='Registr',font=('Arial bold',20))
label_rigester.grid(row=0,column=4,pady=15)

lbl_name =tk.Label(master=window,text='Name: ',font=('Arial bold',9))
lbl_familename =tk.Label(master=window,text='Familename: ',font=('Arial bold',9))
lbl_gender =tk.Label(master=window,text='Gender: ',font=('Arial bold',9))
lbl_email =tk.Label(master=window,text='E-Mail: ',font=('Arial bold',9))
lbl_phone=tk.Label(master=window,text='Phone: ',font=('Arial bold',9))

lbl_name.grid(row=1, column=3,padx=10)
lbl_familename.grid(row=2, column=3,padx=10)
lbl_gender.grid(row=3, column=3,padx=10)
lbl_email.grid(row=4, column=3,padx=10)
lbl_phone.grid(row=5, column=3,padx=10)

################# String##########################
name_value =tk.StringVar
familename_value =tk.StringVar
gender_value =tk.StringVar
email_value =tk.StringVar
phone_value =tk.StringVar
#check_value = IntVar

############### your can input data###############
name_entry = ttk.Entry(master=window,textvariable=name_value,width=35)
familename_entry = ttk.Entry(master=window,textvariable=familename_value,width=35)
gender_entry = ttk.Entry(master=window,textvariable=gender_value,width=35)
email_entry = ttk.Entry(master=window,textvariable=email_value,width=35)
phone_entry = ttk.Entry(master=window,textvariable=phone_value,width=35)

name_entry.grid(row=1,column=4)
familename_entry.grid(row=2,column=4)
gender_entry.grid(row=3,column=4)
email_entry.grid(row=4,column=4)
phone_entry.grid(row=5,column=4)

# check_btn = tk.Checkbutton(text='remember me!',variable=check_value)
# check_btn.grid(row=6,column=4)
######################Button submit (save data)#####################
submit_btn = ttk.Button(master=window,text='Submit',command=get_values)
submit_btn.grid(row=6,column=4,padx=25,pady=12)

######################Button delete ###########################
new_btn = ttk.Button(master=window,text='New',command=dell_forms)
new_btn.grid(row=8,column=4,padx=20,pady=5)

# new_btn = tk.Button(master=window,text='Delete All Form',height=2,width=14,command=dell_forms)
# new_btn.grid(row=2,column=5)


window.mainloop()