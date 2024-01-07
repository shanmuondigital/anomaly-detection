import os
from pathlib import Path


folder = Path("/Users/shanmu/Library/CloudStorage/OneDrive-NortheasternUniversity/MPS Analytics/Quarter 3 - Spring 2023/ALY 6080/XN-Project/Working/logs_202212/20221201")
file = folder/"log_envelopes_202212010000.log"

f = open(file, "r")

for line in f:
    linestrip = line.strip().split(",")
    # print(linestrip.split(","))
    timeStamp = linestrip[0]
    sourceOfEnvelope = linestrip[1]
    eventId = linestrip[2]
    print(linestrip)


f.close()
