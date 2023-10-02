# This manifest installs and configures nginx using puppet

exec {'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
  before   => Exec['install'], 
}

exec {'install':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  before   => Exec['add custom header'],
}

exec {'add custom header':
  command  => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\n\tadd_header X-Served-By \"$(hostname)\";/" /etc/nginx/nginx.conf',
  provider => shell,
  before   => Exec['restart nginx'],
}

exec {'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
