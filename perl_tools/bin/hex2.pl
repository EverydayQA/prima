#!/usr/bin/perl
use strict;
use warnings 'all';
#use v5.14;
use autodie;

{
    my $input = do {
        open my $in, '<', 'f1.txt';
        local $/;
        <$in>
    };

    open my $out, '>', 'sym.txt';
    print $out unpack 'H*', $input;
}

{
    my $input = do {
        open my $in, '<', 'f2.txt';
        local $/;
        <$in>
    };

    open my $out, '>', 'sym2.txt';
    print $out unpack 'H*', $input;
}

open my $fh1, '<', 'sym.txt';
open my $fh2, '<', 'sym2.txt';

until ( eof $fh1 or eof $fh2 ) {

    my @l1 = map hex, split //, <$fh1>;
    my @l2 = map hex, split //, <$fh2>;

    my $n = @l2 > @l1 ? @l2 : @l1;

    my @sum = map {
#        no warnings 'uninitialized';
        $l1[$_] + $l2[$_];
    } 0 .. $n-1;

    @sum = map { sprintf '%X', $_ } @sum;

    open my $out, '>', 'symout.txt';
    print { $out } reverse(@sum), '\n';
}
