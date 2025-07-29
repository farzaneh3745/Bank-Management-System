from tkinter import Tk,Label,Entry,Button,messagebox
from tkinter.ttk import Treeview
from DataAccess.user_data_access import *
# from DataAccess.user_data_access import user_for_enter,get_account_list,disable_account,get_user_by_id,update_account,create_account,withdraw_amount,deposit_amount,show_user_list

login_form=Tk()
login_form.title("Login Form")

user_label=Label(login_form,text="Username:")
user_label.grid(row=0,column=0,padx=10,pady=10,sticky='w')

user_entry=Entry(login_form,width=30)
user_entry.grid(row=0,column=1,padx=10,pady=10,sticky='e')

pass_label=Label(login_form,text="Password:")
pass_label.grid(row=1,column=0,padx=10,pady=10,sticky='w')

pass_entry=Entry(login_form,width=30)
pass_entry.grid(row=1,column=1,padx=10,pady=10,sticky='e')

def login_button_clicked():

    entered_username=user_entry.get()
    entered_password=pass_entry.get()

    if entered_username=='admin' and entered_password=='Admin123':
        login_form.destroy()
        admin_form=Tk()
        admin_form.title("Login Form For Administrator")

        admin_form.grid_rowconfigure(0,weight=1)
        admin_form.grid_columnconfigure(0,weight=1)
        admin_form.grid_columnconfigure(1,weight=1)
        admin_form.grid_columnconfigure(2,weight=1)

        user_list_treeview=Treeview(admin_form,columns=('firstname','lastname','username','password','status'))
        user_list_treeview.grid(row=0,column=0,columnspan=3,padx=10,pady=10,sticky='ewns')

        def create_user_button_clicked():
            create_user_form=Tk()
            create_user_form.title("Create User")

            f_name=Label(create_user_form,text="Last Name:")
            f_name.grid(row=0,column=0,padx=10,pady=10,sticky='w')

            f_entry=Entry(create_user_form,width=30)
            f_entry.grid(row=0,column=1,padx=10,pady=10,sticky='e')

            l_name=Label(create_user_form,text="Last Name:")
            l_name.grid(row=1,column=0,padx=10,pady=10,sticky='w')

            l_entry=Entry(create_user_form,width=30)
            l_entry.grid(row=1,column=1,padx=10,pady=10,sticky='e')

            u_name=Label(create_user_form,text="Username:")
            u_name.grid(row=2,column=0,padx=10,pady=10,sticky='w')

            u_entry=Entry(create_user_form,width=30)
            u_entry.grid(row=2,column=1,padx=10,pady=10,sticky='e')

            p_name=Label(create_user_form,text="Password:")
            p_name.grid(row=3,column=0,padx=10,pady=10,sticky='w')

            p_entry=Entry(create_user_form,width=30)
            p_entry.grid(row=3,column=1,padx=10,pady=10,sticky='e')

            def submit_button_clicked():
                first_name=f_entry.get()
                last_name=l_entry.get()
                user_name=u_entry.get()
                pass_word=p_entry.get()

                insert_user(first_name,last_name,user_name,pass_word)

                create_user_form.destroy()
                load_user_treeview()

            submit_button=Button(create_user_form,text="Submit",command=submit_button_clicked)
            submit_button.grid(row=4,column=1,padx=10,pady=10,sticky='w')

        create_button=Button(admin_form,text="Create User",command=create_user_button_clicked)
        create_button.grid(row=1,column=0,padx=10,pady=10,sticky='ew')

        def delete_user_button_clicked():
            row_selected=int(user_list_treeview.selection()[0])
            delete_user(row_selected)

            load_user_treeview()

        delete_button=Button(admin_form,text="Delete User",command=delete_user_button_clicked)
        delete_button.grid(row=1,column=1,padx=10,pady=10,sticky='ew')

        def disable_user_button_clicked():
            row_selected = int(user_list_treeview.selection()[0])
            disabled_user(row_selected)

            load_user_treeview()

        disable_button=Button(admin_form,text="Disable User",command=disable_user_button_clicked)
        disable_button.grid(row=1,column=2,padx=10,pady=10,sticky='ew')

        user_list_treeview.heading('#0', text='Row')
        user_list_treeview.heading('firstname', text='firstname')
        user_list_treeview.heading('lastname', text='lastname')
        user_list_treeview.heading('username', text='username')
        user_list_treeview.heading('password', text='password')
        user_list_treeview.heading('status', text='status')
        user_list_treeview.column('firstname',anchor='center')
        user_list_treeview.column('lastname', anchor='center')
        user_list_treeview.column('username', anchor='center')
        user_list_treeview.column('password', anchor='center')
        user_list_treeview.column('status', anchor='center')
        user_list_treeview.column('#0', width=40)

        def load_user_treeview():
            user_list_treeview.delete(*user_list_treeview.get_children())
            row_number=1
            users_list=show_user_list()
            for user in users_list:
                user_list_treeview.insert('',"end",iid=user.id,text=row_number,
                                          values=(user.firstname,user.lastname,user.username,user.password,user.status))

                row_number+=1

        load_user_treeview()
        admin_form.mainloop()
        return

    userpass_list = user_for_enter()
    for username,password,status in userpass_list:
        if entered_username==username and entered_password==password:
            if status=="disabled":
                messagebox.showinfo("Disabled User",f"User {username} has been disabled")
                return

            bank_form=Tk()
            bank_form.title("Bank Form")

            login_form.destroy()

            bank_form.grid_columnconfigure(index=0, weight=1)
            bank_form.grid_columnconfigure(index=1, weight=1)
            bank_form.grid_columnconfigure(index=2, weight=1)
            bank_form.grid_columnconfigure(index=3, weight=1)
            bank_form.grid_columnconfigure(index=4, weight=1)
            bank_form.grid_columnconfigure(index=5, weight=1)
            bank_form.grid_rowconfigure(index=2, weight=1)

            search_label=Label(bank_form,text='Search Account')
            search_label.grid(row=0,column=0,padx=10,pady=10,sticky='ew')

            search_entry=Entry(bank_form,width=30)
            search_entry.grid(row=0,column=1,columnspan=4,padx=10,pady=10,sticky='ew')

            def search_button_clicked():
                load_treeview()

            search_button=Button(bank_form,text='Search',command=search_button_clicked)
            search_button.grid(row=0,column=5,padx=10,pady=10,sticky='ew')

            def show_create_update_form(update_id=None):
                show_form=Tk()
                show_form.title("Create Account" if not update_id else "Update Account")

                firstname_label=Label(show_form,text="First Name:")
                firstname_label.grid(row=0,column=0,padx=10,pady=10,sticky='w')

                first_name_entry=Entry(show_form,width=30)
                first_name_entry.grid(row=0,column=1,padx=10,pady=10,sticky='e')

                lastname_label=Label(show_form,text="Last Name:")
                lastname_label.grid(row=1,column=0,padx=10,pady=10,sticky='w')

                last_name_entry=Entry(show_form,width=30)
                last_name_entry.grid(row=1,column=1,padx=10,pady=10,sticky='e')

                national_code_label=Label(show_form,text="National Code:")
                national_code_label.grid(row=2,column=0,padx=10,pady=10,sticky='w')

                national_code_entry=Entry(show_form,width=30)
                national_code_entry.grid(row=2,column=1,padx=10,pady=10,sticky='e')

                account_type_label=Label(show_form,text="Account Type:")
                account_type_label.grid(row=3,column=0,padx=10,pady=10,sticky='w')

                account_type_entry=Entry(show_form,width=30)
                account_type_entry.grid(row=3,column=1,padx=10,pady=10,sticky='e')

                account_number_label=Label(show_form,text="Account Number:")
                account_number_label.grid(row=4,column=0,padx=10,pady=10,sticky='w')

                account_number_entry=Entry(show_form,width=30)
                account_number_entry.grid(row=4,column=1,padx=10,pady=10,sticky='e')

                opening_date_label=Label(show_form,text="Opening Date:")
                opening_date_label.grid(row=5,column=0,padx=10,pady=10,sticky='w')

                opening_date_entry=Entry(show_form,width=30)
                opening_date_entry.grid(row=5,column=1,padx=10,pady=10,sticky='e')

                if update_id:
                    selected_account=get_user_by_id(update_id)
                    first_name_entry.insert(0,selected_account.firstname)
                    last_name_entry.insert(0,selected_account.lastname)
                    national_code_entry.insert(0,selected_account.nationalcode)
                    national_code_entry.config(state="readonly")
                    account_type_entry.insert(0,selected_account.accounttype)
                    account_number_entry.insert(0,selected_account.accountnumber)
                    opening_date_entry.insert(0,selected_account.openingdate)

                def submit_button_clicked():
                    acc_f_name=first_name_entry.get()
                    acc_l_name=last_name_entry.get()
                    acc_national_code=national_code_entry.get()
                    acc_account_type=account_type_entry.get()
                    acc_account_number=account_number_entry.get()
                    acc_opening_date=opening_date_entry.get()

                    if update_id:
                        update_account(update_id,acc_f_name,acc_l_name,acc_account_type,acc_account_number,acc_opening_date)
                    else:
                        create_account(acc_f_name,acc_l_name,acc_national_code,acc_account_type,acc_account_number,acc_opening_date)

                    load_treeview()
                    show_form.destroy()

                submit_button = Button(show_form, text='Submit',command=submit_button_clicked)
                submit_button.grid(row=6, column=1, padx=10, pady=10, sticky='w')

                show_form.mainloop()

            create_button=Button(bank_form,text='Create Account',command=show_create_update_form)
            create_button.grid(row=1,column=1,padx=10,pady=10,sticky='ew')

            def update_button_clicked():
                row_selected=int(account_treeview.selection()[0])
                show_create_update_form(row_selected)

            update_button=Button(bank_form,text='Update Account',command=update_button_clicked)
            update_button.grid(row=1,column=2,padx=10,pady=10,sticky='ew')

            def withdraw_button_clicked():
                selected_account=int(account_treeview.selection()[0])
                account=get_user_by_id(selected_account)
                account_status=account.status
                if account_status=='disabled':
                    messagebox.showerror('Error','Account is disabled')
                else:
                    withdraw_form=Tk()
                    withdraw_form.title("Withdraw")

                    withdraw_amount_label=Label(withdraw_form,text="Withdraw Amount:")
                    withdraw_amount_label.grid(row=0,column=0,padx=10,pady=10,sticky='w')

                    withdraw_entry=Entry(withdraw_form,width=30)
                    withdraw_entry.grid(row=0,column=1,padx=10,pady=10,sticky='e')

                    def withdraw_submit_button_clicked():
                        amount=withdraw_entry.get()
                        withdraw_amount(selected_account,amount)

                        load_treeview()
                        withdraw_form.destroy()

                    submit_button=Button(withdraw_form,text='Submit',command=withdraw_submit_button_clicked)
                    submit_button.grid(row=2,column=1,padx=10,pady=10,sticky='w')

                    withdraw_form.mainloop()

            withdraw_button=Button(bank_form,text='Withdraw',command=withdraw_button_clicked)
            withdraw_button.grid(row=1,column=3,padx=10,pady=10,sticky='ew')

            def deposit_button_clicked():
                selected_account=int(account_treeview.selection()[0])
                account=get_user_by_id(selected_account)
                account_status=account.status
                if account_status=='disabled':
                    messagebox.showerror('Error','Account is disabled')
                else:
                    deposit_form=Tk()
                    deposit_form.title("Deposit")

                    deposit_amount_label=Label(deposit_form,text="Deposit Amount:")
                    deposit_amount_label.grid(row=0,column=0,padx=10,pady=10,sticky='w')

                    deposit_entry=Entry(deposit_form,width=30)
                    deposit_entry.grid(row=0,column=1,padx=10,pady=10,sticky='e')

                    def deposit_submit_button_clicked():
                        amount=deposit_entry.get()
                        deposit_amount(selected_account,amount)

                        load_treeview()
                        deposit_form.destroy()

                    submit_button=Button(deposit_form,text='Submit',command=deposit_submit_button_clicked)
                    submit_button.grid(row=2,column=1,padx=10,pady=10,sticky='w')

                    deposit_form.mainloop()

            deposit_button = Button(bank_form, text='Deposit',command=deposit_button_clicked)
            deposit_button.grid(row=1, column=4, padx=10, pady=10, sticky='ew')

            def disable_button_click():
                row_selected=int(account_treeview.selection()[0])
                disable_account(row_selected)
                load_treeview()

            disable_button=Button(bank_form,text='Disable Account',command=disable_button_click)
            disable_button.grid(row=1,column=5,padx=10,pady=10,sticky='ew')

            account_treeview=Treeview(bank_form,columns=('firstname','lastname','nationalCode','accountType','AccountNumber','OpeningDate','accountStatus','balance'))
            account_treeview.grid(row=2,column=1,columnspan=5,padx=10,pady=10,sticky='ewns')

            account_treeview.heading('#0',text='Row')
            account_treeview.heading('firstname',text='firstname')
            account_treeview.heading('lastname',text='lastname')
            account_treeview.heading('nationalCode',text='nationalCode')
            account_treeview.heading('accountType',text='accountType')
            account_treeview.heading('AccountNumber',text='AccountNumber')
            account_treeview.heading('OpeningDate',text='OpeningDate')
            account_treeview.heading('accountStatus',text='accountStatus')
            account_treeview.heading('balance',text='balance')
            account_treeview.column('#0',width=36)
            account_treeview.column('accountType',width=90)
            account_treeview.column('OpeningDate',width=85)
            account_treeview.column('nationalCode',width=95)
            account_treeview.column('firstname',anchor='center')
            account_treeview.column('lastname',anchor='center')
            account_treeview.column('nationalCode',anchor='center')
            account_treeview.column('accountType',anchor='center')
            account_treeview.column('AccountNumber',anchor='center')
            account_treeview.column('OpeningDate',anchor='center')
            account_treeview.column('accountStatus',anchor='center')
            account_treeview.column('balance',anchor='center')

            def load_treeview():
                term = search_entry.get()
                row_number = 1
                account_treeview.delete(*account_treeview.get_children())
                if term:
                    accounts=get_account_list(term)
                else:
                    accounts=get_account_list()

                for account in accounts:
                    account_treeview.insert("",'end',
                                            iid=account.id,
                                            text=row_number,
                                            values=(account.firstname,account.lastname,account.nationalcode,account.accounttype,account.accountnumber,account.openingdate,account.status,account.balance))
                    row_number+=1

            load_treeview()
            bank_form.mainloop()
            return

    messagebox.showinfo("Login Failed", "Username or password is incorrect.")

entrance_button=Button(login_form,text="Login",command=login_button_clicked)
entrance_button.grid(row=2,column=1,padx=10,pady=10,sticky='w')

login_form.mainloop()