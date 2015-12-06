# credit to Kurt in stackoverflow
# modfied a bit, if there is any bad pratice, it is mine
use strict;
use warnings;

use FindBin qw($Bin);
use lib "$Bin/../lib";

use Test::More qw(no_plan);

BEGIN {use_ok('Test::Foo') };

# test sub inside permission3.pl
# at 1 level up 
# you do not have to execute it first
# and you can test the main() as well
require "${Bin}/../permission3.pl";
ok(defined(is_writable("."))==1,"cwd should be writable");
# the main() can be tested, but to be modified to make sense
ok(defined(main())==1,"main reurn nothing");

# the example shows how to comprise and test as many as you could

