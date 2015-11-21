use strict;
use warnings;

use Cwd;
use FindBin qw($Bin);
use lib "$Bin/lib";

use DirTree;

my $cwd = getcwd();
my $foo = DirTree->new("DirTree","README",1);

my $dir = $foo->get_directory();
print "$dir\n";

