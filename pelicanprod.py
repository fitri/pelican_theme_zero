AUTHOR = 'Fitri Rahim'
SITENAME = 'Fitri Rahim'
SITEURL = 'fitri.me' #overwrite with command: pelican content --SITEURL "siteaddress"
THEME = './themes/zero'

PATH = 'content'

# Time and region
TIMEZONE = 'Asia/Kuala_Lumpur'
DEFAULT_DATE_FORMAT = '%b %Y'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = None

PLUGINS = [
]



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
