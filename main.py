from random import randint,choice
import hashlib
import os
from load import load, clear, splash_text
from cmd import Cmd
import shutil
def download_file(url, user):
  from pywget import wget

  link = url
  wget.download(link, f'users/{user}/')
from datetime import datetime
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
##<!>NON-SHELL RELATED STUFF<!>
setup_check = open('setup.log',"r+")
setup_checkkey = setup_check.readline()
if setup_checkkey == "TRUE":
  print(f'{red}No bootable medium found! Halting system.')
  exit()
load()
if setup_checkkey == "NO":
  print(f'Welcome to Konect. {yellow}Built with privacy in mind.{white}')
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
print(f'{red}Konect\n{magenta}{splash_text}.\n{cyan}{current_time}.')
print(f'{white}Please enter your credentials to login to {red}Konect.{white}')
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
      print("This user doesn't exist.")
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
         def help_get(self):
          print("Download stuff from the internet.")
         def help_kill(self):
          print("Instantly terminate the system.")
         def do_kill(self,inp):
          print("Alright.")
          exit()
         def help_sudo_destroy(self):
          print("Redacted.")
         def do_sudo_destroy(self,inp):
          print("Are you sure that you want to do this? This will destroy the operating system! Please continue if it is your last option!")
          acknowledgement = input(f'\nPlease type in \n "I agree to what I am doing."\n\nPlease type it in: ')     
          if acknowledgement == f"I agree to what I am doing." and root == True:
           clear()
           the_final_thing = input(f'One last thing, please type in "yes".')
           if the_final_thing == f'yes':
             clear()
             print(f"Dear {username},\n\nThis replit copy of Konnect currently doesn't allow for you to enter this command. This is because of that minority of users being the trolls that they are trying to wipe all of the hard work that I, defy, put into this. If you'd like to have your fun, please consider downloading a copy from the github repo.\n\nThanks & regards,\n./defy\nCreator of Konnect.")
             import time
             time.sleep(5)
          
         def do_get(self,inp):
          try:
            download_file(inp, username)
            print(f'\nDone! Please check /users/{username} for your requested file.')
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
        true = False
        password_opened = True
    else:
        attempts = attempts - 1
        print(f"You have entered the wrong username/password. You have {attempts} attempts left.")
    if attempts == 0:
        print("No more attempts left. Exiting.")
        exit()
os.system("clear")
choice = "0"
while password_opened:
    clear()
    print(f'\KonnectxDefy {green}©1999 Defy.{white} \nAll rights reserved.\n\nWhat would you like to do today {username}?\n\nCurrent options available to you:\n\n1. Change Password, 2. Account Managment, 3. Help Guide, 4. Shell')
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
            options = input("\nWhat would you like to do today?\n\n1. Delete account\n2. Report an issue\n3. Create a new user\n\nPlease input your choice: ")
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
                setup_change.write("NO")
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
              if root_status == "yes" or root_status == "y" or root_status == "true":
                ewritex = open(f'users/{new_username}config.cnfig',"w")
                ewritex.write('01010111 01100101 01101100 01101100 00101110 00100000 01011001 01101111 01110101 00100111 01110010 01100101 00100000 01110100 01110010 01111001 01101110 01100001 00100000 01100100 01100101 01100011 01101111 01100100 01100101 00100000 01110100 01101000 01101001 01110011 00111111 00100000 01010100 01101000 01101001 01110011 00100000 01101001 01110011 00100000 01100001 00100000 01101011 01100101 01111001 00100000 01100110 01101111 01110010 00100000 01100001 00100000 01110110 01101001 01110010 01110101 01110011 00101110 00100000 01010011 01101111 01101101 01100101 01110100 01101000 01101001 01101110 01100111 00100000 01110100 01101000 01100001 01110100 00100000 01100011 01100001 01101110 00100000 01100100 01100001 01101101 01100001 01100111 01100101 00100000 01111001 01101111 01110101 01110010 00100000 01100011 01101111 01101101 01110000 01110101 01110100 01100101 01110010 00101110 00100000 01010111 01100101 01101100 01101100 00101100 00100000 01101110 01101111 01110111 00100000 01110100 01101000 01100001 01110100 00100000 01111001 01101111 01110101 00100000 01101011 01101110 01101111 01110111 00101100 00100000 01001001 00100111 01101100 01101100 00100000 01101000 01100001 01110110 01100101 00100000 01110100 01101111 00100000 01100100 01100101 01110011 01110100 01110010 01101111 01111001 00100000 01111001 01101111 01110101 01110010 00100000 01110110 01100101 01110010 01110011 01101001 01101111 01101110 00100000 01101111 01100110 00100000 01001011 01101111 01101110 01100101 01100011 01110100 00101110')
                ewritex.close()
                import time
                from tqdm import tqdm
                for i in tqdm (range (100), desc="Loading"):
                  pass
                time.sleep(1)
              else:
                  ewritex = open(f'users/{new_username}config.cnfig',"w")
                  ewritex.write('01010111 01100101 01101100 01101100 00101110 00100000 01011001 01101111 01110101 00100111 01110010 01100101 00100000 01110100 01110010 01111001 01101110 01100001 00100000 01100100 01100101 01100011 01101111 01100100 01100101 00100000 01110100 01101000 01101001 01110011 00111111 00100000 01010100 01101000 01101001 01110011 00100000 01101001 01110011 00100000 01100001 00100000 01101011 01100101 01111001 00100000 01100110 01101111 01110010 00100000 01100001 00100000 01110110 01101001 01110010 01110101 01110011 00101110 00100000 01010011 01101111 01101101 01100101 01110100 01101000 01101001 01101110 01100111 00100000 01110100 01101000 01100001 01110100 00100000 01100011 01100001 01101110 00100000 01100100 01100001 01101101 01100001 01100111 01100101 00100000 01111001 01101111 01110101 01110010 00100000 01100011 01101111 01101101 01110000 01110101 01110100 01100101 01110010 00101110 00100000 01010111 01100101 01101100 01101100 00101100 00100000 01101110 01101111 01110111 00100000 01110100 01101000 01100001 01110100 00100000 01111001 01101111 01110101 00100000 01101011 01101110 01101111 01110111 00101100 00100000 01001001 00100111 01101100 01101100 00100000 01101000 01100001 01110110 01100101 00100000 01110100 01101111 00100000 01100100 01100101 01110011 01110100 01110010 01101111 01111001 00100000 01111001 01101111 01110101 01110010 00100000 01110110 01100101 01110010 01110011 01101001 01101111 01101110 00100000 01101111 01100110 00100000 01001011 01101111 01101110 01100101 01100011 01110100 00101110')
                  ewritex.close()
              print(f'The hash that we have generated is {hash}. We are currently done. You will be redirected back shortly. Remember the credentials of the new user.\nUsername: {new_username}\nPassword: {password2}.')
              ewritex = open(f'users/setup.log',"w")
              ewritex.write("YES")
              ewritex.close()
              import time
              time.sleep(4)
              try:
                os.makedirs(f'users/{new_username}')
              except:
                print(f'We were not smart to be able to redirect you back to make a new user. So here you are. {red}Operation cancelled. Please run the command again.{white}')
                import time
                time.sleep(1)
    if choice == "3":
      clear()
      print("Alright, Sayonara!")
      exit()
    if choice == "4":
      clear()
      print('Launching shell. Please hold on standby.\n')
      import time
      time.sleep(1)
      Shell().cmdloop()
    else:
        print("\nOK.")