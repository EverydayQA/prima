#!/usr/bin/perl
use strict;
use warnings;
 
return 1  unless $0 eq __FILE__;
main(@ARGV) if $0 eq __FILE__;

sub main{
    my @parameters = @_;

    my $file = check_input(@parameters);
    my @headerlines = read_header($file);
    my @ips  = get_ips(@headerlines);

    if(scalar(@ips)>0){
        print "\n*** sender ips @ips\n";
    }else{
        print "\n\n*** did not find sender ip\n";
    }
}

sub check_input{
    my @parameters  = @_;

    if(scalar(@parameters)>0){

    }else{
        print "\n*** add header.txt file, please!\n";
        exit(1);
    }
    my $file = $parameters[0];
    if(-e $file){

    }else{
        print "\n*** input file does not exist\n\n";
        exit(1);
    }
    return $file;
}

sub read_header{
    my $file  = $_[0];
    open(my $FILE, '<', $file);
    my @headerlines = <$FILE>;
    close($FILE);
    return @headerlines;
}

sub get_ips{
    my @headerlines= @_;

    my @ips;
    foreach my $line(@headerlines){
        chomp($line);
        if($line =~ m/Received/ && $line=~ m/from/i){
            if ($line =~ /(\d+\.\d+\.\d+\.\d+)/){
                my $ip = $1;
                push(@ips, $ip);
            }
        }
    }   
    return @ips;
}
