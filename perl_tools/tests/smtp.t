#!/usr/bin/perl -w
use strict;
use warnings;
use Net::SMTP;
use Test::More;


my $smtp = Net::SMTP->new('smtp.gmail.com',
                           Hello => 'my.mail.domain',
                           Timeout => 10,
                           Debug   => 1,
                           SSL     => 1,

                          );
ok($smtp, "set smtp new()\n");

my $uid = "gliang"; 
if($smtp){

}else{
    exit(1);
}
ok($smtp->mail($uid), "smtp_mail set from\n");
$smtp->quit;

exit(0);

if ($smtp->to('postmaster')) {
 $smtp->data();
 $smtp->datasend("To: postmaster\n");
 $smtp->datasend("\n");
 $smtp->datasend("A simple test message\n");
 $smtp->dataend();
} else {
 print "Error: ", $smtp->message();
}

$smtp->quit;

=start
Gmail SMTP server address: smtp.gmail.com
Gmail SMTP user name: Your full Gmail address (e.g. example@gmail.com)
Gmail SMTP password: Your Gmail password
With Gmail 2-step authentication enabled, use an application-specific Gmail password.
Gmail SMTP port (TLS): 587
Gmail SMTP port (SSL): 465
Gmail SMTP TLS/SSL required: yes
=cut

