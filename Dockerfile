FROM kushalsingh007/proxy_ubuntu:v1

MAINTAINER Kushal Singh "kushal.spiderman.singh@gmail.com"

ENV http_proxy "http://proxy.iiit.ac.in:8080"
ENV https_proxy "https://proxy.iiit.ac.in:8080"

# Update aptitude with new repo
RUN apt-get update

# Install software 
RUN apt-get install -y git

# Make ssh dir
RUN mkdir /root/.ssh/

# Copy over private key, and set permissions
ADD id_rsa /root/.ssh/id_rsa

# Create known_hosts
RUN touch /root/.ssh/known_hosts

# Clone the conf files into the docker container
RUN git clone https://github.com/AadityaNair/DockerCI
