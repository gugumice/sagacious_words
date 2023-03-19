#!/bin/sh

while true; do
  nohup python testing.py >> test.out
done &
