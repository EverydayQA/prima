package DirTree;

use 5.006;
use strict;
use warnings FATAL => 'all';

=head1 NAME

DirTree - The great new DirTree!

=head1 VERSION

Version 0.01

=cut

our $VERSION = '0.01';

=head2 new

=cut

sub new{
    my $class = shift;
    my $self = {
        _directory =>shift,
        _depth=>shift,
        _files_aref=>shift

    };
    bless $self, $class;
    return $self;
}


=head1 SYNOPSIS

Quick summary of what the module does.

Perhaps a little code snippet.

    use DirTree;

    my $foo = DirTree->new();
    ...

=head1 EXPORT

A list of functions that can be exported.  You can delete this section
if you don't export anything, such as for a purely object-oriented module.

=head1 SUBROUTINES/METHODS

=head2 get_directory

=cut

sub get_directory {
    my ($self) = @_;
    return $self->{_directory};
}


=head2 get_depth
    # fixed depth - do not change
=cut

sub get_depth {
    my ($self) = @_;
    return $self->{_depth};
}

=head2 get_files
    not being used - 
=cut

sub get_files {
    my ($self) = @_;
    return $self->{_files_aref};
}

=head2 set_files
    not being used
=cut

sub set_files {
    my ($self) = @_;

    my @files = `find $self->{_directory} -maxdepth 1 -type f`;
    $self->{_files} = \@files;
}


=head1 AUTHOR

Gang Liang, C<< <gang.liang.2011 at gmail.com> >>

=head1 BUGS

Please report any bugs or feature requests to C<bug-dirtree at rt.cpan.org>, or through
the web interface at L<http://rt.cpan.org/NoAuth/ReportBug.html?Queue=DirTree>.  I will be notified, and then you'll
automatically be notified of progress on your bug as I make changes.




=head1 SUPPORT

You can find documentation for this module with the perldoc command.

    perldoc DirTree


You can also look for information at:

=over 4

=item * RT: CPAN's request tracker (report bugs here)

L<http://rt.cpan.org/NoAuth/Bugs.html?Dist=DirTree>

=item * AnnoCPAN: Annotated CPAN documentation

L<http://annocpan.org/dist/DirTree>

=item * CPAN Ratings

L<http://cpanratings.perl.org/d/DirTree>

=item * Search CPAN

L<http://search.cpan.org/dist/DirTree/>

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

1; # End of DirTree
