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



rm -rf tmp
mkdir tmp
rm -rf nodes
mkdir nodes
./01_GENERATE_FAUCET_KEY.sh
./02_LIBRA_CONFIG.sh
./03_CREATE_NODES.py
