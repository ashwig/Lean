#!/usr/bin/env bash

# Fetch the changes
git fetch upstream

# checkout master
git checkout master

git merge upstream/master

