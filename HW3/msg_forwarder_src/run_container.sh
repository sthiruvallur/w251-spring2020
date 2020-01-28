#!/usr/bin/env bash
docker run --name msg_forwarder \
--network hw03 \
--rm -ti \
msg_forwarder:latest
