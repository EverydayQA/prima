#
#===============================================================================
#
#         FILE: test_which.t
#
#  DESCRIPTION: 
#
#        FILES: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: YOUR NAME (), 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: 09/08/2019 03:19:40 PM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use Data::Dumper;
use Test::More;
use JSON;
require './which_subdir.pl';

our %dpro;
our %conf;
my $testfile = '/tmp/data.json';

test_file($testfile);
test_file($testfile);

sub test_file{
	my $testfile = shift;


	ok(-e $testfile);

	my $testdata = read_testdata($testfile);
	my $hconf = $$testdata{'conf'};
	our %conf = %$hconf;

	our $dresult = $$testdata{'dresult'};
	# print Dumper(\%conf);
	# print Dumper($dresult);
	my @refs = keys %$dresult;

	for my $fileref(@refs){
		print "<$fileref>\n";
		my @items = split(/\./, $fileref);
		my $action = '';
		my $file2 = pop(@items);
		my $file1 = pop(@items);
		if(@items){
			$action = $items[0];
		}
		my $subdir = which_subdir($file1, $file2, $action);

		my $dexpect = $$dresult{$fileref};
		my $dgot = $dpro{$fileref};
		print Dumper($dexpect);
		print Dumper($dgot);

		my @keys = keys %$dgot;

		for my $key (@keys){
			my $got = $$dgot{$key};
			my $expect = $$dexpect{$key};

			if($key =~ m/subdir/){
		
			}else{
				# use Data::Compare;

				next;
			}
			print "<$key><$got><$expect>\n";
			ok($got eq $expect);
		}
	}
}

done_testing();
