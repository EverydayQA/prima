#!/usr/bin/perl
use strict;
use warnings 'all';

open my $in, "<", "f1.txt";
my $input = do { local $/; <$in> };

open my $out, ">", "sym.txt";
#print $out unpack 'H*', $input;
my $unpacked =get_unpacked($input);
print $out "$unpacked\n";

open my $in1, "<", "f2.txt";
my $input1 = do { local $/; <$in1> };
print "<$input>input1<$input1>\n";

open my $out1, ">", "sym2.txt";
my @unpacked1 =get_unpacked($input1);
foreach my $un(@unpacked1){
    print $out1 "$un\n";
}
my ($fh1,$fh2,$fh_out);
    open($fh1, '<', 'sym.txt') or die $!;
    open($fh2, '<', 'sym2.txt') or die $!;
    open $fh_out, '>', 'symout.txt' or die $!;

print "read file\n";
    my @l1 = map hex, split /\n/, <$fh1>;
    my @l2 = map hex, split /\n/, <$fh2>;
print "L1L2<@l1>  <@l2>\n";
    my $n = @l2 > @l1 ? @l2 : @l1;

    my @sum = map {
    #no warnings 'uninitialized';
        $l1[$_] + $l2[$_];
    } 0 .. $n-1;
    @sum = map { sprintf '%X', $_ } @sum;

        print { $fh_out } reverse(@sum), "\n";


sub get_unpacked{
    my $input = $_[0];
    print "input <$input>\n";
    my @splits  = split(/\n/,$input);
    my @unpackeds;
    foreach my $in(@splits){
        my $unpacked = unpack ('H*',$in);
        print "unpacked<$unpacked>\n";
        push(@unpackeds, $unpacked);
    }
    return @unpackeds;   
}
