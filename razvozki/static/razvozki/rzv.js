function upd_ln(cst_){
    var cst = 'cst_id_' + cst_;
    var cst2 = 'cst_id2_' + cst_;
    document.getElementById(cst).style.display='none';
    document.getElementById(cst2).style.display='block';}

function upd_ln_reverse(cst_, order){
    var cst = 'cst_id_' + cst_;
    var cst2 = 'cst_id2_' + cst_;
    document.getElementById(cst).style.display='block';
    document.getElementById(cst2).style.display='none';}

function upd_ln2(cst_){
    var cst = 'cst_id_' + cst_;
    var cst2 = 'cst_id2_' + cst_;
    var cst3 = 'cst_id3_' + cst_;
    document.getElementById(cst).style.display='none';
    document.getElementById(cst2).style.display='table-row';
    document.getElementById(cst3).style.display='table-row';}

function upd_ln2_reverse(cst_){
    var cst = 'cst_id_' + cst_;
    var cst2 = 'cst_id2_' + cst_;
    var cst3 = 'cst_id3_' + cst_;
    document.getElementById(cst).style.display='table-row';
    document.getElementById(cst2).style.display='none';
    document.getElementById(cst3).style.display='none';}

function add_ln(new_ln){
    document.getElementById(new_ln).style.display='block';}

function add_ln_reverse(new_ln){
    document.getElementById(new_ln).style.display='none';}

function add_ln2(cst_){
    var cst4 = 'cst_id4_' + cst_;
    var cst5 = 'cst_id5_' + cst_;
    var date_r = cst_;

    var line_id = 'dropdown_id_' + date_r;

    var x,xmlhttp,xmlDoc;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "customers.xml", false);
    xmlhttp.send();
    xmlDoc = xmlhttp.responseXML;
    x = xmlDoc.getElementsByTagName("Customer");

    var code_html = ('' +
        '<button class="btn btn-sm btn-outline-success dropdown-toggle" type="button" id="ChooseClientAdd' +
        date_r + '"  data-bs-toggle="dropdown"  aria-haspopup="true" aria-expanded="false">' +
        'Выбрать клиента</button>' +
        '<ul class="dropdown-menu" aria-labelledby="ChooseClientAdd' + date_r + '" id="ChooseCust" >' +
        '<input type="text" class="dropdown-item" placeholder="Поиск.." id="CustInput" onkeyup="filterCust()">')


    for (i = 0; i <x.length; i++) {
        var cst_id = x[i].getElementsByTagName("cst_id")[0].childNodes[0].nodeValue;
        var cst_name =  x[i].getElementsByTagName("name")[0].childNodes[0].nodeValue;
        var cst_address =  x[i].getElementsByTagName("address")[0].childNodes[0].nodeValue;
        var cst_contact =  x[i].getElementsByTagName("contact")[0].childNodes[0].nodeValue;
        code_html += ('<li id="Cust' + date_r + '_'+ cst_id + '">' +
        '<a class="dropdown-item" href="javascript:slc_cst(' +
        "'" + cst_name + "', '" + date_r + "', '" + cst_id +"', '" +
        cst_address + "', '" + cst_contact + "')" + '">' + cst_name + '</a></li>')
        }
        code_html += '</ul>'

    document.getElementById(line_id).innerHTML = code_html;

    document.getElementById(cst4).style.display='table-row';
    document.getElementById(cst5).style.display='table-row';}


function filterCust() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("CustInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("ChooseCust");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function add_ln2_reverse(cst_){
    var cst4 = 'cst_id4_' + cst_;
    var cst5 = 'cst_id5_' + cst_;
    document.getElementById(cst4).style.display='none';
    document.getElementById(cst5).style.display='none';}

function slc_cst(cst_name, rzv_id, cst_id, cst_address, cst_contact){
    var updcust_name = 'updcust_name_' + rzv_id;
    var updcust_id = 'updcust_id_' + rzv_id;
    var updcust_address = 'updcust_address_' + rzv_id;
    var updcust_contact = 'updcust_contact_' + rzv_id;
    var cust_name = cst_name;
    var cust_id = cst_id;
    var cust_address = cst_address;
    var cust_contact = cst_contact;
    document.getElementById(updcust_name).value = cust_name;
    document.getElementById(updcust_address).value = cust_address;
    document.getElementById(updcust_contact).value = cust_contact;
    document.getElementById(updcust_id).value = cust_id;

}

function slc_cst_(cst_name, rzv_id, cst_id, cst_address, cst_contact){
    var updcust_name = 'updcust_name_' + rzv_id;
    var updcust_id = 'updcust_id_' + rzv_id + '_';
    var updcust_address = 'updcust_address_' + rzv_id;
    var updcust_contact = 'updcust_contact_' + rzv_id;
    var cust_name = cst_name;
    var cust_id = cst_id;
    var cust_address = cst_address;
    var cust_contact = cst_contact;
    document.getElementById('customer_name').value = cust_name;
    document.getElementById(updcust_id).value = cust_id;
    document.getElementById('address').value = cust_address;
    document.getElementById('contact').value = cust_contact;

}


