import asyncio
import logging

import kademlia.network

from api import API
import test


from src.const import *


def setup_logging():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log = logging.getLogger('kademlia')
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)

async def run():
    # setup_logging()

    # Create a node and start listening on port 5678
    node = kademlia.network.Server()
    # todo don't expose default kademlia apis OR intercept them with code to disallow entry / verify, etc
    await node.listen(primary_port)
    print("connecting to kademlia network...")

    # todo config value to pull this from
    # connect to the other kademlia node
    await node.bootstrap([("0.0.0.0", bootstrap_port)])
    print("connected.")

    api = API(node)

    await test.test_api(api)

asyncio.run(run())

