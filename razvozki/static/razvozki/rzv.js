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
  a = div.getElementsByTagName("li");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

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

function colapse(id){
    var area = 'collapse_' + id;
    if (document.getElementById(area).style.display =='none'){
    document.getElementById(area).style.display = 'table-row-group';}
    else {document.getElementById(area).style.display = 'none';};
}

function rzv_status(butFulfilled){
    var id = butFulfilled.dataset.id;
    var str_delete = 'delete_' + id;
    var parentRow = Array.from(butFulfilled.parentElement
                                           .parentElement
                                           .children);
    if (butFulfilled.dataset.fulfilled == "False"){
        document.getElementById(str_delete).disabled = true;
        butFulfilled.childNodes[1].className = 'bi bi-check2';
        butFulfilled.classList.add('btn-outline-success');
        butFulfilled.classList.remove('btn-outline-danger');
        butFulfilled.dataset.fulfilled = "True";
        for (var i=3; i<=6; i++){
        parentRow[i].setAttribute('data-bs-toggle', null);
        parentRow[i].setAttribute( 'data-bs-target', null);}
    }
    else{
        document.getElementById(str_delete).disabled = false;
        butFulfilled.childNodes[1].className = 'bi bi-hourglass';
        butFulfilled.classList.add('btn-outline-danger');
        butFulfilled.classList.remove('btn-outline-success');
        butFulfilled.dataset.fulfilled = "False";
        for (var i=3; i<=6; i++){
        parentRow[i].setAttribute('data-bs-toggle', 'modal');
        parentRow[i].setAttribute( 'data-bs-target', '#razvozkaModal');}
    };
    butFulfilled.childNodes
    var xhr = new XMLHttpRequest();
    var url = 'fulfilled_chg/' + id;
    xhr.open("GET", url, true);
    xhr.send();
}

function rzv_return_all(returnObj){
    var id = returnObj.dataset.id;
    var returnGoodsId = returnObj.dataset.return_goods;
    var returnAll = returnObj.children[0].className == "fas fa-person-digging";
    if (returnAll){
        returnObj.children[0].className = "fa-regular fa-handshake";
        returnObj.classList.remove("btn-outline-danger");
        returnObj.classList.add("btn-outline-success");
    }
    else{
        returnObj.children[0].className = "fas fa-person-digging";
        returnObj.classList.remove("btn-outline-success");
        returnObj.classList.add("btn-outline-danger");
    }
    var xhr = new XMLHttpRequest();
    var url = 'return_all/' + returnGoodsId;
    xhr.open("GET", url, true);
    xhr.send(id);
}

