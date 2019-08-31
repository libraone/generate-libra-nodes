#!/usr/bin/python3

############################################################################### 
# Pulish by LibraOne, created by the NodePacific is the member of LibraOne
# 
# Copyright 2019 The NodePacific Authors. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import os

config_suffix = '.node.config.toml'


files = os.listdir("tmp")

for file_name in files:
    if file_name.endswith(config_suffix):
        peer_id = file_name.replace(config_suffix, '')
        peer_id_value = peer_id.replace("validator_", '')
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
        os.system('echo PEER_ID=' + peer_id_value + ' >>' + start_node_path)
        os.system('echo "">>' + start_node_path)
        os.system('echo \${LIBRA_SOURCE}/target/debug/libra_node -f validator_\${PEER_ID}.node.config.toml -p \${PEER_ID}>>' + start_node_path)
        os.system('chmod 755 ' + start_node_path)
        os.system('cp NODE_README.md ' + node_dir + '/README.md')
        print('create ' + node_dir)

#os.system('rm genesis.blob seed_peers.config.toml trusted_peers.config.toml')
#os.system('rm -rf tmp')
