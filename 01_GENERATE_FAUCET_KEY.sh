LIBRA_SOURCE="$(jq -r '.LIBRA_SOURCE'  00_CONFIG.conf)"


${LIBRA_SOURCE}/target/release/generate_keypair -o tmp/faucet_key 
