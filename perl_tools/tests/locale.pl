#!/usr/bin/perl
use strict;
use warnings;
use DateTime::Locale;
use DateTime::Format::CLDR;

my $locale2 = DateTime::Locale->load('cs_CZ');
my $cldr5 = DateTime::Format::CLDR->new(
    pattern     => $locale2->date_format_long,
    locale      => $locale2,
    );

print $cldr5->pattern, "\n";
print $cldr5->parse_datetime('17. listopad 1989');