function updaterecord_rzv_(id){
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

function f_deliver_to(deliverObj){
    var id = deliverObj.dataset.id;
    document.getElementById('delete_' + id).disabled = deliverObj.checked ? true : false;
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

function slc_rzv_(date, r_date, r_id, r_to_do_deliver){
    document.getElementById('upd_date').value = r_date + ' / ' + r_to_do_deliver;
    document.getElementById('upd_id').value = r_id;
    document.getElementById('to_do_take').required = true
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
    document.getElementById('date_id').value = 1;
    document.getElementById('date').value = null;
    document.getElementById('customer').value = null;
    document.getElementById('address').value = null;
    document.getElementById('contact').value = null;
    document.getElementById('mappoint').value = null;
    document.getElementById('to_do_take').value = null;
    document.getElementById('to_do_deliver').value = null;
    document.getElementById('customer_id').value = null;
    document.getElementById('upd_date').value = null;
    document.getElementById('upd_id').value = null;
    var ulElement = document.getElementById('ul_ret');
    while (ulElement.firstChild) {
    ulElement.removeChild(ulElement.lastChild);
  }
}

function select_customer(choseObj){
    var cst_id = choseObj.dataset.id;
    var name = choseObj.outerText;
    var address = choseObj.dataset.address;
    var contact = choseObj.dataset.contact;
    var mappoint= choseObj.dataset.mappoint;

    var x,xmlhttp,xmlDoc,tmp_xml,code_html;
    tmp_xml = 'rzv_return.xml/' + cst_id;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", tmp_xml, false);
    xmlhttp.send();
    xmlDoc = xmlhttp.responseXML;
    code_html = '';
    try{x = xmlDoc.getElementsByTagName("Razvozka");
    if(x.length!=0){
    for (var i = 0; i <x.length; i++) {
    var r_id = x[i].getElementsByTagName("id")[0].childNodes[0].nodeValue;
    var r_date =  x[i].getElementsByTagName("date")[0].childNodes[0].nodeValue;
    var r_customer_name =  x[i].getElementsByTagName("customer_name")[0].childNodes[0].nodeValue;
    var r_to_do_deliver =  x[i].getElementsByTagName("to_do_deliver")[0].childNodes[0].nodeValue;
    code_html = code_html + '<li id="rzv_ret_' + r_date + '_'+ r_id + '"';
    code_html = code_html + '<class="dropdown-item" onclick="javascript:slc_rzv_(';
    code_html = code_html + "'" + rzv_id + "', '" + r_date + "', '" + r_id + "', '" + r_to_do_deliver + "');" + '">';
    code_html = code_html + r_date + ' / ' + r_to_do_deliver + '</li>';
    };
    document.getElementById('ul_ret').innerHTML = code_html;}}
    catch{};

    document.getElementById('customer').value = name;
    document.getElementById('address').value = address;
    document.getElementById('contact').value = contact;
    document.getElementById('mappoint').value = mappoint;
    document.getElementById('customer_id').value = cst_id;
}

function add_razvozka(buttonObj){
    document.getElementById('date').value = buttonObj.parentElement
                                                              .nextElementSibling
                                                              .dataset.date;
    var razvozkiBody = buttonObj.parentElement
                                .parentElement
                                .parentElement
                                .nextElementSibling
                                .children;
    var maxDateId = 0;
    for(var i=0; i<razvozkiBody.length; i++){
        if(maxDateId < razvozkiBody[i].dataset.date_id) maxDateId = razvozkiBody[i].dataset.date_id;
    }
    document.getElementById('date_id').value = parseInt(maxDateId) + 1;
}

function updaterecord_rzv(updObj){
    var parentObj = updObj.parentElement;
    document.getElementById('rzv_id').value = parentObj.dataset.id;
    document.getElementById('date_id').value = parentObj.dataset.date_id;
    document.getElementById('date').value = parentObj.dataset.date;
    document.getElementById('customer').value = parentObj.dataset.customer_name;
    document.getElementById('address').value = parentObj.dataset.address;
    document.getElementById('contact').value = parentObj.dataset.contact;
    document.getElementById('mappoint').value = parentObj.dataset.mappoint;
    document.getElementById('to_do_take').value = parentObj.dataset.to_do_take;
    document.getElementById('to_do_deliver').value = parentObj.dataset.to_do_deliver;
    document.getElementById('customer_id').value = parentObj.dataset.customer_id;

    var x,xmlhttp,xmlDoc,tmp_xml,code_html;
    tmp_xml = 'rzv_return.xml/' + parentObj.dataset.customer_id;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", tmp_xml, false);
    xmlhttp.send();
    xmlDoc = xmlhttp.responseXML;
    code_html = '';
    try{x = xmlDoc.getElementsByTagName("Razvozka");
    if(x.length!=0){
    for (var i = 0; i <x.length; i++) {
    var r_id = x[i].getElementsByTagName("id")[0].childNodes[0].nodeValue;
    var r_date =  x[i].getElementsByTagName("date")[0].childNodes[0].nodeValue;
    var r_customer_name =  x[i].getElementsByTagName("customer_name")[0].childNodes[0].nodeValue;
    var r_to_do_deliver =  x[i].getElementsByTagName("to_do_deliver")[0].childNodes[0].nodeValue;
    code_html = code_html + '<li id="rzv_ret_' + r_date + '_'+ r_id + '"';
    code_html = code_html + '<class="dropdown-item" onclick="javascript:slc_rzv_(';
    code_html = code_html + "'" + rzv_id + "', '" + r_date + "', '" + r_id + "', '" + r_to_do_deliver + "');" + '">';
    code_html = code_html + r_date + ' / ' + r_to_do_deliver + '</li>';
    };
    document.getElementById('ul_ret').innerHTML = code_html;}}
    catch{};

    document.getElementById('upd_date').value = parentObj.dataset.return_goods;
    document.getElementById('upd_id').value = parentObj.dataset.return_id;
}

function clear_return(){
    document.getElementById('upd_date').value = null;
    document.getElementById('upd_id').value = null;
    var ulElement = document.getElementById('ul_ret');
    while (ulElement.firstChild) {
    ulElement.removeChild(ulElement.lastChild);
  }
}