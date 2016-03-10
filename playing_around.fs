let rec sum (lst, acc) = 
    match lst with
        |head :: tail -> (tail, acc + head) |> sum
        |[] -> acc

assert (([0 .. 100], 0) |> sum = 5050);; // Expected 5050 :3

let rec mul (lst, acc) = 
    match lst with
        |head :: tail -> (tail, acc * head) |> mul
        |[] -> acc

assert (([0 .. 100], 1) |> mul = 0);;

//let sum_mul lst = ((lst,0) |> sum, (lst,1) |> mul);;
//[0 .. 100] |> sum_mul;;

let rec len (lst, acc) =
    match lst with
        |head :: tail -> (tail, (acc+1)) |> len
        |[] -> acc;;

assert (([0 .. 100], 0) |> len = 101);; // Expected 101

let append (lst0, lst1) = lst0 @ lst1;;

let rec append (lst0, lst1) =
    match lst1 with
        |[] -> lst0
        |head :: tail -> append(lst0 @ [head], tail);;

assert (([0 .. 50], [51 .. 100]) |> append = [0 .. 100]);;

let rec rev lst =
    match lst with
        |[] -> []
        |head :: tail -> (tail |> rev) @ [head];;
assert ([0 .. 50] |> rev = [50 .. -1 .. 0]);;

let rec is_member (lst, x) =
    match lst with
        |head :: tail -> if head=x then true
                         else is_member(tail, x)
        |[] -> false

assert (([0 .. 50], 35) |> is_member = true);;
assert (([0 .. 50], 100) |> is_member = false);;
