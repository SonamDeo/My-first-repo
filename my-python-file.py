services = "EC2,S3,RDS,Lambda"

service_list = services.split(",")

for service in service_list:
    print(service)
