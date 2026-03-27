import pywikibot
import os
from pywikibot.login import ClientLoginManager

def run_purge():
    site = pywikibot.Site('industrialist', 'miraheze')
    
    password = os.environ.get('PYWIKIBOT_PASSWORD')
    username = 'TRCDBot@TRCDBot_AutoPurge'
    
    manager = ClientLoginManager(site=site, user=username, password=password)
    
    if manager.login():
        print(f"Logged in successfully as {username}")
    else:
        print("Login failed.")
        return

    page = pywikibot.Page(site, "Main Page")
    
    if page.purge():
        print("Success: Page purged.")
    else:
        print("Failure: Purge failed.")

if __name__ == "__main__":
    run_purge()
