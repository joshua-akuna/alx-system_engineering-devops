# Increases the upper limit of the number of requests
# the server can handle

# Increases the ULIMIT of the default file
exec { 'fix--for-nginx':
  path    => '/usr/local/bin/:/bin/'
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
}

# Restarts the Nginx server
exec { 'restart-nginx':
  path    => '/etc/init.d/'
  command => 'nginx restart',
}
