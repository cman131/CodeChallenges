<?php
// Input
$word1 = "because";
$word2 = "cause";
if(isset($argv[1])){
	$word1 = $argv[1];
	$word2 = $argv[2];
}

// Start program
$word1 = str_split($word1);
$word2 = str_split($word2);

$word1tionary = array();
for($i = 0; $i<count($word1); $i++){
	$cur = $word1[$i];
	if(isset($word1tionary[$cur])){
		$word1tionary[$cur]+=1;
	}
	else{
		$word1tionary[$cur]=1;
	}
}

$score1 = 0;
$score2 = 0;

for($i = 0; $i<count($word2); $i++){
	$cur = $word2[$i];
	if(!isset($word1tionary[$cur]) || $word1tionary[$cur]==0){
		$score2 +=1;
	}
	else{
		$word1tionary[$cur]-=1;
	}
}

foreach($word1tionary as $key => $val){
	$score1+=$val;
}

print "Player1: $score1\nPlayer2: $score2\n";

?>
