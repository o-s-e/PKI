FROM debian:latest
ENV PATH /go/bin:/usr/local/go/bin:$PATH
ENV GOPATH /go
ENV USER root

RUN apt-get update && \
    apt-get install -y \
    golang &&\
    go get -u github.com/cloudflare/cfssl/cmd/cfssl && \
    go get -u github.com/cloudflare/cfssl/cmd/...



RUN whereis cfssl

RUN groupadd -r cfssl -g 433 && \
    useradd -u 431 -r -g cfssl -d /opt/cfssl -s /sbin/nologin -c "CFSSL daemon account" cfssl && \
    mkdir -p /opt/cfssl && \
    chown -R cfssl:cfssl /opt/cfssl

USER cfssl
WORKDIR /opt/cfssl

COPY ./config/ca.json /opt/cfssl/ca.json
COPY ./config/config.json /opt/cfssl/config.json

#Initialize the CA cert & key
RUN cfssl genkey  -initca /opt/cfssl/ca.json | cfssljson -bare ca

COPY entrypoint.sh /opt/cfssl/entrypoint.sh
RUN chmod +x /opt/cfssl/entrypoint.sh
CMD ["/tmp/entrypoint.sh"]

