# ILLUMIO take-home submission

Assumptions and a few explanations (important):

- The only supported versions are 2 & 3, but support for other versions won't take much effort.&nbsp;
- The whole process of extracting is done for both ACCEPT and REJECT status.&nbsp;
- The lookup table CSV and the flow logs text file are supposed to be formatted without blank lines in between them and in the default format.&nbsp;
- The tag_counts.csv stores all the tag count information.&nbsp;
- The port and protocol combinations extracted are for the dstport and srcport in different files i.e dst/srcport_protocol_counts.csv (if needed can be combined too.)&nbsp;
- The protocol.py stores a map with a list of all protocol numbers mapped to keywords ex: 6->TCP (later converted to tcp for case matching)&nbsp;

Name of the file to store lookup table = lookup_table.csv&nbsp;
Name of the file to store flow logs = flow_logs.txt&nbsp;

All files are in 1 folder and the only library used is csv. Note: Keep the protocol.py in the same dir as it is required to map from protocol number to keyword.&nbsp;

Run main.py to run the whole code!&nbsp;
