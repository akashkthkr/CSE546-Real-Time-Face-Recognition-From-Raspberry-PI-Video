FROM amazon/aws-lambda-python:3.8

# Copy function code


# Install the function's dependencies using file requirements.txt
# from your project folder.

# COPY install_requirements.sh ${LAMBDA_TASK_ROOT}
# RUN chmod +x ${LAMBDA_TASK_ROOT}/install_requirements.sh
# COPY requirements.txt  .
RUN pip3 install -r requirements.txt
RUN pip3 install torch==1.10.2+cpu torchvision==0.11.3+cpu torchaudio==0.10.2+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html --target "${LAMBDA_TASK_ROOT}"
#RUN pip3 install requests
#RUN pip3 install numpy
#RUN pip3 install pillow
#RUN pip3 install requests

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)


# Define global args
# ARG FUNCTION_DIR="/tmp/"
# ARG FUNCTION_DIR=${LAMBDA_TASK_ROOT}
ARG FUNCTION_DIR="/home/app/"
ARG RUNTIME_VERSION="3.8"
ARG DISTRO_VERSION="3.12"

# Stage 1 - bundle base image + runtime
# Grab a fresh copy of the image and install GCC
FROM python:${RUNTIME_VERSION} AS python-alpine
# Install GCC (Alpine uses musl but we compile and link dependencies with GCC)
#RUN apk add --no-cache \
#    libstdc++

RUN apt-get update \
    && apt-get install -y cmake ca-certificates libgl1-mesa-glx
RUN python${RUNTIME_VERSION} -m pip install --upgrade pip

# Stage 2 - build function and dependencies
FROM python-alpine AS build-image
# Install aws-lambda-cpp build dependencies
#RUN apk add --no-cache \
#    build-base \
#    libtool \
#    autoconf \
#    automake \
#    libexecinfo-dev \
#    make \
#    cmake \
#    libcurl
# Include global args in this stage of the build
ARG FUNCTION_DIR
ARG RUNTIME_VERSION
# Create function directory
RUN mkdir -p ${FUNCTION_DIR}

# Optional – Install the function's dependencies
# RUN python${RUNTIME_VERSION} -m pip install -r requirements.txt --target ${FUNCTION_DIR}
# Install Lambda Runtime Interface Client for Python
RUN python${RUNTIME_VERSION} -m pip install awslambdaric --target ${FUNCTION_DIR}

# Stage 3 - final runtime image
# Grab a fresh copy of the Python image
FROM python-alpine
# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}
# Copy in the built dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}
# (Optional) Add Lambda Runtime Interface Emulator and use a script in the ENTRYPOINT for simpler local runs
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
RUN chmod 755 /usr/bin/aws-lambda-rie

# Install ffmpeg
RUN apt-get install -y ffmpeg

# Copy handler function
COPY requirements.txt ${FUNCTION_DIR}
RUN python${RUNTIME_VERSION} -m pip install -r requirements.txt --target ${FUNCTION_DIR}
COPY entry.sh /

# Copy function code
COPY handler.py ${FUNCTION_DIR}
RUN chmod 777 /entry.sh

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
# CMD [ "handler.handler" ]
ENTRYPOINT [ "/entry.sh" ]
CMD [ "handler.face_recognition_handler" ]
