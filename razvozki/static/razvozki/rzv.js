function upd_ln(cst_){
    cst = 'cst_id_' + cst_;
    cst2 = 'cst_id2_' + cst_;
    document.getElementById(cst).style.display='none';
    document.getElementById(cst2).style.display='block';}

function upd_ln_reverse(cst_){
    cst = 'cst_id_' + cst_;
    cst2 = 'cst_id2_' + cst_;
    document.getElementById(cst).style.display='block';
    document.getElementById(cst2).style.display='none';}

function upd_ln2(cst_){
    cst = 'cst_id_' + cst_;
    cst2 = 'cst_id2_' + cst_;
    cst3 = 'cst_id3_' + cst_;
    document.getElementById(cst).style.display='none';
    document.getElementById(cst2).style.display='table-row';
    document.getElementById(cst3).style.display='table-row';}

function upd_ln2_reverse(cst_){
    cst = 'cst_id_' + cst_;
    cst2 = 'cst_id2_' + cst_;
    cst3 = 'cst_id3_' + cst_;
    document.getElementById(cst).style.display='table-row';
    document.getElementById(cst2).style.display='none';
    document.getElementById(cst3).style.display='none';}

function add_ln(new_ln){
    document.getElementById(new_ln).style.display='block';}

function add_ln_reverse(new_ln){
    document.getElementById(new_ln).style.display='none';}

function add_ln2(cst_){
    cst4 = 'cst_id4_' + cst_;
    cst5 = 'cst_id5_' + cst_;
    document.getElementById(cst4).style.display='table-row';
    document.getElementById(cst5).style.display='table-row';}

function add_ln2_reverse(cst_){
    cst4 = 'cst_id4_' + cst_;
    cst5 = 'cst_id5_' + cst_;
    document.getElementById(cst4).style.display='none';
    document.getElementById(cst5).style.display='none';}

function slc_cst(cst_name, rzv_id, cst_id, cst_address, cst_contact){
    updcust_name = 'updcust_name_' + rzv_id;
    updcust_id = 'updcust_id_' + rzv_id;
    updcust_address = 'updcust_address_' + rzv_id;
    updcust_contact = 'updcust_contact_' + rzv_id;
    cust_name = cst_name;
    cust_id = cst_id;
    cust_address = cst_address;
    cust_contact = cst_contact;
    document.getElementById(updcust_name).value = cust_name;
    document.getElementById(updcust_id).value = cust_id;
    document.getElementById(updcust_address).value = cust_address;
    document.getElementById(updcust_contact).value = cust_contact;

}