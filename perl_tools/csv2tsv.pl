#!/usr/bin/perl 
use warnings;
use strict;
# csv2tsv - filter comma-separated text (csv) into tab-separated text (tsv)
# Steve Kinzler, steve@kinzler.com, Jul 03
# http://kinzler.com/me/home.html#unix

# NOTE: CSV text may be double-quoted and may include commas in quotes,
#       TSV is assumed to never be quoted and all tabs are separators

use Text::CSV;
#se Text::CSV_XS;	# optional, speeds up Text::CSV
my $h;
die "usage: $0 [ file ... ]\n" if $h;

my $csv = Text::CSV->new;

while (<>) {
    print "$_\n"; 
	s/[\r\n]*$//;

	warn("$0: warning, changing tab into 8 spaces in line $. [$_]\n")
		if s/\t/        /g;

	warn("$0: skipping line, parse failed in line $. [$_]\n"), next
		unless $csv->parse($_);

	print join("\t", $csv->fields()), "\n";
}
