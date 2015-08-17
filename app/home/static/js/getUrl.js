/**
GET an url as a reverse() call in Django

namespace -> the name of the view (ex : 'home:getUrl')
arg       -> the arg or kwarg of the view (ex : 1 / the id of a company)
redirect  -> true if you want be redirect to this url directly
          -> false if you want get the url as a string
**/

function getUrl(namespace, arg, redirect){
    link = "/getUrl/" + namespace + "/" + arg;
    $.ajax({
        type: 'GET',
        url: link,

        success: function(data, status) {
            if(redirect){
                window.location = data['url'];
            }
            else{
                return data['url'];
            }
        },

        error: function(resultat, status, erreur) {
        }
    });
}