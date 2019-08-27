# Libra Node startup Guide

[中文版](NODE_README_cn.md)


#### 1. Setup node.config.toml


Change data path:

    [base]
    data_dir_path = "./data"


Change adminssion_control's gRPC address config:


    [admission_control]
    address = "0.0.0.0"
    admission_control_service_port = 46091

Change p2p config:

	[network]
	seed_peers_file = "seed_peers.config.toml"
	listen_address = "/ip4/0.0.0.0/tcp/37993"
	advertised_address = "/ip4/0.0.0.0/tcp/37993"



#### 2. Change peer address on trusted_peers.config.toml

Change seed_peer's address:

	1e5d5a74b0fd09f601ac0fca2fe7d213704e02e51943d18cf25a546b8416e9e1 = ["/ip4/192.168.1.120/tcp/37993"]



#### 3. Start libra_node

Build libra_node program on libra source:

    $ cd libra
    $ cargo build -p libra_node


Back to node's config directory, setup libra source path. Change LIBRA_SOURCE valule on start_node.sh


	LIBRA_SOURCE=<path_to_libra>

execute start_node.sh

	$ ./start_node.sh


#### 4. submit mint transaction

	The faucet_key file is the private key of mint account. You can set this value when start libra_client or libra sdk, then could invoke mint transaction.

