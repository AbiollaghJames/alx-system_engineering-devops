#Executing a command

exec {'killmenow':
  command  =>  'pkill',
  onlyif   =>  'pgrep killmenow',

}
