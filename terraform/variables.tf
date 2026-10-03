variable "postgresql_host" {
     type=string
     default="localhost"
}
variable "postgresql_port" {
     type=number
     default=5566
}
variable "postgresql_user" {
     type=string
     default="postgres"
}
variable "postgresql_password" {
     type=string
     default="admin"
}
variable "postgresql_database" {
     type=string
     default="postgres"
}

