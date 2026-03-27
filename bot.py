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
    
    print(f"Logged in as: {site.user()}")

    page = pywikibot.Page(site, "User:TRCoolDragon675")
    
    params = {
        'action': 'purge',
        'titles': page.title(),
        'forcelinkupdate': True
    }
    
    request = api.Request(site=site, parameters=params)
    try:
        data = request.submit()
        if 'purge' in data:
            print("Success: Page purged via API with active session.")
        else:
            print(f"Failure: Unexpected API response: {data}")
    except Exception as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    run_purge()
