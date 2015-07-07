function initKanboard(baseLien, id, lienGetDetail, linkDeleteCard, linkFounder){
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
                var board = document.getElementById('board');
                var compteurPhase = 0;

                for(phase in data){
                    compteurPhase = compteurPhase +1;

                    var div = document.createElement('div');
                    div.className = "column";

                    var titlePhase = document.createElement('h2');
                    titlePhase.innerHTML = data[phase][0];

                    var ul = document.createElement('ul');
                    ul.className = "sortable phase";
                    ul.id = "phase-"+compteurPhase;

                    for(card in data[phase][1]){
                        var li = document.createElement('li');
                        li.className = "card";
                        li.id = "card-"+card;

                        ul.appendChild(li);

                        refreshCard(card, lienGetDetail, linkDeleteCard, linkFounder);
                    }

                    div.appendChild(titlePhase);
                    div.appendChild(ul);
                    board.appendChild(div);
                }

            initSortable();
            },

            error: function(resultat, status, erreur) {
                alert(erreur);
            }
        });
    }
}