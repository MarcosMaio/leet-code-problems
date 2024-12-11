<?php

$n = 10;
$sequencia = [];

for ($i = 0; $i < $n; $i++) {
  if (empty($sequencia)) {
    $sequencia[] = $i;
    $sequencia[] = $i + 1;
  }

  if (count($sequencia) > 1) {
    $numero_sequencia = $sequencia[$i] + $sequencia[$i + 1];
    $sequencia[] = $numero_sequencia;
  }
}

echo implode(', ', $sequencia);



// $n = 10;
// $sequencia = [0, 1]; 

// for ($i = 2; $i < $n; $i++) {
//     $sequencia[] = $sequencia[$i - 1] + $sequencia[$i - 2];
// }

// echo implode(', ', $sequencia);
