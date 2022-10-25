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
        '<i class="bi bi-person-plus"></i> клиенты </button>' +
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

    var x,xmlhttp,xmlDoc,tmp_xml,code_html;
    tmp_xml = 'rzv_return.xml/' + cust_id;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", tmp_xml, false);
    xmlhttp.send();
    xmlDoc = xmlhttp.responseXML;
    code_html = '';
    try{x = xmlDoc.getElementsByTagName("Razvozka");
    if(x.length!=0){
    for (i = 0; i <x.length; i++) {
    var r_id = x[i].getElementsByTagName("id")[0].childNodes[0].nodeValue;
    var r_date =  x[i].getElementsByTagName("date")[0].childNodes[0].nodeValue;
    var r_customer_name =  x[i].getElementsByTagName("customer_name")[0].childNodes[0].nodeValue;
    var r_to_do_deliver =  x[i].getElementsByTagName("to_do_deliver")[0].childNodes[0].nodeValue;
    code_html = code_html + '<li id="rzv_ret_' + r_date + '_'+ r_id + '">';
    code_html = code_html + '<a class="dropdown-item" href="javascript:slc_rzv_(';
    code_html = code_html + "'" + rzv_id + "', '" + r_date + "', '" + r_id +  "')" + '">';
    code_html = code_html + r_date + ' / ' + r_to_do_deliver + '</a></li>';
    };


    document.getElementById('ul_' + rzv_id).innerHTML = code_html;}}catch{};
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


