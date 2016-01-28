#!/usr/bin/perl
use strict;
use warnings;

# comma separated array or parameters

my @eles_comma = ('a','a','a');
my $str_space = "b b b";
my $str_comma = "c,c,c";
my $str_comma_space = "d, d, d";

array_or_string(@eles_comma);
array_or_string($str_space);
array_or_string($str_comma);
array_or_string($str_comma_space);

array_or_string(qw(c c c));

my $cnt = "abc123:xxx7;5\n" =~ tr/[0-9]//;
print "count<$cnt>\n";
sub array_or_string{

    my @parameters = @_;
    my $size = scalar(@parameters);
    print "<@parameters> size<$size>\n";
}

my @nums = (
    '-0',
    '-0.0',
    "-0.000",
    qw(-0.000),
    sprintf("%.4f", "-0.0"),
    '-0.000',
    -0.000,
);

foreach my $num(@nums){
    my $number = $num;
    my $abs = abs($number);
    print "<$num> abs <$abs>\n";
}

foreach my $num(@nums){
    my $abs_abs = abs(abs($num));
    print "<$num> abs_abs <$abs_abs>\n";
}
