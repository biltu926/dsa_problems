/* 
Problem link: https://www.hackerrank.com/challenges/insertionsort1/problem.

*/

func insertionSort1(n int32, arr []int32) {
    var temp int32 = arr[len(arr) - 1];
    var placed bool = false;
    
    for i:=n-1; i>0; i-- {
        if arr[i-1] < temp {
            arr[i] = temp;
            placed = true;
            break
        }else{
            arr[i] = arr[i-1];
        }
        for _, value:= range arr {
         fmt.Printf("%v ", value)
       }
       fmt.Printf("\n")
    }
    
    if temp<arr[0] {
        arr[0] = temp;
        placed = true;
    }

    if placed == true {
        for _, value:= range arr {
         fmt.Printf("%v ", value)
       }
       fmt.Printf("\n")
    }

}