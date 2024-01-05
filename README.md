Training Guide

Use Python 3.9, due to a bug in `fairseq`. Install all dependencies with `pip install 'vocos[train]'`.

First training, it will automatically download models from Huggingface. See the file `metrics/UTMOS.py`.

Please resample the audio files prior to training.

Run `python -m genlist` to generate train / valid file list.

Run `python train.py -c configs/vocos.yaml` to train the model.
