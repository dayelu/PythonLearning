#!/bin/sh

mkdir -p /usr/local/mongodb/data/db
mkdir -p /usr/local/mongodb/logs
touch /usr/local/mongodb/logs/mongodb.logs
touch /etc/mongodb.conf

echo "dbpath=/usr/local/mongodb/data/db
logpath=/usr/local/mongodb/logs/mongodb.logs
logappend=true
bind_ip=0.0.0.0
port=27017
fork=true
##auth = true" > /etc/mongodb.conf


mongod -f /etc/mongodb.conf
