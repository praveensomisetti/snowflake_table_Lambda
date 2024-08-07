# Use the official AWS Lambda Python image
FROM public.ecr.aws/lambda/python:3.10

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the Lambda function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}
COPY queries.py ${LAMBDA_TASK_ROOT}

# Set the CMD to the Lambda handler
CMD ["lambda_function.lambda_handler"]
