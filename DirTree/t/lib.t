use strict;
use warnings;

use FindBin qw($Bin);
use lib "$Bin/../lib";

use DirTree;

use Test::More qw(no_plan);


BEGIN {use_ok('DirTree') };

require_ok("DirTree");

my $obj = new DirTree("DirTree","READE",1);
my $get_directory = $obj->get_directory();

#like($get_directory, qr/DirTree/,"get_directory() RE test");

is($get_directory, "DirTree", "get_directory() IS test");



