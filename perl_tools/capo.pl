#!perl
use strict;
use warnings;
my $filename = $ARGV[0];
open(INPUT_FILE, $filename)
    or die "Couldn't open $filename for reading!";
while (<INPUT_FILE>) {
        my $currentLine = $_;   
        # Remove empty lines and lines that start with digits
        if ($currentLine =~ /^[\s+|\d+]/){
            next;
        }

        # Remove all carriage returns
        $currentLine =~ s/\R$/ /;

        # Convert all letters to lower case
        $currentLine =~ s/([A-Z])/\l$1/g;

        # Capitalize after period <= STEP THAT DOES NOT WORK
        $currentLine =~ s/\.\s([a-z])/\. \u$1/g;        

        print $currentLine;
}
close(INPUT_FILE);
