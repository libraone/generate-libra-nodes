# 启动Libra Node 接入测试网



#### 1. 节点配置 node.config.toml



修改节点数据保存路径

    [base]
    data_dir_path = "./data"


adminssion_control的gRPC api配置:


    [admission_control]
    address = "0.0.0.0"
    admission_control_service_port = 46091

p2p的配置

	[network]
	seed_peers_file = "seed_peers.config.toml"
	listen_address = "/ip4/0.0.0.0/tcp/37993"
	advertised_address = "/ip4/0.0.0.0/tcp/37993"



#### 2. peer位置 trusted_peers.config.toml

修改每个 seed_peer的服务器地址

	1e5d5a74b0fd09f601ac0fca2fe7d213704e02e51943d18cf25a546b8416e9e1 = ["/ip4/192.168.1.120/tcp/37993"]



#### 3. 启动节点

编译，进入libra源码目录，执行下面命令编译

	cargo build -p libra_node --release


回到node目录，设置libra的项目目录，修改 start_node.sh中的 LIBRA_SOURCE 为libra源码目录

	LIBRA_SOURCE=<path_to_libra>

执行启动命令

	./start_node.sh


#### 4. 发起 mint 交易

	faucet_key就是可以mint账户的私钥，可以再启动客户端或sdk中设置这个值，就可以调用mint交易
