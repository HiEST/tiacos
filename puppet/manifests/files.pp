file { '/home/ubuntu/downloads/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}


file { '/home/ubuntu/applications':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/home/ubuntu/data':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/home/ubuntu/.jupyter':
  ensure => 'directory',
  owner    => 'ubuntu',
  group    => 'ubuntu',         
}


file { '/home/ubuntu/.jupyter/jupyter_notebook_config.py':
          ensure => present,
          replace => true,
          owner    => 'ubuntu',
          group    => 'ubuntu',          
          source => "/vagrant/puppet/files/jupyter_notebook_config.py",
          require => File['/home/ubuntu/.jupyter']
}

file { '/root/clean_image.sh':
          ensure => present,
          replace => true,
          owner    => 'ubuntu',
          group    => 'ubuntu',          
          mode     => '0755',
          source => "/vagrant/puppet/files/clean_image.sh"
}
 

