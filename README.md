# snowflake_table_Lambda
Snowflake table metrics deployment in AWS using Lambda,Docker,ECR and API gateway



**End-to-End Deployment of AWS Lambda Using Docker**
1. Prepare Your Lambda Function Code
Create Your Lambda Function Code : **lambda_function.py**
2. Prepare the requirements.txt
3. Prepare the queries.py File
4. Create a Dockerfile : Create a file named Dockerfile in your project directory
5. Build and Push the Docker Image to Amazon ECR : Ensure you have AWS CLI and Docker installed and configured.
6. Create an Amazon ECR Repository,Authenticate Docker to Amazon ECR,Build the Docker Image,Tag the Docker Image,Push the Docker Image,
7. Create the Lambda Function:Create the Lambda Function Using the Docker Image
    aws lambda create-function --function-name my-lambda-function \
--package-type Image \
--code ImageUri=<your-account-id>.dkr.ecr.<your-region>.amazonaws.com/my-lambda-repo:latest \
--role arn:aws:iam::<your-account-id>:role/<your-lambda-execution-role>
8.  Make sure <your-lambda-execution-role> has the necessary permissions to access your resources (like ECR and Secrets Manager, if applicable).
9.  Update Lambda Function Configuration (if needed)
10. Set Up API Gateway
Create an HTTP API in API Gateway

Go to the API Gateway Console.
Create a new HTTP API.
Configure Routes

Add a route with method GET and path /.
Add Integration

Integrate the route with your Lambda function.
Deploy API

Deploy the API to a stage (e.g., prod).
Retrieve the API Endpoint URL

After deployment, you’ll get an API endpoint URL that you can use to invoke the Lambda function.
11. Test the API
Use curl, Postman, or any HTTP client to test the API endpoint:curl -X GET https://<api-id>.execute-api.<region>.amazonaws.com/prod/

**By following these steps, you will package your Lambda function and its dependencies into a Docker container and deploy it to AWS Lambda using Amazon ECR. This method helps manage large dependencies and simplifies deployment**


