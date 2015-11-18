# credit to Kurt in stackoverflow
# modfied a bit, if there is any bad pratice, it is mine
use strict;
use warnings;

use FindBin qw($Bin);
use lib "$Bin/../lib";

use Test::More qw(no_plan);


BEGIN {use_ok('Test::Foo') };

require_ok("Test::Foo");

# hello()
my $helloCall = Test::Foo::hello();
my $hello_str = "Kurt W. Leucht, good example!";

like($helloCall, qr/Kurt/,"hello() RE test");

is($helloCall, $hello_str, "hello() IS test");

# test bye() 
my $input;

my $bye = Test::Foo::bye($input);
is($bye, "StackOverflow", "bye() $bye");

$input = "github";
$bye = Test::Foo::bye($input);
is($bye, $input, "bye() $bye");
# repeat()

for(my $count =1; $count<11; $count++){
    my $repeatCall = Test::Foo::repeat();
    is($repeatCall, 1, "repeat() IS test");
}

# argumentation()
my $argumentationCall;
my @args;

push(@args, undef);
push(@args, "true");
push(@args, "false");
push(@args, "123");

my $result;
foreach my $arg(@args){
    $result = $arg;
    $argumentationCall = Test::Foo::argumentTest($arg);
    if($arg){
        if($arg eq "123"){
            $result = "unknown";
        }
    }else{
        $result = "null or 0";
    }
    is($argumentationCall, $result, "argumentTest() IS $argumentationCall test");
}

