     function insert(num) {
        document.forms[0].elements.textview.value = document.forms[0].elements.textview.value + num;
      }
      function equal() {
        var exp = document.forms[0].elements.textview.value;
        if(exp) {
          exp = eval(document.forms[0].elements.textview.value);
          document.forms[0].elements.textview.value = exp;
        }
      }
      function clean() {
        document.forms[0].elements.textview.value = "";
      }
      function back() {
        var exp = document.forms[0].elements.textview.value;
        document.forms[0].elements.textview.value = exp.substring(0,exp.length-1);
      }
