#!/bin/bash
cd /home/azureuser/groupwork/src
export $(grep -v '^#' .env)
../venv/bin/python3 report_to_blob.py