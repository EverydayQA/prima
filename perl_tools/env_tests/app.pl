#!/usr/bin/perl
use strict;
use warnings;
use FindBin qw($Bin);
# this is testable
use lib $Bin;

use app;

# better not to use fixed path
# not test friendly
# push @INC, '/app/pl/push/inc';
# use lib "/app/pl/use/lib";
# unshift @INC, "/app/pl/unshift/inc";

foreach my $inc (@INC){
    print "${Bin}/app.pl INC=>$inc\n";
}
