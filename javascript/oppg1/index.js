let A = 4*2
let B = 40/6
let C = A-B

console.log(A, B, C);

let isasleep = false 
let istierd = true


if (istierd == true)
{
    console.log("go to sleep")
    isasleep = true
    istierd = false
    }
else if(istierd == false){
    if (isasleep == true)
        console.log("wake up")
        isasleep= false
    }
    else{
        console.log("have fun")
    }

let rainy = false
let clody = false


if (clody == true){
    if (rainy == true) 
        console.log("wear rain boots");
    else {
        console.log("wear sneaker");
    }
}
else {
    console.log("wear slippers");
}



