#!/usr/bin/perl
use Test::More;
use Test::MockObject;
use Date::Calc;

# scope of mocked Date::Calc
{
    my $import;
    my $mock = Test::MockObject->new();
    $mock->fake_module('Date::Calc', import => sub { $import = caller} );
    $mock->fake_new('Date::Calc');
    $mock->mock('Days_in_Year', sub {print "how to mock parameter - month to be 2\n"});
    # is it possible to mock a parameter? how if possible?
    my $days_mock = $mock->Days_in_Year(2015,6);
    ok($days_mock == 59, "expect: 59, got: $days_mock\n");
}

# unmocked module and methods
my $days_in_year = Date::Calc::Days_in_Year(2015,6);
ok($days_in_year == 181, "expect: 181, got: $days_in_year\n");
done_testing(4);
