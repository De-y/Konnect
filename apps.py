from load import clear
import os
black = "\u001b[30m"
red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
magenta = "\u001b[35m"
cyan = "\u001b[36m"
white = "\u001b[37m"
clear()
print(f'{red}Konnect Apps\n{white}=============================\n{magenta}©1999 Defy. All rights reserved.{white}')
from pathlib import Path

for p in Path('apps/').glob('**/*.py'):
    list = p.name.strip('.py')
    print(f"{list}\n")
launch = input("Please type which app you would like to launch: ")
try:
  clear()
  os.system(f'python3 apps/{launch}.py')
except:
  print("This is not a valid app. Exiting in 5 seconds.")
  import time
  time.sleep(5)