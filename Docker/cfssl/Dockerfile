FROM alpine:3.2

ENV PATH /go/bin:/usr/local/go/bin:$PATH
ENV GOPATH /go
ENV USER root

COPY . /go/src/github.com/cloudflare/cfssl

RUN buildDeps=' \
		go \
		git \
		gcc \
		libc-dev \
		libtool \
		libgcc \
	' \
	set -x && \
	apk update && \
	apk add $buildDeps && \
	cd /go/src/github.com/cloudflare/cfssl && \
	go get github.com/GeertJohan/go.rice/rice && rice embed-go -i=./cli/serve && \
	cp -R /go/src/github.com/cloudflare/cfssl/vendor/github.com/cloudflare/cfssl_trust /etc/cfssl && \
	go build -o /usr/bin/cfssl ./cmd/cfssl && \
	go build -o /usr/bin/cfssljson ./cmd/cfssljson && \
	go build -o /usr/bin/mkbundle ./cmd/mkbundle && \
	go build -o /usr/bin/multirootca ./cmd/multirootca && \
	apk del $buildDeps && \
	rm -rf /var/cache/apk/* && \
	rm -rf /go && \
	echo "Build complete."
RUN whereis cfssl

RUN groupadd -r cfssl -g 433 && \
    useradd -u 431 -r -g cfssl -d /opt/cfssl -s /sbin/nologin -c "CFSSL daemon account" cfssl && \
    mkdir -p /opt/cfssl && \
    chown -R cfssl:cfssl /opt/cfssl

COPY entrypoint.sh /tmp/entrypoint.sh
RUN chown -R cfssl:cfssl chown -R cfssl:cfssl && \
    chmod +x /tmp/entrypoint.sh

USER cfssl
WORKDIR /opt/cfssl

COPY ./config/ca.json /opt/cfssl/ca.json
COPY ./config/config.json /opt/cfssl/config.json

#Initialize the CA cert & key
RUN cfssl genkey  -initca /opt/cfssl/ca.json | cfssljson -bare ca


CMD ["/tmp/entrypoint.sh"]
