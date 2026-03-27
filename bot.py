import pywikibot
import os
from pywikibot.data import api

def run_purge():
    site = pywikibot.Site('industrialist', 'miraheze')
    
    username = 'TRCDBot@TRCDBot_AutoPurge'
    password = os.environ.get('PYWIKIBOT_PASSWORD')

    try:
        site.login(user=username, password=password)
    except Exception as e:
        print(f"Login failed: {e}")
        return

    if not site.logged_in():
        print("Error: Server rejected login. Still acting as IP.")
        return
    
    print(f"Logged in successfully as: {site.user()}")
    
    page_title = "User:TRCoolDragon675"
    
    params = {
        'action': 'purge',
        'titles': page_title,
        'forcelinkupdate': True  # This forces Lua/Templates to re-calculate
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
