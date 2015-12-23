#!/usr/bin/perl -w
use strict;
# call prep.pl with 5 parameters
my $cmd = "./prep.pl aaa_777-1 bbb-6666-2 'Incomplete QA' -reason 'too long, mail me at ben\@example.com :)\n'";
system($cmd);
