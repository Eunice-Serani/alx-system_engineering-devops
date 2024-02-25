# Set up the client SSH configuration file to connect to a server without a password

file { '/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'Turn off pwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
}

file_line { 'Set private key file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
}
