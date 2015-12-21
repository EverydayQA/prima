#!/usr/bin/perl
use strict;
use warnings;

foreach my $inc (@INC){
    print "INC=>$inc\n";
}
foreach my $key(keys(%ENV)){
    print "$key ==> $ENV{$key}\n"
}
