#!/usr/bin/perl
use UNIVERSAL 'isa';

my @array = (1,2,3);
my $aref = \@aref;
my %hash;
$hash{'red'}=1;
$hash{'green'}=2;
my $href = \%hash;
if(ref $href eq ref){
    print "href is ref\n";
}
if(ref %hash eq ref){
    print "hash is ref\n";
    print %hash;
    print "\n";
}
if(ref $aref eq ref){
    print "aref is ref\n";
}
if(ref @array eq ref){
    print "array<@array> is ref\n";
}

my @types = ("HASH","ARRAY","SCALAR");
my @refs = ($aref,$href);
foreach my $ref (@refs){
    foreach my $type(@types){
        my $yes = isa($ref,$type);
        print "$ref is $type, $yes\n";
    }   
}

my %hash_of_array;
$hash_of_array{"a"} = @types;
$hash_of_array{"b"} = @array;
print %hash_of_array;
print "\n";

my @twod;
$twod[0] = $href;
$twod[1] = $href;
my $twod_aref = \@twod;
print "<$towd_aref>\n";


