// Practica 01: Fundamentos de variables y mutabilidad
// Objetivo: Reforzar declaraciones basicas, mutabilidad y constantes.

fn main() {
    // Paso 1: Declara una variable inmutable `let` con tu nombre y muestrala con `println!`.
    let name = "Hernan Cortez".to_string();
    println!("My name is: {}", name);

    // Paso 2: Declara una variable mutable `let mut` con una edad y actualizala dentro del mismo `main`.
    let mut _age = 25;
    _age = 18;

    // Paso 3: Define una constante `const` para la cantidad de meses del anio y utiliza su valor en una salida.
    const MONTHS: i32 = 12;
    println!("The year has {} months", MONTHS);

    // Paso 4: Usa comentarios para explicar cuando elegir una variable mutable, inmutable o constante.
    /*
    "let" crea una variable inmutable cuyo valor se fija al evaluarse y no puede cambiar.
    "let mut" habilita mutabilidad sobre esa misma idea: la variable sigue siendo local al scope, 
    pero puedes reasignarla cuantas veces necesites.
    "const" define un valor constante con tipo declarado explícitamente; se evalúa en compilación, no admite mutabilidad 
    ni puede depender de resultados calculados en tiempo de ejecución, y su alcance es global por defecto si es pub.
     */
}
