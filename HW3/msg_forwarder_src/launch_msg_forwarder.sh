#!/usr/bin/env bash

sudo docker run -it --rm --net=host --network hw03 --runtime nvidia -v /tmp/.X11-unix/:/tmp/.X11-unix -v"$PWD":/msg_forwarder_src  msg_forwarder:latest
