use strict;
use warnings;
use Data::Dumper;
use JSON;

our %conf;
our %dpro;

unless(caller){
	print "call main()\n";
	my $hdata = read_testdata('/tmp/data.json');
	my $hconf = $$hdata{'conf'};
	%conf = %$hconf;
	main();
	print Dumper(\%dpro);
}

sub main{
	# setconf();
	which_subdir('item1', 'item2', '');
	which_subdir('ext-item2', 'ext-item3', 'run');
	which_subdir('item1', 'ext-item3', 'run');
	which_subdir('item1', 'ext-item3', '');
}

sub setconf{
	my %conf = (
          'localrt' => 'old',
          'decisions' => {
                           'item1.ext-item3' => 'IsPass.subdir1',
                           'run.item1.ext-item1' => 'IsPass.subdir1',
                           'run.item1.item2' => 'RmSubdir.subdir1',
                           'item3.item4' => 'IsPass.subdir1',
                           'run.item3.item4' => 'IsPass.subdir1',
                           'item1.ext-item4' => 'IsPass.RmSubdir2017',
                           'run.item1.ext-item4' => 'IsPass.RmSubdir2017',
                           'item1.item2' => 'RmSubdir.subdir1',
                           'item1.ext-item2' => 'IsPass.subdir1',
                           'run.item1.item4' => 'IsPass.subdir1',
                           'run.item1.item3' => 'RmSubdir.subdir1',
                           'item1.item4' => 'IsPass.subdir1',
                           'run.item1.ext-item2' => 'IsPass.subdir1',
                           'item1.ext-item1' => 'IsPass.subdir1',
                           'item1.item3' => 'RmSubdir.subdir1',
                           'run.item2.item3' => 'RmSubdir.subdir1',
                           'item2.item3' => 'RmSubdir.subdir1',
                           'run.item1.ext-item3' => 'IsPass.subdir1'
                         },
          'switchdate' => '20160101',
		  'root' => '2017',
          'valid_subdirs' => [
                                  'item1',
                                  'item2',
                                  'item3',
                                  'item4',
                                  'ext-item1',
                                  'ext-item2',
                                  'ext-item3'
                                ],
          'valid_names' => [
                             'item1',
                             'item2',
                             'item3',
                             'item4',
                             'ext-item1',
                             'ext-item2',
                             'ext-item3'
                           ],
          'active_ext_subdirs' => [
                                       'ext-item1',
                                       'ext-item2',
                                       'ext-item3'
                                     ],
          'tpdates' => {
                         'item3' => '2013-07-07',
                         'item2' => '2012-07-07',
                         'ext-item2' => '2016-07-07',
                         'ext-item1' => '2015-07-07',
                         'item1' => '2011-01-01',
                         'ext-item3' => '2018-07-07',
                         'item4' => '2014-07-07'
                       }
		);
	return \%conf;
}

sub dump_wrapper{
	print Dumper(\%dpro);
	my $jsonfile = "/tmp/data.json";
	dump_testdata($jsonfile);
	print "$jsonfile\n";

	if(-e $jsonfile){
		read_testdata($jsonfile);
	}
}

sub read_testdata{
	my $jsonfile = shift;
	my $jsonstr = `cat $jsonfile`;
	chomp($jsonstr);
	my $testdata = decode_json($jsonstr);
	return $testdata;
}

sub dump_testdata{
	my $jsonfile = shift;

	my %data;
	$data{'conf'} = \%conf;
	$data{'dresult'} = \%dpro;

	# my $json = encode_json(\%data);
	# print "<$json>\n";

	my $json_str_pretty = JSON->new->pretty->encode(\%data);
	print "<$json_str_pretty>\n";
	open my $fh, ">", $jsonfile;
	print $fh $json_str_pretty;
	close $fh;
}

