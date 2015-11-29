use strict;
use warnings;

=head1 NAME

DirFormat - The great new DirFormat!

=head1 VERSION

Version 0.01

=cut

our $VERSION = '0.01';

=head1 SYNOPSIS


=head1 EXPORT


=head1 SUBROUTINES/METHODS

=head2 recursive_dir

=cut

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
=head2 format_dir

=cut

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
=head2 format_file

=cut

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

=head2 get_dirs

=cut

sub get_dirs{
    my $dir = shift;
    my @lists = `find $dir -mindepth 1 -maxdepth 1 -type d`;

    return @lists;
}

=head2 get_lists

=cut

sub get_lists{
    my $dir = shift;
    my @lists = `find $dir -mindepth 1 -maxdepth 1 -type f`;
    return @lists;
}



=head1 AUTHOR

Gang Liang, C<< <gang.liang.2011 at gmail.com> >>

=head1 BUGS

Please report any bugs or feature requests to C<bug-dirtree at rt.cpan.org>, or through
the web interface at L<http://rt.cpan.org/NoAuth/ReportBug.html?Queue=DirFormat>.  I will be notified, and then you'll
automatically be notified of progress on your bug as I make changes.




=head1 SUPPORT

You can find documentation for this module with the perldoc command.

    perldoc DirFormat


You can also look for information at:

=over 4

=item * RT: CPAN's request tracker (report bugs here)

L<http://rt.cpan.org/NoAuth/Bugs.html?Dist=DirFormat>

=item * AnnoCPAN: Annotated CPAN documentation

L<http://annocpan.org/dist/DirFormat>

=item * CPAN Ratings

L<http://cpanratings.perl.org/d/DirFormat>

=item * Search CPAN

L<http://search.cpan.org/dist/DirFormat/>

=back


=head1 ACKNOWLEDGEMENTS


=head1 LICENSE AND COPYRIGHT

Copyright 2015 Gang Liang.

This program is free software; you can redistribute it and/or modify it
under the terms of the the Artistic License (2.0). You may obtain a
copy of the full license at:

L<http://www.perlfoundation.org/artistic_license_2_0>

Any use, modification, and distribution of the Standard or Modified
Versions is governed by this Artistic License. By using, modifying or
distributing the Package, you accept this license. Do not use, modify,
or distribute the Package, if you do not accept this license.

If your Modified Version has been derived from a Modified Version made
by someone other than you, you are nevertheless required to ensure that
your Modified Version complies with the requirements of this license.

This license does not grant you the right to use any trademark, service
mark, tradename, or logo of the Copyright Holder.

This license includes the non-exclusive, worldwide, free-of-charge
patent license to make, have made, use, offer to sell, sell, import and
otherwise transfer the Package with respect to any patent claims
licensable by the Copyright Holder that are necessarily infringed by the
Package. If you institute patent litigation (including a cross-claim or
counterclaim) against any party alleging that the Package constitutes
direct or contributory patent infringement, then this Artistic License
to you shall terminate on the date that such litigation is filed.

Disclaimer of Warranty: THE PACKAGE IS PROVIDED BY THE COPYRIGHT HOLDER
AND CONTRIBUTORS "AS IS' AND WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES.
THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE, OR NON-INFRINGEMENT ARE DISCLAIMED TO THE EXTENT PERMITTED BY
YOUR LOCAL LAW. UNLESS REQUIRED BY LAW, NO COPYRIGHT HOLDER OR
CONTRIBUTOR WILL BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, OR
CONSEQUENTIAL DAMAGES ARISING IN ANY WAY OUT OF THE USE OF THE PACKAGE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


=cut

1; # End of DirFormat
