#pkg update
exec {'update packages':
  command  =>  'apt-get update',
  path     =>  '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

#nginx installation
package {'nginx':
  ensure  =>  'installed',
}

#port 80 HTTP
exec {'allow HTTP':
  command  =>  "ufw allow 'Nginx HTTP'",
  path     =>  '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif   =>  '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

#index page file
file {'/var/www/html/index.html':
  content  =>  "Hello World!\n",
}

#404 page file
file {'/var/www/html/404.html':
  content  =>  "Ceci n'est pas une page\n",
}

#Redirect
file {'Nginx default config file':
  ensure   =>  file,
  path     =>  '/etc/nginx/sites-enabled/default',
  content  =>  
  "server {
	listen 80 default_server;
	listen [::]:80 default_server;
		root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	location / {
		try_files \$uri \$uri/ =404;
	}
	error_page 404 /404.html;
	location  /404.html {
		internal;
	}
	if (\$request_filename ~ redirect_me){
	   rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	}
  }",
}

#Nginx restart
exec {'restart service':
  command  =>  'service nginx restart',
  path     =>  '/usr/bin:/usr/sbin:/bin',
}