sub which_subdir{
	my ($file1, $file2, $action) = @_;
	my $fileref = get_fileref($file1, $file2, '');
	my $mfileref = get_fileref($file1, $file2, $action);
	my $subdir;

	my $dvalid_subdirs = $conf{'valid_subdirs'};
	my $switch = $conf{'switchdate'};
	my @itims_before = ();
	my @itims_after = ();
	my @itims_file1_file2 = ();
	my @itims_file1_switch = ();
	my $date1 = $conf{'tpdates'}{$file1};
	my $date2 = $conf{'tpdates'}{$file2};
	$date1 =~ s/-//g;
	$date2 =~ s/-//g;

	for my $tpx(@$dvalid_subdirs){
		my $datex = $conf{'tpdates'}{$tpx};
		$datex =~ s/-//g;
		if($datex >= $switch){
			push(@itims_after, $tpx);
		}else{
			push(@itims_before, $tpx);
			if($datex > $date1){
				push(@itims_file1_switch, $tpx);
			}
		}
	}

	$dpro{$mfileref}{'itims_before'} = \@itims_before;
	$dpro{$mfileref}{'itims_after'} = \@itims_after;
	$dpro{$mfileref}{'itims_file1_switch'} = \@itims_file1_switch;

	# itims_after
	if($file1 ~~ @itims_after && $file2 ~~ @itims_after){
		$subdir = 'new';
		$dpro{$mfileref}{'subdir_itims_after'} = $subdir;
		$dpro{$mfileref}{'subdir'} = $subdir;
		return $subdir;
	}

	# psql
	$subdir = subdir_psql($file1, $file2, $action);
	if($subdir){
		$dpro{$mfileref}{'subdir_psql'} = $subdir;
		$dpro{$mfileref}{'subdir'} = $subdir;

		return $subdir;
	}

	# itims_before
	if($file1 ~~ @itims_before && $file2 ~~ @itims_before){
		$subdir = 'old';
		$dpro{$mfileref}{'subdir_itims_before'} = $subdir;
		$dpro{$mfileref}{'subdir'} = $subdir;

		return $subdir;
	}	

	# itims_file1_switch
	# postchg
	if(scalar(@itims_file1_switch) == 0){
		$subdir = 'new';
		$dpro{$mfileref}{'subdir_postchg'} = $subdir;
		$dpro{$mfileref}{'subdir'} = $subdir;

		return $subdir;
	}

	if($file2 ~~ @itims_file1_switch){
		# not applied
		undef($subdir);
		$dpro{$mfileref}{'subdir'} = $subdir;
		return;
	}
	$subdir = subdir_file1_switch($file1, $file2, $action);
	$dpro{$mfileref}{'subdir_file1_switch_action'} = $subdir;
	$dpro{$mfileref}{'subdir'} = $subdir;
	return $subdir;
}
sub subdir_file1_switch{
	my ($file1, $file2, $action) = @_;

	# find pass/fail 
	my $mfileref = get_fileref($file1, $file2, $action);
	my $itims_file1_switch_aref = $dpro{$mfileref}{'itims_file1_switch'};
	if(!$itims_file1_switch_aref){
		return 'error';
	}
	if(scalar(@$itims_file1_switch_aref) == 0){
		return 'Unknown should be new?';
	}

	if($file2 ~~ @$itims_file1_switch_aref){
		# not applied
		return;
	}
	#
	my @pass;
	my @fail;
	for my $tpx (@$itims_file1_switch_aref){
		if(!$tpx){
			print "empty tpx <@$itims_file1_switch_aref>\n";
		}
		if($tpx eq $file2){
			next;
		}
		my $filerefx = get_fileref($file1, $tpx, $action);
		my $dec = $conf{'decisions'}{$filerefx};
		if(!$dec){
			next;
		}
		if($dec =~ m/RmSubdir/){
			push(@pass, "$filerefx.$dec");
		}elsif($dec =~ m/IsPass/){
			push(@fail, "$filerefx.$dec");
		}
		
	}
	$dpro{$mfileref}{$mfileref}{'pass'} = \@pass;
	$dpro{$mfileref}{$mfileref}{'fail'} = \@fail;

	if($action){
		if(@fail){
			return 'old';
		}elsif(@pass){
			return 'new';
		}else{
			return subdir_itims_file1_switch($file1, $file2, '');
		}
	}else{
		if(@fail){
			return 'old';
		}elsif(@pass){
			return 'new';
		}else{
			return "not sure, run rm file.pl $file1 $file2?";
		}
	}
}

sub subdir_psql{
	my ($file1, $file2, $action) = @_;

	my $fileref = get_fileref($file1, $file2, $action);

	my $root = $conf{'root'};
	my $localrt = $conf{'localrt'};
	if($localrt){
		if($localrt eq '2017'){
			$dpro{$fileref}{'localrt'} = $localrt;
			return 'new';
		}
	}
	if($root && $root eq '2017'){
		$dpro{$fileref}{'root'} = $root;
		return 'new';
	}
	return;
}

sub get_fileref{
	my ($file1, $file2, $action) = @_;
	my $mfileref = "${file1}.${file2}";
	if($action){
		$mfileref = "${action}.${mfileref}";
	}
	return $mfileref;
}
