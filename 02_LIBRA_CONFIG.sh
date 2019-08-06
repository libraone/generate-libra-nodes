# /* ###############################################################################
# © 2019 nodepacific tech All rights reserved
#
# Libra Generate nodes tool
# The tool to generate libra validator nodes for private Libra blockchain
#
#
# Created by https://www.nodepacific.com
#
###############################################################################  */

LIBRA_SOURCE="$(jq -r '.LIBRA_SOURCE'  00_CONFIG.conf)"
NODE_NUM="$(jq -r '.NODE_NUM' 00_CONFIG.conf)"
PEER_SEED="$(jq -r '.PEER_SEED' 00_CONFIG.conf)"

${LIBRA_SOURCE}/target/release/libra-config --base ${LIBRA_SOURCE}/config/data/configs/node.config.toml --nodes $NODE_NUM -m tmp/faucet_key -o tmp -s $PEER_SEED

#${LIBRA_SOURCE}/target/release/libra-config --base ${LIBRA_SOURCE}/config/data/configs/node.config.toml --nodes $NODE_NUM -m tmp/faucet_key -o tmp -s 7533ae4f06f4b590a7d4c1ef06ca59998fc5f2f20731e1295e441c36277d4e32


