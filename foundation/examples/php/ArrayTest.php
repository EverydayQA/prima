<?php
class ArrayTest extends PHPUnit_Framework_TestCase {
    public function testPushAndPop(){
        // allocaate a tesst fixture
        $fixture = array();
        // assert initally empty, count() is 0
        //
        $this->assertEquals(0,count($fixture));

        // tet array_push()
        // push an item into array
        array_push($fixture,'foo');
        // assert one item, count is 1
        $this->assertEquals(1,count($fixture));

        // assert item pushed
        $this->assertEquals('foo',$fixture[count($fixture)-1]);

        //test array_pop()
        $this->assertEquals('foo',array_pop($fixture));
        $this->assertEquals(0,count($fixture));
    }
}
?>
        



