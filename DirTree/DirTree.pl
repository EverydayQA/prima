use strict;
use warnings;

use Cwd;
use FindBin qw($Bin);
use lib "$Bin/lib";

use DirTree;

my $cwd = getcwd();

# subs to get dirs/files/depth
my @lists = get_lists($cwd);

# print without formatting
my $obj = DirTree->new($cwd,1,\@lists);

my $dir = $obj->get_directory();
my $depth = $obj->get_depth();

my $files_aref = $obj->get_files();
foreach my $file(@$files_aref){
    chomp($file);
    if(-d $file){
        print "recursive_dir($file)\n";
    }else{
        print "formating($file)\n";
    }
}

sub get_lists{
    my $dir = shift;
    my @lists = `find $dir -maxdepth 1`;

    return @lists;
}
# formating - skip


