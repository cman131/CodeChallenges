<?php
  $columnCount = $argv[1];
  $colWidth = $argv[2];
  $file = fopen($argv[3], "r");
  $text = fread($file, filesize($argv[3]));

  $colSize = (strlen($text)/$columnCount);
  $result = "";
  for($i=0; $i<$colSize/$colWidth; $i++){
    for($col=0; $col<$columnCount; $col++){
      $result.=substr($text, intval($i*$colWidth+$col*$colSize), $colWidth);
      if($col!=$columnCount-1){
        $result.=" | ";
      }
    }
    $result.="\n";
  }

  echo $result;
