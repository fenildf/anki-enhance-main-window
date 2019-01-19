import aqt
from aqt import mw

userOption = None
def getUserOption(key = None, default = None):
    global userOption
    if userOption is None:
        userOption = aqt.mw.addonManager.getConfig(__name__)
    if key is None:
        return userOption
    if key in userOption:
        return userOption[key]
    else:
        return default

def update(_):
    global userOption
    userOption = None
    
mw.addonManager.setConfigUpdatedAction(__name__,update)
