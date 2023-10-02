# This manifest installs and configures nginx using puppet

exec {'install':
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx',
  provider => shell,
}

exec {'add custom header':
  command  => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\n\tadd_header X-Served-By \"$(hostname)\";/" /etc/nginx/nginx.conf',
  provider => shell,
}

exec {'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
