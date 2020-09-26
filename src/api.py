
class API:

    def __init__(self, node):
        self.node = node

    # temporary test function
    async def run(self):
        aid = "aid1"
        witness_id = "id1"
        witness_ip = "ip1"
        await self.publish_aid_id_mapping(aid, witness_id)
        await self.publish_id_ip_mapping(witness_id, witness_ip)

        assert witness_id == await self.query_with_aid(aid)
        assert witness_ip == await self.query_with_witness_id(witness_id)
        print('it works')

    async def publish_aid_id_mapping(self, aid, witness_id):
        await self.node.set(aid, witness_id)

    async def publish_id_ip_mapping(self, witness_id, witness_ip):
        # todo verify witness ip is signed
        await self.node.set(witness_id, witness_ip)

    async def query_with_aid(self, aid):
        # todo cache manager to optionally return a key event log (KEL) instead of the id if that is cached
        result = await self.node.get(aid)
        return result

    async def query_with_witness_id(self, witness_id):
        result = await self.node.get(witness_id)
        return result
