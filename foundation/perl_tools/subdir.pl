#!/usr/bin/perl
use strict;
use warnings;

my $dir = $ARGV[0];
opendir(my $DH, $ARGV[0])|| die "$!\n";
    my @dirs = grep {!/^\.\.?\z/ && -d "$dir/$_"} readdir($DH);

    foreach my $dir(@dirs){
        print "<$dir>\n";
    }