function upd_ln_double(){
    var chck = document.querySelector('.btn-check:checked').value;
    var cst_id = chck.slice(2)

    show_cust = 'show_' + cst_id;
    hide_cust = 'hide_' + cst_id;
    document.getElementById(show_cust).style.display='none';
    document.getElementById(hide_cust).style.display='block';
}
function upd_ln_double_reverse(){
    var chck = document.querySelector('.btn-check:checked').value;
    var cst_id = chck.slice(2)
    show_cust = 'show_' + cst_id;
    hide_cust = 'hide_' + cst_id;
    document.getElementById(show_cust).style.display='block';
    document.getElementById(hide_cust).style.display='none';
}

function unite_double(){
    var chck = document.querySelectorAll('.btn-check:checked');
    var chck_length = chck.length;
    if (chck_length == 2) {
        cst_0 = chck[0].defaultValue;
        cst_1 = chck[1].defaultValue;
        if (cst_0.charAt(0) == 'l'){
            cst_lv = cst_0.slice(2);
            cst_dt = cst_1.slice(2);
        }
        else {
            cst_dt = cst_0.slice(2);
            cst_lv = cst_1.slice(2);
        }
    document.getElementById('cst_lv').value = cst_lv;
    document.getElementById('cst_dt').value = cst_dt;
    document.getElementById('final_un').style.display='block';
    document.getElementById('initial_un').style.display='none';
    }
}

function order_cst (order){
    cst_order = order
    document.getElementById('order').innerHTML = order;

    location.reload();
}


 function printDiv(divName) {
        var printContents = document.getElementById(divName).innerHTML;
        w=window.open();
        w.document.write(printContents);
        w.print();
        w.close();
    }

function cst_filterFunction(rzv_id) {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  var myDropdown= ChooseClientAdd+rzv_id
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}



function loadDoc(cst_) {
  var cst1_ = 'cst_id_' + cst_;
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    document.getElementById(cst1_).innerHTML = this.responseText;
    }
      xhttp.open('GET', 'upd_rzv_txt', true);
      xhttp.send();
}


function upd_rzv(cst_, date, date_id, customer, customer_name, address, contact, to_do_take, to_do_deliver, page_number, get_all_todo)
{
  var cst = 'cst_id_' + cst_;
  var cst0 = 'cst_id0_' + cst_;
  var code_html1 = (''+
        '<tr id="' + cst + '" >'+
            '<input type="hidden" id="page_number_upd" name="page_number_upd" value='+ page_number + "'"+'>' +
            '<input type="hidden" name="date" value="' + date +'"' + '>'+
            '<input id="updcust_id_ ' + cst_ + '_"  type="hidden" name="customer" value=None>'+
            '<th scope="rowgroup"><a href="javascript:upd_rzv_reverse(' +
            "'{{rzv.id}}', '{{date_r}}', '{{rzv.date_id}}', '{{rzv.customer_name}}', '{{rzv.address}}', '{{rzv.contact}}', '{{ page_obj.number }}', '{{rzv.get_all_todo}}'" +
            ');"' +
            '"><button type="button" class="btn btn-sm btn-danger" data-toggle="tooltip" data-placement="top" title="отменить">Отменить</button></a></th>'+
                '<th colspan="2">'+
                '<div class="col">'+
                    "<div class='input-group' id='datetimepicker4" + cst_ + "' data-td-target-input='nearest'"+
                    "data-td-target-toggle='nearest'>"+
                   "<input id='datetimepicker4Input" + cst_ + "' type='text' class='form-control'"+
                     "data-td-target='#datetimepicker4" + cst_ +"' name='date' value='"+ date + "'/>"+
                   "<span class='input-group-text' data-td-target='#datetimepicker4" + cst_ + "'"+
                     "data-td-toggle='datetimepicker'>"+
                     "<span class='bi bi-calendar-date-fill'></span>"+
                   "</span> </div> </div>" +
                "<script> new tempusDominus.TempusDominus(document.getElementById('datetimepicker4" + cst_ + "'), {"+
                 "display: {icons:"+
                    "{date:'bi bi-calendar-date-fill', next:'bi bi-chevron-compact-right', previous:'bi bi-chevron-compact-left',},"+
                 "components: {decades: true, year: true, month: true, date: true, hours: false, minutes: false, seconds: false,}}"+
                 "});"+
                "</script> </th> <td>"+
            "<button class='btn btn-success dropdown-toggle' type='button' id='ChooseClientUpd" + cst_ + "' data-bs-toggle='dropdown'  aria-haspopup='true' aria-expanded='false'>"+
                "Выбрать клиента"+
            "</button>"+
            "<ul class='dropdown-menu' aria-labelledby='ChooseClientAdd" + cst_ + "'>"+

                  "{% for cst in  %}" +
                  "<li id='Cust" + cst_ + "_{{cst.id}}_'><a class='dropdown-item' href='javascript:slc_cst_('{{cst.name}}', '" + cst_ + "', '{{cst.id}}', '{{cst.address}}', '{{cst.contact}}')'>{{cst.name}}</a></li>"+
                  "{% endfor %}"+
              "</ul> </td> <td></td>"+
            "<td> <input type='text' class='form-control' id='to_do_take' placeholder='Забрать' name='to_do_take' value='" + to_do_take + "'> </td></tr>");
 var code_html2 = ("<tr id='" + cst0 + "'>  <td></td>" +
            "<td> <input type='number' style='min-width:30px' class='form-control' id='date_id' placeholder='#' name='date_id' value='" + date_id + "'> </td>"+
            "<td> <input type='text' class='form-control' id='customer_name' placeholder='Клиент' name='customer_name' value='" + customer_name + "'> </td>"+
            "<td><textarea class='form-control' id='address' placeholder='Адрес' name='address'> " + address + "</textarea></td>"+
            "<td><textarea class='form-control' id='contact' placeholder='Контакт' name='contact'> "+ contact + "</textarea></td>"+
            "<td> <input type='text' class='form-control' id='to_do_deliver' placeholder='Сдать' name='to_do_deliver' value='" + to_do_deliver + "'></td>"+
            "<td> <button type='submit' class='btn btn-sm btn-success' data-toggle='tooltip' data-placement='top' title='записать'>Записать</button></td>"+
            "</tr>");

    document.getElementById(cst0).innerHTML = code_html2;
    document.getElementById(cst).innerHTML = code_html1;

    }

