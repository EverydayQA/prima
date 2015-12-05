#!/usr/bin/perl
use strict;
use warnings;

use File::Basename;

my $dir = "/shared";
my $w;

my @dirs = `find $dir -maxdepth 1 -mindepth 1 -type d`;


foreach my $tmp(@dirs){
    chomp($tmp);
    my $w = is_writable($tmp);
    if($w){
        print "*******************<$tmp> writable\n";
    }else{
        print "___________________<$tmp> not writable\n";
    } 
}

sub is_writable{
    my $tmp = $_[0];

    if(defined($tmp)){

    }else{
        return undef;
    }

    my $dir = dirname($tmp);
    my $fieparse = fileparse($tmp);

    if(-w $tmp){
        print "<$tmp> writable\n";
        return 1;
    }elsif(-d $tmp){
        print "dir <$tmp> not writable\n";
        return undef;
    }elsif(-f $tmp){
        print "file <$tmp> not writable\n";
        return undef;
    }else{
        print "<$tmp> does not exist\n";
        if(-w $dir){
            return 1;
        }else{
            return undef;
        }
    }
    return undef;
}
