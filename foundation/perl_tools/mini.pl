#!/usr/bin/perl
use strict;

my $output = `/usr/bin/php -q ./mini.php 2>&1 >> /tmp/mini.log &`;
$output = `/usr/bin/php -q ./mini.php 2>&1 &`;
$output = `/usr/bin/php -q ./mini.php &`;
$output = `./mini.php &`;
$output = `/usr/bin/php -v &`;
exec("/usr/bin/php -v ");



=start
http://stackoverflow.com/questions/31850528/perl-exec-usr-bin-php-v-hangs-on-centos-6-6-unless-stdin-is-closed-first
=cut

