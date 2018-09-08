#!/usr/bin/env perl
#===============================================================================
#
#         FILE: perllint.pl
#
#        USAGE: ./perllint.pl
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
#      CREATED: 08/29/2018 06:37:28 PM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use utf8;

use Perl::Critic;
my $file = shift;
my $critic = Perl::Critic->new();
my @violations = $critic->critique($file);
print "\n\n$file violation<@violations>\n";

use Perl::Lint
xxx
my $linter = Perl::Lint->new;
my $target_files = [($file)];
my $violations   = $linter->lint($target_files);
print $violations;
