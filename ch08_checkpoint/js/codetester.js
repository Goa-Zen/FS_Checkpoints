
document.onclick = event => {
    var values_textarea;
    element = document.getElementById('code-txt-area');
    element.addEventListener("blur", function() {

        document.getElementById('code-checker-button').innerHTML = values_textarea.codeRun(this.value); 
    });
    element.addEventListener("focus", function() {

        document.getElementById('code-checker-button').innerHTML = ''; 
        document.getElementById('div-tester-code-output').innerHTML = ''; 
    });
    if (event.target.matches('.open-tester')) {
        
        let selected = event.target;
        let	position = selected.offsetTop + selected.scrollTop;
        
        let padre = selected.parentNode;
        let div = padre.parentNode;
        let search_div = div.querySelector(".div-code");
        let ori_string = search_div.innerHTML;
        
        values_textarea = new codeTextarea(ori_string);
        values_textarea.valuesPrinter();
        document.getElementById('code-checker-button').innerHTML = values_textarea.codeRun(); 
        document.getElementById('abs-code-tester').style.top = position + 'px';    
        document.getElementById('abs-code-tester').style.visibility = 'visible'; 

        event.preventDefault();    
        
    }
    if (event.target.matches('#btn-exit-code-tester')) {

        document.getElementById('abs-code-tester').style.visibility = 'hidden';
        document.getElementById('function-text').innerHTML = '';
        document.getElementById('function-return').innerHTML = '';
        document.getElementById('code-txt-area').value = '';
        document.getElementById('code-error').innerHTML = '';  
        let where_to_print = 'div-tester-code-output';
        document.getElementById(where_to_print).innerHTML = '' ;   
        document.getElementById('function-return_slice1').innerHTML = '';
        document.getElementById('function-return_slice2').innerHTML = '';     
    }
    
    // event.returnValue = true;
};
class codeTextarea {
    constructor(ori_string) {
        this.with_arrows = false;
        let string_in = ori_string.replaceAll('"',"'");
        string_in = string_in.replaceAll('&gt;',">");
        let os_end_pos = string_in.indexOf('{');
        this.function_name = string_in.slice(0, (os_end_pos + 1));
        let left_string = string_in.slice((os_end_pos + 1));

        let arr_el = left_string.split('};');         
        this.function_caller = arr_el.pop();      
        let clean_code = arr_el.join()
        this.clean_code = clean_code.trim();

        let code_return_end = this.function_caller;
        code_return_end = code_return_end.trim();
        
        
        let longitud = code_return_end.length;
        let last_value = code_return_end.slice(longitud -1, longitud)
        
        if (last_value === ";" ){
            // let arr_code_new = arr_code.pop();
            code_return_end = code_return_end.slice(0,longitud -1)
        }

        let code_pre_end = '';
        let lastIndex = code_return_end.lastIndexOf(';');
        // alert(code_return_end);
        if (lastIndex >= 0){
            code_pre_end = code_return_end.slice(0,lastIndex);
            code_return_end = code_return_end.slice(lastIndex + 1,code_return_end.length);
            
            // let arr_code_01 = code_return_end.split('= ');
            // code_return_end = arr_code_01.pop();
        }else{
            code_return_end = code_return_end;
        }
        this.code_pre_end = code_pre_end; 
// alert(code_pre_end);

        lastIndex = code_return_end.lastIndexOf('= ');
        if (lastIndex >= 0){
            code_return_end = code_return_end.slice(lastIndex+1,code_return_end.length);
        }  
        if (code_return_end.indexOf("=>") >= 0){
            this.with_arrows = true;
            code_return_end = code_return_end.replaceAll("=>", "=> document.getElementById('div-tester-code-output').innerHTML =" );
        }
        this.code_return_end = code_return_end;

	}
    valuesPrinter = () => {
        document.getElementById('function-text').innerHTML = '';
        document.getElementById('function-return').innerHTML = '';
        document.getElementById('code-txt-area').value = '';
        let where_to_print = 'div-tester-code-output';
        document.getElementById(where_to_print).innerHTML = '' ;   
        document.getElementById('function-return_slice1').innerHTML = '';
        document.getElementById('function-return_slice2').innerHTML = '';  
        document.getElementById('code-error').innerHTML = '';   

        document.getElementById('function-text').innerHTML = this.function_name;
        document.getElementById('function-return').innerHTML = this.function_caller;
        document.getElementById('code-txt-area').value = this.clean_code;
        document.getElementById('function-return_slice1').innerHTML = this.code_pre_end;
        document.getElementById('function-return_slice2').innerHTML = this.code_return_end;
	}
    codeRun(txt_value) {
        let clean_code_fin = txt_value === undefined ? this.clean_code : txt_value ;
        let where_to_print = 'div-tester-code-output';

        let resultado = `${this.function_name}\n${clean_code_fin}\n};\n${this.code_pre_end};\n ` ;    

        if (this.with_arrows === true){
            resultado = `${resultado} ${this.code_return_end};` ;    
        }else{
            resultado = `${resultado}document.getElementById('${where_to_print}').innerHTML = formatOutput(${this.code_return_end});` ;    
        }
        let output = `<button id="btn-tester-code-output" class="btn" type="submit" onclick="${resultado}"> Run </button>`;
      
        return output;
    } 
}
function formatOutput (output) {
    
    switch (typeof(output)) {
        case "object":
            let content_out = '<ul>';
            for (out in output) {
                content_out = `${content_out} <li> ${output[out]}</li>`;
            }
            content_out = `${content_out}</ul>`;
            return content_out;
        case "string":
            let cont_output = output.replaceAll(":",":<br>");
            cont_output = cont_output.replaceAll(". ",".<br>");
            return cont_output;
        case "number":
            return output;
    }

}