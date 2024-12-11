<?php

$x = 121;

function isPalindrome($x) {
    $string_convertion = strval($x);

    $string_invertion = strrev($string_convertion);

    $number_invertion = intval($string_invertion);
  
    return $x == $number_invertion;
}

if (isPalindrome($x)) {
  echo 'true';
} else {
  echo 'false';
}




// $x = 121;

// function isPalindrome($x) {
//     return $x == strrev($x);

//     return false;
// }

// if (isPalindrome($x)) {
//   echo 'true';
// } else {
//   echo 'false';
// }