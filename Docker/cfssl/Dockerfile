FROM cfssl/cfssl
RUN apt-get update && \
    apt-get -y install python2.7 python-pip && \
    pip install awscli && \
    apt-get clean && \
    groupadd -r cfssl -g 433 && \
    useradd -u 431 -r -g cfssl -d /opt/cfssl -s /sbin/nologin -c "CFSSL daemon account" cfssl && \
    mkdir -p /opt/cfssl && \
    chown -R cfssl:cfssl /opt/cfssl

COPY entrypoint.sh /tmp/entrypoint.sh
RUN chmod +x /tmp/entrypoint.sh

USER cfssl
WORKDIR /opt/cfssl

RUN cfssl \
        genkey \
        -initca /opt/cfssl/ca.json | cfssljson ca


CMD ["/tmp/entrypoint.sh"]