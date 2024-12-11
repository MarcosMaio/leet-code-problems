<?php 

$nums = [2,11,15,7];

$target = 9;

for ($i=0; $i < count($nums); $i++) { 
  for ($j=1; $j < count($nums); $j++) { 
      if($nums[$i] + $nums[$j] == $target) {
        echo $i .','. $j;
      }
  }
}