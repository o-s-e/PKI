#!/usr/bin/env bash


echo "Generating ca keys"
exec cfssl \
        genkey \
        -initca /opt/ca.json | cfssljson ca
        echo "Starting cfssl server"

exec cfssl \
        serve \
        -config /opt/cfssl/config.json \
        -ca /opt/cfssl/ca.pem \
        -ca-key /opt/cfssl/ca-key.pem \
        $@
