exec { 'apt-get update':
  path => '/usr/bin'
}

apt::key { 'dockerkey':
  id      => '58118E89F3A912897C070ADBF76221572C52609D',
  server  => 'ha.pool.sks-keyservers.net',
} 
->
apt::source { 'docker':
  location => 'https://apt.dockerproject.org/repo',
  release  => 'ubuntu-xenial',
  repos    => 'main',
  pin      => '500',
  notify   => Exec['apt_update'],
  before   => Package['docker-engine'],
}


package { ['curl', 'unzip', 'vim', 'make', 'gcc', 'g++', 'automake', 'libtool', 'python-numpy', 'python-nose', 'python-scipy', 'libopenblas-dev', 'git', 'docker-engine', 'linux-image-extra-virtual', "linux-image-extra-$kernelrelease"]:
  ensure => present,
  require => Exec['apt-get update']
}


python::pip { 'jupyter' :
    pkgname       => 'jupyter',
    require => Exec['pip-upgrade']

}


service { "docker":
    ensure  => "running",
    enable  => "true",
    require => Package['docker-engine'],
}

class { 'python' :
    version    => 'system',
    pip        => 'present',
    dev        => 'present',
    virtualenv => 'present',
    gunicorn   => 'absent',
    before     => Package['python-nose', 'python-numpy', 'python-scipy', 'python-nose']
}


exec { 'pip-upgrade':
 cwd     => "/usr/local/bin",
 command => "pip install --upgrade pip",
 require => Class['Python']
}
