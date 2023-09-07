import requests
import os
import shutil

#global variables
url = ""
game_id = None
page = None

print("   _____ _                        _____ __  __ _____        ")
print("  / ____| |                      / ____|  \/  |  __ \       ")
print(" | (___ | |_ ___  __ _ _ __ ___ | |    | \  / | |  | |      ")
print("  \___ \| __/ _ \/ _` | '_ ` _ \| |    | |\/| | |  | |      ")
print("  ____) | ||  __/ (_| | | | | | | |____| |  | | |__| |      ")
print(" |_____/ \__\___|\__,_|_| |_| |_|\_____|_|  |_|_____/       ")
print("  / ____|    | | |         | | (_)                          ")
print(" | |     ___ | | | ___  ___| |_ _  ___  _ __                ")
print(" | |    / _ \| | |/ _ \/ __| __| |/ _ \| '_ \               ")
print(" | |___| (_) | | |  __/ (__| |_| | (_) | | | |              ")
print("  \_____\___/|_|_|\___|\___|\__|_|\___/|_| |_| _            ")
print(" |  __ \                    | |               | |           ")
print(" | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __  ")
print(" | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__| ")
print(" | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |    ")
print(" |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|    ")
print("____________________________________________________________")
                                                           
print('\nImportant:')
print('- Download SteamCMD from official site; put both SteamCMD and Workshop Collection Downloader in the same directory')           
print("- It's VERY simple script so do not expect much.")                                               
print("- Workshop Collection Links do not differ from Workshop Addons, for now I won't prevent from passing addon link instead of collection ¯\_(^^)_/¯, it will just timeout")
print("- Files will be saved in 'mods' directory; if 'mods' directory exists it will be emptied after download")
print('- Currently only for Windows')
print('- Currently only for anonymous downloads')
print('- Currently not validating appid')
print('- List of apps, that allows anonymous downloads is available on steamdb.info')
print('- Certain Antiviruses may false alert due to moving files from "steamapps" to "mods"')                                                           

def fileCleanup():
  if os.path.exists("webContent.txt"):
    os.remove("webContent.txt")
  if os.path.exists("script.txt"):
    os.remove("script.txt")                                                          

def validation(input_url, id):
  #Validate Steam Workshop Url by comparing Urls
  def validSteamWorkshopUrl(input_url):
    urlToCompare="https://steamcommunity.com/sharedfiles/filedetails/?id="
    if input_url.rstrip('0123456789') == urlToCompare:
      return True
    else:
      return False

  #Validate Game Id by comparing with list (TODO)
  def validGameId(id):
    return True

  if validSteamWorkshopUrl(input_url) and validGameId(id):
    return True
  else:
    return False
  
def Input():
  global url, game_id
  url=input('Enter Steam Workshop Collection Url or type "quit" to quit: ')
  if url == 'quit':
    exit()
  game_id = int(input('Enter Game Id: '))
  
def CreateScriptFile():
  global url, game_id, page
  Input()
  print(url, game_id)
  if validation(url, game_id):
    page = requests.get(url)
  else:
    print('Wrong input')
    CreateScriptFile()

  #Urls, prepare script for SteamCMD
  with open("webContent.txt", "w", encoding="utf-8") as wc:
    wc.write(page.text)
  with open("webContent.txt", "r", encoding="utf-8") as wc:
    lines = wc.readlines()
  with open("script.txt", "w", encoding="utf-8") as f: 
    f.write('login anonymous \n')
    for line in lines:
      if line.strip().startswith("SharedFileBindMouseHover("):
        f.write("workshop_download_item " + str(game_id) + " " +(line.strip().removeprefix('SharedFileBindMouseHover( "sharedfile_').split('",')[0]) +"\n")
    f.write('quit \n')

def moveFiles():
  global game_id
  path=f"./steamapps/workshop/content/{game_id}/"
  fileList = os.listdir(path)
  if(os.path.exists("mods")):
    print("WARNING YOUR MODS FOLDER WILL BE OVERRITEN")
    input("PRESS ENTER TO CONTINUE")
    if(os.path.exists("mods")):
      shutil.rmtree("mods")
  os.mkdir("mods")
  for file in fileList:
    shutil.move(f"{path}/{file}", "./mods")

fileCleanup()
CreateScriptFile()

#Start SteamCMD with previously created script
os.system('steamcmd.exe +runscript script.txt')

#moving mods and files cleanup
fileCleanup()
moveFiles()


print("##########")
print("Please, check in logs if every file was downloaded.")
print("Your files were saved to mods folder.")
print("##########")
input('Press enter to quit...') 