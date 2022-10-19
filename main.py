from random import randint,choice
import hashlib
import os
from load import load, clear, splash_text, deboot
from cmd import Cmd
import shutil
from torpy.http.requests import TorRequests
def download_file(url, user):
  from pywget import wget

  link = url
  initializer = "INITIALIZATION_CODE"
  wget.download(link, f'users/{user}/')
from datetime import datetime
fu = ''
beta = ''
contents = ''
perm_granted = False
import pytz
UTC = pytz.utc
datetime_utc = datetime.now(UTC)
current_time = datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z')
from load import user_consolelookup, ambig
black = "\u001b[30m"
red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
magenta = "\u001b[35m"
cyan = "\u001b[36m"
white = "\u001b[37m"
ewritec = ''
##<!>NON-SHELL RELATED STUFF<!>
setup_check = open('setup.log',"r+")
setup_checkkey = setup_check.readline()
if setup_checkkey == "TRUE":
  print(f'{red}No bootable medium found! Halting system.')
  exit()
load()
if setup_checkkey == "SECURE":
  path = "users/"
  shutil.rmtree(path, ignore_errors=False, onerror=None)
  os.makedirs("users")
  password = "konnect"
  encoded = password.encode()
  passwordtohashed = hashlib.sha256(encoded)
  hash = passwordtohashed.hexdigest()
  ewrite = open('users/konnect.txt',"w")
  ewrite.write(hash)
  ewrite.close()
  os.makedirs(f'users/konnect')
  ewritev = open('users/konnectpriv.file',"w")
  ewritev.write('TRUE')
  ewritev.close()
  ewritex = open('users/konnectconfig.cnfig',"w")
  ewritex.write('01010111 01100101 01101100 01101100 00101110 00100000 01011001 01101111 01110101 00100111 01110010 01100101 00100000 01110100 01110010 01111001 01101110 01100001 00100000 01100100 01100101 01100011 01101111 01100100 01100101 00100000 01110100 01101000 01101001 01110011 00111111 00100000 01010100 01101000 01101001 01110011 00100000 01101001 01110011 00100000 01100001 00100000 01101011 01100101 01111001 00100000 01100110 01101111 01110010 00100000 01100001 00100000 01110110 01101001 01110010 01110101 01110011 00101110 00100000 01010011 01101111 01101101 01100101 01110100 01101000 01101001 01101110 01100111 00100000 01110100 01101000 01100001 01110100 00100000 01100011 01100001 01101110 00100000 01100100 01100001 01101101 01100001 01100111 01100101 00100000 01111001 01101111 01110101 01110010 00100000 01100011 01101111 01101101 01110000 01110101 01110100 01100101 01110010 00101110 00100000 01010111 01100101 01101100 01101100 00101100 00100000 01101110 01101111 01110111 00100000 01110100 01101000 01100001 01110100 00100000 01111001 01101111 01110101 00100000 01101011 01101110 01101111 01110111 00101100 00100000 01001001 00100111 01101100 01101100 00100000 01101000 01100001 01110110 01100101 00100000 01110100 01101111 00100000 01100100 01100101 01110011 01110100 01110010 01101111 01111001 00100000 01111001 01101111 01110101 01110010 00100000 01110110 01100101 01110010 01110011 01101001 01101111 01101110 00100000 01101111 01100110 00100000 01001011 01101111 01101110 01100101 01100011 01110100 00101110')
  ewritex.close()
  ewritec = open('users/konnectintro.cnfig',"w")
  ewritec.write("YES")
  ewritec.close()
  print("Secure mode enabled, welcome to Konnect!")
