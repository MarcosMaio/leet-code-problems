

<?php
  $nums = [-4,-2,1,4,8];
  // $nums_positive = array_map('abs', $nums);
  // $lower_num = "";

  // foreach ($nums_positive as $key => $value) {

  //     if($lower_num == "") {
  //       $lower_num = $value;
  //     } else {
  //       if($value < $lower_num) {
  //         $lower_num = $value;
  //       }
  //     }
  // };

  // echo $lower_num;


  // function findClosestNumber($nums) {
  //   $nums_positive = array_map('abs', $nums);
  //   $lower_num = min($nums_positive);
  //   return $lower_num;
  // }


  // function findClosestNumber2($nums) {
  //   return min(array_map('abs', $nums));
  // }
  

  // findClosestNumber($nums);
  // findClosestNumber2($nums);


  // $nums = [-4,-2,1,4,8];
  // $nums_positive = array_map('abs', $nums);
  // $lower_num_close_to_zero = "";

  // foreach ($nums as $key => $value) {
  //   if($lower_num_close_to_zero == "") {
  //     $lower_num_close_to_zero = $value;
  //   } else {
  //     if(abs($value) < abs($lower_num_close_to_zero)) {
  //       $lower_num_close_to_zero = $value;
  //     }
  //   }
  // };

  // echo $lower_num_close_to_zero;


  function findClosestNumber($nums) {
    $lower_num_close_to_zero = "";
    foreach ($nums as $key => $value) {
        if($lower_num_close_to_zero == "") {
            $lower_num_close_to_zero = $value;
        } else {
            if(abs($value) == abs($lower_num_close_to_zero)) {
                $lower_num_close_to_zero = max($value,$lower_num_close_to_zero,);
            } else if(abs($value) <= abs($lower_num_close_to_zero)) {
                $lower_num_close_to_zero = $value;
            }
        }
    }
    echo $lower_num_close_to_zero;
}

findClosestNumber($nums);