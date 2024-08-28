# ILLUMIO take-home submission

Assumptions and few explanations (important):

- The only versions that are supported are 2 & 3 but support for other versions wont take much effort.&nbsp;
- The whole process of extracting is done for both ACCEPT and REJECT status.&nbsp;
- The lookup table csv and the flow logs text file is supposed to be formatted without blank lines in between them and in default format.&nbsp;
- The tag_counts.csv stores all the tag counts information.&nbsp;
- The port and protocol combinations extracted is for the dstport and srcport in different files i.e dst/srcport_protocol_counts.csv (if needed can be combined too.)&nbsp;
- The protocol.py stores a map with a list of all protocol number mapped to keywords ex: 6->TCP (later converted to tcp for case matching)&nbsp;

Name of the file to store lookup table = lookup_table.csv&nbsp;
Name of the file to stor flow logs = flow_logs.txt&nbsp;

All files are in 1 folder and only library used is csv. Note: Keep the protocol.py in the same dir as it is required to map from protocol number to keyword.&nbsp;

Run main.py to run the whole code!&nbsp;