function upd_rzv(id){
  var fulfilled = document.getElementById('rzv_fulfilled_but_'+id).name;
  if(fulfilled == 1){fulfilled = 'True';}else{fulfilled = 'False';};
  if (fulfilled != 'True'){
  var date = document.getElementById('date_' + id).textContent;
  var date_id = document.getElementById('rzv_id_'+id).textContent;
  var customer = document.getElementById('customer_'+id).textContent;
  var customer_name = document.getElementById('customer_name_'+id).textContent;
  var address = document.getElementById('address_'+id).textContent;
  var contact = document.getElementById('contact_'+id).textContent;
  var page_number = document.getElementById('page_number').textContent;
  var map_point = document.getElementById('map_point_'+id).textContent;
  try{var to_do_take = document.getElementById('to_do_take_'+id).textContent;
  to_do_take = to_do_take.slice(9,);}
  catch{var to_do_take = '';};
  try{var to_do_deliver = document.getElementById('to_do_deliver_'+id).textContent;
  to_do_deliver = to_do_deliver.slice(8,);}
  catch{var to_do_deliver = '';};
  try{var d_t = document.getElementById('btn_checked_'+id).value;
  if(d_t == 1){var deliver_to = 'True';}else{
  var deliver_to = 'False';}}
  catch{var deliver_to = 'False';};
  var return_from = document.getElementById('return_from_'+id).value;
  try{var return_goods = document.getElementById('return_goods_'+id).value;
  var return_goods_id = document.getElementById('return_goods_id_'+id).value;
  var return_goods_customer_name = document.getElementById('return_goods_customer_name_'+id).value;
  var return_goods_to_do_take = document.getElementById('return_goods_to_do_take_'+id).value;}
  catch{var return_goods = '';};
  try{var r_a =document.getElementById('rzv_return_all_'+id).name; if (r_a == 1){
  var return_all = 'True';}else{var return_all = 'False';}}
  catch{var return_all = 'False';};


  var cst = 'cst_id_' + id;
  var onclick = '"javascript:upd_rzv_reverse(' + id +');"';
  var code_html = ('<td hidden><input form="updaterecord_rzv_' + id + '" name="page_number_upd" value="' + page_number + '"></td>' +
    '<td hidden><input name="map_point" id="map_point_' + id + '" value="' + map_point + '" form="updaterecord_rzv_' +
    id + '">+</td>' + '<td hidden><input name="customer" id="customer_' + id + '" value="' + customer +
    '" form="updaterecord_rzv_' + id + '"></td>' +
    '<input type=text hidden id="rzv_return_all_' + id + '" value="' + return_all + '">' +
    '<input type="text" id="return_from_' + id + '" hidden value="' + return_from + '">' +
    '<td ><input type="text" value="' + date_id + '" id="rzv_id_' + id + '" ' +
    'name="rzv_id" style="max-width:40px" class="form-control" form="updaterecord_rzv_' + id +
    '"></td><td class="text-unwrap" ><input style="max-width:110px; font-size:80%;" type="date" id="date_' + id + '" ' +
    'class="form-control" value="' + date + '" name="date" form="updaterecord_rzv_' + id + '">');
  if(date == '2100-01-01'){
  var date_until = document.getElementById('date_until2_' + id).value;
  var date_create = document.getElementById('date_create2_' + id).value;
  var date_until1 = document.getElementById('date_until_' + id).textContent;
  var date_create1 = document.getElementById('date_create_' + id).textContent;
  date_until1 = date_until1.slice(3)
  date_create1 = date_create1.slice(3)
  code_html += ('<br><br><label style="font-size:80%;" for="date_until_' + id + '">срок до</label>' +
     '<input style="max-width:110px; font-size:80%;" type="date" id="date_until2_' + id + '" ' +
     'class="form-control" value="' + date_until + '" name="date_until" form="updaterecord_rzv_' + id + '">' +
     '<input type="text" hidden id="date_create2_' + id + '" value="' + date_create +'">' +
     '<input type="text" hidden id="date_create_' + id + '" value="' + date_create1 +'">' +
     '<input type="text" hidden id="date_until_' + id + '" value="' + date_until1 +'">');}
  code_html +=('</td>' +
    '<td colspan="3" style="font-size:100%;"><div class="row p-1"><div class="col">' +
    '<textarea name="customer_name" class="form-control" form="updaterecord_rzv_' + id +
    '" id="customer_name_' + id + '">' + customer_name +
    '</textarea></div><div class="col"><textarea name="address" class="form-control" form="updaterecord_rzv_' + id +
    '" id="address_' + id + '" placeholder="Адрес">' +
    address + '</textarea></div>' + '<div class="col p-1" style="text-align:left;">' +
    '<textarea  name="contact"  class="form-control"' +
    'form="updaterecord_rzv_' + id + '" id="contact_' + id + '" placeholder="Контакт">' +
    contact + '</textarea></div></div>' + '<div class="row p-1" style="font-size:100%">' +
    '<div class="col form-floating" style="min-width:460px;"><textarea  name="to_do_take"' +
    'class="form-control" form="updaterecord_rzv_' + id +
    '" id="to_do_take_' + id + '" placeholder="">' +
    to_do_take + '</textarea>' + '<label for="to_do_take_' + id + '">забрать</label>' +
    '</div><div class="col text-center" style="min-width:120px;">');

  var x,xmlhttp,xmlDoc,tmp_xml;
  tmp_xml = 'rzv_return.xml/' + customer;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", tmp_xml, false);
  xmlhttp.send();
  xmlDoc = xmlhttp.responseXML;
  try{x = xmlDoc.getElementsByTagName("Razvozka");
  if(x.length!=0 || return_from){
  code_html += ('<button type="button" class="btn btn-sm btn-outline-danger dropdown-toggle" data-bs-toggle="dropdown"' +
    'aria-haspopup="true" aria-expanded="false" id=Choosereturn' + id + '"><i class="bi bi-arrow-return-left">' +
    '</i>возврат</button>' +
    '<input type="text" hidden id="return_goods_customer_name_' + id + '" value="' + return_goods_customer_name + '">' +
    '<input type="text" hidden id="return_goods_to_do_take_' + id + '" value="' + return_goods_to_do_take + '">' +
    '<ul class="dropdown-menu" aria-labelledby="Choosereturn' + id + '">');
  for (i = 0; i <x.length; i++) {
  var r_id = x[i].getElementsByTagName("id")[0].childNodes[0].nodeValue;
  var r_date =  x[i].getElementsByTagName("date")[0].childNodes[0].nodeValue;
  var r_customer_name =  x[i].getElementsByTagName("customer_name")[0].childNodes[0].nodeValue;
  var r_to_do_deliver =  x[i].getElementsByTagName("to_do_deliver")[0].childNodes[0].nodeValue;
  code_html += (''+

    '<li id="rzv_ret_' + r_date + '_'+ r_id + '">' +
    '<a class="dropdown-item" href="javascript:slc_rzv(' +
    "'" + date + "', '" + r_date + "', '" + r_id +  "', '" + id + "')" + '">' +
    r_date + ' / ' + r_to_do_deliver + '</a></li>')
    }
    if (r_id === undefined){r_id = return_goods_id}
    code_html +=  ('</ul>' +
    '<input style="font-size:80%;" type="text" name="return_goods" class="form-control" value="' + return_goods +
    '" readonly form="updaterecord_rzv_' + id + '" id="r_date_' + date + id + '"> ' +
    '<input type="text" hidden id="r_id_' + date + id + '" value="' + r_id + '" ' +
    'form="updaterecord_rzv_' + id + '" name="return_goods_id">');    }}catch{};

     code_html += ('</div>'+
    '<div class="col form-floating" style="min-width:480px;">' +
    '<textarea  name="to_do_deliver"  class="form-control" form="updaterecord_rzv_' + id +
    '" id="to_do_deliver_' + id + '" placeholder="Сдать">' + to_do_deliver +
    '</textarea>' + '<label for="to_do_deliver_' + id + '">сдать</label></div><div class="col align-center text-end" hidden >');
  if (deliver_to == 'True'){
  code_html += ('<input type="checkbox" class="btn-check" id="btn_checked_' + id + '" autocomplete="off" checked ' +
    'name="deliver_to" value="1" form="updaterecord_rzv_' + id + '" onclick="javascript:f_deliver_to(' + id + ');">' +
    '<label class="btn btn-sm btn-outline-danger" for="btn_checked_' + id + '" >' +
    '<i class="bi bi-arrow-repeat"></i>&nbsp;на переработку</label>');}
  else {
  code_html += ('<input type="checkbox" class="btn-check" id="btn_checked_' + id + '" autocomplete="off"' +
    'name="deliver_to" value="0" form="updaterecord_rzv_' + id + '" onclick="javascript:f_deliver_to(' + id + ');">' +
    '<label class="btn btn-sm btn-outline-danger" for="btn_checked_' + id + '">' +
    '<i class="bi bi-arrow-repeat"></i>&nbsp;на переработку</label>');
  }
  code_html += '</div></div></td><td class="text-end align-middle"><div class="col">';
  code_html += ('<a href=' + onclick + '><button class="btn btn-sm btn-outline-danger fw-bold" data-toggle="tooltip"' +
    'data-placement="top" title="назад"><i class="bi bi-arrow-counterclockwise"></i></button></a><br><br><br>' +
    '<button class="btn btn-sm btn-outline-success fw-bold" type="submit" form="updaterecord_rzv_' + id +
    '" data-toggle="tooltip" data-placement="top" title="записать"><i class="bi bi-check-lg"></i>' +
    '</button></div> </td>');
  document.getElementById(cst).innerHTML = code_html;
  if (customer != ''){var cust_id = 'customer_name_' + id;
  document.getElementById(cust_id).readOnly = true;;};
};}

