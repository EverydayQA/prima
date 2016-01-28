#!/usr/bin/perl
use Test::More;
use Test::MockObject;
use strict;
use warnings;
use FindBin qw($Bin);
use lib "$Bin/../lib";
# Arithmetic declared to be package
use Arithmetic;

# scope of mocked Arithmetic
{
    my $import;
    my $mock = Test::MockObject->new();
    $mock->fake_module('Arithmetic', import => sub { $import = caller} );
    $mock->fake_new('Arithmetric');
    $mock->mock('add', 
        sub {
            print "This example only mock a return value\n"; 
            return 45;
        }
    );

    my $addition_mock = $mock->add(2015,6);
    ok($addition_mock == 45, "expect: 45, got: $addition_mock\n");

    # if mock multiply has no definition, return null
    my $mul_mock = $mock->multiply(3,33);
    ok($mul_mock eq '', "expect: '', got: <$mul_mock>\n");
}

# unmocked module and methods
my $addition = add(2015,6);
ok($addition == 2021, "expect: 2021, got: $addition\n");
done_testing();
