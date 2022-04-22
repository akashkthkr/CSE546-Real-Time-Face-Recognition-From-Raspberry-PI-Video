# Real Time Face Recognition Service From Raspberry PI Captured Video

## Motivation

We will build a **distributed application** that utilizes PaaS services and IoT devices to perform real-time **face recognition** on real videos recorded by the devices.

Specifically, we will develop this application using **Amazon Lambda** based **PaaS** and **Raspberry Pi based IoT**. **Lambdas** is the first and the most widely used **Function as a Service PaaS.** 

Raspberry Pi is the most widely used IoT development platform. This project will provide you with experience in developing **real-world, IoT data driven cloud applications**.

## Description
### High-level Architecture
The Raspberry Pi records the videos using its attached camera. The cloud performs face recognition on the collected videos, looks up the recognized students in the database, and returns the relevant academic information of each recognized student back to the user. 

### 1. Edge (using Raspberry Pi)
Your program on the Pi should continuously record videos and send them to the cloud. The program should receive the output from the cloud for each recognized person in the videos and output the person’s name and academic information in the following format: 

The #NUMBER person recognized: NAME, MAJOR, YEAR.

To evaluate the performance of your app, your program on the Pi should also report the response time (see Testing) of every request in the following format: 

Latency: X.XX seconds.

Suggestions:
### 1) Install the OS on Raspberry Pi. Refer to: https://docs.google.com/document/d/1MaHuP5qyA29oy2vhYwPEdCB6vR5qJtOu5nQp2tVIJaM/edit?usp=sharing

### 2) Use the camera on Raspberry Pi. Refer to: https://docs.google.com/document/d/1PFTHat0wToYxTvkffI29EnksyHyGUPMKTP3-HjNd45Q/edit?usp=sharing
	
### 3) To measure latency, you can measure the time between when a face is recorded by the camera and when the student’s academic information is returned to the Pi. You can use the “time” package.

Example python snippet:
**Import time**
**start_time = time.time()**

**……..**

**latency = time.time() - start_time**

**print("Latency: {:.2f} seconds.".format(latency))**





## Acknowledgements
### Team Members Group 11:
[Akash Kant](https://github.com/akashkthkr), (akant1)

[Ayush Kalani](https://github.com/ayushkalani), (akalani2)

[Nakul Vaidya](https://github.com/NakulVaidya), (nvaidya7)
