import pywikibot
import os

def run_purge():
    site = pywikibot.Site()
    bot_password = os.environ.get('PYWIKIBOT_PASSWORD')
    
    if not bot_password:
        print("Error: PYWIKIBOT_PASSWORD not found.")
        return

    site.login(password=bot_password)

    page_title = "Main Page" 
    page = pywikibot.Page(site, page_title)

    if page.purge():
        print(f"Successfully purged '{page_title}'.")
    else:
        print(f"Failed to purge '{page_title}'.")

if __name__ == "__main__":
    run_purge()
