#!/usr/bin/perl
use strict;
use warnings;

# http://stackoverflow.com/questions/34623721/trouble-finding-all-expected-value
# 4 negatives in a row

# test data as simple as possible
my @tiers =(
    "support.tier.1",
    "support.tier.2",
    qw("support\.tier\.1"),
    "support\.tier\.2",
    quotemeta("support.tier.1\@example.com"),
    "support.tier.2\@example.com",
    "support\.tier\.1\@example\.com",
    "support\.tier\.2\@example\.com",
    "sales\@example\.com"
 );

my $count = 0;
foreach my $tier(@tiers){
    if($tier =~ m/support\\?.tier\\?.1/){
        print "$count: $tier\n";
    }
    $count++;
}