function upd_rzv_reverse(cst_, date, date_id, customer_name, address, contact, page_number, get_all_todo)
{
  var cst = 'cst_id_' + cst_;
  var cst0 = 'cst_id0_' + cst_;

  var code_html1 = ("" +
    '<tr id="' + cst + '">' +
        '<th scope="row"></th>' +
        '<td  style="width:70px">' + date_id + '</td>' +
        '<td style="width:180px">' +
           ' <a href="javascript:upd_rzv({{rzv.id}}, "{{date_r}}", {{rzv.date_id}}, {{rzv.customer.id}},' +
           "'{{rzv.customer_name}}', '{{rzv.address}}', '{{rzv.contact}}', '{{rzv.to_do_take}}'," +
            '"{{rzv.to_do_deliver}}", {{ page_obj.number }}, "{{ rzv.get_all_todo }}");"' +
            '  class="text-dark">' + customer_name + '</a>' +
        '</td>' +
        '<td class="text-dark">' + address + '</td>' +
        '<td class="text-dark">' + contact + '</td>' +
        '<td class="text-dark">' + get_all_todo + '</td>' +
        '<td ><a href="delete_rzv/{{ rzv.id }}"><button class="btn btn-sm btn-outline-danger fw-bold"' +
        'data-toggle="tooltip" data-placement="top" title="удалить развозку">Удалить</button></a></td>' +
    '</tr>');

  var code_html2 = ("<tr id='" + cst0 + "'></tr>");


   document.getElementById(cst0).innerHTML = code_html2;
   document.getElementById(cst).innerHTML = code_html1;

    }

