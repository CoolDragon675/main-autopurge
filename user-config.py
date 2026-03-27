import pywikibot

site_url = 'https://industrialist.miraheze.org'
site = pywikibot.Site(url=site_url)
family = site.family.name
mylang = site.code
usernames[family][mylang] = 'TRCDBot'
