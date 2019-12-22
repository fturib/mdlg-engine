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

Ensure you have a docker server running
Use the command `docker build --rm -f "Dockerfile" -t mdlg:latest "."`

## Launch the image

Use the command `docker run --rm -it -p 3000:3000/tcp mdlg:latest`
