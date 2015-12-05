# credit to Kurt in stackoverflow
# modfied a bit, if there is any bad pratice, it is mine
use strict;
use warnings;

use FindBin qw($Bin);
use lib "$Bin/../lib";

use Test::More qw(no_plan);

BEGIN {use_ok('Test::Foo') };

# test sub inside permission.pl
# at 1 level up 
# you have to execute it first
require "${Bin}/../permission.pl";