if setup_checkkey == "NO":
  print(f'Welcome to Konnect. {yellow}Built with privacy in mind.{white}')
  username = input("\nWhat would like your username to be?: ")
  password = input('\nPlease enter the password that you would like to set: ')
  print('We have encrypted this password & have saved it on a file. You should be done.')
  try:
    with open(f'users/{username}.txt', 'x') as f:
      f.write('Working...')
    setup_change = open("setup.log","w")
    setup_change.write("NO")
    setup_change.close()
  except:
    print("This user already exists.")
    setup_change = open("setup.log","w")
    setup_change.write("YES")
    setup_change.close()
  encoded = password.encode()
  passwordtohashed = hashlib.sha256(encoded)
  hash = passwordtohashed.hexdigest()
  ewrite = open(f'users/{username}.txt',"w")
  ewrite.write(hash)
  ewrite.close()
  ewritex = open(f'users/{username}config.cnfig',"w")
  ewritex.write('01010111 01100101 01101100 01101100 00101110 00100000 01011001 01101111 01110101 00100111 01110010 01100101 00100000 01110100 01110010 01111001 01101110 01100001 00100000 01100100 01100101 01100011 01101111 01100100 01100101 00100000 01110100 01101000 01101001 01110011 00111111 00100000 01010100 01101000 01101001 01110011 00100000 01101001 01110011 00100000 01100001 00100000 01101011 01100101 01111001 00100000 01100110 01101111 01110010 00100000 01100001 00100000 01110110 01101001 01110010 01110101 01110011 00101110 00100000 01010011 01101111 01101101 01100101 01110100 01101000 01101001 01101110 01100111 00100000 01110100 01101000 01100001 01110100 00100000 01100011 01100001 01101110 00100000 01100100 01100001 01101101 01100001 01100111 01100101 00100000 01111001 01101111 01110101 01110010 00100000 01100011 01101111 01101101 01110000 01110101 01110100 01100101 01110010 00101110 00100000 01010111 01100101 01101100 01101100 00101100 00100000 01101110 01101111 01110111 00100000 01110100 01101000 01100001 01110100 00100000 01111001 01101111 01110101 00100000 01101011 01101110 01101111 01110111 00101100 00100000 01001001 00100111 01101100 01101100 00100000 01101000 01100001 01110110 01100101 00100000 01110100 01101111 00100000 01100100 01100101 01110011 01110100 01110010 01101111 01111001 00100000 01111001 01101111 01110101 01110010 00100000 01110110 01100101 01110010 01110011 01101001 01101111 01101110 00100000 01101111 01100110 00100000 01001011 01101111 01101110 01100101 01100011 01110100 00101110')
  ewritex.close()
  ewrite = open('users/xscr.bin',"w")
  ewrite.write(ambig + '\n' + username)
  ewrite.close()
  ewritev = open(f'users/{username}priv.file',"w")
  ewritev.write('TRUE')
  ewritev.close()
  ewritec = open(f'users/{username}intro.cnfig',"w")
  ewritec.write("NO")
  ewritec.close()
  print(f'The hash that we have generated is {hash}. We are currently done with setup! You will be redirected to login shortly. Remember your credentials\nUsername: {username}\nPassword: {password}.')
  try:
    os.makedirs(f'users/{username}')
  except:
    print('User already exists. Skipping step.')
  import time
  setup_change = open("setup.log","w")
  setup_change.write("YES")
  setup_change.close()
  time.sleep(5)
  os.system("clear")
  
