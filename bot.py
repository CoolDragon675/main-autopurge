import pywikibot
import os, sys, time
from datetime import datetime, timedelta, timezone

def precision_warmup():
  now = datetime.now(timezone.utc)
  
  if now.hour >= 22:
    target = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    
    print("::group::Warm-up period (Waiting for Midnight)")
    print(f"Runner started at: {now.strftime('%H:%M:%S')} UTC")
    
    while datetime.now(timezone.utc) < target:
      print(f"Heartbeat: {datetime.now(timezone.utc).strftime('%H:%M:%S')} - Active.")
      sys.stdout.flush()
      time.sleep(300) 
      
    print("::endgroup::")
    print("Midnight reached! Proceeding to purge logic...")
    
  else:
    print(f"Started at {now.strftime('%H:%M:%S')} UTC. No wait required.")

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
      f.write(f"{today_utc}: Last purge attempt succeeded at {time_str}")
  else:
    print("Failure: Purge failed.")
    sys.exit(1)

if __name__ == "__main__":
  precision_warmup()
  run_purge()
