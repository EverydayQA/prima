#!/usr/bin/perl
use strict;
use warnings;

use Mail::Header;
use Mail::Field;
 
open(my $file, '<', './header.txt');
my @headerlines = <$file>;
close($file);
my $header = Mail::Header->new(@headerlines);

my @recfields = Mail::Field->extract('Received', $header);
print "<@recfields>\n";
#my $firstip = $recfields[0]->parse_tree->{'address'};
#print $firstip;
