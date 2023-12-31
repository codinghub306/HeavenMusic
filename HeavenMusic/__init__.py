from HeavenMusic.core.bot import Heaven
from HeavenMusic.core.dir import dirr
from HeavenMusic.core.git import git
from HeavenMusic.core.userbot import Userbot
from HeavenMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Heaven()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
