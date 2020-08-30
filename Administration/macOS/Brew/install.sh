#!/bin/bash

# Install Packages
for i in $(cat packages.txt); do brew install -f $i;done

# Install Casks
for i in $(cat casks.txt); do brew cask install $i --force; done
