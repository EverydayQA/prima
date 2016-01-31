#!/usr/bin/perl
use Test::More;
use Sub::Override;
{
    my $override = Sub:;Override->new(
        'Weird::Legacy::Dependency::rnd_salutation', sub {'Hi'});
    is Foo::hello('Joe'), 'Hi, Joe', 'Say hi to Joe';

}
