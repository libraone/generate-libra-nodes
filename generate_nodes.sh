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


rm -rf tmp
mkdir tmp
rm -rf nodes
mkdir nodes
./01_GENERATE_FAUCET_KEY.sh
./02_LIBRA_CONFIG.sh
./03_CREATE_NODES.py
