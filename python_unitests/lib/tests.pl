#!/usr/bin/perl
use strict;
use warnings;

use FindBin qw($Bin);

# hardcoded for now
my @testdirs = (
    "${Bin}/DirTree",
    "${Bin}/perl_tools",
    "${Bin}/foundation/Test-Foo"
);

# test count - NA
# test log- NA
# test coverage - NA
#
foreach my $dir(@testdirs){
    print "\n*** $dir\n";
    if(-d $dir){
        chdir($dir);
        my $cmd = "prove -lvr .";
        system($cmd);
    }else{
        print "\n==> <$dir> does not exist\n";
    }
}

my @testdirs_nose = (
    "${Bin}/udacity_python",
    "${Bin}/foundation/python_e2",
    "${Bin}/foundation/python_test1",
    "${Bin}/python_tools",
    "${Bin}/quiz"

);

# python tests
foreach my $dir(@testdirs_nose){
    chdir($dir);
    my $cmd = "nosetests -v -w .";
    system($cmd);
}
