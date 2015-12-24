#!/usr/bin/perl
use strict;
use warnings;

my $cmd;
# fille contains env variables and @INC
# could be saved somewhere else
my @lines = `cat /tmp/env.txt`;
foreach my $line(@lines){
    chomp($line);
    my @splits = split(/,/, $line);
    my $key = $splits[0];
    if($key eq "INC"){
        push(@INC, $line);
    }else{
        $ENV{$key} = $splits[1];
    }
}

my @parameters = @ARGV;
if(scalar(@parameters)==0){
    print "no parameters defined\n";
    exit(0);
}
my $script = $parameters[0];

system($script);
