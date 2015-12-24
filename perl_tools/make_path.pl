#!/usr/bin/perl
use strict;
use File::Basename;
use File::Path qw/make_path/;

my $file = "/home/bob/test/foo.txt";
my $dir = dirname($file);
make_path($dir);

open my $fh, '>', $file or die "Ouch: $!\n"; # now go do stuff 
