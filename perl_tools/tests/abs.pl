#!/usr/bin/perl -w
use strict;
my @nums = (
    '-0',
    '-0.0',
    "-0.000",
    qw(-0.000),
    sprintf("%.4f", "-0.0"),
    '-0.000',
    -0.000,
);

print "***use single abs()\n";
foreach my $num(@nums){
    my $number = $num;
    my $abs = abs($number+0);
    print "<$num> abs <$abs>\n";
}

print "\n***use abs(abs())\n";
foreach my $num(@nums){
    my $abs_abs = abs(abs($num));
    print "<$num> double abs <$abs_abs>\n";
}
