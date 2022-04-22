# Real Time Face Recognition Service From Raspberry PI Captured Video
[![License](https://img.shields.io/github/license/qcenergy/qudra.svg?style=popout-square)](https://opensource.org/licenses/Apache-2.0)

## Motivation

We will build a **distributed application** that utilizes PaaS services and IoT devices to perform real-time **face recognition** on real videos recorded by the devices.

Specifically, we will develop this application using **Amazon Lambda** based **PaaS** and **Raspberry Pi based IoT**. **Lambdas** is the first and the most widely used **Function as a Service PaaS.** 

Raspberry Pi is the most widely used IoT development platform. This project will provide you with experience in developing **real-world, IoT data driven cloud applications**.

## Description
### High-level Architecture
The Raspberry Pi records the videos using its attached camera. The cloud performs face recognition on the collected videos, looks up the recognized students in the database, and returns the relevant academic information of each recognized student back to the user. 

![alt text](https://github.com/akashkthkr/CSE546-Real-Time-Face-Recognition-From-Raspberry-PI-Video/blob/main/README_images/Description_Design.png?raw=true)


### 1. Edge (using Raspberry Pi)
Your program on the Pi should continuously record videos and send them to the cloud. The program should receive the output from the cloud for each recognized person in the videos and output the person’s name and academic information in the following format: 

To evaluate the performance of your app, your program on the Pi should also report the response time (see Testing) of every request in the following format: 

Latency: X.XX seconds.

Suggestions:
#### 1) Install the OS on Raspberry Pi. Refer to: https://docs.google.com/document/d/1MaHuP5qyA29oy2vhYwPEdCB6vR5qJtOu5nQp2tVIJaM/edit?usp=sharing

#### 2) Use the camera on Raspberry Pi. Refer to: https://docs.google.com/document/d/1PFTHat0wToYxTvkffI29EnksyHyGUPMKTP3-HjNd45Q/edit?usp=sharing
	
#### 3) To measure latency, you can measure the time between when a face is recorded by the camera and when the student’s academic information is returned to the Pi. You can use the “time” package.

Example python snippet:
**Import time**
**start_time = time.time()**

**……..**

**latency = time.time() - start_time**

**print("Latency: {:.2f} seconds.".format(latency))**


### 2. Cloud (using AWS) 
The videos sent from the Pi should be stored in S3.

Your Lambda functions should perform the following tasks:
#### 1) Extract frames from the video (Alternatively, you can extract the frames using your program on the Pi).
#### 2) Recognize faces from the frames. To simplify your program, you can assume there is only one face in the videos (although the faces can change), and your application does recognition every 0.5 second.
#### 3) Fetch each reorganized student’s academic information, including name, major, and year (e.g., Sparky, Physics, Junior) from the database.
#### 4) Send the recognized student’s academic information to the edge.


**Implement different functionalities in different Lambda functions.**


## Testing
Test your code thoroughly. During testing, your team members can show your faces on the camera alternatively, and each of you should appear on the camera for at least 3 seconds.

#### 1) The videos are sent from the Pi to the cloud continuously;
#### 2) All the received videos in cloud are properly saved in S3;
#### 3) All the faces in the sent videos are recognized (every 0.5 second);
#### 4) The face recognition results are correct. More than 60% of the face recognition results are correct. Although some results are incorrect, they should be among your team members;
#### 5) The Lambda functions are autoscaled correctly;
#### 6) The student academic information is stored properly in DynamoDB;
#### 7) All the recognized students’ academic information is correctly returned to the Pi;
#### 8) The end-to-end latency (the time between when a face is recorded by the camera and when the student’s academic information is returned to the Pi) should be reasonably short.

## Installation

Our team's contribution is supposed to go into the `CSE546-Real-Time-Face-Recognition-From-Raspberry-PI-Video/` folder. So move there
```console
cd .
```


## Building from source

To build `CSE546-Real-Time-Face-Recognition-From-Raspberry-PI-Video` from source, pip install using:

```bash
git clone https://github.com/akashkthkr/CSE546-Real-Time-Face-Recognition-From-Raspberry-PI-Video.git
pip install --upgrade .
```

If you also want to download the dependencies needed to run optional tutorials, please use `pip install --upgrade .[dev]` or `pip install --upgrade '.[dev]'` (for `zsh` users).


#### Installation for Devs

If you intend to contribute to this project, please install `CSE546-Real-Time-Face-Recognition-From-Raspberry-PI-Video` in editable mode as follows:
```bash
git clone https://github.com/akashkthkr/CSE546-Real-Time-Face-Recognition-From-Raspberry-PI-Video.git
pip install -e .[dev]
```

python3 -m venv venv
. venv/bin/activate
Please use `pip install -e '.[dev]'` if you are a `zsh` user.

## AWS Details

### SSH Details Dummy

ssh -i "Akash_key.pem" ec2-user@ec2-3-86-234-121.compute-1.amazonaws.com

### Resources Used in AWS as Naming:
```python
AWS_S3_INPUT_BUCKET_NAME = ""

AWS_S3_OUTPUT_BUCKET_NAME = ""

AWS_LAMBDA_NAME = ""

AWS_DYNAMO_DB_NAME = ""

REGION_NAME = "us-east-1"

AWS_ACCESS_KEY_ID = "AAAAAAAAAAAAAAA"

AWS_ACCESS_KEY_SECRET = "BBBBBBBBBBBBBBBB"
```

### We have also loaded the script at startup of the instance on AMI load:

```bash
sudo yum update -y
sudo yum install git -y
echo export AWS_ACCESS_KEY_ID="AAAAAAAAAAAAAAA" >> /etc/profile
echo export AWS_SECRET_ACCESS_KEY="BBBBBBBBBBBBBBBB"" >> /etc/profile
git clone https://token@github.com/akashkthkr/CSE546-Real-Time-Face-Recognition-From-Raspberry-PI-Video
.git
```




## Acknowledgements
### Team Members Group 11:
[Akash Kant](https://github.com/akashkthkr), (akant1)

[Ayush Kalani](https://github.com/ayushkalani), (akalani2)

[Nakul Vaidya](https://github.com/NakulVaidya), (nvaidya7)