function add_rzv(date_r, page_number) {
   var cst6 = 'cst_id6_' + date_r;
   var cst7 = 'cst_id7_' + date_r;
   var cst8 = 'cst_id8_' + date_r;


   var code_html6 = ('<tr>'+

        '<input type="hidden" id="' + page_number +'" name="' + page_number + '" value="' + page_number + '">' +
        '<input type="hidden" name="date" value="' + date_r + '">' +
        '<th scope="rowgroup"><a href="javascript:add_rzv_reverse(' +
        "'" + date_r + "'" + ');">' +
            '<button type="button" class="btn btn-sm btn-danger" data-toggle="tooltip" data-placement="top" title="отменить">Отменить</button></a></th>' +
        '<input id="updcust_id_{{rzv.id}}"  type="hidden" name="customer" value=None>' +
        '<td> <input type="number" style="min-width:30px" class="form-control" placeholder="#" name="date_id" value="0"> </td>' +
        '<td ><input type="text" id="updcust_name_{{date_r}}" class="form-control" placeholder="Клиент"  name="customer_name"></td>' +
        '<td> <textarea id="updcust_address_{{date_r}}" class="form-control" placeholder="Адрес" name="address"></textarea> </td>' +
        '<td> <textarea id="updcust_contact_{{date_r}}" class="form-control" placeholder="Контакт" name="contact"></textarea> </td>' +
        '<td> <input type="text" class="form-control" placeholder="Забрать" name="to_do_take"> </td></tr>');

   var code_html7 = (''+
   '<tr class="dropdown" id="cst_id7_' + date_r + '">' +
        '<td></td>' +
        '<td></td>' +
        '<td>' +
        '<button class="btn btn-success dropdown-toggle" type="button" id="ChooseClientAdd{{date_r}}"  data-bs-toggle="dropdown"  aria-haspopup="true" aria-expanded="false">' +
            'Выбрать клиента' +
        '</button>' +
        '<ul class="dropdown-menu" aria-labelledby="ChooseClientAdd' + date_r + '">' +

              '{% for cst in cust %}' +
              "<li id='Cust{{date_r}}_{{cst.id}}'><a class='dropdown-item' href='javascript:slc_cst('{{cst.name}}', '{{date_r}}', '{{cst.id}}', '{{cst.address}}', '{{cst.contact}}')'>{{cst.name}}</a></li>" +
              '{% endfor %}' +
          '</ul>' +
        '</td>' +
        '<td></td>' +
        '<td></td>' +
        '<td> <input type="text" class="form-control" placeholder="Сдать" name="to_do_deliver"></td>' +
        '<td> <input type="submit" class="btn btn-sm btn-success" data-toggle="tooltip" data-placement="middle" value="Записать"></td>' +
   '</tr>');

   var code_html8 = ('' +
        '<input type="text" id="updcust0_name_{{date_r}}" class="form-control" placeholder="Клиент"  name="customer_name">' +
        '<button type="button" class="btn btn-sm btn-danger" data-toggle="tooltip" data-placement="top" title="отменить">Отменить</button>' +
        '<input type="number" style="min-width:30px" class="form-control" placeholder="#" name="date_id" value="0">' +
        '<textarea id="updcust0_address_{{date_r}}" class="form-control" placeholder="Адрес" name="address"></textarea>' +
        '<textarea id="updcust0_contact_{{date_r}}" class="form-control" placeholder="Контакт" name="contact"></textarea>' +
        '<input type="text" class="form-control" placeholder="Забрать" name="to_do_take">' +
        '<input type="text" class="form-control" placeholder="Сдать" name="to_do_deliver">'+
        '<input type="submit" class="btn btn-sm btn-success" data-toggle="tooltip" data-placement="middle" value="Записать">');

        document.getElementById(cst8).innerHTML = code_html8;
}

function add_rzv_reverse(date_r) {
   var cst6 = 'cst_id6_' + date_r;
   var cst7 = 'cst_id7_' + date_r;
   var cst8 = 'cst_id8_' + date_r;


   var code_html6 = '';
   var code_html7 = '';
   var code_html8 = '';


   document.getElementById(cst6).innerHTML = code_html6;
   document.getElementById(cst7).innerHTML = code_html7;
   document.getElementById(cst8).innerHTML = code_html8;
}

function cst_list(date_r) {
    var line_id = 'dropdown_id_' + date_r;

    var x,xmlhttp,xmlDoc
    xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "customers.xml", false);
    xmlhttp.send();
    xmlDoc = xmlhttp.responseXML;
    x = xmlDoc.getElementsByTagName("object");

    var code_html = ('<a href="javascript:cst_list(' + '{{' + date_r + "|date:'Y-m-d'}'" +');">' +
        '<button class="btn btn-sm btn-outline-success dropdown-toggle" type="button" id="ChooseClientAdd{{' +
        date_r + '}}"  data-bs-toggle="dropdown"  aria-haspopup="true" aria-expanded="false">' +
        'Выбрать клиента</button> </a>' +
        '<ul class="dropdown-menu" aria-labelledby="ChooseClientAdd{{' + date_r + '}}">')


    for (i = 0; i <x.length; i++) {
        var cst_id = x[i].getElementsByTagName("pk")[0].childNodes[0].nodeValue;
        var cst_name =  x[i].getElementsByTagName("name")[0].childNodes[0].nodeValue;
        var cst_address =  x[i].getElementsByTagName("address")[0].childNodes[0].nodeValue;
        var cst_contact =  x[i].getElementsByTagName("contact")[0].childNodes[0].nodeValue;
        code_html += ('<li id="Cust{{' + date_r + '}}_{{'+ cst.id + '}}">' +
        '<a class="dropdown-item" href="javascript:slc_cst(' +
        "'{{" + cst_name + "}}', '{{" + date_r + "|date:'Y-m-d'}}', '{{" + cst_id +"}}', '{{" +
        cst_address + "}}', '{{" + cst_contact + "}}')" + '">{{' + cst_name + '}}</a></li>')
        }
        code_html += '</ul>'

    document.getElementById(line_id).innerHTML = code_html;
}