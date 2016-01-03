#!/usr/bin/perl
use strict;
use warnings;
my $string = "...so, that's our art. the 4 of us can now have a dialog. we can have a conversation. we can speak to...\n";
print $string;
# from OP
my $str = $string;
$str = $string;
$str =~ s/\.\s([a-z])/\. \u$1/g;
print $str;
$str = $string;
$str =~ s/([\.!?]\s*)(\w)/$1\U$2/g;
print $str;

# my modified version
$str =~ s/(\.)(\s)(\w)/$1$2\U$3/g;
print $str;

# others
$str = $string;
$str =~ s/(?<=\w\.\s)(\w)/\U$1/g;
print $str;
$str = $string;
$str =~ s/\w\.\s\K(\w)/\U$1/g;
print $str;



