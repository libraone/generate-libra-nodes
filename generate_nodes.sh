
rm -rf tmp
mkdir tmp
rm -rf nodes
mkdir nodes
./01_GENERATE_FAUCET_KEY.sh
./02_LIBRA_CONFIG.sh
./03_CREATE_NODES.py
