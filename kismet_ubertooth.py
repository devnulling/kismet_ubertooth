#!/usr/bin/env python
from kismetclient import Client as KismetClient
from kismetclient import handlers

from pprint import pprint

import logging
log = logging.getLogger('kismetclient')
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

address = ('127.0.0.1', 2501)
k = KismetClient(address)

def handle_BTBBDEV(client, lap, bdaddr):
	print 'bdaddr: %s - lap: %s' % (bdaddr, lap)

k.register_handler('BTBBDEV', handle_BTBBDEV)


try:
    while True:
        k.listen()
except KeyboardInterrupt:
    pprint(k.protocols)
    log.info('Exiting...')
