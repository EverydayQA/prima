#!/usr/bin/perl
use strict;
use warnings;

foreach my $par(@ARGV){
    print "par<$par>\n";
}
my $count = scalar(@ARGV);
print "$count\n";
exit( scalar(@ARGV) );
