#!/usr/bin/env python3.6
# coding: utf-8

import pandas as pd

df = pd.read_csv('../data/raw/data_input.csv', encoding='latin1')

df.to_csv('../data/processed/output.csv', index=False)