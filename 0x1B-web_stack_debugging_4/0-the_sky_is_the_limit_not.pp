#Increase traffic on Nginx server

exec { 'nginx-traffic':
  command  =>  'sed -i "s/15/2000/" /etc/default/nginx',
  path     =>  '/usr/local/bin/'
}

#Restart Nginx
exec { 'restart':
  command  =>  '/usr/sbin/service nginx restart'
}
