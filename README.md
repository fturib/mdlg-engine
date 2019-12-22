# Mandlagore using dhSegment

@inproceedings{oliveiraseguinkaplan2018dhsegment,
  title={dhSegment: A generic deep-learning approach for document segmentation},
  author={Ares Oliveira, Sofia and Seguin, Benoit and Kaplan, Frederic},
  booktitle={Frontiers in Handwriting Recognition (ICFHR), 2018 16th International Conference on},
  pages={7--12},
  year={2018},
  organization={IEEE}
}

**Mandlagore** aims to extract the illuminations from the manuscripts

## Demo

Have a try at the [demo](https://dhsegment.readthedocs.io/en/latest/start/demo.html) to train (optional) and apply dhSegment in page extraction using the `demo.py` script.

## Build a Docker image

Use the command:

```bash
docker build --rm -f "Dockerfile" -t mdlg:latest "."
```

## Run the mdlg-engine container using the mdlg-data volume

Ensure you have a docker server running:

```bash
docker run --rm -it -p 3000:3000/tcp -v mdlg-data:/data  mdlg:latest
```

## Build the docker volume for the shared data with mdlg-engine

In fact, the volume is ceate with the first container using it.

```bash
docker volume rm mdlg-data
docker volume create mdlg-data
```

## initialize the volume with demo images/models

Run an Ubuntu container that share the same volume `mdlg-data`

```bash
docker run -it -v mdlg-data:/data --name mdlg-data-linux ubuntu /bin/bash
```

once you have the prompt of this container, download and expand the files for demo:

```bash
apt-get update
apt-get install unzip -y
apt-get install wget -y
cd /data/demo && wget https://github.com/dhlab-epfl/dhSegment/releases/download/v0.2/pages.zip && unzip pages.zip
cd /data/demo && wget https://github.com/dhlab-epfl/dhSegment/releases/download/v0.2/model.zip && unzip model.zip
```

Keep open this terminal, to be able to share data with the mdlg-engine container that run predictions and trainings.

## Call for execution of training on demo folder

```bash
# verify the server is up by calling the hello world
wget http://127.0.0.1:3000/hello

# run the training on default demo (files shared above)
wget http://127.0.0.1:3000/demo

# run your own training/prediction for the demo process. You need to initialize properly the volume
# -> below, will run the demo program on the folder 'whatever' of the mdlg-data volume
wget http://127.0.0.1:3000/demo/whatever
```
