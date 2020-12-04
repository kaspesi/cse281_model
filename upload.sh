#!/bin/bash
zip -9 bundle.zip lambda_function.py
cd ~/project/lib/python2.7/site-packages/
zip -r9 ~/project/bundle.zip *
cd ~/project/lib64/python2.7/site-packages/
zip -r9 ~/project/bundle.zip *
cd
aws s3 cp project/bundle.zip s3://opencvforlambda/opencv/bundle.zip