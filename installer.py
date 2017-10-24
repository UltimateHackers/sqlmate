import pip
import os


# ----------------
#  Function to check and install dependencies automatically
# ----------------
def install_dependencies():
    global any_install
    any_install = False

    # installing mechanize
    try:
        import mechanize
        pass
    except ImportError:
        if not os.system("cls") == 0:
            os.system("clear")
            pass
        print "[!] Installing mechanize"
        pip.main(["install", "mechanize"])
        any_install = True
        pass

    # installing bs4
    try:
        import bs4
        pass
    except ImportError:
        if not os.system("cls") == 0:
            os.system("clear")
            pass
        print "[!] Installing bs4"
        pip.main(["install", "bs4"])
        any_install = True
        pass

    # installing HTMLparser
    try:
        import HTMLparser
        pass
    except ImportError:
        if not os.system("cls") == 0:
            os.system("clear")
            pass
        print "[!] Installing HTMLparser"
        pip.main(["install", "HTMLparser"])
        any_install = True
        pass

    # installing argparse
    try:
        import argparse
        pass
    except ImportError:
        if not os.system("cls") == 0:
            os.system("clear")
            pass
        print "[!] Installing argparse"
        pip.main(["install", "argparse"])
        any_install = True
        pass

    # installing requests
    try:
        import requests
        pass
    except ImportError:
        if not os.system("cls") == 0:
            os.system("clear")
            pass
        print "[!] Installing requests"
        pip.main(["install", "requests"])
        any_install = True
        pass

    # installing urlparse
    try:
        import urlparse
        pass
    except ImportError:
        if not os.system("cls") == 0:
            os.system("clear")
            pass
        print "[!] Installing urlparse"
        pip.main(["install", "urlparse"])
        any_install = True
        pass

    # exiting on any install
    if any_install:
        print "[!] Dependencies installed\n[!] Exiting sqlmate"
        os._exit(0)
    pass
