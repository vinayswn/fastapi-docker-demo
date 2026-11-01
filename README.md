Deploy FastAPI to AWS using the AWS Console – Step by Step
We'll deploy your FastAPI application (fastapi-docker-demo) using Amazon ECS Express Mode with AWS Fargate.
2. Prepare your FastAPI application
Your GitHub repository:
https://github.com/vinayswn/fastapi-docker-dem

docker build -t fastapi-docker-demo .
docker run -p 8000:8000 fastapi-docker-demo

3. Create an Amazon ECR repository
1.	Sign in to the AWS Management Console.
2.	Search for Elastic Container Registry.
3.	Select Amazon ECR.
4.	Select Private registry → Repositories.
5.	Click Create repository.
6.	Configure:
Setting	Value
Visibility	Private
Repository name	fastapi-docker-demo
Image tag mutability	Mutable
Encryption	AES-256
7. Click Create repository.
Your repository will look like:

4. Upload your Docker image to ECR

•  Open your newly created ECR repository.
•  Click View push commands.
•  Select the commands for your operating system.
•  Run the commands in PowerShell on your development machine.

aws configure


AWS Access Key ID: YOUR_ACCESS_KEY
AWS Secret Access Key: YOUR_SECRET_KEY
Default region name: us-east-1
Default output format: json

step 2. Get the ECR login password

aws ecr get-login-password --region us-east-1

Step 3. Login to AWS ECR

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 636621823007.dkr.ecr.us-east-1.amazonaws.com
Login Succeeded

4 Docker info
docker info



Step 5. Tag your Docker image
docker tag fastapi-docker-demo:latest 636621823007.dkr.ecr.us-east-1.amazonaws.com/fastapi-docker-demo:latest


Step 6. Push image to AWS ECR
docker push 636621823007.dkr.ecr.us-east-1.amazonaws.com/fastapi-docker-demo:latest

5. Deploy using ECS Express Mode
This is the main deployment step.
 

1.	Open Amazon ECS Console.
2.	In the left navigation, select Express mode.
3.	Select Create service or the equivalent create option.
4.	Under Let's set up your app, configure:
Field	Value
Image source	Amazon ECR
Repository	fastapi-aws-demo
Image	latest
Image selection	Image digest recommended
Task execution role	Create new role
Infrastructure role	Create new role
5. Expand Additional configurations.
Configure the following:
Setting	Value
Service name	fastapi-aws-service
Container port	8000
Health check path	/health
CPU	1 vCPU
Memory	2 GB
Minimum tasks	1
Maximum tasks	3
CPU architecture	X86_64
Important: The port must be 8000, matching the Dockerfile and Uvicorn configuration.
6. Configure networking:
•	Use the default VPC if available.
•	Select public networking defaults.
•	Keep the service accessible through its HTTPS load balancer.
7. Configure logging:
•	Enable CloudWatch logging.
•	Use the default log group or name it /ecs/fastapi-aws-service.
8.	Review all settings.
9.	Click Create.
ECS Express Mode automatically provisions the underlying Fargate service, load balancer, HTTPS endpoint, scaling configuration and monitoring resources

7. Access your FastAPI application
Once the deployment is complete, ECS Express Mode provides an HTTPS Application URL.

