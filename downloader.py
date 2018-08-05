from requests import get
import os, sys
### from https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)
        print(". Done")

def get_mod_folder():
    foldername = ""
    initial = "mods"
    index = 1
    if os.path.exists(os.path.join(os.getcwd(), initial)):
        while True:
            if os.path.exists(os.path.join(os.getcwd(), initial + index)):
                index += 1
            else:
                return os.path.join(os.getcwd(), initial + index)
    return os.path.join(os.getcwd(), initial)

print("Reading modlist from mods.csv in current working directory")

mod_list = []
try:
    with open("mods.csv", "r") as mods:
        mod_list = [x.replace("\n","") for x in mods.readlines()]
except Exception as e:
    print("An unexpected error ocurred: {}".format(str(e)))
    sys.exit()

print("Downloading {} mods to {} folder.".format(len(mod_list), get_mod_folder()))

mod_folder = get_mod_folder()

try:
    os.mkdir(mod_folder)
except Exception as e:
    print("An unexpected error ocurred: {}".format(str(e)))
    sys.exit()

for item in mod_list:
    print("Downloading {}...".format(item), end="")
    download("https://minecraft.curseforge.com/projects/{}/files/latest".format(item), os.path.join(mod_folder, item) + ".jar")

print("Finished downloading everything.")