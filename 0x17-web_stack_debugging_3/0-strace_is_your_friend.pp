# manifest to fix typo in log file
exec { 'fix_typo':
  command =>  'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-include/class-wp-locale.phpp',
  path    =>  ['/bin', '/usr/bin'],
}

service {'apache2':
  ensure  =>  'running'
}

