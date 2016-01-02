#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper;

my $PolymerSize=6;

# each monomer/node can bond upto 3 times
my $maxNeighbors=3;

#Store coordinates and number of neighbors for each  monomer/node
# (in C would be an array of structs)

my %HoA;
my %BondHoA; #who are my neighbors
my @coordsNeighbors;
my $element; #Iteration dummy variable
my %dist; #temporary distance hash
my $return_flag;

$coordsNeighbors[0]=0; #Xcoord
$coordsNeighbors[1]=0; #YCoord
$coordsNeighbors[2]=0; #ZCoord
$coordsNeighbors[3]=0; #How many bonded neighbors?

#Intialize origin (first node/monomer)
push @{$HoA{0}}, $coordsNeighbors[0];
push @{$HoA{0}}, $coordsNeighbors[1];
push @{$HoA{0}}, $coordsNeighbors[2];
push @{$HoA{0}}, $coordsNeighbors[3];

#Generate new nodes/monomer and "grow" polymer
do{
    for(my $j=0;$j<3;$j++){
        #generate coords of potent. monomers/node
        $coordsNeighbors[$j] = int($PolymerSize*rand());
    }

    $coordsNeighbors[3]=0;

    #loop through existing monomers/nodes
    foreach $element ( keys %HoA) {
        #if this monomer doesn't have the max bonds proceed
        if( ($HoA{$element}[3])!=$maxNeighbors) {
            my $tempx=$HoA{$element}[0]-$coordsNeighbors[0];
            my $tempy=$HoA{$element}[1]-$coordsNeighbors[1];
            my $tempz=$HoA{$element}[2]-$coordsNeighbors[2];

            #make hash of L1 distances
            $dist{$element} .=abs($tempx)+abs($tempy)+abs($tempz);
        }
    }

    #check if any distance is != 1; no-bond could be made if so
    foreach(keys %dist){
        if($dist{$_}!=1) {
            delete $dist{$_};
        }
    }

    #potential monomer is good, so add to HoA and update bonds
    foreach $element (keys %dist){
        $HoA{$element}[3]++;
        my $newKey=scalar (keys %HoA);
        if($newKey <=($PolymerSize-1)){
            push @{$HoA{$newKey}}, $coordsNeighbors[0];
            push @{$HoA{$newKey}}, $coordsNeighbors[1];
            push @{$HoA{$newKey}}, $coordsNeighbors[2];
            push @{$HoA{$newKey}}, $coordsNeighbors[3]+1;
            push @{$BondHoA{$element}}, "$newKey";
            push @{$BondHoA{$newKey}}, "$element";
        }
        delete $dist{$element};
    }

} while((keys %HoA)<=$PolymerSize-1);

# not ordered
# missing 1 line
my @elements;
foreach $element (keys %HoA) {
    push(@elements, $element);
}

my @elements_new = sort(@elements);
foreach $element (@elements_new) {
    print "$element \t $HoA{$element}[0] \t $HoA{$element}[1] \t $HoA{$element}[2]\n";
}

