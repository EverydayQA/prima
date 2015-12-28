#!/usr/bin/perl
use warnings;
use strict;
use utf8;
binmode STDOUT, "utf8";
my $string = "été";

my $re = re1($string);
print "<$string> to <$re>\n";

sub re1{
    my $string = $_[0];
    $string =~ s/[áàâã]/a/gi; #This line always prepends an "a"
    $string =~ s/[éèêë]/e/gi;
    $string =~ s/[úùûü]/u/gi;
    return $string;
}


