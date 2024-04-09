var todayIs = function() {
    let ahora = Date.now();
    let today = new Date(ahora);
    return "Today is " + today.toDateString();
}


var stringOperator = {
    str: null,
    opcion: null,
    showArgs: function (caller_value) {
        this.opcion = caller_value;
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
    },
    showResultStringFunction: function(str) {
        // var str = '   El veloz murciélago hindú prueba feliz cardillo y kiwi';
        
        var arguments = [];
        var el = document.getElementById("value_one");
        arguments.push(el.value);
        el = document.getElementById("value_two");
        arguments.push(el.value);
        if (arguments[0]==='' || arguments[1]==='') {
            return "Has de introducir algún valor en los parámetros";
        }
        try {
            switch (this.opcion){
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

}
