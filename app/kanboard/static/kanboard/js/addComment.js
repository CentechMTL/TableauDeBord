function addComment(lien, cardId){
    var textarea = document.getElementById('textarea');

    lien = lien.replace(/([0-9]+)/, cardId);
    $.ajax({
        type: 'POST',
        url: lien,
        data: '&comment=' + textarea.value,

        success: function(data, status) {
            var div = document.getElementById("listComments");
            var newComment = document.createElement('div');
            newComment.style.borderBottom = "1px dashed black";
            newComment.style.padding = "10px";
            newComment.innerHTML = data.comment + "<br>" + data.created + " - " + data.creator;

            div.appendChild(newComment);

            textarea.value = "";
        },

        error: function(resultat, status, erreur) {
            alert('error');
        }
    });
}