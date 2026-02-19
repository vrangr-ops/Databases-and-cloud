**Deployment models of cloud**  
![41b25c6277dd5e77f1a39832b6f2749e.png](images/41b25c6277dd5e77f1a39832b6f2749e.png)

**Types of cloud computing**  
![211c3a82eabdd0d4b6b621a48602d170.png](images/211c3a82eabdd0d4b6b621a48602d170.png)

* * *

## Launching an EC2 instance in VM

- \*The section below concerns the configuration setting for an EC2 instance.

<div class="joplin-table-wrapper"><table border="1" style="border-collapse: collapse; width: 100.008%;" class="jop-noMdConv"><colgroup class="jop-noMdConv"><col style="width: 49.9587%;" class="jop-noMdConv"><col style="width: 49.9587%;" class="jop-noMdConv"></colgroup><thead class="jop-noMdConv"><tr class="jop-noMdConv"><th scope="col" class="jop-noMdConv"><p><span class="jop-noMdConv" style="color: rgb(255, 255, 255);"><span style="font-weight: bolder;" class="">Name</span></span></p><ul style="font-weight: 400;" class="jop-noMdConv"></ul></th><th scope="col" class="jop-noMdConv"><span style="font-weight: 400; background-color: rgb(16, 21, 26);" class="">Follow an appropriate convention. e.g. organization-name-project title.</span></th></tr></thead><tbody class="jop-noMdConv"><tr class="jop-noMdConv"><td class="jop-noMdConv"><span style="font-weight: bold;" class="">Application and OS Images</span></td><td class="jop-noMdConv"><p>Select ubuntu LTS image 64bit x86.</p></td></tr><tr class="jop-noMdConv"><td class="jop-noMdConv"><span style="font-weight: bolder; background-color: rgb(16, 21, 26);" class="">Instance type</span></td><td class="jop-noMdConv"><p>t3 micro</p></td></tr><tr class="jop-noMdConv"><td class="jop-noMdConv"><span style="font-weight: bolder;" class="">Select SSH key</span></td><td class="jop-noMdConv">See comments section below</td></tr><tr class="jop-noMdConv"><td class="jop-noMdConv"><p><strong class="jop-noMdConv">Network</strong></p><p><em class="jop-noMdConv">Configure security group by selecting <mark class="jop-noMdConv">edit</mark> option.</em></p></td><td class="jop-noMdConv"><p>Name security group. e.g. organization-name-project-sg</p><ul class="jop-noMdConv"><li class="jop-noMdConv">SSH, source type =custom, source =0.0.0.0/0, port range= 22</li><li class="jop-noMdConv">Custom TCP, source type =custom, source =0.0.0.0/0, port range =3000</li><li class="jop-noMdConv">HTTP, source type =custom, source =0.0.0.0/0, port range =80</li></ul></td></tr><tr class="jop-noMdConv"><td class="jop-noMdConv"><span style="font-weight: bolder;" class="">Configure storage</span></td><td class="jop-noMdConv"><ul class="jop-noMdConv"><li class="jop-noMdConv">1Gb,Gp3</li></ul></td></tr></tbody></table></div>

**With the setting above the EC2 instance can be launched.**

* * *

## Connecting to EC2 via SSH

\*Prerequisites - have SSH client e.g. Gitbash installed if using widows.

https://git-scm.com/install/

1.  Open an SSH client. Ensure directory is in /.ssh folder
2.  Navigate to connect to instance
3.  ![](https://github.com/vrangr-ops/App-development/blob/main/_resources/08bfc33ab14cc25a8526c23b68825038.png)
4.  Select SSH connection
5.  `run chmod 400 "se-name-key-pair.pem"`
6.  Run command
7.  `ssh -i "se-name-key-pair.pem" ubuntu@ec2-3-255-106-70.eu-west-1.compute.amazonaws.com`

* * *

## Installing nginx

Use Bash terminal (gitbash)

### Update packages

`Sudo apt update -y`

### Upgrade packages

`sudo apt upgrade -y`

* * *

## Install nginx

1.  `sudo apt install nginx -y`
2.  `sudo systemctl restart nginx`
3.  `sudo systemctl status nginx`

\# enable nginx - to make it start up on boot

- `sudo systemctl enable nginx`
- Test HTTP connectionddd  
    \-- To check connection navigate to web browser and type the public IP address with the HTTP prefix

* * *

# S3 Buckets

Amazon Simple Storage Service (S3), buckets are the fundamental containers used to store, organize, and manage data as "objects".

## **Key Characteristics**

- **Logical Containers**: A bucket acts like a root folder for your data, but S3 uses a flat object-based storage structure rather than a traditional hierarchical file system.
- **Globally Unique Names**: Bucket names must be unique across all of AWS globally, meaning no two AWS accounts can have a bucket with the same name.
- **Regional Placement**: When you create a bucket, you choose a specific AWS Region to store its data. This helps minimize latency and manage storage costs.
- **Unlimited Capacity**: You can store a virtually unlimited number of objects in a single bucket. Individual objects can range from 0 bytes up to **5 TB** in size.

## **Core Features**

- **Versioning**: This can be enabled to preserve every version of an object, protecting against accidental deletions or overwrites.
- **Access Control**: Security is managed at the bucket level through **Bucket Policies** (JSON-based rules) or **Access Control Lists (ACLs)** to define who can read or write data.
- **Storage Classes**: You can assign different s3 storage classes (e.g., Standard, Infrequent Access, or Glacier) to objects within a bucket to optimize costs based on how often the data is accessed.
- **Replication**: Buckets can be configured to automatically replicate objects to other buckets in the same or different regions for disaster recovery.

**Common Use Cases**

- **Data Lakes**: Storing massive amounts of raw data for big data analytics.
- **Backup & Restore**: Providing durable, long-term storage for critical backups and disaster recovery.
- **Static Website Hosting**: Hosting frontend layers (HTML, CSS, JS) directly from a bucket without needing a web server.
- **Media Hosting**: Storing and distributing images, videos, and music files for applications.

S3 file structure  
![bf79f93f6f73c62fa7992bc39f4720f5.png](images/bf79f93f6f73c62fa7992bc39f4720f5.png)  
adds prefixes to simulate file strucure/hiaracy

![95cf53be9b6d59cfedc300c49830b489.png](images/95cf53be9b6d59cfedc300c49830b489.png)



