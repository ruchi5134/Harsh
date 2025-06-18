from SystemMusic.core.bot import System
from SystemMusic.core.dir import dirr
from SystemMusic.core.git import git
from SystemMusic.core.userbot import Userbot
from SystemMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = System()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
