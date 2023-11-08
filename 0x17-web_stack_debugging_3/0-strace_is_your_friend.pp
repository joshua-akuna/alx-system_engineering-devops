# The puppet manifest automates a fix for the apache2 server returning a 500 error

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
