import pywikibot
import os
from pywikibot.data import api

def run_purge():
    # 1. Initialize site
    site = pywikibot.Site('industrialist', 'miraheze')
    
    # 2. Get credentials
    username = 'TRCDBot@TRCDBot_AutoPurge'
    password = os.environ.get('PYWIKIBOT_PASSWORD')

    # 3. FORCE LOGIN (This is the critical part)
    # We use site.login() directly which handles cookies better than the manager
    try:
        site.login(user=username, password=password)
    except Exception as e:
        print(f"Login failed: {e}")
        return

    # 4. DOUBLE CHECK LOGIN
    if not site.logged_in():
        print("Error: Server rejected login. Still acting as IP.")
        return
    
    print(f"Logged in as: {site.user()}")

    # 5. EXECUTE PURGE (Forcing the session cookie)
    page = pywikibot.Page(site, "Main Page")
    
    # We use a custom request to ensure the 'write' token and cookies are sent
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
