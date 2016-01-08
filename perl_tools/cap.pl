#!/usr/bin/perl
use POSIX qw(locale_h);
use locale;
use strict;
use warnings;
setlocale(LC_CTYPE);
setlocale(LC_CTYPE,"zh_CN");

=start
These character class all work for me
use re '/a';
use re '/aa';
use locale;
use re '/u';
=cut

my $string = "...so, that's our art. the 4 of us can now have a dialog. we can have a conversation. we can speak to...\n";
print $string;

# from OP
my $str = $string;
$str = $string;
$str =~ s/\.\s([a-z])/\. \u$1/g;
print "$str\n";
$str = $string;
$str =~ s/([\.!?]\s*)(\w)/$1\U$2/g;
print "$str\n";

# my modified version
$str =~ s/(\.)(\s)(\w)/$1$2\U$3/g;
print "$str\n";

# others
$str = $string;
$str =~ s/(?<=\w\.\s)(\w)/\U$1/g;
print "$str\n";
$str = $string;
$str =~ s/\w\.\s\K(\w)/\U$1/g;
print "$str\n";

print qw("$$$$$$$$$$$$$$$$$$$$$$$$$\n")."\n";
print '$$$$$$$$$$$$$\n';
print "\n";
my $count = 9;

my @listOfLists = map [], split(//, 1 x $count) ;

foreach my $ele(@listOfLists){
    print "ele<$ele>\n";
}

my @lists = map [], 0 .. $count;
foreach my $ele(@lists){
    print "Ele<$ele>\n";
}


