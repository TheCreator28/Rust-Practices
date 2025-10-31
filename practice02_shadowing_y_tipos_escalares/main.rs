// Practica 02: Shadowing y tipos escalares
// Objetivo: Comprender el shadowing y repasar tipos escalares basicos.
pub fn get_typename<T>(_: &T) -> String {
    std::any::type_name::<T>().to_string()
}

fn main() {
    // Paso 1: Crea una variable `let` llamada `valor` y reasignala con shadowing para convertir un entero en cadena.
    // Paso 2: Imprime cada version de `valor` con `println!` mostrando su tipo mediante anotaciones.
    // Paso 3: Declara ejemplos de `i32`, `u8`, `f64` y `bool`, luego muestra sus valores.
    // Paso 4: Explica en comentarios cuando preferirias shadowing en lugar de `let mut`.

    // Escribe tu solucion aqui siguiendo los pasos anteriores.
    let value = 10;
    println!("Outside the block: {} - Tipo {:?}", value, get_typename(&value));
    {
        let value = value.to_string();
        println!("Inside the block: {} - Tipo {:?}", value, get_typename(&value));
    }

    let myi32 = 20;
    let myu8 = 30;
    let myf32 = 3.1416;
    let mybool = true;

    println!("{:?}: {}", get_typename(&myi32), myi32);
    println!("{:?}: {}", get_typename(&myu8), myu8);
    println!("{:?}: {}", get_typename(&myf32), myf32);
    println!("{:?}: {}", get_typename(&mybool), mybool);
}
