$(document).ready(function(){

    // insertion_section
       $("input").focus(function() {
           $(this).css("opacity",1)
       })
       $("input").blur(function() {
           $(this).css("opacity",.2)
       })
   
       // close tr event
       $(".close").click(function(){
           $(this).parents(".tab").hide(500)
       })
   
       // add book info
       $("#add").click(function(){
           let mem_name = $("#memName").val(),
               mem_type = $("#typeName").val(),
               mem_id = $("#idno").val(),
               mem_dept = $("#deptname").val(),
               mem_due = $("#due").val(),
               new_tr = document.createElement("tr"),
               new_th_mem_name = document.createElement("th"),
               new_th_mem_type = document.createElement("td"),
               new_th_mem_id = document.createElement("td"),
               new_th_mem_dept = document.createElement("td"),
               new_th_mem_due = document.createElement("td"),
               table_mem_name = document.createTextNode(mem_name),
               table_mem_type = document.createTextNode(mem_type),
               table_mem_id = document.createTextNode(mem_id),
               table_mem_dept = document.createTextNode(mem_dept),
               table_mem_due = document.createTextNode(mem_due);
   
           // add txt
           new_th_mem_name.appendChild(table_mem_name);
           new_th_mem_type.appendChild(table_mem_type);
           new_th_mem_id.appendChild(table_mem_id);
           new_th_mem_dept.appendChild(table_mem_dept);
           new_th_mem_due.appendChild(table_mem_due);
           
   
           // add new_tr --> td
           let name_tab = new_tr.appendChild(new_th_mem_name);
           let type_tab = new_tr.appendChild(new_th_mem_type);
           let id_tab = new_tr.appendChild(new_th_mem_id);
           let dept_tab = new_tr.appendChild(new_th_mem_dept);
           let due_tab = new_tr.appendChild(new_th_mem_due);
           new_th_mem_name.setAttribute("scope","row")
   
           // add new_tr --> table
           let new_table = document.getElementById("tabs");
           new_table.appendChild(new_tr);
           new_tr.setAttribute("class","tab");
           
   
           // close button
           let but_td = document.createElement("td"),
               but = document.createElement("button"),
               but_span = document.createElement("span"),
               span_txt = document.createTextNode("X");
   
           but_td.appendChild(but);
           but.appendChild(but_span);
           but_span.appendChild(span_txt);
           new_tr.appendChild(but_td);
   
           but.setAttribute("type","button");
           but.setAttribute("class","close");
           but.setAttribute("aria-label","Close");
           but_span.setAttribute("aria-hidden","true");
   
           // click --> form reset
           this.form.reset();
   
           // close form item
           $(".close").click(function(){
               $(this).parents(".tab").hide(500)
   
           })
   
           
       })
       
   })