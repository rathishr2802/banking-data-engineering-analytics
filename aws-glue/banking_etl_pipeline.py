import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1785937391804 = glueContext.create_dynamic_frame.from_catalog(database="banking_raw_db", table_name="customers_csv", transformation_ctx="AWSGlueDataCatalog_node1785937391804")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1785937682411 = glueContext.create_dynamic_frame.from_catalog(database="banking_raw_db", table_name="loans_csv", transformation_ctx="AWSGlueDataCatalog_node1785937682411")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1785937646755 = glueContext.create_dynamic_frame.from_catalog(database="banking_raw_db", table_name="cards_csv", transformation_ctx="AWSGlueDataCatalog_node1785937646755")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1785937552485 = glueContext.create_dynamic_frame.from_catalog(database="banking_raw_db", table_name="transactions_csv", transformation_ctx="AWSGlueDataCatalog_node1785937552485")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1785937495458 = glueContext.create_dynamic_frame.from_catalog(database="banking_raw_db", table_name="accounts_csv", transformation_ctx="AWSGlueDataCatalog_node1785937495458")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1785937616285 = glueContext.create_dynamic_frame.from_catalog(database="banking_raw_db", table_name="branches_csv", transformation_ctx="AWSGlueDataCatalog_node1785937616285")

# Script generated for node Change Schema
ChangeSchema_node1785937799745 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1785937391804, mappings=[("customer_id", "string", "customer_id", "string"), ("first_name", "string", "first_name", "string"), ("last_name", "string", "last_name", "string"), ("gender", "string", "gender", "string"), ("dob", "string", "dob", "date"), ("phone", "long", "phone", "string"), ("email", "string", "email", "string"), ("address", "string", "address", "string"), ("city", "string", "city", "string"), ("state", "string", "state", "string"), ("pincode", "long", "pincode", "string"), ("occupation", "string", "occupation", "string"), ("annual_income", "long", "annual_income", "int"), ("marital_status", "string", "marital_status", "string"), ("customer_since", "string", "customer_since", "date"), ("kyc_status", "string", "kyc_status", "string"), ("customer_status", "string", "customer_status", "string"), ("risk_category", "string", "risk_category", "string")], transformation_ctx="ChangeSchema_node1785937799745")

# Script generated for node Change Schema
ChangeSchema_node1785937870264 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1785937682411, mappings=[("loan_id", "string", "loan_id", "string"), ("customer_id", "string", "customer_id", "string"), ("loan_type", "string", "loan_type", "string"), ("loan_amount", "long", "loan_amount", "long"), ("interest_rate", "double", "interest_rate", "double"), ("loan_term_months", "long", "loan_term_months", "int"), ("emi", "double", "emi", "double"), ("start_date", "string", "start_date", "date"), ("end_date", "string", "end_date", "date"), ("loan_status", "string", "loan_status", "string")], transformation_ctx="ChangeSchema_node1785937870264")

# Script generated for node Change Schema
ChangeSchema_node1785937858651 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1785937646755, mappings=[("card_id", "string", "card_id", "string"), ("customer_id", "string", "customer_id", "string"), ("account_id", "string", "account_id", "string"), ("card_number", "long", "card_number", "string"), ("card_type", "string", "card_type", "string"), ("card_network", "string", "card_network", "string"), ("issue_date", "string", "issue_date", "date"), ("expiry_date", "string", "expiry_date", "date"), ("cvv", "long", "cvv", "int"), ("daily_limit", "long", "daily_limit", "int"), ("status", "string", "status", "string")], transformation_ctx="ChangeSchema_node1785937858651")

# Script generated for node Change Schema
ChangeSchema_node1785937823348 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1785937552485, mappings=[("transaction_id", "string", "transaction_id", "string"), ("account_id", "string", "account_id", "string"), ("transaction_date", "string", "transaction_date", "timestamp"), ("transaction_type", "string", "transaction_type", "string"), ("amount", "double", "amount", "double"), ("merchant", "string", "merchant", "string"), ("payment_method", "string", "payment_method", "string"), ("city", "string", "city", "string"), ("status", "string", "status", "string"), ("remarks", "string", "remarks", "string")], transformation_ctx="ChangeSchema_node1785937823348")

# Script generated for node Change Schema
ChangeSchema_node1785937811528 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1785937495458, mappings=[("account_id", "string", "account_id", "string"), ("customer_id", "string", "customer_id", "string"), ("account_type", "string", "account_type", "string"), ("balance", "long", "balance", "double"), ("opening_date", "string", "opening_date", "date"), ("account_status", "string", "account_status", "string"), ("branch_id", "string", "branch_id", "string")], transformation_ctx="ChangeSchema_node1785937811528")

# Script generated for node Change Schema
ChangeSchema_node1785937845115 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1785937616285, mappings=[("branch_id", "string", "branch_id", "string"), ("branch_name", "string", "branch_name", "string"), ("branch_code", "string", "branch_code", "string"), ("ifsc_code", "string", "ifsc_code", "string"), ("city", "string", "city", "string"), ("state", "string", "state", "string"), ("region", "string", "region", "string"), ("address", "string", "address", "string"), ("manager_name", "string", "manager_name", "string"), ("phone", "long", "phone", "string"), ("email", "string", "email", "string"), ("opened_date", "string", "opened_date", "date")], transformation_ctx="ChangeSchema_node1785937845115")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeSchema_node1785937799745, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1785922484424", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1785937922638 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1785937799745, connection_type="s3", format="glueparquet", connection_options={"path": "s3://banking-etl-pipeline-28/processed/customers/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1785937922638")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeSchema_node1785937870264, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1785922484424", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1785937981784 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1785937870264, connection_type="s3", format="glueparquet", connection_options={"path": "s3://banking-etl-pipeline-28/processed/loans/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1785937981784")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeSchema_node1785937858651, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1785922484424", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1785937969590 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1785937858651, connection_type="s3", format="glueparquet", connection_options={"path": "s3://banking-etl-pipeline-28/processed/cards/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1785937969590")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeSchema_node1785937823348, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1785922484424", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1785937945615 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1785937823348, connection_type="s3", format="glueparquet", connection_options={"path": "s3://banking-etl-pipeline-28/processed/transactions/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1785937945615")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeSchema_node1785937811528, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1785922484424", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1785937934579 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1785937811528, connection_type="s3", format="glueparquet", connection_options={"path": "s3://banking-etl-pipeline-28/processed/accounts/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1785937934579")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeSchema_node1785937845115, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1785922484424", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1785937956444 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1785937845115, connection_type="s3", format="glueparquet", connection_options={"path": "s3://banking-etl-pipeline-28/processed/branches/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1785937956444")

job.commit()