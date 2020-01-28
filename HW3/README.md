# Pipeline for Face detection from the Edge to cloud

## Steps to replicate the workflow
   The brokers on cloud and jetson will be instantiated first so that the bridge is activated
   
   Pls review the bridge configs under jetson_broker_src and cloud_broker for details on bridge setup.
   
   Listing the steps below to instantiate the necessary containers in the appropriate order

#### Mosquitto broker on Jetson TX2

```
  cd jetson_broker_src
  ./build_docker_image.sh (to build Docker image for the first time)
  ./run_container.sh      (to launch the container)
```

#### Cloud broker 

```
  cd cloud_broker
  ./build_docker_image.sh (to build Docker image for the first time)
  ./run_container.sh
```

  The msg forwarder on Jetson will subscribe to the topic 'detect_faces' on Jetson broker and will forward these images to Cloud broker using the topic 'persist_faces'  


#### Msg forwarder on Jetson TX2

```
  cd msg_forwarder_src
  ./build_docker_image.sh (to build Docker image for the first time)
  ./run_container.sh      (to launch the container)
```


#### Cloud image persister

```
  cd cloud_persist_msg
  ./build_docker_image.sh
  ./run_container.sh
```

#### Face detector src

```
  cd face_detector_src
  ./build_docker_image.sh
  ./launch_nvidia_container.sh 
```

The face detector source requires to be run in a priviliged container, this will require user authentication to accord appropriate access
