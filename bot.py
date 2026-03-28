import pywikibot
import os
from datetime import datetime, timedelta, timezone

def run_purge():
    log_file = "lastSuccess.txt"
    now_utc = datetime.now(timezone.utc)
    today_utc = now_utc.strftime("%Y-%m-%d")
    now_hkt = now_utc + timedelta(hours=8)
    time_str = f"{now_hkt.strftime('%Y-%m-%d, %H:%M')} UTC+8"

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            content = f.read()
            if today_utc in content:
                print(f"Skipping: Already succeeded on {today_utc}.")
                return

    site = pywikibot.Site('industrialist', 'miraheze')
    site.login()

    if not site.logged_in():
        print("Login failed.")
        return

    page = pywikibot.Page(site, "Main Page")
    
    if page.purge(forcelinkupdate=True):
        print(f"Success: Page purged at {time_str}")
        with open(log_file, "w") as f:
            f.write(f"Last purge attempt succeeded at {time_str}")
    else:
        print("Failure: Purge failed.")
        exit(1)

if __name__ == "__main__":
    run_purge()
