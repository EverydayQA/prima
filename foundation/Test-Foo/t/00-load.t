#!perl -T
use 5.006;
use strict;
use warnings FATAL => 'all';
use Test::More;

plan tests => 2;

BEGIN {
    use_ok( 'Test::Foo' ) || print "Bail out!\n";
    use_ok( 'Test::Bar' ) || print "Bail out!\n";
}

diag( "Testing Test::Foo $Test::Foo::VERSION, Perl $], $^X" );
