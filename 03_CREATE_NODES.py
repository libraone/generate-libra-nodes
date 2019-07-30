#!/usr/bin/python3

import os

config_suffix = '.node.config.toml'


files = os.listdir("tmp")

for file_name in files:
    if file_name.endswith(config_suffix):
        peer_id = file_name.replace(config_suffix, '')
        node_dir = "nodes/node-" + peer_id
        if os.path.exists(node_dir):
           os.system('rm -rf ' + node_dir) 
        os.mkdir(node_dir)
        os.system('mv tmp/' + file_name + ' ' + node_dir + '/')
        key_toml = peer_id + '.node.keys.toml'
        os.system('mv tmp/' + key_toml + ' ' + node_dir + '/')
        os.system('cp tmp/genesis.blob ' + node_dir + '/')
        os.system('cp tmp/seed_peers.config.toml ' + node_dir + '/')
        os.system('cp tmp/trusted_peers.config.toml ' + node_dir + '/')
        os.system('cp tmp/faucet_key ' + node_dir + '/')

        start_node_path = node_dir + '/start_node.sh'
        os.system('echo LIBRA_SOURCE=\<path_to_libra\> > ' + start_node_path)
        os.system('echo PEER_ID=' + peer_id + ' >>' + start_node_path)
        os.system('echo "">>' + start_node_path)
        os.system('echo \${LIBRA_SOURCE}/target/release/libra_node -f \${PEER_ID}.node.config.toml -p \${PEER_ID}>>' + start_node_path)
        os.system('chmod 755 ' + start_node_path)
        os.system('cp NODE_README.md ' + node_dir + '/README.md')
        print('create ' + node_dir)

#os.system('rm genesis.blob seed_peers.config.toml trusted_peers.config.toml')
#os.system('rm -rf tmp')
