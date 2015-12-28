#!/usr/bin/perl
use strict;
use warnings;
use Test::More ;
use File::Basename;

return 1  unless $0 eq __FILE__;
main(@ARGV) if $0 eq __FILE__;

sub mock_gzip{
    my $file = $_[0];
    my $cmd;
    $cmd = "gzip -f $file";
    to_sys($cmd,1)
}
sub mock_gunzip{
    my $file = $_[0];
    my $cmd;
    $cmd = "gunzip -f $file";
    to_sys($cmd,1);
}
sub fileowner{
    my $file = $_[0];
    my $uid = `stat -c %u $file`;
    chomp($uid);
    return $uid;
}
sub get_inode{
    my $file =$_[0];
    my $inode = `stat -c %i $file`;
    chomp($inode);
    return  $inode;
}
sub to_sys{
    my ($cmd,$run) = @_;
    print "***$cmd\n";
    if($run){
        system($cmd);
    }
}
sub main{
    #simulate real life situation - user A
    my $file = "/shared/shared/colourbar.nii.gz";
    my $dirname = dirname($file);
    my $basename = fileparse($file);

    my $fileu = $file;
    $fileu =~ s/.gz$//g;
    ok(-e $file,"$file Found\n");
    my $fileowner = fileowner($file);
    ok($fileowner>0,"$file -- fileowner <$fileowner>\n");
    my $inode  = get_inode($file);
    ok($inode>0,"$file -- inode <$inode>\n");

    # user B - gunzip/gzip owner changed
    # in tmp
    my $cmd = "cp -vf $file /tmp";
    to_sys($cmd,1);
    my $file_tmp = "/tmp/$basename";
    my $file_tmpu = $file_tmp;
    $file_tmpu =~ s/.gz$//g;

    mock_gunzip($file_tmp);
    mock_gzip($file_tmpu);
    my $fileowner_tmp = fileowner($file_tmp);
    ok($fileowner_tmp>0,"$file_tmp -- fileowner <$fileowner_tmp>\n");
    my $inode_tmp  = get_inode($file_tmp);
    ok($inode_tmp>0,"$file_tmp -- inode <$inode_tmp>\n");

    $cmd= "cp -vf $file_tmp $dirname";
    to_sys($cmd,1);

    my $fileowner_gzip = fileowner($file);
    ok($fileowner_gzip==$fileowner,"$file -- fileowner <$fileowner_gzip>\n");
    my $inode_gzip  = get_inode($file);
    ok($inode_gzip==$inode,"$file -- inode <$inode_gzip>\n");

    # solution, or verified no solution to be decided

}
