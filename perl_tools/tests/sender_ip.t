#!/usr/bin/perl
use strict;
use warnings;
use Test::More;

use FindBin qw($Bin);
require "${Bin}/../sender_ip.pl";

return 1  unless $0 eq __FILE__;
test() if $0 eq __FILE__;

sub test{
    my $file = "${Bin}/../src/header.txt";
    ok(-e $file,"$file Found\n");
    my @headerlines = read_header($file);
    ok(scalar(@headerlines)>0,"array not empty\n");
    my @ips  = get_ips(@headerlines);
    ok(scalar(@ips)>0,"found ip as expected\n");
    done_testing(3);
}
