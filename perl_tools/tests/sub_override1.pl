#!/usr/bin/perl
use Test::More;
use Sub::Override;
use FindBin qw($Bin);
use lib "${Bin}/../lib";
use Arithmetic;

# override add of Arithmetric
{
    my $override = Sub::Override->new(
        'add', sub {'Hi'; return 11;}
    );
    my $addition = add(2,3);
    ok($addition == 11, "expect 11, got: $addition");

}
done_testing();