function upd_rzv_reverse(id){
  var fulfilled  = 'False';
  var date = document.getElementById('date_' + id).textContent;
  var date_id = document.getElementById('rzv_id_'+id).value;
  var customer = document.getElementById('customer_'+id).textContent;
  var customer_name = document.getElementById('customer_name_'+id).textContent;
  var address = document.getElementById('address_'+id).textContent;
  var contact = document.getElementById('contact_'+id).textContent;
  var page_number = document.getElementById('page_number').textContent;
  var map_point = document.getElementById('map_point_'+id).textContent;
  try{var to_do_take = document.getElementById('to_do_take_'+id).textContent}
  catch{var to_do_take = '';};
  try{var to_do_deliver = document.getElementById('to_do_deliver_'+id).textContent;}
  catch{var to_do_take = '';};
  try{var d_t = document.getElementById('btn_checked_'+id).value;
  if(d_t == 1){var deliver_to = 'True';}else{
  var deliver_to = 'False';}}
  catch{var deliver_to = 'False';};
  var return_from = document.getElementById('return_from_'+id).value;
  try{var return_goods = document.getElementById('r_date_'+date+id).value;
  if(return_goods == ''){var return_from = 'False';}else{
  var return_goods_id = document.getElementById('r_id_'+date+id).value
  var return_goods_customer_name = document.getElementById('return_goods_customer_name_'+id).value;
  var return_goods_to_do_take = document.getElementById('return_goods_to_do_take_'+id).value;}}
  catch{var return_goods = '';};
  try{var r_a = document.getElementById('rzv_return_all_'+id).value;
  var return_all = r_a;}
  catch{var return_all = 'False';};
  var page_number = document.getElementById('page_number').textContent;
  var cst = 'cst_id_' + id;
  var onclick = 'onclick="javascript:upd_rzv(' + id +');"';


  var code_html = ('<td id="map_point_' + id + '" hidden>' + map_point + '</td>' +
                   '<input type="text" id="return_from_' + id + '" hidden value="' + return_from + '">' +
                   '<td id="rzv_id_' + id + '">' + date_id + '</td>' +
                   '<td class="text-unwrap" style="min-width:140px;"><div class="col p-1" id="rzv_fulfilled_' + id + '">');
  if (date != '2100-01-01'){
  if (fulfilled == 'True'){
  code_html += ('<button class="btn btn-sm btn-outline-success" type="button" onclick="javascript:rzv_status(' +
               id + ');" name="1" id="rzv_fulfilled_but_' + id + '">' +
               '<i class="bi bi-check2"></i>выполнено</button>');}
  else {
  code_html += ('<button class="btn btn-sm btn-outline-danger" type="button"onclick="javascript:rzv_status(' +
            id + ');" name="0" id="rzv_fulfilled_but_' + id + '">' +
            '<i class="bi bi-hourglass"></i>в процессе</button >');};
  code_html += '</div><div class="col p-1" id="razv_return_all_' + id + '">';
  if (return_from == 'True'){
    if (return_all == 'True'){
    code_html += ('<button class="btn btn-sm btn-outline-success" type="button" id="rzv_return_all_' + id + '" ' +
                  'onclick="javascript:rzv_return_all(' +
                  id + ',' + return_goods_id + ');" name="1"><i class="fa-regular fa-handshake"></i>полностью</button>');}
    else{
    code_html += ('<button class="btn btn-sm btn-outline-danger" type="button" id="rzv_return_all_' + id + '" ' +
                  'onclick="javascript:rzv_return_all(' +
                  id + ',' + return_goods_id + ');" name="0"><i class="fas fa-person-digging"></i>&nbsp;&nbsp;  частично</button >');}
  };}
  else{
  var date_until = document.getElementById('date_until2_'+id).value;
  var date_until1 = document.getElementById('date_until_'+id).value;
  var date_create = document.getElementById('date_create2_'+id).value;
  var date_create1 = document.getElementById('date_create_'+id).value;
  code_html += ('<div class="col p-1" id="date_create_' + id + '" >от ' + date_create1 + '</div><br>' +
                '<div class="col p-1" id="date_until_' + id + '" >до ' + date_until1 + '</div>' +
                '<input name="0" hidden type="text" id="rzv_fulfilled_but_' + id + '" value="' + fulfilled + '">' +
                '<input type="text" hidden id="date_create2_' + id + '" value="' + date_create + '">' +
                '<input type="text" hidden id="date_until2_' + id + '" value="' + date_until + '">');}
  code_html += '</div></td><td colspan="3">';
  code_html += ('<div class="row"' + onclick + '><div class="col p-1" id="customer_name_' + id + '">'
                + customer_name + '</div><div class="col p-1" id="address_' + id + '">' +
                address + '</div><div class="col p-1" ' + ' id="contact_' + id + '">' +
                contact + '</div></div>');
  code_html += ('' +
                '<div class="row text-success border border-success mt-2 pt-2 pb-1 bg-light align-self-bottom"' +
                 'style="font-size:100%" >');
  if (to_do_take != ''){
  code_html += '<div class="col p-1" id="to_do_take_' + id + '"><strong>ЗАБРАТЬ: </strong>' + to_do_take + '</div>';
    if (return_from == 'True'){
    code_html += ('<div class="col p-1" >' +
                  '<button type="button" class="btn btn-sm btn-outline-danger" data-bs-toggle="modal"' +
                  'data-bs-target="#rzv_return' + id + '">' +
                  'c переработки ' + return_goods + '</button></div>');
    code_html += (''+
                 '<div class="modal fade" id="rzv_return' + id +
                 '" tabindex="-1" aria-labelledby="rzv_return' + id + 'Label" aria-hidden="true">' +
                 '<div class="modal-dialog"><div class="modal-content"> <div class="modal-header">' +
                 '<h5 class="modal-title" id="rzv_return' + id + 'Label">Что отвозили</h5>' +
                 '<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>' +
                 '</div><div class="modal-body"><div> дата: '  + return_goods + ', кому: ' +
                 return_goods_customer_name + '</div><br> <h6>' + return_goods_to_do_take +
                 '</h6></div></div></div></div>');
    code_html += ('<input type="text" hidden id="return_goods_id_' + id + '" value="' + return_goods_id + '">' +
                 '<input type="text" hidden id="return_goods_' + id + '" value="' + return_goods + '">' +
                  '<input type="text" hidden id="return_goods_customer_name_' + id + '" value="' +
                  return_goods_customer_name + '">' + '<input type="text" hidden id="return_goods_to_do_take_' +
                  id + '" value="' + return_goods_to_do_take + '">');
    };};

  if (to_do_deliver != ''){
  code_html += ('<div class="col" ' + 'id="to_do_deliver_' +
                id + '"><strong>СДАТЬ: </strong>' + to_do_deliver + '</div>');
    if (deliver_to == 'True'){
    code_html += ('<div class="col p-1 text-end align-center" ><input type="checkbox" class="btn-check" id="btn_checked_'+
                  id + '" autocomplete="off" checked onclick="javascript:f_deliver_to(' + id + ');"' +
                  '><label class="btn btn-sm btn-outline-danger" for="btn_checked_' +
                  id + '" ><i class="bi bi-arrow-repeat"></i>&nbsp;на переработку</label></div>');}
    else {
    code_html += ('<div class="col p-1 text-end align-center"><input type="checkbox" class="btn-check" id="btn_checked_' +
                 id + '" autocomplete="off" onclick="javascript:f_deliver_to(' + id + ');">' +
                 '<label class="btn btn-sm btn-outline-danger" for="btn_checked_' + id +
                 '"><i class="bi bi-arrow-repeat"></i>&nbsp;на переработку</label></div>');};
    };
  code_html += '</div></td>'
  code_html += ('<td class="text-end"id="rzv_delete_' + id + '"><a href="delete_rzv/' + id + '">' +
                '<button class="btn btn-sm btn-outline-danger fw-bold" data-toggle="tooltip" data-placement="top"' +
                'title="удалить развозку"><i class="bi bi-x-lg"></i></button></a></td>');

  document.getElementById(cst).innerHTML = code_html;
  if (fulfilled == 'True'){document.getElementById('rzv_delete_' + id).disabled = true};

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


function colapse(id){
    var area = 'collapse_' + id;
    var button = area + '_but';
    var button_minus = '<button type=button class="btn btn-sm btn-outline-secondary" ><i class="fas fa-bars"></i></button>';
    var button_plus = '<button type=button class="btn btn-sm btn-outline-success" ><i class="fas fa-bars"></i></button>';
    if (document.getElementById(area).style.display =='none'){
    document.getElementById(button).innerHTML = button_minus;
    document.getElementById(area).style.display = 'table-row-group';}
    else {document.getElementById(button).innerHTML = button_plus;
    document.getElementById(area).style.display = 'none';};
}

function rzv_status(id){
    var str_id = 'rzv_fulfilled_' + id;
    var but_id = 'rzv_fulfilled_but_' + id;
    var str_delete = 'rzv_delete_' + id;
    var str_content = document.getElementById(but_id).textContent;
    var delete_disable = ('<button class="btn btn-sm btn-outline-danger fw-bold" data-toggle="tooltip" disabled ' +
                       'data-placement="top"' + 'title="удалить развозку"><i class="bi bi-x-lg"></i></button>');
    var delete_enable = ('<a href="delete_rzv/' + id + '">' +
                '<button class="btn btn-sm btn-outline-danger fw-bold" data-toggle="tooltip" data-placement="top"' +
                'title="удалить развозку"><i class="bi bi-x-lg"></i></button></a>');
    var fulfilled = ('<button class="btn btn-sm btn-outline-success" type="button"' +
                    'onclick="javascript:rzv_status(' + id + ');" name="1" ' +
                    'id="rzv_fulfilled_but_' + id + '">' +
                    '<i class="bi bi-check2"></i>выполнено');
    var waiting = ('<button class="btn btn-sm btn-outline-danger" type="button"' +
                    'onclick="javascript:rzv_status(' + id + ');" name="0"' +
                    'id="rzv_fulfilled_but_' + id + '">' +
                    '<i class="bi bi-hourglass"></i>в процессе');
    if (str_content.includes('процесс')){
    document.getElementById(str_id).innerHTML = fulfilled;
    document.getElementById(str_delete).innerHTML = delete_disable;}
    else {document.getElementById(str_id).innerHTML = waiting;
    document.getElementById(str_delete).innerHTML = delete_enable;};
    var xhr = new XMLHttpRequest();
    var url = 'fulfilled_chg/' + id;
    xhr.open("GET", url, true);
    xhr.send();
}

function rzv_return_all(id, rzv_id){
    var str_id = 'razv_return_all_' + id;
    var str_content = document.getElementById(str_id).textContent
    var fulfilled = ('<button class="btn btn-sm btn-outline-success" type="button"' +
                    'onclick="javascript:rzv_return_all(' + id + ', ' + rzv_id + ');" value="1">' +
                    '<i class="fa-regular fa-handshake"></i>полностью');
    var waiting = ('<button class="btn btn-sm btn-outline-danger" type="button"' +
                    'onclick="javascript:rzv_return_all(' + id + ', ' + rzv_id +');" value="0">' +
                    '<i class="fas fa-person-digging"></i>&nbsp;&nbsp;  частично');
    if (str_content.includes('частично')){
    document.getElementById(str_id).innerHTML = fulfilled;}
    else {document.getElementById(str_id).innerHTML = waiting;};
    var xhr = new XMLHttpRequest();
    var url = 'return_all/' + rzv_id;
    xhr.open("GET", url, true);
    xhr.send(id);
}

function updaterecord_rzv(id){
  var fulfilled  = 'False';
  var date = document.getElementById('date_' + id).txtValue;
  var date_id = document.getElementById('rzv_id_'+id).value;
  var customer = document.getElementById('customer_'+id).value;
  var customer_name = document.getElementById('customer_name_'+id).value;
  var address = document.getElementById('address_'+id).value;
  var contact = document.getElementById('contact_'+id).value;
  var page_number = document.getElementById('page_number').value;
  var map_point = document.getElementById('map_point_'+id).value;
  try{var to_do_take = document.getElementById('to_do_take_'+id).value;
  }
  catch{var to_do_take = '';};
  try{var to_do_deliver = document.getElementById('to_do_deliver_'+id).value;
  }
  catch{var to_do_deliver = '';};
  try{document.getElementById('btn_checked_'+id).value;
  var deliver_to = 'True';}
  catch{var deliver_to = 'False';};
  try{var return_goods = document.getElementById('return_goods_'+id).value;
  var return_from = 'True';}
  catch{var return_goods = '';
  var return_from = 'False';};
  try{document.getElementById('return_all_'+id).name;
  var return_all = 'True';}
  catch{var return_all = 'False';};
  var page_number = document.getElementById('page_number').value;
  var cst = 'cst_id_' + id;
  var onclick = 'onclick="javascript:upd_rzv(' + id +');"';


  var code_html = ('<td id="map_point_' + id + '" hidden>' + map_point + '</td><td id="rzv_id_' + id + '">' + date_id +
        '<td class="text-unwrap" style="min-width:140px;"><div class="col p-1" id="rzv_fulfilled_' + id + '">');
  if (fulfilled == 'True'){
  code_html += ('<button class="btn btn-sm btn-outline-success" type="button" onclick="javascript:rzv_status(' +
               id + ');" name="1" id="rzv_fulfilled_but_' + id + '">' +
               '<i class="bi bi-check2"></i>выполнено</button>');}
  else {
  code_html += ('<button class="btn btn-sm btn-outline-danger" type="button"onclick="javascript:rzv_status(' +
            id + ');" name="0" id="rzv_fulfilled_but_' + id + '">' +
            '<i class="bi bi-hourglass"></i>в процессе</button >');};
  code_html += '</div><div class="col p-1" id="rzv_return_all_' + id + '">';
  if (return_from == 'True'){
    if (return_all == 'True'){
    code_html += ('<button class="btn btn-sm btn-outline-success" type="button" onclick="javascript:rzv_return_all(' +
    id + ');" name="1"><i class="fa-regular fa-handshake"></i>полностью</button>');}
    else{
    code_html += ('<button class="btn btn-sm btn-outline-danger" type="button" onclick="javascript:rzv_return_all(' +
                  id + ');" name="0"><i class="fas fa-person-digging"></i>&nbsp;&nbsp;  частично</button >');}
  };
  code_html += '</div></td><td colspan="2" ' + onclick + '>';
  code_html += ('<div class="row" ><div class="col p-1" id="customer_name_' + id + '">'
                + customer_name + '</div><div class="col p-1" id="address_' + id + '">' +
                address + '</div></div><div class="row" style="font-size:100%">');
  if (to_do_take != ''){
  code_html += '<div class="col p-1 text-success" id="to_do_take_' + id + '">ЗАБРАТЬ: ' + to_do_take;
    if (return_from == 'True'){
    code_html += '</div><div class="col p-1 text-danger" id="return_goods_' + id + '">&nbsp; c переработки' +
                 return_goods + '</div>'; };};
  code_html += '</div></td><td ><div class="col p-1" ' + onclick + ' id="contact_' + id + '">' +
                contact + '</div>';
  code_html += '<div class="col text-success" style="font-size:100%"><div class="row p-1">';
  if (to_do_deliver != ''){
  code_html += ('<div class="col align-self-bottom" ' + onclick + 'style="min-width:420px;" id="to_do_deliver_' +
                id + '"> СДАТЬ: ' + to_do_deliver + '</div>');
    if (deliver_to == 'True'){
    code_html += ('<div class="col p-1 text-end align-center"><input type="checkbox" class="btn-check" id="btn-checked_'+
                  id + '" autocomplete="off" checked><label class="btn btn-sm btn-outline-danger" for="btn-checked_' +
                  id + '" ><i class="bi bi-arrow-repeat"></i>&nbsp;на переработку</label></div>');}
    else {
    code_html += ('<div class="col p-1 text-end align-center"><input type="checkbox" class="btn-check" id="btn-check_' +
                 id + '" autocomplete="off"><label class="btn btn-sm btn-outline-danger" for="btn-check_' + id +
                 '"><i class="bi bi-arrow-repeat"></i>&nbsp;на переработку</label></div>');};
    };
  if (fulfilled == 'False'){
  code_html += ('</div></div></td><td class="text-end"id="rzv_delete_' + id + '"><a href="delete_rzv/' + id + '">' +
                '<button class="btn btn-sm btn-outline-danger fw-bold" data-toggle="tooltip" data-placement="top"' +
                'title="удалить развозку"><i class="bi bi-x-lg"></i></button></a></td>');}
  else{
  code_html += ('</div></div></td><td class="text-end" id="rzv_delete_' + id + '">' +
                '<button class="btn btn-sm btn-outline-danger fw-bold" data-toggle="tooltip" data-placement="top"' +
                'title="удалить развозку" disabled><i class="bi bi-x-lg"></i></button></td>');};

  document.getElementById(cst).innerHTML = code_html;

  var url = 'updaterecord_rzv/' + id;

  var xhr = new XMLHttpRequest();
  xhr.open("POST", url, true);
  xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  xhr.onreadystatechange = function () {
  if (xhr.readyState == 4 && xhr.status == 200) {
     var json = JSON.parse(xhr.responseText);
     console.log(json.date_id + ", " + json.date + ", " + json.customer + ", " + json.customer_name + ", " + json.address);
  }
  };
  var data = ("fulfilled=" + fulfilled + "&date=" + date + "&rzv_id=" + date_id + "&customer=" + customer +
   "&customer_name=" + customer_name + "&address=" + address + "&contact=" + contact + "&page_number=" + page_number +
   "&map_point=" + map_point + "&to_do_take=" + to_do_take + "&to_do_deliver=" + to_do_deliver + "&return_goods=" +
   return_goods + "&return_all=" + return_all + "&return_from=" + return_from + "&deliver_to=" + deliver_to)
  xhr.send(data);
}

function f_deliver_to(id){
    var xhr = new XMLHttpRequest();
    var url = 'deliver_to/' + id;
    xhr.open("GET", url, true);
    xhr.send();

}

function slc_rzv(date, r_date, rzv_id, id){
    var upd_date = 'r_date_' + date + id;
    var upd_id = 'r_id_' + date + id;

    var r_date = r_date;
    var r_id = rzv_id;

    document.getElementById(upd_date).value = r_date;
    document.getElementById(upd_id).value = r_id;
    document.getElementById('to_do_take_'+id).required = true
}

function slc_rzv_(date, r_date, rzv_id){
    var upd_date = 'r_date_' + date;
    var upd_id = 'r_id_' + date;

    var r_date = r_date;
    var r_id = rzv_id;
    document.getElementById(upd_date).value = r_date;
    document.getElementById(upd_id).value = r_id;
    document.getElementById('to_do_take_'+date).required = true

}


function clear_customer_modal(){
    document.getElementById('cst_id').value = null;
    document.getElementById('customer').value = null;
    document.getElementById('address').value = null;
    document.getElementById('contact').value = null;
    document.getElementById('mappoint').value = null;}

function update_modal_customer(customerObj){
    var id = customerObj.dataset.id;
    var customer = customerObj.dataset.customer;
    var address = customerObj.dataset.address;
    var contact = customerObj.dataset.contact;
    var mappoint = customerObj.dataset.mappoint;
    document.getElementById('cst_id').value = id;
    document.getElementById('customer').value = customer;
    document.getElementById('address').value = address;
    document.getElementById('contact').value = contact;
    document.getElementById('mappoint').value = mappoint;
}

function clear_rzv_modal(){
    document.getElementById('rzv_id').value = null;
    document.getElementById('customer').value = null;
    document.getElementById('address').value = null;
    document.getElementById('contact').value = null;
    document.getElementById('mappoint').value = null;
    document.getElementById('to_do_take').value = null;
    document.getElementById('to_do_deliver').value = null;
}
