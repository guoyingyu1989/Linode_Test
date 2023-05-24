# Linode_Test
This is just a personal hobby of creating codes.

_________________
## Linode_creation.py
This script is to specify the CPU while creating a VM on linode. i.e. *I don't want AMD EPYC 7601 32-Core Processor, but a 7713 model.*
It's a bit embarrasing to create linode VMs with specific CPU model, while they offer many CPU types. Can take a lot of time in **TryingYourLuck**.
So I created this script.

This code a pretty ugly as the VM provisioning -> booting -> actual running would usually take some time. So you can see there's a `sleep()`, which is never a good method to use.
You're welcomed to help optimize this code. Be positive.

when specifying the linode VM type, please use `linode-cli` as downloaded from Linode official site. 
Run command:
``` bash
linode-cli linodes types
```
you will get an output similiar to this:
![image](https://github.com/guoyingyu1989/Linode_Test/assets/52042057/8a060229-bf0c-40d1-99d6-d968a21f1a5b)

It is perfectly matched with the pricing list as in their official site. Just make sure you choose the right types.
![image](https://github.com/guoyingyu1989/Linode_Test/assets/52042057/cca6d983-5ee1-4e36-8151-14996c23fa8a)

As I'm only taking a screenshot as an example, the price might change as time goes on. Please verify yourself about the price at https://www.linode.com/pricing/
