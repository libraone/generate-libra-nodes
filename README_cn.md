

# generate-libra-nodes Guide

[中文版](README_cn.md)


#### Build libra source:

Because the libra source is updated very quickly. This version only supports Libra's testnet branch. Please download the libra source code and execute the following command to switch branches.


    $ git checkout testnet
    
Build comamnds that used by generate-libra-nodes:

    $ cargo build

PS： master version of generate-libra-nodes will update soon.


#### Install Independence:

	sudo pip3 install sha3
	sudo pip3 install mnemonic
	sudo apt install jq

#### generate peer's seed

enter generate-libra-nodes directory:

    $ cd generate-libra-nodes

create peer seed:

	$ python ./create_seed.py
	
	dda068eec093f40053d737564b8be5d6455f543330b745195379191e6e6bb03a

output dda068eec093f40053d737564b8be5d6455f543330b745195379191e6e6bb03a is the seed value

#### 配置 00_CONFIG.conf

        {
            "LIBRA_SOURCE": "\/home\/name\/new-libra\/libra",
            "NODE_NUM":2,
            "PEER_SEED":"7533ae4f06f4b590a7d4c1ef06ca59998fc5f2f20731e1295e441c36277d4e32"
        }


- LIBRA_SOURCE： libra source directory
- NODE_NUM： number of peer nodes
- PEER_SEED： seed value that create by create_seed.py on last step

#### Execute generate node script

	$ generate_nodes.sh

The nodes' config files will put on directory nodes:

    node-12ef71a8e1c51c4c5abaaabc7d76be85296dbed6632f8f6087d17bf24e24030c
    node-3141d7ff54ea8318041447898eceaeea4cde1c344c6732d60b7d4bf231ebee19

Then you can copy every node's direcotry to node's server, change setup and startup libra_node program, by followwing the README.md in the node's config directory.

