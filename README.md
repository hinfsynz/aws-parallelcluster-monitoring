# ParallelCluster for Power Grid Simulation

## Cluster Main Page
![Cluster main page](docs/ClusterMainPage.png?raw=true "ParallelCluster for power grid simulation")

## Run Submission Page
![Run submission page](docs/RunSubmitPage.png?raw=true "Select a study system to run")
![Run submission succeed](docs/RunSubmitSucceed.png?raw=true "Run submitted")

## Job Status Monitoring
![Job pending](docs/JobPending.png?raw=true "Job pending after run submitted")
![Job in progress](docs/JobInProgress.png?raw=true "Job under execution on running nodes")


# Grafana Dashboard for AWS ParallelCluster (from aws-samples repo) 

This is a sample solution based on Grafana for monitoring various component of an HPC cluster built with AWS ParallelCluster.
There are 6 dashboards that can be used as they are or customized as you need.
* [ParallelCluster Summary](https://github.com/aws-samples/aws-parallelcluster-monitoring/blob/main/grafana/dashboards/ParallelCluster.json) - this is the main dashboard that shows general monitoring info and metrics for the whole cluster. It includes Slurm metrics and Storage performance metrics.
* [Master Node Details](https://github.com/aws-samples/aws-parallelcluster-monitoring/blob/main/grafana/dashboards/master-node-details.json) - this dashboard shows detailed metric for the Master node, including CPU, Memory, Network and Storage usage.
* [Compute Node List](https://github.com/aws-samples/aws-parallelcluster-monitoring/blob/main/grafana/dashboards/compute-node-list.json) - this dashboard show the list of the available compute nodes. Each entry is a link to a more detailed page.
* [Compute Node Details](https://github.com/aws-samples/aws-parallelcluster-monitoring/blob/main/grafana/dashboards/compute-node-details.json) - similarly to the master node details this dashboard show the same metric for the compute nodes.
* [GPU Nodes Details](https://github.com/aws-samples/aws-parallelcluster-monitoring/blob/main/grafana/dashboards/gpu.json) - This dashboard shows GPUs releated metrics collected using nvidia-dcgm container.
* [Cluster Logs](https://github.com/aws-samples/aws-parallelcluster-monitoring/blob/main/grafana/dashboards/logs.json) - This dashboard shows all the logs of your HPC Cluster. The logs are pushed by AWS ParallelCluster to AWS ClowdWatch Logs and finally reported here.
* [Cluster Costs](https://github.com/aws-samples/aws-parallelcluster-monitoring/blob/main/grafana/dashboards/costs.json)(beta / in developemnt) - This dashboard shows the cost associated to AWS Service utilized by your cluster. It includes: [EC2](https://aws.amazon.com/ec2/pricing/), [EBS](https://aws.amazon.com/ebs/pricing/), [FSx](https://aws.amazon.com/fsx/lustre/pricing/), [S3](https://aws.amazon.com/s3/pricing/), [EFS](https://aws.amazon.com/efs/pricing/).

## Quickstart
Create a cluster using [AWS ParallelCluster](https://www.hpcworkshops.com/03-hpc-aws-parallelcluster-workshop.html) and include the following configuration:

```ini
[cluster yourcluster]
...
post_install = https://raw.githubusercontent.com/aws-samples/aws-parallelcluster-monitoring/main/post-install.sh
post_install_args = https://github.com/aws-samples/aws-parallelcluster-monitoring/tarball/main,aws-parallelcluster-monitoring,install-monitoring.sh
additional_iam_policies = arn:aws:iam::aws:policy/CloudWatchFullAccess,arn:aws:iam::aws:policy/AWSPriceListServiceFullAccess,arn:aws:iam::aws:policy/AmazonSSMFullAccess,arn:aws:iam::aws:policy/AWSCloudFormationReadOnlyAccess
tags = {"Grafana" : "true"}
...
```

## AWS ParallelCluster
**AWS ParallelCluster** is an AWS supported Open Source cluster management tool that makes it easy for you to deploy and
manage High Performance Computing (HPC) clusters in the AWS cloud.
It automatically sets up the required compute resources and a shared filesystem and offers a variety of batch schedulers such as AWS Batch, SGE, Torque, and Slurm.
* More info on: https://aws.amazon.com/hpc/parallelcluster/
* Source Code on Git-Hub: https://github.com/aws/aws-parallelcluster
* Official Documentation: https://docs.aws.amazon.com/parallelcluster/


## Solution components
This project is build with the following components:

* **Grafana** is an [open-source](https://github.com/grafana/grafana) platform for monitoring and observability. Grafana allows you to query, visualize, alert on and understand your metrics as well as create, explore, and share dashboards fostering a data driven culture. 
* **Prometheus** [open-source](https://github.com/prometheus/prometheus/) project for systems and service monitoring from the [Cloud Native Computing Foundation](https://cncf.io/). It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts if some condition is observed to be true.  
* The **Prometheus Pushgateway** is on [open-source](https://github.com/prometheus/pushgateway/) tool that allows ephemeral and batch jobs to expose their metrics to Prometheus.
* **[Nginx](http://nginx.org/)** is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server.
* **[Prometheus-Slurm-Exporter](https://github.com/vpenso/prometheus-slurm-exporter/)** is a Prometheus collector and exporter for metrics extracted from the [Slurm](https://slurm.schedmd.com/overview.html) resource scheduling system.
* **[Node_exporter](https://github.com/prometheus/node_exporter)** is a Prometheus exporter for hardware and OS metrics exposed by \*NIX kernels, written in Go with pluggable metric collectors.

Note: *while almost all components are under the Apache2 license, only **[Prometheus-Slurm-Exporter is licensed under GPLv3](https://github.com/vpenso/prometheus-slurm-exporter/blob/master/LICENSE)**, you need to be aware of it and accept the license terms before proceeding and installing this component.*


## Example Dashboards

![ParallelCluster](docs/ParallelCluster.png?raw=true "AWS ParallelCluster")

![Master](docs/Master.png?raw=true "Master Node")

![Compute Node List](docs/List.png?raw=true "Compute Node List")

![Logs](docs/Logs.png?raw=true "AWS ParallelCluster Logs")

![Costs](docs/Costs.png?raw=true "Best - AWS ParallelCluster Costs")


## How to install it

You can simply use the post-install script that you can find [here](https://github.com/aws-samples/aws-parallelcluster-monitoring/blob/main/post-install.sh) as it is, or customize it as you need. For instance, you might want to change your [Grafana password](https://github.com/aws-samples/aws-parallelcluster-monitoring/blob/main/docker-compose/docker-compose.master.yml#L43) to something more secure and meaningful for you, or you might want to customize some dashboards by adding additional components to monitor.

```bash
#Load AWS Parallelcluster environment variables
. /etc/parallelcluster/cfnconfig

#get GitHub repo to clone and the installation script
monitoring_url=$(echo ${cfn_postinstall_args}| cut -d ',' -f 1 )
monitoring_dir_name=$(echo ${cfn_postinstall_args}| cut -d ',' -f 2 )
monitoring_tarball="${monitoring_dir_name}.tar.gz"
setup_command=$(echo ${cfn_postinstall_args}| cut -d ',' -f 3 )
monitoring_home="/home/${cfn_cluster_user}/${monitoring_dir_name}"

case ${cfn_node_type} in
    MasterServer)
        wget ${monitoring_url} -O ${monitoring_tarball}
        mkdir -p ${monitoring_home}
        tar xvf ${monitoring_tarball} -C ${monitoring_home} --strip-components 1
    ;;
    ComputeFleet)
    
    ;;
esac

#Execute the monitoring installation script
bash -x "${monitoring_home}/parallelcluster-setup/${setup_command}" >/tmp/monitoring-setup.log 2>&1
exit $?
``` 
The proposed post-install script will take care of installing and configuring everything for you through the [install-monitoring.sh](https://github.com/aws-samples/aws-parallelcluster-monitoring/blob/main/parallelcluster-setup/install-monitoring.sh) script. Though, few additional parameters are needed in the AWS ParallelCluster config file: the post_install_args, additional IAM policies, security group, and a tag. You can find an AWS ParallelCluster template [here](https://github.com/aws-samples/aws-parallelcluster-monitoring/blob/main/parallelcluster-setup/pcluster-template.config). Please note that, at the moment, the installation script has only been tested using [Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/).

```ini
base_os = alinux2

post_install = s3://<my-bucket-name>/post-install.sh

post_install_args = https://github.com/aws-samples/aws-parallelcluster-monitoring/tarball/main,aws-parallelcluster-monitoring,install-monitoring.sh

additional_iam_policies = arn:aws:iam::aws:policy/CloudWatchFullAccess,arn:aws:iam::aws:policy/AWSPriceListServiceFullAccess,arn:aws:iam::aws:policy/AmazonSSMFullAccess,arn:aws:iam::aws:policy/AWSCloudFormationReadOnlyAccess

tags = {“Grafana” : “true”}
```

Make sure that port `80` and port `443` of your master node are accessible from the internet (or form your network). You can achieve this by creating the appropriate security group via AWS Web-Console or via [CLI](https://docs.aws.amazon.com/cli/index.html), see an example below:

```bash
aws ec2 create-security-group --group-name my-grafana-sg --description "Open HTTP/HTTPS ports" —vpc-id vpc-1a2b3c4d
aws ec2 authorize-security-group-ingress --group-id sg-12345 --protocol tcp --port 443 —cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id sg-12345 --protocol tcp --port 80 —cidr 0.0.0.0/0
```

More information on how to create your security groups [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-sg.html#creating-a-security-group).  
Finally, set the additional_sg parameter in the `[VPC]` section of your ParallelCluster config file.  
After your cluster is created, you can just open a web-browser and connect to `https://your_public_ip` or `http://your_public_ip` (all `http` connections will be automatically redirected to `https`), a landing page will be presented to you with links to the Prometheus database service and the Grafana dashboards.


Note: *Because of the higher volume of network traffic due to the compute nodes continuously pushing metrics to the master node,
in case you expect to run a large scale cluster (hundreds of instances), we would recommend to use an instance type slightly bigger than what you planned for your master node.*

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the [LICENSE](https://github.com/aws-samples/aws-parallelcluster-monitoring/blob/main/LICENSE) file.
