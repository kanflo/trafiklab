#!/usr/bin/env python
import trafiklab
import sys
import logging
try:
    import coloredlogs
except ModuleNotFoundError:
    print("Sorry, but I am rather fond of coloredlogs")
    sys.exit(1)

if len(sys.argv) == 2:
    api_key = sys.argv[1]
else:
    try:
        with open(".api.key") as f:
            api_key = f.readline().rstrip()
    except:
        print("Error: please specify you API key on the command line or in .api.key")
        sys.exit(1)

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', fmt='%(asctime)s,%(msecs)03d %(name)s %(levelname)-8s %(message)s')

t = trafiklab.tripmonitor()
time_to_walk_to_the_bus_stop_in_minutes = 15
t.init(time_to_walk_to_the_bus_stop_in_minutes, api_key)
if not t.add_route("Dalby Buss", "Lund Central"):
    logging.error("Failed to add route")
    sys.exit(1)
t.blacklist_line("174")
logging.info("Refreshing")
t.refresh()
t.dump()
logging.info("Refreshing")
t.refresh()
t.dump()
