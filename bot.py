import pywikibot
import os, sys, hashlib
from datetime import datetime, timedelta, timezone

def run_purge():
  log_file = "lastSuccess.txt"
  utc = datetime.now(timezone.utc)
  today_utc = utc.strftime("%Y%m%d")
  today_hash = hashlib.md5(today_utc.encode()).hexdigest()
  hash_id = f"{int(today_hash[:8], 16)}"
  hkt = utc + timedelta(hours=8)
  time_str = f"{hkt.strftime('%Y-%m-%d, %H:%M:%S')} UTC+8"

  if os.path.exists(log_file):
    with open(log_file, "r") as f:
      content = f.read()
      if hash_id in content:
        print(f"Skipping: Succeeded on {today_str}.")
        return

  site = pywikibot.Site('industrialist', 'miraheze')
  site.login()

  if not site.logged_in():
    print("Login failed.")
    sys.exit(1)

  page = pywikibot.Page(site, "Main Page")
  
  if page.purge(forcelinkupdate=True):
    print(f"Success: Page purged at {time_str}")
    with open(log_file, "w") as f:
      f.write(f"Success: Page purged at {time_str}\nHash ID: {hash_id}")
  else:
    print("Failure: Purge failed.")
    sys.exit(1)

if __name__ == "__main__":
  run_purge()
