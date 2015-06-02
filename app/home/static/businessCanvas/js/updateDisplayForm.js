<!-- Display the add form-->
function updateDisplayForm(id, force){
    var forms = ["KeyPartner", "KeyActivitie", "KeyResource", "ValueProposition", "CustomerRelationship", "Channel", "CustomerSegment", "CostStructure", "RevenueStream", "BrainstormingSpace"];
    for (var i in forms) {
        //Reference of the form
        form = document.getElementById(forms[i]);
        //Visibility of the form
        var forceDisplay = "False"
        if (arguments.length == 2){
            forceDisplay = force
        }
        if(forceDisplay == "True" && forms[i] == id){
            form.style.visibility= 'visible';
            form.style.display= 'inline';
        }
        else{
            if(forms[i] != id || form.style.display != 'none'){
                form.style.visibility= 'hidden';
                form.style.display= 'none';
                var inputs = form.getElementsByTagName('input');
                //inputs[0] -> token CSRF
                inputs[1].value = "";
                inputs[2].value = "";
                inputs[3].value = "False";;
            }
            else{
                form.style.visibility= 'visible';
                form.style.display= 'inline';
            }
        }

    }
}