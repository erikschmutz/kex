import * as cdk from "@aws-cdk/core";
import * as ec2 from "@aws-cdk/aws-ec2";
import * as iam from "@aws-cdk/aws-iam";

class KexStack extends cdk.Stack {
  constructor(scope: cdk.App) {
    super(scope, "KexStack", undefined);

    const vpc = new ec2.Vpc(this, "Vpc");
    const userData = ec2.UserData.forLinux();
    userData.addCommands(
      "cd /home/ec2-user",
      "sudo yum update -y",
      "sudo yum install git -y",
      "git clone https://github.com/erikschmutz/kex.git",
      "cd kex && chmod 777 start.sh && ./start.sh"
    );

    const linuxImage = new ec2.AmazonLinuxImage({
      generation: ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
    });

    const role = new iam.Role(this, "InstanceRole", {
      roleName: "KexInstanceRole",
      assumedBy: new iam.ServicePrincipal("ec2.amazonaws.com"),
    });

    const securityGroup = new ec2.SecurityGroup(this, "SecurityGroup", {
      vpc: vpc,
      securityGroupName: "KexSecurityGroup",
    });

    securityGroup.addIngressRule(
      ec2.Peer.anyIpv4(),
      ec2.Port.tcp(22),
      "SSH-Connection"
    );

    const trackerService = new ec2.Instance(this, "TrackerService", {
      vpc,
      securityGroup: securityGroup,
      role,
      instanceType: ec2.InstanceType.of(
        ec2.InstanceClass.T3,
        ec2.InstanceSize.MEDIUM
      ),
      userData,
      instanceName: "KexInstanceName",
      machineImage: linuxImage,
      vpcSubnets: { subnetType: ec2.SubnetType.PUBLIC },
      keyName: "kex-pem",
    });
  }
}

const app = new cdk.App();
new KexStack(app);