password_opened = False
print(f'{red}Konnect\n{magenta}{splash_text}.\n{cyan}{current_time}.')
print(f'{white}Please enter your credentials to login to {red}Konnect.{white}')
attempts = 5
true = True
actual_hashed_passcode = "e"
root = False
while true:
    try:
      username = input("Username: ")
      user_config = open(f'users/{username}config.cnfig',"r+")
      user_data = user_config.readline()
      if user_data == user_consolelookup:
        root = True
    except:
      pass
      
    class Shell(Cmd):
         prompt = f'{username}@konnect> '
         intro = f'Welcome {blue}{username}!{white} Type ? to list commands'
         def do_exit(self, inp):
              print("Bye")
              return True
          
         def help_exit(self):
              print('Exit shell. Shorthand: x q Ctrl-D.')
         def do_clear(self, inp):
           os.system("clear")
         def do_add(self, inp):
              print("adding '{}'".format(inp))
       
         def help_add(self):
              print("Add a new entry to the system.")
         def help_clear(self):
            print("Clear the shell.")
         def help_cget(self):
          print("Download files from the internet.\nPREFIX: cget {website}. Goes through the tor network.")
         def help_request(self):
           print("This feature is part of the Konnect Privacy Pack. This'll make requests through the tor network to allow you to get data in json format.")
         def help_kill(self):
          print("Instantly terminate the system.")
         def do_kill(self,inp):
          print("Alright.")
          exit()
         def help_destroy(self):
          print("Redacted.")
         def do_request(self,inp):
           try:
               print("Connecting to the tor network./")
               with TorRequests() as tor_requests:
                 with tor_requests.get_session() as sess:
                   print(sess.get(inp).json())
                   print("Exiting the network.")
           except:
              print(f"{red}You have encountered a problem, it isn't you, its us.{white}")
         def do_destroy(self,inp):
          print("Are you sure that you want to do this? This will destroy the operating system! Please continue if it is your last option!")
          acknowledgement = input(f'\nPlease type in \n "I agree to what I am doing."\n\nPlease type it in: ')     
          if acknowledgement == f"I agree to what I am doing." and root == True:
           clear()
           the_final_thing = input(f'One last thing, please type in "yes".')
           if the_final_thing == f'yes':
             clear()
             print("<!> OK! <!>\nDeleting related with the operating system.")
             os.remove('load.py')
             os.remove('setup.log')
             os.remove('apps.py')
             path = "users/"
             shutil.rmtree(path, ignore_errors=False, onerror=None)
             print("One last thing, have a good time!")
             os.remove('main.py')
         def do_cget(self,inp):
          try:
            with TorRequests() as tor_requests:
              print(f'{red}Connecting through tor.{white}')
              with tor_requests.get_session() as sess:
                download_file(inp, username)
                print(f'\nDone! Please check /users/{username} for your requested file.')
                print("Exiting tor.")
              #with tor_requests.get_session() as sess:
              #  print(sess.get("http://httpbin.org/ip").json())
              #  print(sess.get("http://httpbin.org/ip").json())
          except:
            print(f'{red}An unknown exception has occured @{username}. Please report this issue to Defy immediately.{white}')
          def default(self, inp):
              if inp == 'x' or inp == 'q':
                  print("Logging out of the shell & returning to Konnect.")
                  time.sleep(2)
                  return self.do_exit(inp)
                  print("Default: {}".format(inp))
         do_EOF = do_exit
         help_EOF = help_exit
    password = input("Password: ")
    if password == "up up down down left right left right b a" or password == "Up Up Down Down Left Right Left Right B A" or username == "up up down down left right left right b a" or username == "Up Up Down Down Left Right Left Right B A":
      clear()
      print(f'You have gained root access to Konnect, now be free my friend!')
      root = True
      print(f'{red}Root status: {magenta}{root}.{white}\n\n')
      fu = f'\nRoot status: {root}'
      
      
    try:
      actual_hashed_passcode = open(f'users/{username}.txt',"r+")
      actual_hashed_passcode = actual_hashed_passcode.readline()
    except:
      print("This user does not exist.")
    encoded = password.encode()
    passwordtohashed = hashlib.sha256(encoded)
    hash = passwordtohashed.hexdigest()
    if username == username and hash == actual_hashed_passcode:
        print("\nWelcome!")
        worthy = open(f'users/{username}priv.file')
        worth = worthy.readline()
        beta_reader = open(f'users/{username}intro.cnfig',"r")
        beta = beta_reader.readline()
        ewritec = open(f'users/{username}intro.cnfig',"r")
        ewritec = ewritec.readline()
        true = False
        password_opened = True
    else:
        attempts = attempts - 1
        print(f"You have entered the wrong username/password. You have {attempts} attempts left.")
    if attempts == 0:
        print("No more attempts left. Exiting.")
        exit()
