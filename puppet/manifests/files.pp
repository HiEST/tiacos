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

