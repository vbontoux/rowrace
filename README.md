# streamlit-cdk-fargate
You're one command away from deploying your [Streamlit](https://www.streamlit.io/) app on [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html)!

## TLDR: What is that one command you're teasing us with?

`git clone https://github.com/tzaffi/streamlit-cdk-fargate.git && cd streamlit-cdk-fargate && make deploy-streamlit`

### Caveats

Ok, so that was actually assuming the following pre-req's:
* you have an AWS account
* have configured the AWS CLI
* installed AWS CDK on your machine
* and have the `git` and `make` commands available

## Attribution - Standing on the Shoulders of Giants
* Maël Fabien's [excellent post](https://maelfabien.github.io/project/Streamlit/). I ripped off his very trim Streamlit app and Dockerfile.
* Nicolas Metalo's [very comprehensive tutorial](https://github.com/nicolasmetallo). I ripped off most of the rest of this code from there, except that I tried to streamline the CDK stack definition a bit, and summarized the various commands using `make`.


## ANTIQUATED - keeping as reminder to add `cdk bootstrap` to make command. - DON'T FORGET TO REMOVE

**I did that, but I got some nasty error about "This stack uses assets..."**

Try `cdk bootstrap` from inside of the `streamlit/` directory. Thent try `cdk deploy` again.

## What if I don't have those pre-reqs?
Here's [an explanation](#pre-requisites)

# Ok, that was a little sparse. I want to understand how this all works and what I should do with my streamlit app.
The basicd steps are to:

1. Setup your Streamlit Docker image
2. Test the Docker image
3. Setup your CDK streamlit stack, copying the Docker project into the cdk project
4. [Deploy](#deploy-the-streamlit-docker-on-fargate-using-cdk) the CDK stack
5. Tear-down the CDK stack when you're done using it


# Deploy the Streamlit Docker on Fargate using CDK

I've now taken the next step and deployed it using [AWS CDK (Cloud Development Kit)](https://docs.aws.amazon.com/cdk/index.html) on [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html).

The infrastructure setup on AWS was written 100% using CDK in ***python***. In particular, I **DIDN'T NEED TO TOUCH** any of the of the following:
* AWS GUI
* AWS CLI
* AWS Cloud Formation (thank god I didn't have to mess with that!)

I just had to modify [20 lines of code in one file](https://github.com/CognicalNYC/macgyver/blob/master/cdk/streamlit/streamlit/streamlit_stack.py#L14) - the CDK "stack definition" file that was auto-generated when I initiated the project (`cdk init streamlit`).

After getting the stack definition in place, deploying was as simple as `cdk deploy`. You can see from the resources output at the bottom, that those 20 lines delivered quite a punch. In particular, the following resources were all stood up and configured:
* EC2:
  * VPC
  * Subnet
  * RouteTable
  * SubnetRoutTableAssociation
  * Route
  * NatGateway
  * InternetGateway
  * Cluster
  * SecurityGroup
  * Service
  * ServiceGroup
* ELB
* IAM:
  * Role
  * Policy
* ECS:
  * TaskDefinition
* Logs:
  * LogGroups


## Instructions
0.  Install Node.js as well as CDK (see [macgyver README](https://github.com/CognicalNYC/macgyver/blob/master/README.md#deploying-streamlit-on-fargate-using-aws-cdk) for more details)
1. `git clone git@github.com:CognicalNYC/macgyver.git`
2. The rest is described in the [macgyver README](https://github.com/CognicalNYC/macgyver/blob/master/README.md#deploying-streamlit-on-fargate-using-aws-cdk) but you're a single command away after steps 0. and 1. (`make cdk-deploy PROJECT=streamlit`)
3. Don't forget to clean up when you're all done with either a `make cdk-clean PROJECT=streamlit` or directly inside `cdk/streamlit` with `cdk destoy`


## Resources that CDK Configured and Stood Up

```
Resources
[+] AWS::EC2::VPC ZephStreamlitVPC ZephStreamlitVPC40984819
[+] AWS::EC2::Subnet ZephStreamlitVPC/PublicSubnet1/Subnet ZephStreamlitVPCPublicSubnet1Subnet1A2AA945
[+] AWS::EC2::RouteTable ZephStreamlitVPC/PublicSubnet1/RouteTable ZephStreamlitVPCPublicSubnet1RouteTable583840F3
[+] AWS::EC2::SubnetRouteTableAssociation ZephStreamlitVPC/PublicSubnet1/RouteTableAssociation ZephStreamlitVPCPublicSubnet1RouteTableAssociationB4A02982
[+] AWS::EC2::Route ZephStreamlitVPC/PublicSubnet1/DefaultRoute ZephStreamlitVPCPublicSubnet1DefaultRoute082FB422
[+] AWS::EC2::EIP ZephStreamlitVPC/PublicSubnet1/EIP ZephStreamlitVPCPublicSubnet1EIP026E0E8A
[+] AWS::EC2::NatGateway ZephStreamlitVPC/PublicSubnet1/NATGateway ZephStreamlitVPCPublicSubnet1NATGateway44972270
[+] AWS::EC2::Subnet ZephStreamlitVPC/PublicSubnet2/Subnet ZephStreamlitVPCPublicSubnet2Subnet9BBD958C
[+] AWS::EC2::RouteTable ZephStreamlitVPC/PublicSubnet2/RouteTable ZephStreamlitVPCPublicSubnet2RouteTableC9BCFF80
[+] AWS::EC2::SubnetRouteTableAssociation ZephStreamlitVPC/PublicSubnet2/RouteTableAssociation ZephStreamlitVPCPublicSubnet2RouteTableAssociationC7002783
[+] AWS::EC2::Route ZephStreamlitVPC/PublicSubnet2/DefaultRoute ZephStreamlitVPCPublicSubnet2DefaultRoute6BA5157F
[+] AWS::EC2::EIP ZephStreamlitVPC/PublicSubnet2/EIP ZephStreamlitVPCPublicSubnet2EIP75476F55
[+] AWS::EC2::NatGateway ZephStreamlitVPC/PublicSubnet2/NATGateway ZephStreamlitVPCPublicSubnet2NATGatewayA8222148
[+] AWS::EC2::Subnet ZephStreamlitVPC/PrivateSubnet1/Subnet ZephStreamlitVPCPrivateSubnet1SubnetD20AE7C7
[+] AWS::EC2::RouteTable ZephStreamlitVPC/PrivateSubnet1/RouteTable ZephStreamlitVPCPrivateSubnet1RouteTable8052D12D
[+] AWS::EC2::SubnetRouteTableAssociation ZephStreamlitVPC/PrivateSubnet1/RouteTableAssociation ZephStreamlitVPCPrivateSubnet1RouteTableAssociation0FCA6A09
[+] AWS::EC2::Route ZephStreamlitVPC/PrivateSubnet1/DefaultRoute ZephStreamlitVPCPrivateSubnet1DefaultRoute41382E72
[+] AWS::EC2::Subnet ZephStreamlitVPC/PrivateSubnet2/Subnet ZephStreamlitVPCPrivateSubnet2SubnetBB9AB52B
[+] AWS::EC2::RouteTable ZephStreamlitVPC/PrivateSubnet2/RouteTable ZephStreamlitVPCPrivateSubnet2RouteTableE7CB2958
[+] AWS::EC2::SubnetRouteTableAssociation ZephStreamlitVPC/PrivateSubnet2/RouteTableAssociation ZephStreamlitVPCPrivateSubnet2RouteTableAssociation15975235
[+] AWS::EC2::Route ZephStreamlitVPC/PrivateSubnet2/DefaultRoute ZephStreamlitVPCPrivateSubnet2DefaultRoute8643277B
[+] AWS::EC2::InternetGateway ZephStreamlitVPC/IGW ZephStreamlitVPCIGW73E796BB
[+] AWS::EC2::VPCGatewayAttachment ZephStreamlitVPC/VPCGW ZephStreamlitVPCVPCGW683753A9
[+] AWS::ECS::Cluster ZephStreamlitCluster ZephStreamlitCluster66F13F7D
[+] AWS::ElasticLoadBalancingV2::LoadBalancer ZephFargateService/LB ZephFargateServiceLB23A42DAD
[+] AWS::EC2::SecurityGroup ZephFargateService/LB/SecurityGroup ZephFargateServiceLBSecurityGroupD2E76CD5
[+] AWS::EC2::SecurityGroupEgress ZephFargateService/LB/SecurityGroup/to streamlitZephFargateServiceSecurityGroup0445EB7E:8501 ZephFargateServiceLBSecurityGrouptostreamlitZephFargateServiceSecurityGroup0445EB7E850136068A37
[+] AWS::ElasticLoadBalancingV2::Listener ZephFargateService/LB/PublicListener ZephFargateServiceLBPublicListenerC7EDB90F
[+] AWS::ElasticLoadBalancingV2::TargetGroup ZephFargateService/LB/PublicListener/ECSGroup ZephFargateServiceLBPublicListenerECSGroupAAED681A
[+] AWS::IAM::Role ZephFargateService/TaskDef/TaskRole ZephFargateServiceTaskDefTaskRoleE745B9F4
[+] AWS::ECS::TaskDefinition ZephFargateService/TaskDef ZephFargateServiceTaskDef28DE8CEF
[+] AWS::Logs::LogGroup ZephFargateService/TaskDef/web/LogGroup ZephFargateServiceTaskDefwebLogGroupAD28A891
[+] AWS::IAM::Role ZephFargateService/TaskDef/ExecutionRole ZephFargateServiceTaskDefExecutionRole0B5B4D15
[+] AWS::IAM::Policy ZephFargateService/TaskDef/ExecutionRole/DefaultPolicy ZephFargateServiceTaskDefExecutionRoleDefaultPolicy48707106
[+] AWS::ECS::Service ZephFargateService/Service/Service ZephFargateService8DC10953
[+] AWS::EC2::SecurityGroup ZephFargateService/Service/SecurityGroup ZephFargateServiceSecurityGroupF8F38911
[+] AWS::EC2::SecurityGroupIngress ZephFargateService/Service/SecurityGroup/from streamlitZephFargateServiceLBSecurityGroup61AD5FB1:8501 ZephFargateServiceSecurityGroupfromstreamlitZephFargateServiceLBSecurityGroup61AD5FB185018651D62E
```

# MERGE 2

## Streamlit Example (using Spacy - Named Entity Recognizer)
Very much inspired by [Maël Fabien](https://maelfabien.github.io/project/Streamlit/#the-application)

### Build and Run
`make streamlit-iup`

You'll be able to run the app at [http://localhost:8501](http://localhost:8501)

## Deploying Streamlit on Fargate using AWS CDK

A slimmed down version of [nicolasmetallo](https://github.com/nicolasmetallo)'s [comprehensive tutorial](https://github.com/nicolasmetallo/legendary-streamlit-demo)

### **TLDR**

1. Run `make cdk-deploy PROJECT=streamlit`
2. Navigate to the URL printed when the stack is successfully deployed

### What you actually need to do from scratch:

1. [Install node](https://changelog.com/posts/install-node-js-with-homebrew-on-os-x) (CDK's local engine needs it)
2. [Install AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/work-with.html#work-with-prerequisites) (this is mainly just an `npm install -g aws-cdk`)
3. Initialize the "Streamlit Stack" (e.g. `make cdk-init PROJECT=streamlit` which creates the directory `./cdk/streamlit`)
4. Add CDK dependencies (e.g. `make cdk-install PROJECT=streamlit PACKS="aws_cdk.aws_ec2 aws_cdk.aws_ecs aws_cdk.aws_ecs_patterns"`)
5. Copy the streamlit docker project into the `cdk/streamlit` project (e.g. `cp -r streamlit cdk/streamlit/app`)
6. Modify the stack definition file `cdk/streamilt/streamlit/streamlit_stack.py` - this is really the crux of the "Code as Infrastrucure" definition
7. Deploy the stack to AWS (e.g. `cd cdk/streamlit && cdk deploy`)
8. Navigate to the URL printed when the stack is successfully deployed
9. Don't forget to **CLEAN UP** when you don't need the stack anymore (e.g. `cd cdk/streamlit && cdk destroy`)


## Pre-requisites
* Get an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) if you don't already have access to one
* Install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) if you haven't already done so and make sure to configure the client to connect with your AWS account (use the command `aws configure` after installation)
* Install the [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) on your machine. NOTE: You'll need to install Node.js as part of the process.
* Install `git` and `make` if you don't already have these on your machine. These will probably be installed if you're using Mac OS or Linux. On windows, you'll have to do a little more work. The last time I was using Windows (circa 2017), I enjoyed the [Chocalatey application](https://chocolatey.org/install) which made installing git and make as simple as running the following commands:
  * `choco install git`
  * `choco install make`
