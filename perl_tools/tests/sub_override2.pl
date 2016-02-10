#!/usr/bin/perl
use Test::More;
use Sub::Override;
use FindBin qw($Bin);
use lib "${Bin}/../lib";

sub local_add_add{
    my ($a, $b) = @_;
    my $result = ($a + $b + $a + $b);
    return $result;
}

{
    my $override = Sub::Override->new(
        'local_add_add' => sub {
            return 11;
        }
    );
    # local_add_add() - with overriden sub
    my $addition = local_add_add(2,3);
    ok($addition == 11, "expect 11, got: $addition");

}


my $real = local_add_add(2,3);
ok($real == 10, "expect: 10, got: $real");

done_testing();
