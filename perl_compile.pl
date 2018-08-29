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
my $test = Test::Compile->new();
my $cwd = getcwd();
my @dirs = ($cwd);
$test->all_files_ok(@dirs);
$test->done_testing();

