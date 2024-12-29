#!/bin/bash

cd /home/ec2-user/python-quart-dummy-api/quart-apis

source quart-env/bin/activate

hypercorn -k asyncio -b 0.0.0.0:5000 app:app