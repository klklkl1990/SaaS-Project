# Starting a linux image in aws
FROM amazonlinux:2

# Install Python
# OG: RUN yum install -y python37 && \
RUN yum install -y python37 && \
    yum install -y python3-pip && \
    yum install -y zip && \
    yum install -y unzip && \
    yum install -y numpy && \
    yum clean all

# Set up PIP and Venv
RUN python3 -m pip install mangum
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install virtualenv
RUN python3 -m venv base
RUN source base/bin/activate

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt -t ./python

# Zip it up for deployment. for the Docker container's entry point
RUN zip -r layer.zip ./python/
ENTRYPOINT ["/bin/bash", "-l"]