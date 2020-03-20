#!/usr/bin/perl
use strict;
use warnings;
use experimental 'smartmatch';
my @parameters = @ARGV;
my $s1 = $parameters[0];
my $s2 = $parameters[1];

print "\n\n*** $0 <@parameters>\n";
self_call($s1, $s2);
print "end of @parameters\n\n";


sub self_call{
    # self call is dangerous
    # unless there is proper exit conditions
    my ($s1, $s2) = @_;

    my @all = (1, 2, 3, 4, 5, 6, 7, 8);

    # condition 1: both must be valid
    if($s1 ~~ @all && $s2 ~~ @all){
        # fine
    }else{
	print "not both in all\n";
        return;
    } 

 	
    my $index1 = 0;
    my $index2 = 0;
    my $index = 0;
    for my $x(@all){
	$index++;
	if($s1 == $x){
	    $index1 = $index;	
	}
	if($s2 == $x){
	    $index2 = $index;	
	}
    }
    if($index2 <= $index1){
	    print "order wrong $s1 $index1 $s2 $index2\n";
	    return;
    }
    my $start = 0;
    for my $x(@all){
	if($x == $s1){
	   $start = 1;
	   next;
	}
	if(!$start){
		next;
	}
	if($x == $s2){
	    print "exit condition x $x eq s2 $s2 for ${s1}.${s2}\n";
	    last;
	}
 	my $cmd = "$0 $s1 $x";
	print "$cmd\n";
	system($cmd);
    }
}
