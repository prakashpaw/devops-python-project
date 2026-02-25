output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.devops_server.public_ip
}

output "app_url" {
  value = "http://${aws_instance.devops_server.public_ip}"
}

output "grafana_url" {
  value = "http://${aws_instance.devops_server.public_ip}:3000"
}
