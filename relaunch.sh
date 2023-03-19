#!/bin/sh

while true; do
  nohup python3 /opt/sw/typewriter.py >> test.out
done &
