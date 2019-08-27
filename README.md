



# Libra网络搭建流程


#### 编译libra源码



因为官方代码更新很快。这个版本只支持libra的 testnet 分支节点搭建。请下载libra源码后，执行下面命令切换分支

    $ git checkout testnet
    
然后根据执行下面命令libra

    $ cargo build

PS： master分支的支持我们很快就会更新


#### 安装 python3 依赖:

	sudo pip3 install sha3
	sudo pip3 install mnemonic




#### 生成创建 peer节点的seed

使用 create_seed.py 创建peer seed

	$ python ./create_seed.py
	
	dda068eec093f40053d737564b8be5d6455f543330b745195379191e6e6bb03a

输出的dda068eec093f40053d737564b8be5d6455f543330b745195379191e6e6bb03a 就是seed值

#### 配置 00_CONFIG.conf

        {
            "LIBRA_SOURCE": "\/home\/name\/new-libra\/libra",
            "NODE_NUM":2,
            "PEER_SEED":"7533ae4f06f4b590a7d4c1ef06ca59998fc5f2f20731e1295e441c36277d4e32"
        }


- LIBRA_SOURCE： libra的源码目录
- NODE_NUM： 生成peer的数量
- PEER_SEED： 节点的id的seed， 使用上面一步的create_seed.py创建的值

#### 执行创建节点命令

	generate_nodes.sh

生成节点的配置文件在nodes目录下

    node-12ef71a8e1c51c4c5abaaabc7d76be85296dbed6632f8f6087d17bf24e24030c
    node-3141d7ff54ea8318041447898eceaeea4cde1c344c6732d60b7d4bf231ebee19

然后分别将个各节点目录传送到对应的服务器，根据目录中的README.md教程操作，修改配置，启动节点