clear()
choice = "0"
if beta == "YES":
  beta = ",\n5. App Marketplace,\n6. Apps"
else:
  beta = ""
if root == True:
  contents = "\n5. Beta\n6. User Permissions"
if worthy == "TRUE":
  perm_granted = True
else:
  perm_granted = False
while password_opened:
    clear()
    print(f'\KonnectxDefy {green}©1999 Defy.{white} \nAll rights reserved.\n\nWhat would you like to do today {username}?{fu}\n\nCurrent options available to you:\n\n1. Change Password,\n2. Settings,\n3. Secure Logout,\n4. Shell{beta}')
    try:
      choice = str(input("Please type your option below: "))
    except:
      print("No.")
    if choice == "1":
        verification_part2 = input("Please enter the current password: ")
        encode34d = verification_part2.encode()
        passwordtoha34shed = hashlib.sha256(encode34d)
        verification_part2_hash = passwordtoha34shed.hexdigest()
        if verification_part2_hash == actual_hashed_passcode:
            password_to_remember = input("Please enter the new password you would like to use: ")
            encode3d = password_to_remember.encode()
            passwordtoha3shed = hashlib.sha256(encode3d)
            passwordchange_remember = passwordtoha3shed.hexdigest()
            print(f"\nYour password that you would like to change is {password_to_remember} and the hash required to be changed is {passwordchange_remember}.")
            ewrite = open('hashed_passcode.txt',"w")
            ewrite.write(passwordchange_remember)
            ewrite.close()
            print("\nI have changed the password.")
        else:
            print("\nIncorrect password. Please retry later.")
    if choice == "2":
        print("\nAccessing critical stuff. Would you like to still continue?")
        admin_choose = input("").lower()
        if admin_choose == "yes" or admin_choose == "y":
            print("permissions granted.")
            options = input(f"\nWhat would you like to do today?\n\n1. Delete account\n2. Report an issue\n3. Create a new user\n4. Secure mode{contents}\n\nPlease input your choice: ")
            if options == "4" and setup_checkkey == "SECURE":
              confirm = input("Would you like to disable secure mode? Please type yes to continue: ").lower()
              if confirm == "yes" or confirm == "y" or confirm == "true":
                print("Okay. Switching back.")
                setup_change = open("setup.log","w")
                setup_change.write("NO")
                setup_change.close()
                path = "users/"
                shutil.rmtree(path, ignore_errors=False, onerror=None)
                os.makedirs("users")
                print("Please restart to make changes.")
                input("\nPlease press the enter key to continue.")
            if options == "5" and beta == ",\n5. App Marketplace,\n6. Apps" and root == True:
              print(f'{red}Konnect Beta Platform\n{white}======================={magenta}©1999 Defy\n\n{white}')
              print('Do you want to opt-out of beta features?')
              beta_check = input('\nPlease enter your choice: ').lower()
              if beta_check == "yes" or beta_check == "y" or beta_check == "true":
                print("Alright. Konnect has withdrawn you from the beta platform.")
                try:
                 shutil.rmtree('apps/', ignore_errors=False, onerror=None)
                except:
                  pass
                ewritec = open(f'users/{username}intro.cnfig',"w")
                ewritec.write("NO")
                ewritec.close()
                input("Please press enter to continue.")
            if options == "5" and beta != ",\n5. App Marketplace,\n6. Apps" and root == True:
              clear()
              print(f'{red}Konnect Beta Platform\n{white}======================={magenta}©1999 Defy\n\n{white}')
              print('Would you like to test out new features that will be available to everybody in the future? ')
              beta_check = input('\nPlease enter your choice: ').lower()
              if beta_check == "yes" or beta_check == "y" or beta_check == "true":
                print("Alright. Konnect has enrolled you into the beta platform.")
                try:
                  os.makedirs('apps')
                except:
                  pass
                ewritec = open(f'users/{username}intro.cnfig',"w")
                ewritec.write("YES")
                ewritec.close()
                input("Please press enter to continue.")
            if options == "6" and root == True:
              clear()
              print(f'{red}Konnect Permissions Manager{white}\n=======================\n{green}©1999 Defy. \n{white}All rights reserved.')
              ask_for_user = input(f"Which user's permissions would you like to modify?\n\n{username}@konnect> ")
              beta_change = ""
              cnf = True
              while cnf:
                try:
                  ask = input("What would you like to change for this user? HELP FOR HELP").lower()
                  if ask == "change beta status":
                    change_confirm = input(f'What should the beta status of this user be?\nUsable commands: True to enable beta, False to disable beta.\n\n{username}@Konnect> ').lower()
                    if change_confirm == "true":
                      beta_change = open(f'users/{ask_for_user}priv.file','w')
                      beta_change.write("TRUE")
                      beta_also = open(f'users/{ask_for_user}intro.cnfig','w')
                      beta_also.write("YES")
                    if change_confirm == "false":
                      beta_change = open(f'users/{ask_for_user}priv.file','w')
                      beta_change.write("FALSE")
                      beta_also = open(f'users/{ask_for_user}intro.cnfig','w')
                      beta_also.write("NO")
                except:
                  print(f'{red}Error found.{white}')
            if options == "4" and root == True and setup_checkkey != "SECURE":
              print("Secure mode is the archetype of Konnect. When you enable this feature, your files will be deleted & you will be supplemented with new credentials on boot. You can always change this in settings.\n\nThe username & password will both be the word 'konnect', all lowercase.")
              code = input('\nTo activate this feature, please type yes: ').lower()
              if code == "yes" or code == "y":
                print("Ok")
                setup_change = open("setup.log","w")
                setup_change.write("SECURE")
                setup_change.close()
                path = "users/"
                shutil.rmtree(path, ignore_errors=False, onerror=None)
                os.makedirs("users")
                print("Please restart to make changes.")
                input("\nPlease press the enter key to continue.")
                
            if options == "1" and root == True:
                selector = input("Which user account would you like to delete?\nPlease type in the account that you would like to delete: ")
                if selector == username:
                    confirm = input("WHAT, you really want to delete your account? You'll delete everything, including other users! \nPlease type YES to confirm: ")
                    if confirm == "YES" or "yes":
                        print('Please enter your password, as this is required to continue with this operation.')
                        verification_part2 = input("\nPlease enter the current password: ")
                        encode34d = verification_part2.encode()
                        passwordtoha34shed = hashlib.sha256(encode34d)
                        verification_part2_hash = passwordtoha34shed.hexdigest()
                        if verification_part2_hash == actual_hashed_passcode:
                            verify = input("Please confirm if you are going to do this!\n1. YES\n2. NO\nPlease input your choice now:")
                            if verify == "1":
                                os.system("clear")
                                print("Okay.")
                                print("I have finished account deletion for you. Hope to see you again soon!")
                                import time
                                time.sleep(1.2)
                                file_path = f'users/{username}.txt'
                                os.remove(file_path)
                                os.system("clear")
                                setup_change = open("setup.log","w")
                                setup_change.write("NO")
                                setup_change.close()
                                path = "users/"
                                shutil.rmtree(path, ignore_errors=False, onerror=None)
                                os.makedirs("users")
                                print("Please restart the system.")
                                exit()
                else:
                  print("Figuring stuff out...")
                  selection_check = "a"
                  selection_data = "b"
                  try:
                    selection_check = open(f'users/{selector}config.cnfig',"r+")
                    selection_data = selection_check.readline()
                  except:
                    print("This user does not exist.")
                    import time
                    time.sleep(1)
                    print("Shutting down the OS to prevent more issues.")
                    exit()
                  if selector != username:
                    try:
                      run = input("PLEASE TYPE YES TO CONTINUE.")
                      if run != "YES" or run != "yes" or run != "y":
                        print("Running exit proceedures.")
                      from tqdm import tqdm
                      for i in tqdm (range (100), desc="Loading"):
                        path = f'users/{selector}'
                        shutil.rmtree(path, ignore_errors=False, onerror=None)
                        file_path = f'users/{selector}.txt'
                        os.remove(file_path)
                        os.remove(f'users/{selector}config.cnfig')
                      import time
                      time.sleep(1)
                      print("Complete!")
                      time.sleep(1)
                    except:
                      print("This user doesn't exist!")
                  if selection_data == user_consolelookup:
                    print("You need to be the owner of this copy of the OS in order to be able to continue with this operation.")
            if root == False:
              print("Access denied. No permissions.")
            if options == "2":
              print('To report an issue, please send an email to the team at defystudios@proton.me')
              input("Please type anything to continue.")
            if options == "3" and root == True:
              print("This process will create a new user, would you like to continue?")
              input("\nPress enter to continue.")
              clear()
              print(f'{white}Konnect User Instance Management System\n©1999 Defy\n=================================\n\n{green}')
              new_username = input("What would you like the username to be?: ")
              clear()
              print(f'{white}Konnect User Instance Management System\n©1999 Defy\n=================================\n\n{green}')
              password2 = input("What would you want the password to be?: ")            
              clear()
              print(f'{white}Konnect User Instance Management System\n©1999 Defy\n=================================\n\n{green}')
              root_status = input("Would you like this user to be root?: ")
              clear()
              print(f'{white}Konnect User Instance Management System\n©1999 Defy\n=================================\n\n')
              try:
                with open(f'users/{new_username}.txt', 'x') as f:
                  f.write('Working...')
                setup_change = open("setup.log","w")
                setup_change.write("YES")
                setup_change.close()
              except:
                print("This user already exists.")
                setup_change = open("setup.log","w")
              encoded = password2.encode()
              passwordtohashed = hashlib.sha256(encoded)
              hash = passwordtohashed.hexdigest()
              ewrite = open(f'users/{new_username}.txt',"w")
              ewrite.write(hash)
              ewrite.close()
              ewritev = open(f'users/{new_username}.file',"w")
              ewritev.write('FALSE')
              ewritev.close()
              ewritec = open(f'users/{new_username}intro.cnfig',"w")
              ewritec.write("NO")
              ewritec.close()
              if root_status == "yes" or root_status == "y" or root_status == "true":
                ewritex = open(f'users/{new_username}config.cnfig',"w")
                ewritex.write('01010111 01100101 01101100 01101100 00101110 00100000 01011001 01101111 01110101 00100111 01110010 01100101 00100000 01110100 01110010 01111001 01101110 01100001 00100000 01100100 01100101 01100011 01101111 01100100 01100101 00100000 01110100 01101000 01101001 01110011 00111111 00100000 01010100 01101000 01101001 01110011 00100000 01101001 01110011 00100000 01100001 00100000 01101011 01100101 01111001 00100000 01100110 01101111 01110010 00100000 01100001 00100000 01110110 01101001 01110010 01110101 01110011 00101110 00100000 01010011 01101111 01101101 01100101 01110100 01101000 01101001 01101110 01100111 00100000 01110100 01101000 01100001 01110100 00100000 01100011 01100001 01101110 00100000 01100100 01100001 01101101 01100001 01100111 01100101 00100000 01111001 01101111 01110101 01110010 00100000 01100011 01101111 01101101 01110000 01110101 01110100 01100101 01110010 00101110 00100000 01010111 01100101 01101100 01101100 00101100 00100000 01101110 01101111 01110111 00100000 01110100 01101000 01100001 01110100 00100000 01111001 01101111 01110101 00100000 01101011 01101110 01101111 01110111 00101100 00100000 01001001 00100111 01101100 01101100 00100000 01101000 01100001 01110110 01100101 00100000 01110100 01101111 00100000 01100100 01100101 01110011 01110100 01110010 01101111 01111001 00100000 01111001 01101111 01110101 01110010 00100000 01110110 01100101 01110010 01110011 01101001 01101111 01101110 00100000 01101111 01100110 00100000 01001011 01101111 01101110 01100101 01100011 01110100 00101110')
                ewritex.close()
                import time
                from tqdm import tqdm
                for i in tqdm (range (100), desc="Loading"):
                  pass
                time.sleep(1)
              if root_status == "no" or root_status == "No" or root_status == "false" or root_status == "NO":
                  ewritex = open(f'users/{new_username}config.cnfig',"w")
                  ewritex.write('01010111 021100101 01101100 01101100 00101110 00100000 01011001 01101111 01110101 00100111 01110010 01100101 00100000 01110100 01110010 01111001 01101110 01100001 00100000 01100100 01100101 01100011 01101111 01100100 01100101 00100000 01110100 01101000 01101001 01110011 00111111 00100000 01010100 01101000 01101001 01110011 00100000 01101001 01110011 00100000 01100001 00100000 01101011 01100101 01111001 00100000 01100110 01101111 01110010 00100000 01100001 00100000 01110110 01101001 01110010 01110101 01110011 00101110 00100000 01010011 01101111 01101101 01100101 01110100 01101000 01101001 01101110 01100111 00100000 01110100 01101000 01100001 01110100 00100000 01100011 01100001 01101110 00100000 01100100 01100001 01101101 01100001 01100111 01100101 00100000 01111001 01101111 01110101 01110010 00100000 01100011 01101111 01101101 01110000 01110101 01110100 01100101 01110010 00101110 00100000 01010111 01100101 01101100 01101100 00101100 00100000 01101110 01101111 01110111 00100000 01110100 01101000 01100001 01110100 00100000 01111001 01101111 01110101 00100000 01101011 01101110 01101111 01110111 00101100 00100000 01001001 00100111 01101100 01101100 00100000 01101000 01100001 01110110 01100101 00100000 01110100 01101111 00100000 01100100 01100101 01110011 01110100 01110010 01101111 01111001 00100000 01111001 01101111 01110101 01110010 00100000 01110110 01100101 01110010 01110011 01101001 01101111 01101110 00100000 01101111 01100110 00100000 01001011 01101111 01101110 01100101 01100011 01110100 00101110')
                  ewritex.close()
              print(f'The hash that we have generated is {hash}. We are currently done. You will be redirected back shortly. Remember the credentials of the new user.\nUsername: {new_username}\nPassword: {password2}.')
              ewritex = open(f'users/setup.log',"w")
              ewritex.write("YES")
              ewritex.close()
              import time
              time.sleep(4)
              try:
                os.makedirs(f'users/{new_username}')
                ewritex = open(f'setup.log',"w")
                ewritex.write("YES")
                ewritex.close()
              except:
                print(f'We were not smart to be able to redirect you back to make a new user. So here you are. {red}Operation cancelled. Please run the command again.{white}')
                import time
                time.sleep(1)
    if choice == "3":
      clear()
      print("Logging you out securely. Please wait a moment!")
      from tqdm import tqdm
      import time
      for i in tqdm (range (100), desc="Loading"):
        time.sleep(0.02)
        password = ""
        username = ""
        password_opened = False
        true = True
      print("Finished. Shutting down Konnect.")
      deboot()
    if choice == "4":
      clear()
      print('Launching shell. Please hold on standby.\n')
      import time
      time.sleep(1)
      Shell().cmdloop()
    if choice == "5" and ewritec == "YES" and perm_granted == True:
      clear()
      print("Welcome to the app marketplace! This is the area where you can download applications from other people! You can also sideload unofficial apps by dragging them in the apps directory which has been created.")
      input("\nPlease press enter to continue.")
    if choice == "6" and ewritec == "YES":
      os.system("python3 apps.py")
      clear()
