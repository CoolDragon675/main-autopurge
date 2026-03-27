import pywikibot

def run_purge():
    # Pywikibot will now automatically find the username and 
    # password from user-config.py and passwordfile
    site = pywikibot.Site('industrialist', 'miraheze')
    site.login()

    if not site.logged_in():
        print("Login failed.")
        return

    page = pywikibot.Page(site, "Main Page")
    if page.purge(forcelinkupdate=True):
        print("Success: Page purged.")
    else:
        print("Failure: Purge failed.")

if __name__ == "__main__":
    run_purge()
