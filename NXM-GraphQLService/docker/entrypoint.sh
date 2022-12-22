#!/bin/sh

echo 'launch application'
sed -i s/port=5050/host=\'0.0.0.0\',port=5000/g /root/scripts/server.py

cd /root/scripts/

#node server.js
python server.py
