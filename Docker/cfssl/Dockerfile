FROM ubuntu:xenial
MAINTAINER ose
ENV PATH /go/bin:/usr/local/go/bin:$PATH
ENV GOPATH /go
ENV USER root

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    golang \
    gcc \
    git &&\
    echo "Prerequesites installed"

RUN echo "Building cfssl" && \
    go get -u github.com/cloudflare/cfssl/cmd/cfssl && \
    echo "Building cfssl toolset" && \
    go get -u github.com/cloudflare/cfssl/cmd/... && \
    echo "Build complete"


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

#  RUN chmod +x /opt/cfssl/entrypoint.sh

CMD ["/tmp/entrypoint.sh"]

# Works upstream docker 1.12
#HEALTHCHECK --interval=5m --timeout=3s \
# CMD curl -f http://localhost/ || exit 1