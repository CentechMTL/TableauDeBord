function refreshCard(id, baseLien, linkDeleteCard, linkFounder, username){
    var linkGetDetail = baseLien;
    var myRegexp = /([0-9]+)/g;
    var match = myRegexp.exec(baseLien); //match[1] is the id of the archive
    if(match[1]){
        var pos = baseLien.lastIndexOf('/'); // position du dernier "/"
        baseLien = baseLien.substr(0, pos+1);
        var lien = baseLien+id;

        $.ajax({
            type: 'GET',
            url: lien,

            success: function(data, status) {
                //Reset all the content of the card
                var li = document.getElementById("card-"+data.id);
                li.innerHTML = "";

                //Coloration of the card
                if(new Date() > new Date(data.deadline)){
                    li.style.backgroundColor = '#eedada';
                }
                else
                {
                   li.style.backgroundColor = '#ffffff';
                }

                //Title
                var titre = document.createElement('h3');
                titre.innerHTML = data.title;

                //Creator
                var creator = document.createElement('span');
                creator.innerHTML = "créé par : " + data.creator + "<br>";

                //Deadline
                var date = document.createElement('span');
                if(data.deadline){
                    date.innerHTML = "pour le : " + data.deadline + "<br>";
                }

                //Link to delete this card
                var spanDelete = document.createElement('span');
                spanDelete.className = data.id;
                spanDelete.setAttribute('onclick',"deleteCard(this.className,'"+linkDeleteCard+"');");
                spanDelete.innerHTML = "<i class='fa fa-trash'></i>";
                spanDelete.style.float = "right";
                var linkDelete = document.createElement('a');

                //Link to edit this card
                var spanEdit = document.createElement('span');
                spanEdit.className = data.id;
                spanEdit.setAttribute('onclick',"editCard(this.className,'"+linkGetDetail+"');");
                spanEdit.innerHTML = "<i class='fa fa-pencil-square-o'></i>";
                spanEdit.style.float = "right";
                var linkEdit = document.createElement('a');

                //Description of the card
                var p = document.createElement('p');
                p.innerHTML = "<br>" + data.comment;

                //Picture of assigned
                if(data.picture){
                    var linkAssigned = document.createElement('a');

                    lien = linkFounder;
                    var pos = lien.lastIndexOf('/'); // position du dernier "/"
                    lien = lien.substr(0, pos+1);
                    var lien = lien+data.assigned;
                    linkAssigned.href = lien;
                    linkAssigned.className = "assigned";

                    var imgAssigned = document.createElement('img');
                    imgAssigned.className = "avatar";
                    imgAssigned.src = "/media/" + data.picture;
                    imgAssigned.style.width = "40px";

                    linkAssigned.appendChild(imgAssigned);
                }

                //We can edit and delete only if we are the creator of the task/card
                if(data.creator == username){
                    linkDelete.appendChild(spanDelete);
                    linkEdit.appendChild(spanEdit);
                    titre.appendChild(linkDelete);
                    titre.appendChild(linkEdit);
                }
                li.appendChild(titre);
                li.appendChild(creator);
                if(data.deadline){
                    li.appendChild(date);
                }
                li.appendChild(p);
                if(data.picture){
                    li.appendChild(linkAssigned);
                }

                //Change column for go in the new phase
                var ul = li.parentElement;
                var newUl = document.getElementById('phase-'+ data.phase);

                if(ul != newUl){
                    ul.removeChild(li);
                    newUl.appendChild(li);
                }
            },

            error: function(resultat, status, erreur) {
                alert(erreur);
            }
        });
    }
}