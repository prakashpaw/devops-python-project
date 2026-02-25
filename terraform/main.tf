resource "aws_instance" "devops_server" {
  ami           = "ami-051a31ab2f4d498f5" # Amazon Linux 2
  instance_type = "t3.micro"
  key_name      = "ami-051a31ab2f4d498f5"

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo amazon-linux-extras install docker -y
              sudo service docker start
              sudo usermod -a -G docker ec2-user
              EOF

  tags = { Name = "Python-DevOps-Final" }
}
