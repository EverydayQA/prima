#!/usr/bin/perl
use strict;
use warnings;
my $cmd;
foreach my $key(keys(%ENV)){
    if($key=~ m/PATH/|| $key=~ m/PERL/){
        $cmd = "echo '$key,$ENV{$key}' >> /tmp/env.txt";
        system($cmd);
    }
}
foreach my $inc (@INC){
    $cmd = "echo 'INC,$inc'>> /tmp/env.txt";
    system($cmd);
}
print "current env saved in this file: /tmp/env.txt\n";

