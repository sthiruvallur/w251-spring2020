# Pipeline for Face detection from the Edge to cloud

## Pipeline to achieve
![alt text](https://github.com/sthiruvallur/w251-spring2020/blob/3ea98473c5887e944bd26ab0324fc0f2a253e8e4/HW3/end_to_end_workflow.png "End to End workflow")

## Steps to set up the pipeline
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

The cloud image persister is a docker container based on ubuntu. This process to persist will connect only to the cloud broker and will listen to the topic *persist_faces*. Upon receipt of the message, it will write to a S3 bucket via a shared volume.

#### Face detector src

```
  cd face_detector_src
  ./build_docker_image.sh
  ./launch_nvidia_container.sh 
```

Face detector is then launched on the Jetson TX2. It uses the Open CV library to detect faces from a web cam's live stream. The faces are then seriarlized to binary data and published to local broker on topic 'detect_faces' 

The face detector source requires to be run in a priviliged container, which will require user authentication to accord appropriate access

With the pipeline set up complete, the images should be persisted on S3 Cloud object store such as [S3 object url](https://cloud.ibm.com/objectstorage/crn%3Av1%3Abluemix%3Apublic%3Acloud-object-storage%3Aglobal%3Aa%2F326c3ee185184be698c4e12a96575777%3A2c613095-e2c4-4dda-8314-8e1022dc4694%3A%3A?paneId=manage)
