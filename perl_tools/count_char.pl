#/usr/bin/perl -w
use strict;
return 1 unless $0 eq __FILE__;
main() if $0 eq __FILE__;
sub main{
    my $str = "ru8xysyyyyyyysss6s5s";
    my $char = "y";
    my $count = count_occurrence($str, $char);
    my $count2 = () = $str =~ /$char/g;
    my $count3 = `fold -w 1 <<< $str|grep -c $char`;
    chomp($count3);
    my $count4 = `grep -o $char <<< $str|wc -l`;
    chomp($count4);
    my $count5 = () = $str =~ /\Q$char\E/gms;
    print "count<$count> <$count2> <$count3> <$count4> <$count5>  of <$char> in <$str>\n";   
}
sub count_occurrence{
    my ($str, $char) = @_;
    my $len = length($str);
    $str =~ s/$char//g;
    my $len_new = length($str);
    my $count = $len - $len_new;
    return $count;
}
