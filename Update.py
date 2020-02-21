# import theese nutz

import platform
import subprocess
import time 
import warnings

# remove Deprecation Warnings, update the code once i learn the new ones.
warnings.filterwarnings("ignore", category=DeprecationWarning) 


dist = platform.linux_distribution() # stores os name in Tuple called dist
win = platform.release() # stores the windows version 


if "Ubuntu" in dist: # cheeks if "Ubuntu" is stored within Tuple
    
    print("supported OS, enter your password to start the update")
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "upgrade"])

# subprocess.run(["word1", "word2"]) need but commands like that

elif win == "10":
    subprocess.run(["bash"])
#opens bash on windows 10

else:
    print(dist)
    print("your OS not suppuprted, scrpit closes in 10 seconds")
    time.sleep(10)    # pause 10(10.5) for seconds
# Error message.

