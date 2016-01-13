#!/usr/bin/perl
use strict;
use warnings;
use Test::More;

use FindBin qw($Bin);
use lib "${Bin}/../lib/";
use Arithmetic;

return 1  unless $0 eq __FILE__;

main() if $0 eq __FILE__;

sub main{
    print "$Bin\n";
    my $date = `date`;
    chomp($date);
    $date =~ s/ /_/g;
    $date =~ s/:/_/g;

    my $log = "${Bin}/test_${date}.log";
    my $err = "${Bin}/err_${date}.log";
    Test::More->builder->output($log);
    Test::More->builder->failure_output($err);

    use_ok('Arithmetic');
    my $file = "${Bin}/math_add.txt";
    ok(-e $file,"$file Found\n");
    my @lines = `cat $file`;
    ok(scalar(@lines)>0,"array not empty\n");
    foreach my $line(@lines){
        chomp($line);
        my @splits = split(/,/,$line);
        my $expected = pop(@splits);
        my $result = add($splits[0], $splits[1]);
        cmp_ok($result, 'eq', $expected, "add @splits, got: <$result>, expecting: <$expected>\n");
        cmp_ok($result, '==', $expected, "add @splits, got: <$result>, expecting: <$expected>\n");

    }
    done_testing(9);
}
