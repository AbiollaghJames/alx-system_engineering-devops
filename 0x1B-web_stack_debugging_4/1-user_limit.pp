#Increase limit for Holberton user


exec { 'increase-hard-limit':
  command  =>  'sed -i "s/5/4000" /etc/security/limits.conf/',
  path     =>  '/usr/local/bin/'
}
exec { 'increase-soft-limit':
  command  =>  'sed -i "s/4/2000" /etc/security/limit.conf',
  path     =>  '/usr/local/bin'
}
