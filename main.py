import csv
from protocol import protocol_map


lookup_dict = {}
tag_count = {}
srcport_protocol_count = {}
dstport_protocol_count = {}

def load_table():
    file = "lookup_table.csv"
    with open(file, mode='r') as f:
        dict = csv.DictReader(f)
        for row in dict:
            port = row['dstport']
            protocol = row['protocol'].lower()
            tag = row['tag']
            lookup_dict[(port, protocol)] = tag

def parse_dstport_protocol(line):
    parts = line.split()
    version = int(parts[0])
    if version == 2:
        srcport = parts[5]
        dstport = parts[6]
        protocol = protocol_map[int(parts[7])].lower()
    elif version == 3:
        srcport = parts[9]
        dstport = parts[10]
        protocol = protocol_map[int(parts[13])].lower()

    return srcport, dstport, protocol

def process_logs():
    file = "flow_logs.txt"
    with open(file, mode='r') as f:
        for line in f:
            srcport, dstport, protocol = parse_dstport_protocol(line.strip())
            if (dstport,protocol) in lookup_dict:
                tag = lookup_dict[(dstport,protocol)]
            else:
                tag = "Untagged"
            tag_count[tag] = tag_count.get(tag, 0) + 1
            
            dstport_protocol_count[(dstport,protocol)] = dstport_protocol_count.get((dstport,protocol), 0) + 1
            srcport_protocol_count[(srcport,protocol)] = srcport_protocol_count.get((srcport,protocol), 0) + 1

def write_tag_counts():
    with open("tag_counts.csv", mode='w', newline='') as file:
        write = csv.writer(file)
        write.writerow(['Tag', 'Count'])
        for tag, count in tag_count.items():
            write.writerow([tag, count])

def write_port_dstport_protocol():
    with open("dstport_protocol_counts.csv", mode='w', newline='') as file:
        write = csv.writer(file)
        write.writerow(['Port', 'Protocol', 'Count'])
        for port_protocol,count in dstport_protocol_count.items():
            write.writerow([port_protocol[0], port_protocol[1],count])

def write_port_srcport_protocol():
    with open("srcport_protocol_counts.csv", mode='w', newline='') as file:
        write = csv.writer(file)
        write.writerow(['Port', 'Protocol', 'Count'])
        for port_protocol,count in srcport_protocol_count.items():
            write.writerow([port_protocol[0], port_protocol[1],count])


if __name__ == "__main__":
    load_table()
    process_logs()
    write_tag_counts()
    write_port_dstport_protocol()
    write_port_srcport_protocol()

