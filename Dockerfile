# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
#FROM python:alpine

# If you prefer miniconda:
FROM continuumio/miniconda3

LABEL Name=mdlg-engine Version=0.0.1
EXPOSE 3000

WORKDIR /mdlg
ADD . /mdlg

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
RUN conda create -n dh_segment python=3.6
# WARNING: invokind "conda activate" do not work directly. Need to 'source' activate, and each Docker's "RUN" command ignore the env of the preceding, so you need to activate on each run/cmd
# create conda env for dhsegment (see https://dhsegment.readthedocs.io/en/latest/start/install.html)
# I prefer keep on version 0.5.0 of dhsegment (I am sure it is stable)
RUN /bin/bash -c ". activate dh_segment && \
    pip install git+https://github.com/dhlab-epfl/dhSegment@v0.5.0 && \
    conda install tensorflow=1.13.1 && \
    pip install better-exceptions && \
    pip install bottle"


# Run the REST API (bottle app) on port 3000
# we expect that the container will have a /data folder shared for getting images and models
CMD /bin/bash -c ". activate dh_segment && bottle.py -b 0.0.0.0:3000 --reload --debug server:app"
