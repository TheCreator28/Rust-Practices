from __future__ import annotations

import re
import unicodedata
from pathlib import Path


def slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "_", ascii_text.lower()).strip("_")
    return slug or "practica"


practices = [
    {
        "title": "Fundamentos de variables y mutabilidad",
        "goal": "Reforzar declaraciones basicas, mutabilidad y constantes.",
        "steps": [
            "Paso 1: Declara una variable inmutable `let` con tu nombre y muestrala con `println!`.",
            "Paso 2: Declara una variable mutable `let mut` con una edad y actualizala dentro del mismo `main`.",
            "Paso 3: Define una constante `const` para la cantidad de meses del anio y utiliza su valor en una salida.",
            "Paso 4: Usa comentarios para explicar cuando elegir una variable mutable, inmutable o constante.",
        ],
    },
    {
        "title": "Shadowing y tipos escalares",
        "goal": "Comprender el shadowing y repasar tipos escalares basicos.",
        "steps": [
            "Paso 1: Crea una variable `let` llamada `valor` y reasignala con shadowing para convertir un entero en cadena.",
            "Paso 2: Imprime cada version de `valor` con `println!` mostrando su tipo mediante anotaciones.",
            "Paso 3: Declara ejemplos de `i32`, `u8`, `f64` y `bool`, luego muestra sus valores.",
            "Paso 4: Explica en comentarios cuando preferirias shadowing en lugar de `let mut`.",
        ],
    },
    {
        "title": "Conversion de tipos y formato",
        "goal": "Practicar conversiones basicas y formato de cadenas.",
        "steps": [
            "Paso 1: Solicita al usuario un numero usando `std::io` y almacenalo en una cadena.",
            "Paso 2: Usa `trim` y `parse::<i32>()` para convertir la cadena a entero manejando posibles errores con `expect`.",
            "Paso 3: Muestra el numero en formato binario, hexadecimal y cientifico usando especificadores de `println!`.",
            "Paso 4: Anota en comentarios que pasa si el parse falla y como podrias manejarlo sin `expect`.",
        ],
    },
    {
        "title": "Condicionales con if y else",
        "goal": "Reforzar condiciones compuestas y ramas multiples.",
        "steps": [
            "Paso 1: Crea una funcion que reciba un puntaje `i32` y devuelva una calificacion de texto.",
            "Paso 2: Usa `if`, `else if` y `else` para clasificar el puntaje en tres rangos.",
            "Paso 3: Llama a la funcion varias veces desde `main` probando valores en el limite de cada rango.",
            "Paso 4: Agrega comentarios explicando como Rust evalua las condiciones y detiene las ramas.",
        ],
    },
    {
        "title": "Condiciones como expresiones",
        "goal": "Usar `if` como expresion para inicializar valores.",
        "steps": [
            "Paso 1: Declara dos variables numericas y determina el mayor usando una expresion `if` en una sola linea.",
            "Paso 2: Usa otra expresion `if` para asignar un mensaje segun el signo de un numero.",
            "Paso 3: Comprueba el resultado imprimiendo ambos valores con `println!`.",
            "Paso 4: Describe en comentarios las reglas de tipos cuando `if` devuelve valores.",
        ],
    },
    {
        "title": "Bucle loop con break y continue",
        "goal": "Practicar ciclos infinitos controlados manualmente.",
        "steps": [
            "Paso 1: Crea un `loop` que incremente un contador y se detenga con `break` al llegar a 10.",
            "Paso 2: Usa `continue` para saltar numeros pares y solo imprimir los impares.",
            "Paso 3: Captura el valor devuelto por `break` y asignalo a una variable.",
            "Paso 4: Escribe comentarios explicando las diferencias entre `loop`, `while` y `for`.",
        ],
    },
    {
        "title": "Bucle while y validaciones",
        "goal": "Aplicar `while` para validar entrada o repetir tareas.",
        "steps": [
            "Paso 1: Simula pedir contrasena comparando una entrada fija dentro de un `while`.",
            "Paso 2: Lleva la cuenta de intentos y corta el ciclo con `break` tras tres fallos.",
            "Paso 3: Usa un `boolean` para decidir si mostrar mensaje de acceso concedido o denegado.",
            "Paso 4: Documenta en comentarios cuando `while` es preferible a `loop`.",
        ],
    },
    {
        "title": "Bucle for y rangos",
        "goal": "Usar rangos y colecciones con `for`.",
        "steps": [
            "Paso 1: Itera sobre un rango inclusivo usando `for numero in 1..=10` y muestra cada valor.",
            "Paso 2: Calcula la suma de los numeros usando una variable acumuladora.",
            "Paso 3: Recorre un arreglo de cadenas con `for item in items.iter()` mostrando el indice con `enumerate()`.",
            "Paso 4: Agrega comentarios sobre las diferencias entre rangos inclusivos y exclusivos.",
        ],
    },
    {
        "title": "Match y patrones basicos",
        "goal": "Introducir coincidencia de patrones con `match`.",
        "steps": [
            "Paso 1: Crea una funcion que reciba un dia de la semana como cadena y devuelva si es laboral o fin de semana.",
            "Paso 2: Usa `match` para evaluar los casos, incluyendo un caso comodin `_`.",
            "Paso 3: Muestra resultados para varias entradas incluyendo mayusculas y minusculas.",
            "Paso 4: Explica en comentarios como Rust garantiza la exhaustividad de `match`.",
        ],
    },
    {
        "title": "If let y while let",
        "goal": "Practicar coincidencia parcial con `if let` y `while let`.",
        "steps": [
            "Paso 1: Declara una opcion `Option<i32>` y usa `if let` para imprimir el valor solo si existe.",
            "Paso 2: Usa `else` para manejar el caso `None` con un mensaje predeterminado.",
            "Paso 3: Implementa un `while let` que consuma elementos de un vector con `pop()` hasta quedar vacio.",
            "Paso 4: Documenta cuando `if let` simplifica un `match` de dos ramas.",
        ],
    },
    {
        "title": "Ownership con String y scope",
        "goal": "Comprender el traspaso de ownership y el alcance de las variables.",
        "steps": [
            "Paso 1: Crea una funcion que reciba un `String` por valor y muestre su contenido.",
            "Paso 2: Observa que ocurre si intentas usar la variable original tras pasarla a la funcion.",
            "Paso 3: Usa `clone()` para preservar la version original y compara la diferencia en comentarios.",
            "Paso 4: Explica en comentarios como el ownership evita dobles liberaciones.",
        ],
    },
    {
        "title": "Prestamos inmutables y mutables",
        "goal": "Ejercitar el uso de referencias y el borrow checker.",
        "steps": [
            "Paso 1: Crea una funcion que reciba una referencia inmutable `&String` y cuente sus caracteres.",
            "Paso 2: Implementa otra funcion que reciba `&mut String` y agregue un sufijo.",
            "Paso 3: Desde `main`, llama a ambas funciones respetando las reglas de prestamos simultaneos.",
            "Paso 4: Agrega comentarios describiendo las restricciones de Rust para prestamos mutables.",
        ],
    },
    {
        "title": "Slices en arrays y cadenas",
        "goal": "Trabajar con slices y comprender sus limites.",
        "steps": [
            "Paso 1: Declara un arreglo fijo de enteros y crea un slice de los tres primeros elementos.",
            "Paso 2: Itera sobre el slice mostrando cada valor y su indice original.",
            "Paso 3: Crea un slice de una cadena tomando solo la primera palabra usando rangos.",
            "Paso 4: Explica en comentarios que ocurre si intentas tomar un slice fuera de los limites.",
        ],
    },
    {
        "title": "Strings y UTF8",
        "goal": "Manipular cadenas y comprender caracteres multibyte.",
        "steps": [
            "Paso 1: Crea un `String` con caracteres que incluyan emojis o tildes y observa su longitud con `len()`.",
            "Paso 2: Itera sobre sus bytes y describe lo que ves en comentarios.",
            "Paso 3: Itera sobre sus `chars()` e indica la diferencia con la iteracion de bytes.",
            "Paso 4: Agrega comentarios sobre por que no puedes indexar un `String` directamente.",
        ],
    },
    {
        "title": "Vectores: creacion y mutacion",
        "goal": "Dominar operaciones basicas de `Vec`.",
        "steps": [
            "Paso 1: Crea un `Vec<i32>` vacio y agrega elementos con `push`.",
            "Paso 2: Elimina el ultimo elemento con `pop` y maneja el resultado con `match`.",
            "Paso 3: Accede a elementos con `get` y maneja el caso `None` cuando el indice no existe.",
            "Paso 4: Describe en comentarios la diferencia entre usar `get` y el indice `vec[idx]`.",
        ],
    },
    {
        "title": "Vectores: iteracion y map",
        "goal": "Aplicar loops y transformaciones sobre vectores.",
        "steps": [
            "Paso 1: Crea un vector de numeros enteros y recorrelo con `for` para imprimir cada cuadrado.",
            "Paso 2: Usa `iter().map()` para construir un nuevo vector con los valores multiplicados por 2.",
            "Paso 3: Imprime el vector original y el nuevo para comparar resultados.",
            "Paso 4: Explica en comentarios como `iter()` evita mover los valores originales.",
        ],
    },
    {
        "title": "Vectores: filtrado y suma",
        "goal": "Filtrar datos y reducirlos a un resultado.",
        "steps": [
            "Paso 1: Genera un vector con los numeros del 1 al 20 usando un rango y `collect()`.",
            "Paso 2: Usa `iter().filter()` para conservar solo los multiplos de 3.",
            "Paso 3: Calcula la suma de los valores filtrados con `fold` o `sum`.",
            "Paso 4: Describe en comentarios cuando preferir `fold` sobre `sum`.",
        ],
    },
    {
        "title": "HashMap basico",
        "goal": "Introducirse al manejo de diccionarios con `HashMap`.",
        "steps": [
            "Paso 1: Crea un `HashMap<String, i32>` para registrar cantidades de articulos.",
            "Paso 2: Inserta algunos valores y muestra el contenido iterando sobre pares clave valor.",
            "Paso 3: Usa `get` para recuperar una clave existente y otra inexistente, manejando ambos casos.",
            "Paso 4: Comenta cuando preferir `HashMap` frente a un vector de tuplas.",
        ],
    },
    {
        "title": "HashMap: conteo y agrupamiento",
        "goal": "Agrupar datos textuales usando `HashMap` y ciclos.",
        "steps": [
            "Paso 1: Crea un vector de palabras repetidas y recorrelo con `for`.",
            "Paso 2: Usa `entry().or_insert(0)` para contar cuantas veces aparece cada palabra.",
            "Paso 3: Agrupa las palabras por inicial colocando `Vec<String>` como valor del mapa.",
            "Paso 4: Explica en comentarios como `entry` evita escribir logica condicional repetida.",
        ],
    },
    {
        "title": "Funciones y modularizacion basica",
        "goal": "Dividir el codigo en funciones reutilizables.",
        "steps": [
            "Paso 1: Escribe una funcion `calcular_promedio` que reciba un slice `&[i32]` y devuelva `f64`.",
            "Paso 2: Escribe otra funcion `mostrar_resultado` que reciba el promedio y un umbral para imprimir un mensaje.",
            "Paso 3: Llama a ambas funciones desde `main` separando responsabilidades.",
            "Paso 4: Agrega comentarios sobre los beneficios de funciones pequenas y orientadas a una tarea.",
        ],
    },
    {
        "title": "Closures y captura de entorno",
        "goal": "Trabajar con closures y referencias al contexto.",
        "steps": [
            "Paso 1: Crea un vector de nombres y define una closure que cuente cuantos cumplen cierta condicion.",
            "Paso 2: Usa `iter().filter()` con la closure para contar coincidencias.",
            "Paso 3: Haz que la closure capture una variable externa para personalizar el filtro.",
            "Paso 4: Explica en comentarios como Rust decide si la closure toma prestado o mueve valores.",
        ],
    },
    {
        "title": "Iteradores encadenados",
        "goal": "Componer transformaciones con metodos de iteradores.",
        "steps": [
            "Paso 1: Genera los numeros del 1 al 100 y encadena `filter` y `map` para obtener los cuadrados de los pares.",
            "Paso 2: Limita el resultado a los primeros cinco valores usando `take`.",
            "Paso 3: Convierte el resultado en un vector con `collect` y muestra su contenido.",
            "Paso 4: Comenta las ventajas de usar iteradores perezosos frente a bucles tradicionales.",
        ],
    },
    {
        "title": "Iteradores con fold y reduce",
        "goal": "Aplicar `fold` para reducir colecciones a un valor agregado.",
        "steps": [
            "Paso 1: Crea un vector de transacciones positivas y negativas representado por enteros.",
            "Paso 2: Usa `iter().fold(0, |acc, valor| acc + valor)` para calcular el balance final.",
            "Paso 3: Implementa un `fold` adicional que construya una cadena con los valores separados por comas.",
            "Paso 4: Escribe comentarios comparando `fold` con `sum` y `reduce`.",
        ],
    },
    {
        "title": "Option y manejo de ausencia",
        "goal": "Modelar valores opcionales con `Option`.",
        "steps": [
            "Paso 1: Crea una funcion que busque un usuario en un vector y devuelva `Option<&String>`.",
            "Paso 2: Usa `match` para mostrar un mensaje distinto segun exista o no el usuario.",
            "Paso 3: Refactoriza el manejo usando `unwrap_or` o `map` segun consideres util.",
            "Paso 4: Explica en comentarios por que `Option` evita nulos y errores en tiempo de ejecucion.",
        ],
    },
    {
        "title": "Result y propagacion de errores",
        "goal": "Propagar errores con el operador `?`.",
        "steps": [
            "Paso 1: Crea una funcion que lea un numero desde la entrada estandar y devuelva `Result<i32, std::io::Error>`.",
            "Paso 2: Usa el operador `?` para propagar errores en la funcion.",
            "Paso 3: Desde `main`, maneja el `Result` mostrando un mensaje apropiado.",
            "Paso 4: Describe en comentarios que efecto tiene `?` sobre el tipo de retorno.",
        ],
    },
    {
        "title": "Structs simples",
        "goal": "Diseñar estructuras de datos personalizadas.",
        "steps": [
            "Paso 1: Define un `struct Usuario` con campos para nombre, correo y edad.",
            "Paso 2: Crea una funcion constructora que devuelva un `Usuario` inicializado.",
            "Paso 3: Instancia dos usuarios en `main` y muestra sus campos con `println!` usando `Debug`.",
            "Paso 4: Comenta cuando preferir estructuras con nombre frente a tuplas.",
        ],
    },
    {
        "title": "Structs con metodos",
        "goal": "Agregar comportamiento a las estructuras.",
        "steps": [
            "Paso 1: Implementa `impl Usuario` con un metodo `es_mayor_de_edad` que devuelva `bool`.",
            "Paso 2: Agrega un metodo que actualice el correo recibiendo `&mut self`.",
            "Paso 3: Llama a los metodos desde `main` demostrando las diferencias entre `&self` y `&mut self`.",
            "Paso 4: Documenta en comentarios cuando usar metodos asociados `Self::nuevo`.",
        ],
    },
    {
        "title": "Structs y traits de formato",
        "goal": "Implementar `Debug` y `Display` para estructuras personalizadas.",
        "steps": [
            "Paso 1: Deriva `Debug` para `Usuario` y usa `println!(\"{:?}\", instancia)`.",
            "Paso 2: Implementa manualmente `std::fmt::Display` para personalizar la salida.",
            "Paso 3: Crea un metodo que devuelva la representacion en cadena usando `format!` y `self`.",
            "Paso 4: Explica en comentarios la diferencia entre `Debug` y `Display`.",
        ],
    },
    {
        "title": "Traits y polimorfismo basico",
        "goal": "Definir traits y aplicarlos a multiples tipos.",
        "steps": [
            "Paso 1: Declara un trait `Descripcion` con un metodo `descripcion(&self) -> String`.",
            "Paso 2: Implementa el trait para dos structs distintos, por ejemplo `Usuario` y `Producto`.",
            "Paso 3: Crea una funcion que reciba un `impl Descripcion` e imprima el resultado.",
            "Paso 4: Comenta cuando preferir `impl Trait` frente a genericos explicitos.",
        ],
    },
    {
        "title": "Traits y polimorfismo dinamico",
        "goal": "Usar trait objects para almacenar tipos heterogeneos.",
        "steps": [
            "Paso 1: Reutiliza el trait `Descripcion` y crea un vector de `Box<dyn Descripcion>`.",
            "Paso 2: Inserta instancias de distintos structs que implementen el trait.",
            "Paso 3: Itera sobre el vector y llama al metodo del trait para cada elemento.",
            "Paso 4: Explica en comentarios las diferencias entre polimorfismo estatico y dinamico.",
        ],
    },
    {
        "title": "Genericos en funciones",
        "goal": "Generalizar funciones con parametros de tipo.",
        "steps": [
            "Paso 1: Escribe una funcion `mayor` que reciba dos parametros genericos que implementen `PartialOrd`.",
            "Paso 2: Usa la funcion con enteros, flotantes y cadenas para mostrar su versatilidad.",
            "Paso 3: Documenta con comentarios como se leen las anotaciones de genericos.",
            "Paso 4: Experimenta agregando `Copy` y comenta por que podria ser necesario.",
        ],
    },
    {
        "title": "Genericos en structs",
        "goal": "Crear estructuras genericas y metodos asociados.",
        "steps": [
            "Paso 1: Define un struct `Contenedor<T>` que almacene un valor generico.",
            "Paso 2: Implementa metodos para obtener el valor y reemplazarlo por otro.",
            "Paso 3: Crea dos instancias con tipos distintos y demuestra su uso.",
            "Paso 4: Escribe comentarios explicando como se instancian structs con genericos.",
        ],
    },
    {
        "title": "Genericos con bounds de traits",
        "goal": "Combinar genericos con restricciones de traits.",
        "steps": [
            "Paso 1: Extiende `Contenedor<T>` para requerir que `T: PartialOrd + Copy` en un metodo `maximo`.",
            "Paso 2: Implementa una funcion generica que reciba cualquier slice ordenable y devuelva el mayor.",
            "Paso 3: Usa anotaciones de `where` para reescribir las restricciones y compara legibilidad.",
            "Paso 4: Comenta casos donde multiples bounds son imprescindibles.",
        ],
    },
    {
        "title": "Enums con datos y patrones",
        "goal": "Diseñar enums ricos y hacer pattern matching.",
        "steps": [
            "Paso 1: Define un enum `Respuesta` con variantes `Exito(i32)`, `Error(String)` y `Pendiente`.",
            "Paso 2: Crea una funcion que devuelva `Respuesta` segun un valor de entrada.",
            "Paso 3: Usa `match` para manejar cada caso y mostrar mensajes distintos.",
            "Paso 4: Explica en comentarios como los enums modelan estados mutuamente excluyentes.",
        ],
    },
    {
        "title": "Pattern matching avanzado con guardas",
        "goal": "Utilizar guardas y patrones multiples en `match`.",
        "steps": [
            "Paso 1: Reusa el enum `Respuesta` e implementa un `match` con guardas `if` que discriminen valores especificos.",
            "Paso 2: Agrupa multiples patrones en una sola rama usando el simbolo `|`.",
            "Paso 3: Introduce un patron que haga binding de valores y los use en una expresion.",
            "Paso 4: Documenta como las guardas afectan el orden de evaluacion.",
        ],
    },
    {
        "title": "Lifetimes basicos",
        "goal": "Entender lifetimes en funciones que retornan referencias.",
        "steps": [
            "Paso 1: Escribe una funcion `mayor_referencia` que reciba dos `&str` y devuelva el mas largo.",
            "Paso 2: Anota lifetimes explicitos y comenta por que son necesarios.",
            "Paso 3: Prueba la funcion con cadenas externas y literales para validar el prestamo.",
            "Paso 4: Describe en comentarios que ocurre si intentas devolver una referencia a un valor local.",
        ],
    },
    {
        "title": "Borrow checker con slices",
        "goal": "Practicar prestamos sobre slices mutables e inmutables.",
        "steps": [
            "Paso 1: Crea una funcion que reciba `&mut [i32]` y multiplique cada elemento por 2.",
            "Paso 2: Desde `main`, crea un vector y pasa un slice mutable de una seccion intermedia.",
            "Paso 3: Obten simultaneamente un slice inmutable de otra seccion valida.",
            "Paso 4: Explica en comentarios por que los slices no se pueden solapar cuando alguno es mutable.",
        ],
    },
    {
        "title": "Modulos y visibilidad",
        "goal": "Organizar codigo en modulos internos.",
        "steps": [
            "Paso 1: Declara un modulo interno `mod util` dentro de `main.rs` con una funcion publica.",
            "Paso 2: Define una funcion privada en el modulo y trata de usarla desde `main` explicando el error.",
            "Paso 3: Usa `pub use` para reexportar una funcion y simplificar su acceso.",
            "Paso 4: Documenta las reglas basicas de visibilidad en Rust.",
        ],
    },
    {
        "title": "Modulos en archivos separados",
        "goal": "Mover modulos a archivos dedicados.",
        "steps": [
            "Paso 1: Crea un directorio `modulos` dentro de la carpeta de la practica.",
            "Paso 2: Define un archivo `modulos/util.rs` con funciones relacionadas con cadenas.",
            "Paso 3: Declara `mod modulos::util;` en `main.rs` y usa las funciones desde `main`.",
            "Paso 4: Agrega comentarios indicando como Rust localiza archivos de modulos.",
        ],
    },
    {
        "title": "Tests unitarios basicos",
        "goal": "Escribir pruebas unitarias simples.",
        "steps": [
            "Paso 1: Agrega un modulo `#[cfg(test)]` dentro de `main.rs`.",
            "Paso 2: Crea una funcion a probar y dos tests que validen casos positivos y negativos.",
            "Paso 3: Corre `cargo test` (fuera de esta practica) y observa el resultado.",
            "Paso 4: Comenta buenas practicas para nombrar funciones de prueba.",
        ],
    },
    {
        "title": "Iteradores personalizados",
        "goal": "Implementar el trait `Iterator` para una estructura.",
        "steps": [
            "Paso 1: Crea una estructura que represente un contador con limite superior.",
            "Paso 2: Implementa `Iterator` para la estructura devolviendo `Option<i32>` en `next`.",
            "Paso 3: Usa tu iterador en un `for` y con metodos como `sum` o `collect`.",
            "Paso 4: Anota en comentarios los requisitos de `Iterator` y el valor asociado `Item`.",
        ],
    },
    {
        "title": "Traits con metodos default",
        "goal": "Proveer implementaciones compartidas en traits.",
        "steps": [
            "Paso 1: Define un trait `Validable` con un metodo `es_valido` sin implementacion.",
            "Paso 2: Agrega un metodo default `validar_y_reportar` que use `es_valido` para imprimir un mensaje.",
            "Paso 3: Implementa `Validable` para dos structs con logica distinta.",
            "Paso 4: Explica en comentarios como los metodos default reducen codigo repetido.",
        ],
    },
    {
        "title": "Smart pointer Box",
        "goal": "Usar `Box<T>` para datos en el heap.",
        "steps": [
            "Paso 1: Crea una estructura recursiva simple como una lista enlazada que use `Box`.",
            "Paso 2: Implementa metodos para insertar y recorrer los nodos de la lista.",
            "Paso 3: Imprime la lista para verificar el orden de los elementos.",
            "Paso 4: Anota en comentarios por que `Box` habilita tipos recursivos.",
        ],
    },
    {
        "title": "Rc y Arc para compartir ownership",
        "goal": "Compartir datos inmutables entre multiples propietarios.",
        "steps": [
            "Paso 1: Crea un `Rc<String>` y clona referencias para simular multiples lectores.",
            "Paso 2: Muestra el conteo de referencias con `Rc::strong_count` y explica el resultado.",
            "Paso 3: Repite el ejercicio con `Arc<String>` dentro de `std::thread::spawn`.",
            "Paso 4: Comenta diferencias entre `Rc` y `Arc` y cuando usar cada uno.",
        ],
    },
    {
        "title": "RefCell y mutabilidad interior",
        "goal": "Experimentar con mutabilidad interior y reglas dinamicas.",
        "steps": [
            "Paso 1: Crea un `RefCell<Vec<i32>>` y pide prestado mutablemente con `borrow_mut()`.",
            "Paso 2: Inserta valores en el vector y libera el prestamo mutable antes de pedir uno inmutable.",
            "Paso 3: Intenta violar las reglas solicitando dos prestamos mutables y observa el panic.",
            "Paso 4: Explica en comentarios las diferencias entre comprobaciones en tiempo de compilacion y de ejecucion.",
        ],
    },
    {
        "title": "Threads y sincronizacion simple",
        "goal": "Crear hilos y sincronizarlos con `join`.",
        "steps": [
            "Paso 1: Lanza multiples hilos con `std::thread::spawn` que impriman mensajes con un identificador.",
            "Paso 2: Guarda las referencias a los `JoinHandle` en un vector.",
            "Paso 3: Recorre el vector para llamar `join()` y asegurar que todos los hilos terminen.",
            "Paso 4: Documenta en comentarios los riesgos de compartir datos sin sincronizacion.",
        ],
    },
    {
        "title": "Channels y paso de mensajes",
        "goal": "Comunicar hilos mediante `mpsc`.",
        "steps": [
            "Paso 1: Crea un canal con `std::sync::mpsc::channel()` y comparte el transmisor con diferentes hilos.",
            "Paso 2: Envia mensajes desde cada hilo usando `send` y manten un identificador.",
            "Paso 3: Recibe los mensajes en el hilo principal con un bucle `for` sobre el receptor.",
            "Paso 4: Explica en comentarios como los channels ayudan a evitar datos compartidos mutables.",
        ],
    },
    {
        "title": "Mutex y datos compartidos",
        "goal": "Proteger datos mutables con `Mutex`.",
        "steps": [
            "Paso 1: Envuelve un contador en `Arc<Mutex<i32>>` y comparte la referencia con varios hilos.",
            "Paso 2: Incrementa el contador dentro de cada hilo adquiriendo el candado con `lock()`.",
            "Paso 3: Una vez unidos los hilos, imprime el valor final del contador.",
            "Paso 4: Documenta en comentarios los posibles bloqueos y como evitarlos.",
        ],
    },
    {
        "title": "Macros declarativas basicas",
        "goal": "Crear una macro simple con `macro_rules!`.",
        "steps": [
            "Paso 1: Define una macro `imprime_valores!` que acepte multiples expresiones y las muestre.",
            "Paso 2: Usa patrones de repeticion `$( ),*` para aceptar argumentos variables.",
            "Paso 3: Invoca la macro con diferentes tipos de datos y analiza la expansion mentalmente.",
            "Paso 4: Escribe comentarios sobre cuando preferir macros frente a funciones genericas.",
        ],
    },
    {
        "title": "Proyecto integrador final",
        "goal": "Combinar modulos, traits, genericos y colecciones en una mini aplicacion.",
        "steps": [
            "Paso 1: Disena modulos para separar dominio, servicios e interaccion con el usuario.",
            "Paso 2: Define structs y traits para modelar entidades y comportamientos reutilizables.",
            "Paso 3: Usa genericos, closures y iteradores para procesar una lista de datos con agrupamiento y reduce.",
            "Paso 4: Integra manejo de errores con `Result` y documenta los puntos clave de la solucion.",
        ],
    },
]


def main() -> None:
    base_dir = Path.cwd()
    for index, practice in enumerate(practices, start=1):
        slug = slugify(practice["title"])
        folder_name = f"practice{index:02d}_{slug}"
        practice_dir = base_dir / folder_name
        practice_dir.mkdir(parents=True, exist_ok=True)

        lines = [
            f"// Practica {index:02d}: {practice['title']}",
            f"// Objetivo: {practice['goal']}",
            "",
            "fn main() {",
        ]

        for step in practice["steps"]:
            lines.append(f"    // {step}")

        lines.extend(
            [
                "",
                "    // Escribe tu solucion aqui siguiendo los pasos anteriores.",
                "}",
                "",
            ]
        )

        content = "\n".join(lines)
        (practice_dir / "main.rs").write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
