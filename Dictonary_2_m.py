
# ec2_instance = {
#     "id" : "Oabcd1234",
#     "ip" : "t3.medium",
#     "status" : "running",
#     "tags": {"Name": "Production-Web-Server"}
#     }

# fleet = [
#     {
#     "id" : "S3",
#     "ip" : "172.16.0.29",
#     "status" : "running",
#     },
#     {
#     "id" : "EC2",
#     "ip" : "172.16.0.24",
#     "status" : "stooped",
#     },
#     {
#     "id" : "RDS",
#     "ip" : "172.16.0.50",
#     "status" : "running",
#     },
#     {
#     "id" : "WEB",
#     "ip" : "172.16.0.99",
#     "status" : "stooped",
#     },
# ]

# server_name = ec2_instance["tags"]["Name"]
# print(f"The server Name is: {server_name}")

# for server in fleet:
#     if server["status"] == "stooped":
#         print(f"WARNING: server {server['id']} with ip: {server['ip']} is stooped!!!")



# server = {
#     "hostname": "Web-Prod-01",
#     "status": "active",
#     "network": {
#         "ip": "10.0.0.57",
#         "dns": "8.8.8.8",
#         "secondary_dns": "1.1.1.1",
#         "subnet": "255.255.255.0",
#         "getway": "10.0.0.1"
#     }
# }

# server_ip = server["network"]["ip"]
# server_dns = server["network"]["dns"]

# print(f"The IP address is : {server_ip}")
# print(f"The dns server to IP address {server_ip} is: {server_dns} ")

server = {
    "hostname": "Web-Prod-01",
    "network": {"ip": "10.0.0.23"}
}

fleet = [
    {
    "hostname": "Web-01",
    "network": {"ip": "10.0.0.196"}
},
{
    "hostname": "Web-02",
    "network": {"ip": "10.0.0.71"}
},
{
   "hostname": "DNS-Server",
   "network": {"ip": "10.0.0.239"}
}
]

target_ips = ["10.0.0.139","10.0.0.71","10.0.0.2","10.0.0.7","192.168.41.95",]
print("---Starting Scan Network---")

for server_info in fleet:
    current_ip = server_info["network"]["ip"]
    if current_ip in target_ips: 
      print(f"The IP address to {server_info['hostname']} is {current_ip}")
    else:
       print(f"Skipping {server_info['hostname']}...")




       csdcsdcsdsdsdcsdc