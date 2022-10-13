#!/usr/bin/env python
import trafiklab
import sys
import logging
try:
    import coloredlogs
except ModuleNotFoundError:
    print("Sorry, but I am rather fond of coloredlogs")
    print("sudo -H python -m pip install coloredlogs")
    sys.exit(1)

if "-k" in sys.argv:
    api_key = sys.argv[sys.argv.index("-k") + 1]
else:
    try:
        with open(".api.key") as f:
            api_key = f.readline().rstrip()
    except:
        print("Error: please specify you API key on the command line or in .api.key")
        sys.exit(1)

logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG" if "-d" in sys.argv else "INFO", fmt='%(asctime)s,%(msecs)03d %(name)s %(levelname)-8s %(filename)s:%(lineno)d %(message)s')

t = trafiklab.tripmonitor()
# No use in presenting buses we cannot catch unless we run for our lives
time_to_walk_to_the_bus_stop_in_minutes = 15
t.init(time_to_walk_to_the_bus_stop_in_minutes, api_key)
# Partial names are supported. The full names below are
# "Dalby busstation (Lund kn)" and "Lund Centralstation"
if not t.add_route("Dalby Buss", "Lund Central"):
    logging.error("Failed to add route")
    sys.exit(1)
# The API returns "possible" routes which can be very far from "desirable" routes
t.blacklist_line("174")
logging.info("Refreshing")
t.refresh()
t.dump()
logging.info("Refreshing")
t.refresh()
t.dump()
