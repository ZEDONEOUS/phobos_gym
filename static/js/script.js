$(document).ready(function(){
    var flag = true;
    $('.dashboard-admin-list h5 div.btn').click(function(){
        $(this).parentsUntil('.card').find('ul').stop().slideToggle();
        if(flag){
            $(this).text("Recoger")
        }else{
            $(this).text("Desplegar")
        }
        flag = !flag;
    });
});
