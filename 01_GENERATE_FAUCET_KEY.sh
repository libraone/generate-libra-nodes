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


${LIBRA_SOURCE}/target/release/generate_keypair -o tmp/faucet_key 
