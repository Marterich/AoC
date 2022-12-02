#! /usr/bin/env python3
bin_data = bin(int(open("example1.txt","r").readline(),16))[2:]
#print(bin_data[:3])
packet_version = int(bin_data[:3],2)
#print(bin_data[3:6])
packet_id = int(bin_data[3:6],2)
#print(bin_data[6:11])
packet_a = bin_data[6:11]
#print(bin_data[11:16])
packet_b = bin_data[11:16]
#print(bin_data[16:21])
packet_c = bin_data[16:21]

literal_value = "".join([packet_a,packet_b,packet_c])
print(f"{packet_version=}\n{packet_id=}\n{literal_value=}")
