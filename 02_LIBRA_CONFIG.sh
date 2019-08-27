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


LIBRA_SOURCE="$(jq -r '.LIBRA_SOURCE'  00_CONFIG.conf)"
NODE_NUM="$(jq -r '.NODE_NUM' 00_CONFIG.conf)"
PEER_SEED="$(jq -r '.PEER_SEED' 00_CONFIG.conf)"

${LIBRA_SOURCE}/target/debug/libra-config --base ${LIBRA_SOURCE}/config/data/configs/node.config.toml --nodes $NODE_NUM -m tmp/faucet_key -o tmp -s $PEER_SEED



