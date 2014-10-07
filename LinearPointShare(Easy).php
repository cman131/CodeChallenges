<?php
// Input
$equation1 = "y=2x+2";
$equation2 = "y=5x-4";

// Start program
$equation1 = explode('x', explode('=', $equation1)[1]);
$equation2 = explode('x', explode('=', $equation2)[1]);

$eq1 = (object) array('m' => intval($equation1[0]), 'b' => intval($equation1[1]));
$eq2 = (object) array('m' => intval($equation2[0]), 'b' => intval($equation2[1]));
if($eq1=>m - $eq2=>m != 0){
    $x = ($eq2=>b - $eq1=>b) / ($eq1=>m - $eq2=>m);
    $y = $eq1=>m * $x + $eq1=>b;
    echo "<h1>Answer: (" . $x . "," . $y . ")</h1>";
}
else{
    echo "</h1>No Solution(Parellel)<h1>";
}
?>