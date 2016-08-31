def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    users_username = input("what is your username? \n >>> ")
    if users_username not in usernames:
        print("Access denied")
    else:
        print("Access granted")

main()