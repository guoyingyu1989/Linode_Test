import requests
import time
import os

# Set your Linode API access token
ACCESS_TOKEN = "YOUR_API_TOKEN"

# Set deployment parameters
region = "us-iad"  # Replace with your desired region
image = "linode/ubuntu22.04"  # Replace with your desired Ubuntu image
label = "TestCodeInstance"  # Replace with your desired label
root_pass = "YourRootPassword,./"  # Replace with your desired root password
type = "g6-dedicated-2"  # Replace with your desired instance type
desired_cpu_version = "EPYC 7713"  # Replace with your desired CPU version

# Provision 10 instances with desired CPU model
counter = 0 #initial counter
while counter < 10: #condition for 10 instances to be provisioned
    print(f"Provisioning instance {counter}...")

    # Create the Linode instance
    create_instance_payload = {
        "label": f"{label}{counter}",
        "image": image,
        "type": type,
        "region": region,
        "root_pass": root_pass,
        "booted": True
    }

    create_instance_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    create_instance_response = requests.post(
        "https://api.linode.com/v4/linode/instances",
        json=create_instance_payload,
        headers=create_instance_headers
    )

    # Extract the Linode instance ID from the response
    instance_id = create_instance_response.json().get("id")

    # Wait for the Linode instance to be running
    while True:
        instance_status_response = requests.get(
            f"https://api.linode.com/v4/linode/instances/{instance_id}",
            headers=create_instance_headers
        )

        instance_status = instance_status_response.json().get("status")

        if instance_status == "running":
            break
        #let the linode instance done all the initial setup
        time.sleep(150)

    # Get the Linode instance IP address
    instance_ip = instance_status_response.json().get("ipv4")[0]

    # SSH into the Linode instance and check the CPU version
    ssh_command = f"sshpass -p '{root_pass}' ssh -o StrictHostKeyChecking=no root@{instance_ip} lscpu"
    cpu_version = os.popen(ssh_command).read()

    # Compare the CPU version
    if desired_cpu_version in cpu_version:
        print(f"Ubuntu server on Linode {instance_id} has the desired CPU version: {desired_cpu_version}")
        counter += 1
    else:
        print(f"Ubuntu server on Linode {instance_id} does not have the desired CPU version. Current CPU version: {cpu_version}")
        print(f"Deleting Linode {instance_id}...")
        delete_instance_response = requests.delete(
            f"https://api.linode.com/v4/linode/instances/{instance_id}",
            headers=create_instance_headers
        )
