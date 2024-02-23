# Install flask from pip3.

# Install Python (3.8.10)
package { 'python':
  ensure => present,
}

# Install pip
package { 'python3-pip':
  ensure  => present,
}

# Install Werkzeug (2.1.1)
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# Install flask (2.1.0)
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
