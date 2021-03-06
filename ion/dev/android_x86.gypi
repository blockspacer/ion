#
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
{
  'variables' : {
    # These are inputs to android_common.
    'android_arch': 'x86',
    'android_abi': 'x86',
    'android_tool_prefix': 'i686-linux-android',
  },
  'includes': [
    'android_common.gypi',
  ],
  'target_defaults': {
    'target_conditions': [
      ['_toolset == "target"', {
        'defines': [
          '<@(android_common_defines)',
          'ARCH_PIII',
         ],
        'include_dirs': [
          '<(android_ndk_sysroot)',
        ],
        'cflags': [
          '<@(android_common_cflags)',
          '-march=i686',
          '-msse3',
          '-mstackrealign',
          '-mfpmath=sse',
        ],
        'cflags_cc': [
          '<@(android_common_cflags_cc)',
        ],
        'ldflags': [
          '<@(android_common_ldflags)',
          # The libraries go here, instead of in a link_settings block, because
          # gyp complains about using a link_settings block in a configuration.
          # Since these are all -lfoo style link settings, it should be OK.
          '<@(android_common_libraries)',
        ],
      }],
    ],  # target_conditions
  },
}
