FROM nvcr.io/nvidia/l4t-base:r32.3.1

#RUN apt-get install dialog apt-utils -y

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     libavcodec-dev \
#     libavformat-dev \
#     libavutil-dev \
#     #libeigen3-dev \
#     #libglew-dev \
#     #libtiff5-dev \
#     libjpeg-dev \
#     libpng-dev \
#     #libpostproc-dev \
#     #libswscale-dev \
#     libtbb-dev \
#     #libgtk2.0-dev \
#     #libxvidcore-dev \
#     #libx264-dev \
#     #pkg-config \
#     #zlib1g-dev \
#     && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    #python-dev \
    python-pip \
    python-numpy \
    #python-py \
    #python-pytest \
    python-opencv \
    python-opencv-apps \
    python-paho-mqtt \
    libcanberra-gtk-module \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    #python3-dev \
    python3-pip \
    python3-numpy \
    #python3-py \
    #python3-pytest \
    python3-opencv \
    libcanberra-gtk3-module \
    python3-paho-mqtt \
    mosquitto-clients \
    #libopencv-python \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# GStreamer support
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y  \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY face_detect.py /media/code/
COPY haarcascade_frontalface_default.xml /media/code/

WORKDIR /media/code
CMD ["./face_detect.py"]

