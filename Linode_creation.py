import linode_api4 
import paramiko
import datetime
import time

client = linode_api4.LinodeClient('<Your API TOKEN>‘)
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def create_vm():
    new_linode, root_password  = client.linode.instance_create(
        ltype="g6-dedicated-2",
        region="eu-central",
        image="linode/ubuntu22.04", 
    )
    
    host = new_linode.ipv4[0]
    username = 'root'
    password = root_password
    port = '22'
    vm = (host, port, username, password,new_linode)
    return vm


def check_cpu(vm):
    time.sleep(240)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(vm[0], vm[1], vm[2], vm[3])
    stdin, stdout, stderr = ssh.exec_command("grep 'model name' /proc/cpuinfo")
    for line in stdout:
        cpu_model = line[22:26]
    print(cpu_model)
    return cpu_model


def delete_vm(vm):
    vm[4].delete()

vm = create_vm()
cpu_model = check_cpu(vm)


while cpu_model != 7713:
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(vm[0],end='\n')
    print(current_time)
    delete_vm(vm)
    vm = create_vm()
    cpu_model = check_cpu(vm)
