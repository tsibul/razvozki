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
    document.getElementById(cst4).style.display='table-row';
    document.getElementById(cst5).style.display='table-row';}

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
    document.getElementById(updcust_id).value = cust_id;
    document.getElementById(updcust_address).value = cust_address;
    document.getElementById(updcust_contact).value = cust_contact;

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