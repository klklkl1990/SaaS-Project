import * as cdk from 'aws-cdk-lib';
//import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as lambda from 'aws-cdk-lib/aws-lambda'
//import { Lambda } from 'aws-cdk-lib/aws-ses-actions';

export class CopykittInfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const layer=new lambda.LayerVersion(this,"BaseLayer",{code:lambda.Code.fromAsset("lambda_base/layer.zip"), compatibleRuntimes:[lambda.Runtime.PYTHON_3_9],})
    // The code that defines your stack goes here
    const APILambda= new lambda.Function(
      this,"APIFunc",{
        runtime:lambda.Runtime.PYTHON_3_9,
        //code: lambda.Code.fromAsset("../SaaS-Project",)
        code: lambda.Code.fromAsset("../app",),
        handler:"copykitt_api.handler",
        layers:[layer],
      })
    }
    // example resource
    // const queue = new sqs.Queue(this, 'CopykittInfraQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });
  }
