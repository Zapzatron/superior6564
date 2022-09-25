"""
:authors: Superior_6564
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2022 Superior_6564
"""
import requests
import os
import subprocess
import sys
from IPython.display import Image, display
import itertools


def get_info():
    """
    Args:

    """
    """
    Description:
        get_info() displays information about the package.
    """

    with open("readme.md", "wb") as f:
        f.write(requests.get('https://raw.githubusercontent.com/Superior-GitHub/superior6564/main/README.md').content)

    path = os.getcwd() + "/readme.md"
    line_need = []
    name_need = ["Name", "Vers", "Desc", "Home", "Down", "Wiki", "Auth", "Lice"]
    with open(path) as f:
        for i in range(19):
            line = f.readline()
            if line[:4] in name_need:
                line_need.append(line)

    dictionary = {"Name": line_need[0], "Version": line_need[1], "Description": line_need[2],
                  "Home-Page": line_need[3], "Download-URL": line_need[4], "Wiki": line_need[5],
                  "Author": line_need[6], "Author-email": line_need[7], "License": line_need[8]}
    print(dictionary["Name"] + dictionary["Version"] + dictionary["Description"] +
          dictionary["Home-Page"] + dictionary["Download-URL"] + dictionary["Wiki"] +
          dictionary["Author"] + dictionary["Author-email"] + dictionary["License"])


def install_package(package: str, output: bool = True, version: str = None):
    """
    Args:
        package (str): Name of package
        output (bool): whether name of package will be output or not.
        version (str): Version of package.
    """
    """
    Description:
        install_package(package: str, check=True) installs package.
    """
    if version is None:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
            if output:
                print(f"Library {package} installed.")
        except subprocess.CalledProcessError:
            print("ERROR: Bad name or Bad version.")
            print("Write the correct name or version.")
    else:
        try:
            new_package = package + "==" + version
            subprocess.check_call([sys.executable, "-m", "pip", "install", new_package])
            if output:
                print(f"Library {package}({version}) installed.")
        except subprocess.CalledProcessError:
            print("ERROR: Bad name or Bad version.")
            print("Write the correct name or version.")


def pip_upgrade():
    """
    Args:

    """
    """
    Description:
        pip_upgrade() upgrades pip.
    """

    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])


def show_degget():
    """
    Args:

    """
    """
    Description:
        show_degget() shows image of degget.
    """

    with open("degget_elite.jpg", "wb") as f:
        f.write(requests.get('https://github.com/Superior-GitHub/superior6564/raw/main/superior6564/degit_Elite.jpg').content)

    display(Image(filename="degget_elite.jpg"))


def gen_ru_words():
    """
    Args:

    """
    """
    Description:
        gen_ru_words() generates RU words.
    """

    with open("russian_nouns.txt", "wb") as f:
        f.write(requests.get('https://raw.githubusercontent.com/Superior-GitHub/Superior6564/main/superior6564/russian_nouns.txt').content)

    print("Write all of letters which do you have")
    letters = input("Write in this line: ")
    print("Write length of words which do you need")
    length_of_words = int(input("Write in this line: "))
    with open('russian_nouns.txt', encoding='utf-8') as f:
        list_of_ru_words = []
        for i in range(51300):
            list_of_ru_words.append(f.readline()[0:-1])
        result = ""
        result += f"Слова из {length_of_words} букв:\n"
        words = set(itertools.permutations(letters, r=length_of_words))
        count_2 = 1
        for word in words:
            count = 0
            generate_word = "".join(word)
            for j in range(len(list_of_ru_words)):
                if generate_word == list_of_ru_words[j] and count == 0:
                    result += f"{count_2} слово: {generate_word}\n"
                    count += 1
                    count_2 += 1
    print(result)