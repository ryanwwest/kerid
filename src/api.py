from quart import Quart, jsonify
import asyncio

app = Quart(__name__)
node = None

def run_api(kademlia_node):
    global node
    node = kademlia_node
    app.run(loop=asyncio.get_event_loop())

@app.route('/id/<aid>')
async def get_id_with_aid(aid):
    # todo verify
    id = await node.get(aid)
    return jsonify(id)

@app.route('/id/<aid>/<witness_id>', methods=['POST'])
async def publish_aid_id_mapping(aid, witness_id):
    # todo verify
    await node.set(aid, witness_id)
    return jsonify("done")

@app.route('/ip/<witness_id>')
async def get_ip_with_id(witness_id):
    # todo verify
    ip = await node.get(witness_id)
    return jsonify(ip)

@app.route('/ip/<witness_id>/<witness_ip>', methods=['POST'])
async def publish_id_ip_mapping(witness_id, witness_ip):
    # todo verify
    await node.set(witness_id, witness_ip)
    return jsonify("done")
