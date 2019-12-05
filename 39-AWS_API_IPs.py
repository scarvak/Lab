import requests

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
print (ip_ranges)
amazon = [item['ip_prefix'] for item in ip_ranges if item["service"] == "AMAZON"]
ec2_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "EC2"]
us_west_2 = [item['ip_prefix'] for item in ip_ranges if item["region"] == "us-west-2"]
us_east_1 = [item['ip_prefix'] for item in ip_ranges if item["region"] == "us-east-1"]

# print(aws_west)
# print(type(us_northwest))

ec2_us_west_2_ips = []

for ip in ec2_ips:
    if ip in us_west_2 or us_east_1:
        ec2_us_west_2_ips.append(ip)

amazon_ips = []

for ip in ec2_us_west_2_ips:
    if ip in amazon:
        amazon_ips.append(ip)

print ("\n".join(str(i) for i in ec2_us_west_2_ips))
print ("\n".join(str(i) for i in amazon_ips))

outfile = open("USWest-Public-Endpoints.txt", "w+")
print ("\n".join(str(i) for i in ec2_us_west_2_ips),file=outfile) # printing directly to a file
outfile.close

outfile = open("AWS-Public-Endpoints.txt", "w+")
print ("\n".join(str(i) for i in amazon_ips),file=outfile) # printing directly to a file
outfile.close


