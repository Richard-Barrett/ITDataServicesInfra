#!/bin/bash

# Clear Page Cache
sync; echo 1 > /proc/sys/vm/drop_caches

# Clear Dentries and inodes
echo "echo 2 > /proc/sys/vm/drop_caches"
