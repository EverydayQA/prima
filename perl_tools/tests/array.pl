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
sub array_or_string{

    my @parameters = @_;
    my $size = scalar(@parameters);
    print "<@parameters> size<$size>\n";
}
