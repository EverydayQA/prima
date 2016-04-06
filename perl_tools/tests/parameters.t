#!/usr/bin/perl
use Test::More;
use Test::MockObject;
use strict;
use warnings;
use FindBin qw($Bin);
use lib "$Bin/../lib";
# Arithmetic declared to be package
use Arithmetic;
use Getopt::Long qw(GetOptionsFromString);

my $string = "--length=8 --file='1.dat' --verbose";

my ($ret, $args) = GetOptionsFromString($string);
print "<$ret><@$args>\n";

=start
GetOptions("length=i" => \$length,
    "file=s" => \$string,
    "verbose" => \$verbose)
or die("Error in options @ARGV\n");
=cut


my $addition = add(2015,6);
ok($addition == 2021, "expect: 2021, got: $addition\n");
done_testing();
