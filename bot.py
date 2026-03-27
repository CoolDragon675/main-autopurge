import pywikibot
import os

def run_purge():
    site = pywikibot.Site('industrialist', 'miraheze')
    
    site.login()

    if not site.logged_in():
        print("Error: Still not logged in.")
        return

    page = pywikibot.Page(site, "Main Page")
    if page.purge():
        print("Success: Purged.")
    else:
        print("Failure: Purge failed.")

if __name__ == "__main__":
    run_purge()
