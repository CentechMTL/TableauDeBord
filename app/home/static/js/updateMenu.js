function updateMenu(value){

    // GET for set the session variable

    var lien = "/setCompanyInSession/"+value;
    $.ajax({
        type: 'GET',
        url: lien,

        error: function(resultat, status, erreur) {
            alert("erreur setSessionVariable -> " + resultat + status + erreur);
        }
    });

    var Class = ["menuCompany", "menuIrl", "menuTrl", "menuExperiment", "menuBusinessCanvas", "menuFinance", "menuKanboard"];
    var Link = ["/company/", "/kpi/irl/", "/kpi/trl/", "/experiment/", "/businessCanvas/", "/finance/", "/kanboard/"];
    for (var i = 0; i < Class.length; i++) {
        //Reference of the link
        var lien = document.getElementsByClassName(Class[i])[0];
        lien.href = Link[i]+value;
        //Visibility of the link
        if(value == 0){
            lien.style.visibility= 'hidden';
        }
        else{
            lien.style.visibility= 'visible';
        }
    }
}