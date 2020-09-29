function calc()
     {
			var i = document.getElementById("i").value;
			var list = [0,1];
			while (i != 0) {
					var a = (list[list.length - 1]) + (list[list.length - 2]);
					list.push(a);
					i = i-1;
						
				}
     			document.getElementById("show").innerHTML=list;		
     	}
     		