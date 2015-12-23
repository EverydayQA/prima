#!/usr/bin/perl -w
use strict;
my @parameters = @ARGV;
my $count = scalar(@parameters);

my @parameters_new = wrap_parameters(@parameters);
my $cmd = "./prep_v2.pl @parameters_new";
print "prep.pl #<$count> parameters\n";
system($cmd);

sub wrap_parameters{
    my @parameters = @_;
    my @parameters_new;
    foreach my $var(@parameters){
        $var = quotemeta($var);
        push(@parameters_new, $var);
    }
    return @parameters_new;
}
