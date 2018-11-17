from users import *
#from filters.py import *
from convert_to_json import *
#import quickstart.py

denero = Professor({}, "John Denero", "EECS", ["61a"], ["Interesting research stuff"],
                    ["Rapping"], "I'm John Denero!", "john_denero@berkeley.edu", "www.johndenero.com")
gireeja = Professor({}, "Gireeja Ranade", "EECS", ["16a"], ["Interesting topics"], ["Passive aggressiveness on Piazza"],
                        "I'm Gireeja Ranade!", "gireeja_ranade@berkeley.edu", "www.gireeja_ranade.com")

professors = [denero, gireeja]
list_of_profs_to_json(professors)
