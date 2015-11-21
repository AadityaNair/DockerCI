FROM ubuntu:precise

#install syslibs needed
RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install libssl-dev swig python-dev curl git -y

# install pip
RUN curl --silent --show-error --retry 5 https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python2.7

# mount the current project workspace under /project inside the container
ADD . /project

# install pip dependencies!
RUN pip install -r /project/requirements/dev.txt
RUN rm -rf /project

WORKDIR /project
CMD pip install -r /project/requirements/dev.txt && nosetests --with-xunit  --traverse-namespace --with-xcoverage --cover-package=encryptor --cover-html -v

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
