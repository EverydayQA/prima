
#!usr/bin/perl

use strict;
use warnings;
use File::Basename;
use IO::Handle;
my $file ='/home/abhishek/Videos/lua.mp4';
$file = "/home/gliang/Downloads/Burn.Notice.S07E08.HDTV.x264-EVOLVE.mp4";
my $base = File::Basename::dirname($file);

my $size = -s "$file";
my $begin=0;
my $end=$size;
(my $name, my $dir, my $ext) = fileparse($file, qr/\.[^.]*/);
open (my $fh, '<', $file)or die "can't open $file: $!";
binmode $fh;
my $content_length = $end - $begin;
print "Content-Type: text/html\r\n";
print "Content-Type: application/x-vlc-plugin\r\n";
print "Cache-Control: public, must-revalidate, max-age=0\r\n";
print "Pragma: no-cache\r\n" ;
print "Accept-Ranges: bytes\r\n";
print "Content-Length: $content_length", "\r\n";
print "Content-Range: bytes ${begin}-${end}/${size}\r\n";
print "Content-Disposition: inline; filename=\"$name$ext\"\r\n";
print "Content-Transfer-Encoding: binary\r\n";
print "Connection: close\r\n"; 
print "\r\n";
=start
print "Content-Type: application/x-vlc-plugin \n";
print "Cache-Control: public, must-revalidate, max-age=0";
print "Pragma: no-cache" ;
print "Accept-Ranges: bytes";
print "Content-Length:  $end - $begin\n\n";
print "Content-Range: bytes $begin'-'$end'/'$size";
print "Content-Disposition: inline; filename=\"$name$ext\"\n";
print "Content-Transfer-Encoding: binary";
print "Connection: close"; 
=cut
my $cur=$begin;
seek($fh,$begin,0);
while(!eof($fh) && $cur < $end)
{
    my $buf=1024*16;
    read $fh, $buf, $end-$cur;
    $cur+=1024*16;
    #print $buf;
}
close $fh;
STDOUT->autoflush;

