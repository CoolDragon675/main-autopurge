from pywikibot import family


class Family(family.Family):
  name = 'miraheze'
  langs = {
      'industrialist': 'industrialist.miraheze.org',
  }

 def scriptpath(self, code):
    return '/w'

  def protocol(self, code):
    return 'https'
