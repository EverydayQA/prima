#!/usr/bin/perl -w
use strict;
my @parameters = @ARGV;
my $count = scalar(@parameters);
print "prep_v2.pl #<$count> parameters\n";

foreach my $var (@parameters){
    print "<$var>\n";
}
