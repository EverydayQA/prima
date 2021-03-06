#!/usr/bin/perl
use Date::Calc;
use Test::MockModule;
use Test::More;

my ($big_day, $mock_today, $today);
$big_day = 32;

{
my $module = Test::MockModule->new('Date::Calc');
$module->mock('Today', sub {return $big_day});
$mock_today = Date::Calc::Today();
}

$today = Date::Calc::Today();

ok($mock_today == $big_day, "mock today, expect: $big_day, got: $mock_today\n");
ok($today<=31, "today for real expect:<=31, got: $today\n");
done_testing(2);
