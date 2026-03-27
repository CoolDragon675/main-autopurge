import pywikibot
import os
from pywikibot.login import ClientLoginManager
from pywikibot.data import api

def run_purge():
    site = pywikibot.Site('industrialist', 'miraheze')
    
    username = 'TRCDBot@TRCDBot_AutoPurge'
    password = os.environ.get('PYWIKIBOT_PASSWORD')

    manager = ClientLoginManager(site=site, user=username, password=password)
    
    try:
        if manager.login():
            site.login() 
            print(f"Logged in successfully as {username}")
        else:
            print("Login failed: Incorrect credentials.")
            return
    except Exception as e:
        print(f"Login error: {e}")
        return

    page_title = "Main Page"
    params = {
        'action': 'purge',
        'titles': page_title,
        'forcelinkupdate': True
    }
    
    request = api.Request(site=site, parameters=params)
    try:
        data = request.submit()
        if 'purge' in data:
            print(f"Success: Hard Purge completed for '{page_title}'.")
        else:
            print(f"Failure: Unexpected API response: {data}")
    except Exception as e:
        print(f"API Error during purge: {e}")

if __name__ == "__main__":
    run_purge()
