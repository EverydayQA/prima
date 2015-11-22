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

    foreach my $file(@$files_aref){
        chomp($file);
        if(-d $file){
            if($file eq $dir){
                format_dir($file, $depth);

            }else{
                recursive_dir($file, $depth);
            }
        }else{
            format_file($file, $depth);
        }
    }
}
sub format_dir{
    my ($file, $depth) = @_;
    my $fileparse = fileparse($file);

    my @splits = split(/\//, $file);
    my $margin = scalar(@splits) - $depth;
    $margin = ($margin)*2;
    my $i=0;
    my $str = "+--";
    while($i<=$margin/2){
        $i++;
        $str = " ${str}";
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
    my $str = "|--";
    while($i<=$margin){
        $i++;
        $str = " ${str}";
    }

    $fileparse = "${str}${fileparse}";
    my $line = sprintf("%-50s",$fileparse);
    print "$line\n";

    return $fileparse;
}

sub get_lists{
    my $dir = shift;
    my @lists = `find $dir -maxdepth 1`;

    return @lists;
}

