//COUNT SORT
// FIND THE MAX
//CREATE A COUNT ARRAY
//CALCLATE THE FREQUENCY OF ALL ELEMEENTS
//CUMALITE FREQ
//CREATE O P ARRAY

//RADIX SORT
/*
-->Non-Comparision algo
-->multi-digit no
-->constant length strings
--> Inspired BY bucket sort

Example array : {325 , 426 , 012 , 003 , 032}


S1 : Calulate max : 426
    This has how many digits ? = 3
    so 3 PASSES

S2 : Create 0 - 9 10buckets              {0 , 1 , 2 , 3, 4, 5, 6, 7, 8, 9}
    checking units place position        

    P1: [012, 032, 003, 325, 426 ]
    P2 :[003, 012, 325, 426, 032 ]
    P3 :[003, 012, 032, 325, 426 ]

    HOW DO YOU CONTROL THE NUMBER OF PASSES IN RADIX SORT

    for (int exp = 1; ,max/exp > 0 ; exp *= 10){
        countsort(arr,size,exp);
    }
        here exp = 426
        so, exp = 1 ; max/exp = 426 ; exp = 10;
        so, exp = 10 ; max/exp = 42 ; exp = 100;
        so, exp = 100 ; max/exp = 4 ; exp = 1000;
        for loop stops after this one

    SO WE CAN CONTROL THE NUMBER OF PASSES IN RADIX SORT WITH THE LENGTH OF THE MAX VALUE


*/