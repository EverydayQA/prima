#!/usr/bin/perl
use strict;
use warnings;
use Cwd;
use File::Spec;
use File::Basename;
use Data::Dumper;
use JSON;

# this module is to test Cwd::abs_path() vs File::Spec->rel2abs()
# Path::Tiny?
#

my $path = "/tmp/do/not//exists//file";
my $abspath = abspath_filespec($path);
my $abspath_cwd = Cwd::abs_path($path);

print "abspath <$abspath> Cwd::abs_path<$abspath_cwd>\n";
print_path($path);

my $hostname = `hostname`;
chomp($hostname);
my $username = $ENV{LOGNAME} || $ENV{USER} || getpwuid($<);
chomp($username);
my $timestamp = localtime(time);
$timestamp =~ s/ //g;

our %hconf;
$hconf{'script'} = $0;
$hconf{'path'} = $path;
$hconf{'abspath'} = $abspath;
$hconf{'abspath_cwd'} = $abspath_cwd;
$hconf{'host'} = $hostname;
$hconf{'user'} = $username;
$hconf{'timestamp'} = $timestamp;

print Dumper(\%hconf);

my $log = "/tmp/log.${timestamp}.json";

dump_hash($log);

sub dump_hash{
	my $log = shift;
	my $json = encode_json(\%hconf);

	open my $fh, '>', $log or die "Can't create $log: $!\n";

	print $fh $json;
	close $fh;
}

sub abspath_filespec{
	my $path = shift;
	# Cwd::abs_path return undef if not
	return File::Spec->rel2abs($path);
}

sub print_path{
	my $path = shift;

	my $realpath = abspath_filespec($path);
	print "realpath<$realpath>\n";
	my $dirname = File::Basename::dirname($realpath);
	print "dirname<$dirname>\n";
	my $basename = File::Basename::basename($realpath);
	print "basename<$basename>\n";

}
