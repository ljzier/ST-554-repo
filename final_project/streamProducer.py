# Linda Zier
# ST 554
# Final Project
# 4/29/2026

# This file was created as a companion file to Zier_ST_554_Final_Project.ipynb

import pandas as pd
import time
import os

# read in the data file we'll use to mimic streaming data
streamFile = pd.read_csv("data/power_streaming_data.csv")

# loop 20 times
for i in range(10): 
    # sample 5 rows
    sample = streamFile.sample(n=5)
    
    # write to the streaming data folder
    sample.to_csv(f"streaming_data/batch_{i}.csv", index = False)
    
    print(f"BATCH {i} WRITTEN")
    
    # pause 10 seconds
    time.sleep(10)
    
for s in spark.streams.active:
    s.stop()