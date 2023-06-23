#Executing a kill command

exec {'killmenow':
  command  =>  'pkill -f killmenow',
}
