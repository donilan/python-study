#!/usr/bin/env bash

if [ -e ./env ] ; then
    source ./env/bin/activate
fi
pip install -r requirements.txt -i http://pypi.douban.com/simple
