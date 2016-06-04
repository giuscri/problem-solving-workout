open System

let replicate n lst =
    let rec fn n x =
        match n with
        | 0 -> []
        | n when n < 0 -> invalidArg "n" "Can't compute with negative numbers."
        | n -> x::(fn (n - 1) x)

    List.fold (fun acc el -> acc @ (fn n el)) [] lst

let rec fn lst =
    match lst with
    | [] -> ()
    | x::xs ->
        do printf "%d\n" x
        do fn xs

[<EntryPoint>]
let main argv =
    let S = int(Console.ReadLine())

    let lines =
        Seq.initInfinite (fun _ -> Console.ReadLine())
        |> Seq.takeWhile (fun line -> line <> null)

    let lst = [ for line in lines -> int(line) ]

    let res = replicate S lst

    do fn res

    0
