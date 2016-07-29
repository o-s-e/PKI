#!/usr/bin/env bash
echo "Starting cfssl server"
exec cfssl serve -address 0.0.0.0 -config /opt/cfssl/config.json -ca /opt/cfssl/ca.pem -ca-key /opt/cfssl/ca-key.pem $@
