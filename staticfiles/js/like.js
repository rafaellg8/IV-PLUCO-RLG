$(function(){
        $(".like").click(function() {
            var id;
            id = $(this).attr("data-catid");

             $.get('/foros/like', {idCom: id}, function(data){
                      /*
                      Obtenemos el like_count con id igual que el idCom.
                      Lo usamos para mostrar el número de Likes.
                      like_oculto lo usamos para ocultar el botón después.
                      */
                       var like_count = document.getElementById(id);
                       //Obtenemos la id que sea liken, donde n es el número de comentario
                       var like_oculto = document.getElementById('like'+id);
                       $(like_count).html(data);
                       $(like_count).show();
                       $(like_oculto).hide();

                   });
        });
});
