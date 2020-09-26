import logging
import asyncio
from const import *
from kademlia.network import Server

def setup_logging():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log = logging.getLogger('kademlia')
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)

async def run():
    # Create a node and start listening on port 5678
    node = Server()
    # todo don't expose default kademlia apis OR intercept them with code to disallow entry / verify, etc
    await node.listen(primary_port)

    print("connecting to kademlia network...")

    # todo config value to pull this from
    await node.bootstrap([("0.0.0.0", bootstrap_port)])

    await node.set("rwest", "best")
    result = await node.get("rwest")
    print(result)

asyncio.run(run())