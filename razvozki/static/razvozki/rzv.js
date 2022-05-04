function upd_ln(cst_){
    cst = 'cst_id' + cst_;
    cst2 = 'cst_id2' + cst_;
    document.getElementById(cst).style.display='none';
    document.getElementById(cst2).style.display='block';}

function upd_ln_reverse(cst_){
    cst = 'cst_id' + cst_;
    cst2 = 'cst_id2' + cst_;
    document.getElementById(cst).style.display='block';
    document.getElementById(cst2).style.display='none';}
D
function upd_ln2(cst_){
    cst = 'cst_id' + cst_;
    cst2 = 'cst_id2' + cst_;
    cst3 = 'cst_id3' + cst_;
    document.getElementById(cst).style.display='none';
    document.getElementById(cst2).style.display='table-row';
    document.getElementById(cst3).style.display='table-row';}

function upd_ln2_reverse(cst_){
    cst = 'cst_id' + cst_;
    cst2 = 'cst_id2' + cst_;
    cst3 = 'cst_id3' + cst_;
    document.getElementById(cst).style.display='block';
    document.getElementById(cst2).style.display='none';
    document.getElementById(cst3).style.display='none';}

function add_ln(new_ln){
    document.getElementById(new_ln).style.display='block';}

function add_ln_reverse(new_ln){
    document.getElementById(new_ln).style.display='none';}