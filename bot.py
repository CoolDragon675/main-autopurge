import pywikibot
import os
from pywikibot.login import ClientLoginManager

def run_purge():
    site = pywikibot.Site('industrialist', 'miraheze')
    password = os.environ.get('PYWIKIBOT_PASSWORD')
    
    # Use the full Account@BotName string here as well
    manager = ClientLoginManager(site=site, user='TRCDBot@TRCDBot_AutoPurge', password=password)
    manager.login()

    page = pywikibot.Page(site, "Main Page")
    if page.purge():
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    run_purge()
