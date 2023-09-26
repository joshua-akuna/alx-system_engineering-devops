# This manifest install and configures nginx using puppet

package {'nginx':
  ensure => 'present',
}

exec {'installation':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'index':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.youtube.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

exec {'server_restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
