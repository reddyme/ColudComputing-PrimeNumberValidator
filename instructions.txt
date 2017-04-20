# ColudComputing-PrimeNumberValidator

Steps followed to create the project:

1) Created Amazon EC2 Instance(VM) from https://aws.amazon.com/ 
2) During the process of step1, we get a unique public key which is required for VM access. Saved it as tutorials.pem 
3) Below ssh command is used to connect to the EC2 Virtual Machine ssh -i tutorials.pem ec2-user@50.112.32.181 
Note: ec2-user is the user, tutorials.pem is the public key 
4) Used Python Flask framework to implement the webservice development

Steps to Execute the project: 

1) Run the below URL to run the "Prime number test" for a given number http://50.112.32.181:5000/login 
Note: Created Elastic IP for the EC2 instance, So we don't have to change the URL when the instance is rebooted. 
2) Used CSS for background styles, HTMl for creating input fields, Python Flask as WebServer 
3) Following validations are taken care as part of the work 
	(i) Nagative numbers can't be prime numbers 
	(ii) Number must be an Integer, and Strings are not allowed to enter
