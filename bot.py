import pywikibot
import os

def run_purge():
    site = pywikibot.Site('industrialist', 'miraheze')
    
    # Trigger login
    site.login()

    # SAFETY CHECK: If this returns False, the bot isn't logged in
    if not site.logged_in():
        print("CRITICAL ERROR: Login failed. The bot is still an anonymous IP.")
        return

    # Only if logged in, try the purge
    page = pywikibot.Page(site, "Main Page")
    if page.purge():
        print("Success: Purged as logged-in user.")
    else:
        print("Failure: Purge rejected.")

if __name__ == "__main__":
    run_purge()
