use strict;
use warnings;

use FindBin qw($Bin);

# any lib path should be set by env
# use lib "/app/pm/use/lib";
# unshift @INC, "/app/pm/unshift/inc";

foreach my $inc (@INC){
    print "${Bin}/app.pm INC=>$inc\n";
}

sub app_libname{
	return "${Bin}/app.pm";
}
1;
