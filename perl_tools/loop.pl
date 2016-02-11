#!/usr/bin/perl
use warnings;
use strict;

my @arr = (1,2);
my $i = loop2(@arr);
print "return <$i>\n";

sub loop2{
    my @arr = @_;
    foreach my $i( @arr){
        my $j  = "processing $i";
        print "$j\n";
        return $j; 
    }
}
