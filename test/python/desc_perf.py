#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

import nixl._utils as nixl_utils
from nixl._api import nixl_agent

if __name__ == "__main__":
    desc_count = 24 * 64 * 1024
    agent = nixl_agent("test", None)
    addr = nixl_utils.malloc_passthru(256)

    addr_list = [(addr, 256, 0)] * desc_count

    start_time = time.perf_counter()

    descs = agent.get_xfer_descs(addr_list, "DRAM", True)

    end_time = time.perf_counter()

    assert descs.descCount() == desc_count

    print(
        "Time per desc add in us:", (1000000.0 * (end_time - start_time)) / desc_count
    )
    nixl_utils.free_passthru(addr)
