#!/bin/sh

sleep 3m

cd `dirname $0`
nohup sudo python dht11_sendToFocuslight.py 1>/dev/null 2>/dev/null &
