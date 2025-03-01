#!/bin/bash
conda env create -f ./dotfiles-installer.yml
conda activate dotfiles-installer
python py-install.py
