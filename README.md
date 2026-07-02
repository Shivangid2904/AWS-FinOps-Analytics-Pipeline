# AWS FinOps Analytics Pipeline

**Serverless Cloud Cost Analytics using AWS Cost & Usage Reports (CUR),
Amazon Athena, AWS Glue, AWS Lambda, and Amazon EventBridge**

## Overview

AWS FinOps Analytics Pipeline is a serverless cloud cost analytics
project that demonstrates how AWS native services can be combined to
analyze cloud spending, identify idle resources, and automate scheduled
cost monitoring.

The project ingests AWS Cost & Usage Reports (CUR), catalogs the data
using AWS Glue, performs SQL-based analytics using Amazon Athena, and
invokes a Lambda function on a scheduled basis using Amazon EventBridge.

> **Note:** This project was implemented using an AWS Academy lab
> environment during November--December 2025. The lab environment has
> since expired, so this repository contains the implementation
> artifacts, SQL queries, architecture, screenshots, and documentation
> rather than a live deployment.

------------------------------------------------------------------------

## Architecture

``` text
AWS Cost & Usage Report (CUR)
            │
            ▼
        Amazon S3
            │
            ▼
     AWS Glue Crawler
            │
            ▼
   Glue Data Catalog
            │
            ▼
     Amazon Athena
            │
   SQL Cost Analytics
            │
            ▼
     AWS Lambda
            │
            ▼
 Amazon EventBridge
 (Scheduled Execution)
```

------------------------------------------------------------------------

## Features

-   Automated AWS Cost & Usage Report (CUR) delivery to Amazon S3
-   Metadata discovery using AWS Glue Crawlers
-   Serverless SQL analytics using Amazon Athena
-   Service-wise cloud cost analysis
-   Daily cloud spending trend analysis
-   Idle EC2 usage detection
-   Scheduled automation using Amazon EventBridge
-   AWS Lambda workflow for recurring FinOps analysis
-   IAM-based secure access

------------------------------------------------------------------------

## Technology Stack

### AWS Services

-   Amazon S3
-   AWS Cost & Usage Reports (CUR)
-   AWS Glue
-   AWS Glue Data Catalog
-   Amazon Athena
-   AWS Lambda
-   Amazon EventBridge
-   AWS IAM
-   Amazon CloudWatch

### Languages

-   SQL
-   Python

------------------------------------------------------------------------

## Workflow

1.  AWS Cost & Usage Reports are exported to Amazon S3.
2.  AWS Glue Crawlers scan CUR data and build the Glue Data Catalog.
3.  Amazon Athena queries the cataloged data using serverless SQL.
4.  Analytics identify:
    -   Cost by AWS service
    -   Daily spending trends
    -   Low-utilization EC2 instances
5.  Amazon EventBridge invokes AWS Lambda every six hours.
6.  Lambda executes the scheduled FinOps monitoring workflow.

------------------------------------------------------------------------

## SQL Analytics

### Cost by AWS Service

``` sql
SELECT product_servicecode,
       SUM(line_item_unblended_cost) AS cost
FROM finops_cur_db.cur_data
GROUP BY product_servicecode
ORDER BY cost DESC;
```

### Daily Cost Trend

``` sql
SELECT DATE(line_item_usage_start_date) AS day,
       SUM(CAST(line_item_unblended_cost AS DOUBLE)) AS cost
FROM finops_cur_db.cur_data
GROUP BY 1
ORDER BY day;
```

### Idle EC2 Detection

``` sql
SELECT line_item_resource_id AS instance_id,
       SUM(CAST(line_item_usage_amount AS DOUBLE)) AS total_hours
FROM finops_cur_db.cur_data
WHERE line_item_product_code='AmazonEC2'
  AND line_item_usage_type LIKE '%BoxUsage%'
GROUP BY line_item_resource_id
ORDER BY total_hours ASC;
```

------------------------------------------------------------------------

## Repository Structure

``` text
aws-finops-analytics-pipeline/
│
├── architecture/
│   └── architecture.jpg
│
├── lambda/
│   └── remediation_bot.py
│
├── sql/
│   ├── cost_by_service.sql
│   ├── daily_cost_trend.sql
│   └── idle_ec2_detection.sql
│
├── screenshots/
│
├── report/
│   └── AWS-Hyper-Efficient-FinOps.pdf
│
└── README.md
```

------------------------------------------------------------------------

## Current Capabilities

-   Automated CUR ingestion
-   Glue metadata catalog creation
-   Athena-based SQL analytics
-   Scheduled FinOps workflow using EventBridge
-   Identification of potentially idle EC2 resources
-   Serverless architecture using AWS managed services

------------------------------------------------------------------------

## Screenshots

Include screenshots for:

-   S3 Bucket
-   CUR Storage
-   Glue Crawler
-   Glue Database
-   Athena Queries
-   EventBridge Scheduler
-   Architecture Diagram

------------------------------------------------------------------------

## Limitations

-   Uses historical CUR data rather than real-time metrics.
-   Lambda currently demonstrates the scheduled workflow and does not
    automatically stop EC2 instances.
-   Amazon QuickSight dashboards were not implemented because they were
    unavailable in the AWS Academy environment.

------------------------------------------------------------------------

## Future Enhancements

-   Automatic EC2 stop/hibernate for confirmed idle resources
-   SNS email notifications
-   Amazon QuickSight dashboards
-   Cost allocation by tags
-   Multi-account AWS Organizations support
-   Cost anomaly detection using machine learning

------------------------------------------------------------------------

## Learning Outcomes

-   AWS Cost & Usage Reports (CUR)
-   Serverless Data Engineering
-   AWS Glue Data Catalog
-   Amazon Athena
-   SQL Analytics
-   Event-Driven Architecture
-   Cloud Cost Optimization (FinOps)
-   AWS IAM and Security

------------------------------------------------------------------------

## Author

**Shivangi Dubey**

B.Tech Computer Science & Engineering (AI & ML)

SRM University-AP
