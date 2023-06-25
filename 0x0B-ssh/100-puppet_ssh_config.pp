#Create ssh configuration file in puppet
file_line {'Identity file':
  ensure  =>  'present',
  path    =>  '/etc/ssh/ssh_config',
  line    =>  'IdentityFile ~/.ssh/school',
}

file_line {'Password authentication not allowed':
  ensure  =>  'present',
  path    =>  '/etc/ssh/ssh_config',
  line    =>  'PasswordAuthentication no',
}