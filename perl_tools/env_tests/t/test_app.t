#!/usr/bin/perl
use strict;
use warnings;

use FindBin qw($Bin);

use Test::More;
use app;

# do not use anything affect INC
# use prove -I/path/to/test/lib
# BEGIN{
#	use lib "/test_app/t/BEGIN";
#}

foreach my $inc (@INC){
	print "test_app.t INC=>$inc\n";
}
ok($Bin eq $Bin, $Bin);
my $exit = `perl -I/tmp2 -I$Bin/../ $Bin/../app.pl`;
print "<$exit>\n";

ok('a' eq 'a', 'pass');
my $libname = app_libname();
ok($libname eq $libname, $libname);
done_testing();

