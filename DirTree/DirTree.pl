use strict;
use warnings;

use File::Basename;

use Cwd;
use FindBin qw($Bin);
use lib "$Bin/lib";

use DirTree;
use DirFormat;

my $cwd = getcwd();
my @splits = split(/\//, $cwd);

recursive_dir($cwd, scalar(@splits) );

