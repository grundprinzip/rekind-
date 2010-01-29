import rekindle
from rekindle.rekindle import Rekind
import rekindle.configuration as config

def processHandler(f):
    """ Handle the rekind process """
    Titanium.API.log(f);
    r = Rekind(f, config.ACM)
    r.start()
