FROM amazon/aws-lambda-python:3.8

# Copy function code

COPY eval_face_recognition.py ${LAMBDA_TASK_ROOT}
COPY build_custom_model.py ${LAMBDA_TASK_ROOT}
COPY models ${LAMBDA_TASK_ROOT}/models
COPY checkpoint ${LAMBDA_TASK_ROOT}/checkpoint
COPY handler.py ${LAMBDA_TASK_ROOT}
# Install the function's dependencies using file requirements.txt
# from your project folder.

# COPY install_requirements.sh ${LAMBDA_TASK_ROOT}
# RUN chmod +x ${LAMBDA_TASK_ROOT}/install_requirements.sh
RUN pip3 install torch==1.10.2+cpu torchvision==0.11.3+cpu torchaudio==0.10.2+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html --target "${LAMBDA_TASK_ROOT}"
RUN pip3 install pillow
RUN pip3 install requests
RUN pip3 install numpy

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "handler.face_recognition_handler" ]