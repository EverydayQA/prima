use strict;
use warnings;
1;

sub recursive_dir{
    my $dir = $_[0];
    my $depth = $_[1];


    my @lists = get_lists($dir);
    my $obj = DirTree->new($dir,$depth,\@lists);
    $dir = $obj->get_directory();
    $depth = $obj->get_depth();
    my $files_aref = $obj->get_files();

    # current dir
    format_dir($dir, $depth);
    foreach my $file(@$files_aref){
        chomp($file);
        format_file($file, $depth);
    }

    my @subdirs = get_dirs($dir);
    if(scalar(@subdirs)<=1){
        return;
    } 
    foreach  my $subdir(@subdirs){
        chomp($subdir);
        if(-d $subdir){

        }else{
            next;
        }
        recursive_dir($subdir, $depth);
    }
}
sub format_dir{
    my ($file, $depth) = @_;
    my $fileparse = fileparse($file);

    my @splits = split(/\//, $file);
    my $margin = scalar(@splits) - $depth;
    $margin = ($margin)*2;
    my $i=0;
    my $str = "__";
    while($i<=$margin/2){
        $i++;
        $str = "_${str}";
    }

    $fileparse = "${str}${fileparse}";
    my $line = sprintf("%-50s",$fileparse);
    print "$line\n";

    return $fileparse;
}

sub format_file{
    my ($file, $depth) = @_;
    my $fileparse = fileparse($file);

    my @splits = split(/\//, $file);
    my $margin = scalar(@splits) - $depth;
    $margin = $margin*2;
    my $i=0;
    my $str = "|__";
    while($i<=$margin){
        $i++;
        $str = " ${str}";
    }

    $fileparse = "${str}${fileparse}";
    my $line = sprintf("%-50s",$fileparse);
    print "$line\n";

    return $fileparse;
}
sub get_dirs{
    my $dir = shift;
    my @lists = `find $dir -mindepth 1 -maxdepth 1 -type d`;

    return @lists;
}

sub get_lists{
    my $dir = shift;
    my @lists = `find $dir -mindepth 1 -maxdepth 1 -type f`;

    
    return @lists;
}

