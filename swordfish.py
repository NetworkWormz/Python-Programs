while True :
    print ('Who are you ? ')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    passowrd = input ()
    if passowrd == 'swordfish':
        break
print ('Access Granted. ')
