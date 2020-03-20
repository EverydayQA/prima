#!/usr/bin/env perl 
#===============================================================================
#
#         FILE: perl_compile.pl
#
#        USAGE: ./perl_compile.pl  
#
#  DESCRIPTION: 
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: YOUR NAME (), 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: 08/29/2018 07:01:10 PM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use utf8;
use Cwd;
# The OO way (recommended)
use Test::Compile;
use Test::More;
my $test = Test::Compile->new();
my $cwd = getcwd();
my @dirs = ($cwd);
$test->all_files_ok(@dirs);
$test->all_pm_files_ok(@dirs);
my @files = `find $cwd -name "*.pl"`;
my @pms = `find $cwd -name "*.pm"`;

for my $pfile(@pms){
	chomp($pfile);
	pm_file_compiles($pfile, $pfile);
	pm_file_ok($pfile, $pfile);

}

for my $pfile(@files){
	chomp($pfile);
	pl_file_ok($pfile, $pfile);
}

$test->done_testing();
