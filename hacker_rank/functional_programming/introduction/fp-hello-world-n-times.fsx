open System

let rec fn N =
    match N with
        |0 -> ()
        |N ->
            printf "Hello World\n"
            fn (N-1)

[<EntryPoint>]
let main argv =
    let N = int (Console.ReadLine().Trim())
    fn N
    0
