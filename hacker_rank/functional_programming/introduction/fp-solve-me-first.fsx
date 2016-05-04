open System

[<EntryPoint>]
let main argv =
    let a = int (Console.ReadLine())
    let b = int (Console.ReadLine())
    printf "%d\n" (a + b)
    0
