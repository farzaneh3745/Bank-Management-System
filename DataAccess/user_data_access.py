import sqlite3
from Entities.account import Account
from Entities.user import User

def user_for_enter():
    username_list=[]
    with sqlite3.connect('BankManagement.db') as connection:
        cursor=connection.cursor()
        cursor.execute(""" SELECT username,password,status FROM User;  """)
        username_list=cursor.fetchall()
    return username_list

def get_account_list(term=None):
    data_list = []
    with sqlite3.connect('BankManagement.db') as connection:
        cursor=connection.cursor()
        if not term:
         cursor.execute(""" SELECT id,firstname,lastname,nationalcode,account_type,account_number,opening_date,disabled,balance FROM Accounts;""")
        else:
            cursor.execute(f"""SELECT 
                id,firstname,lastname,nationalcode,account_type,account_number,opening_date,disabled,balance
            FROM Accounts  WHERE nationalcode LIKE'%{term}%' OR account_number LIKE'%{term}%';""")
        account_list=cursor.fetchall()
        for row in account_list:
            accounts=Account(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
            data_list.append(accounts)
    return data_list

def disable_account(id):
    with sqlite3.connect('BankManagement.db') as connection:
        cursor=connection.cursor()
        cursor.execute(f"""UPDATE Accounts SET disabled = 'disabled' WHERE id = {id};""")
        connection.commit()

def get_user_by_id(user_id):
    with sqlite3.connect('BankManagement.db') as connection:
        cursor=connection.cursor()
        cursor.execute(f"""
        SELECT id,firstname,lastname,nationalcode,account_type,account_number,opening_date,disabled,balance FROM Accounts WHERE id={user_id};        
        """)
        row=cursor.fetchone()
        selected_account=Account(*row)
    return selected_account

def update_account(account_id,new_firstname,new_lastname,new_account_type,new_account_number,new_opening_date):
    with sqlite3.connect('BankManagement.db') as connection:
        cursor=connection.cursor()
        cursor.execute(f""" UPDATE Accounts SET firstname = '{new_firstname}',lastname = '{new_lastname}',
        account_type = '{new_account_type}',account_number = '{new_account_number}',opening_date = '{new_opening_date}' 
        WHERE id = {account_id} """)
        connection.commit()

def create_account(firstname,lastname,national_code,account_type,account_number,opening_date):
    with sqlite3.connect('BankManagement.db') as connection:
        cursor=connection.cursor()
        cursor.execute(f"""INSERT INTO Accounts (firstname,lastname,nationalcode,account_type,account_number,opening_date,disabled)
        VALUES ('{firstname}','{lastname}','{national_code}','{account_type}','{account_number}','{opening_date}','enable' );""")
        connection.commit()

def withdraw_amount(account_id,amount):
    with sqlite3.connect('BankManagement.db') as connection:
        cursor=connection.cursor()
        cursor.execute(f"""UPDATE Accounts SET balance = balance - {amount} WHERE id = {account_id} AND balance >= {amount};""")
        connection.commit()

def deposit_amount(account_id,amount):
    with sqlite3.connect('BankManagement.db') as connection:
        cursor=connection.cursor()
        cursor.execute(f"""UPDATE Accounts SET balance = balance + {amount} WHERE id = {account_id};""")
        connection.commit()

def show_user_list():
    users_list=[]
    with sqlite3.connect('BankManagement.db') as connection:
        cursor=connection.cursor()
        cursor.execute(f"""SELECT * FROM User;""")
        user_list=cursor.fetchall()
        for row in user_list:
            user=User(row[0],row[1],row[2],row[3],row[4],row[5])
            users_list.append(user)
    return users_list

def insert_user(firstname,lastname,username,password):
    with sqlite3.connect('BankManagement.db') as connection:
        cursor=connection.cursor()
        cursor.execute(f"""INSERT INTO User (firstname,lastname,username,password,status)
                 VALUES ('{firstname}','{lastname}','{username}','{password}','enable');""")
        connection.commit()

def delete_user(deleted_id):
    with sqlite3.connect('BankManagement.db') as connection:
        cursor=connection.cursor()
        cursor.execute(f"""DELETE FROM User WHERE id = {deleted_id};""")

        connection.commit()

def disabled_user(disabled_id):
    with sqlite3.connect('BankManagement.db') as connection:
        cursor=connection.cursor()
        cursor.execute(f"""UPDATE User SET status = 'disabled' WHERE id = '{disabled_id}' """)
        connection.commit()