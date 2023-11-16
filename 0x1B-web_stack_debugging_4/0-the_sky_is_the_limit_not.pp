# Increases the upper limit of the number of requests
# the server can handle

# Increases the ULIMIT of the default file
exec { 'modify file config':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

# Restarts the Nginx server
exec { 'restart-nginx':
  path    => '/etc/init.d/'
  command => 'nginx restart',
}
