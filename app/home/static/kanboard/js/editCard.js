// Change the form for update element
function editCard(id, baseLien){
    idCard = id;
    var myRegexp = /([a-zA-Z]+)/g;
    var match = myRegexp.exec(id); //match[1] is the id of element
    if(match[1]){
        card = match[1];
        var pos = baseLien.lastIndexOf('/'); // position du dernier "/"
        baseLien = baseLien.substr(0, pos+1);
        var lien = baseLien+idCard;

        $.ajax({
          type: 'GET',
          url: lien,

          success: function(data, status) {
                alert("It's ok sîr!");
                var form = document.getElementById(card);
                var inputs = form.getElementsByTagName("input");
                //inputs[0] -> token CSRF
                inputs[1].value = data.title;
                inputs[2].value = data.comment;
                inputs[3].value = idElement;

                updateDisplayForm(type, "True");
            },

          error: function(resultat, status, erreur) {
            alert(erreur); }
        });
    }
}