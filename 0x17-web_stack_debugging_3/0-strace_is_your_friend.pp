# This is fixing a 500 error
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
  ensure => present,
  source => '/var/www/html/wp-includes/class-wp-locale.php',
}
