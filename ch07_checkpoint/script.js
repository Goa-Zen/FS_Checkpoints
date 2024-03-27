var areTheyNumeric = {
    isNumberFunction: function (inputValue) {
        var typedata = typeof(inputValue);
        switch (typedata) {
            case "object":
                try {
                    const reducer = (accumulator, curr) => accumulator + Number(curr);
                    var sum = (inputValue.reduce(reducer));
                    sum = Number(sum);
                    return typeof(sum)==="number" ? true : false;
                } catch (error) {
                    return false;
                }
            default:
                return false;
        }
    },
    tester: function(inputValue) {
        return this.isNumberFunction(inputValue);
    } 
}

function operationsExercise(firstArg, secondArg, thirdArg, fourthArg) {

    let lista = [firstArg, secondArg, thirdArg, fourthArg];
    if (areTheyNumeric.tester(lista) === false) {
        return  'Los valores introducidos han de ser numéricos!!';
    } else {
        var sum = Number(firstArg) + Number(secondArg);
        var sum1 = Number(thirdArg) + Number(fourthArg);
        var mult = sum * sum1;
        
        var output = mult > 50 ?  " ¡El número es mayor que 50!" : " ¡El número es menor que 50!";
        return "Result: " + mult + output;
    }
}


function operations(number_one_id, number_two_id, number_three_id, number_four_id) {


    let lista = [document.getElementById(number_one_id).value,
                document.getElementById(number_two_id).value,
                document.getElementById(number_three_id).value,
                document.getElementById(number_four_id).value];
    let firstArg = lista[0];
    let secondArg = lista[1];
    let thirdArg = lista[2];
    let fourthArg = lista[3];

    if (firstArg ==='' || secondArg ==='' || thirdArg ==='' || fourthArg ==='') {
      return "Has de introducir algún valor en los parámetros";
  }
    // a = document.getElementById(number_one_id);
    // alert(a.value);
    // alert(lista);
    var element = document.getElementById('div_exercise_with_inputs');
    // lista = [firstArg, secondArg, thirdArg, fourthArg];
    if (areTheyNumeric.tester(lista) === false) {
        element.innerHTML =  'Los valores introducidos han de ser numéricos!!';
    } else {
        var sum = Number(lista[0]) + Number(lista[1]);
        var sum1 = Number(lista[2]) + Number(lista[3]);
        var mult = sum * sum1;
        var output = mult > 50 ?  " ¡El número es mayor que 50!" : " ¡El número es menor que 50!";
        element.innerHTML = "Result: " + mult + output;
    }
}

function testerName (str_name) {
  var name = str_name;
  var response = null;                        
  if (name === 'Alba' || name === 'Rocio'){
      response = 'You are who I spect.';
  } else if(name === 'Asier' ){
      response = 'You are not allowed to be here!!';            
  } else {
      response = 'You are not who I spect.';
  }
  return response;
}
function showArgs (caller_value){
  switch (caller_value){
      case "toUpperCase()":
      case "toLowerCase()":
      case "trim()":
          return '<input type="hidden" id="value_one" value="error" ></input> ' +
                 '<input type="hidden" id="value_two" value="error" ></input> ';
      case "charAt(number)":
          return '<label for="value_one">Introduce the numeric argument:</label> '  +
                 '<input type="number" id="value_one" value="" required placeholder = "Introduce the numeric argument:" ></input> '  +
                 '<input type="hidden" id="value_two" value="error" ></input> ';

      case "slice(start_position, end_position -optional)":    
          return '<label for="value_one">Introduce the numeric argument:</label> '  +
                 '<input type="number" id="value_one" value="" required placeholder = "Introduce the numeric argument:" ></input> ' +
                 '<label for="value_one">OPTIONAL: Introduce the numeric argument:</label> '  +
                 '<input type="number" id="value_two" value="" placeholder = "OPTIONAL Introduce the numeric argument:" ></input> ';
      case "replace(cadena_search/RegExp_search, cadena_replace/regular_expr_replace)":
          return '<label for="value_one">Introduce the argument:</label> '  +
                  '<input type="text" id="value_one" value="" required placeholder = "Introduce the argument:" ></input> '  +
                  '<label for="value_two">Introduce the argument:</label> '  +                   
                  '<input type="text" id="value_two" value="" required placeholder = "Introduce the argument:" ></input>';            
      default:
          return '<label for="value_one">Introduce the argument:</label> ' + 
                 '<input type="text" id="value_one" value="" required placeholder = "Introduce the argument:" ></input> '  +
                 '<input type="hidden" id="value_two" value="error" ></input> ';
  }
}


function showResultStringFunction (str, str_function_param_value, arguments) {
  if (arguments[0]==='' || arguments[1]==='') {
      return "Has de introducir algún valor en los parámetros";
  }
  try {
      switch (str_function_param_value){
      case "toUpperCase()":
          return str.toUpperCase();
      case "toLowerCase()":
          return str.toLowerCase();
      case "charAt(number)":
          return str.charAt(arguments[0]);
      case "trim()":
          return str.trim();
      case "slice(start_position, end_position -optional)":  
          if (arguments[1]==='') {
              return str.slice(arguments[0],arguments[1]);
          }else {
              return str.slice(arguments[0],arguments[1]);
          }
          
      case "concat(cadena)":
          return str.concat(arguments[0]);
      case "includes(cadena)":
          return str.includes(arguments[0]);

      case "endsWith(cadena)":
          return str.endsWith(arguments[0]);
      case "startsWith(cadena)":
          return str.startsWith(arguments[0]);
      case "replace(cadena_search/RegExp_search, cadena_replace/regular_expr_replace)":
          return str.replace(arguments[0],arguments[1]);
      case "match(cadena/RegExp)":
          return str.match(arguments[0]);
      case "search(cadena/RegExp)":
          return str.search(arguments[0]);
      case "indexOf(cadena))":
          return str.indexOf(arguments[0]);
      case "lastIndexOf(cadena)":    
          return str.lastIndexOf(arguments[0]);
      default:
          throw "The function does not exist!!";
      }
  } catch (error) {

      return "Has de introducir algún valor en los parámetros";
  }
}


