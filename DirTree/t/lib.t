use strict;
use warnings;

use FindBin qw($Bin);
use lib "$Bin/../lib";

use DirTree;

use Test::More qw(no_plan);


BEGIN {use_ok('DirTree') };

require_ok("DirTree");
my $pwd = `pwd`;
chomp($pwd);
my $obj = new DirTree($pwd,1,undef);
my $dir = $obj->get_directory();

is($dir, $pwd, "get_directory() passed");

$pwd = "/opt/hdf5/lib64";
$obj = new DirTree($pwd,1,undef);
$dir = $obj->get_directory();
my $depth = $obj->get_depth();
is($depth,1,"get_depth()");
isnt($depth,3,"get_depth()");
like($dir, qr/hdf5/, "get_directory()");
cmp_ok($dir, 'eq', $pwd, "$dir return $pwd");


