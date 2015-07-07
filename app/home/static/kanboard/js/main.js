$(function() {

    initKanboard("{% url "kanboard:getDetailKanboard" 1 %}",
                    {{company.id}},
                    "{% url "kanboard:kanboardGetDetailCard" 1 %}",
                    "{% url "kanboard:kanboardDeleteCard" 1 %}",
                    "{% url "founder:detail" 1 %}"
                    );

    var dialog, form,

    dialog = $( "#dialog-form" ).dialog({
      autoOpen: false,
      height: 450,
      width: 350,
      modal: true,
      buttons: {
        "Create": function() {
          if(document.getElementById("title").value != ""){
            addCard('{% url "kanboard:kanboard" 1 %}',
                    "{% url "kanboard:kanboardGetDetailCard" 1 %}",
                    {{company.id}},
                    "{% url "kanboard:kanboardDeleteCard" 1 %}",
                    "{% url 'founder:detail' 1 %}"
                    );

            dialog.dialog( "close" );
            document.getElementById("title").style.border = "1px solid #a9a9a9";
          }
          else{
            document.getElementById("title").style.border = "1px solid red";
          }
        },
        Cancel: function() {
          dialog.dialog( "close" );
        }
      },
      close: function() {
        form[ 0 ].reset();
        document.getElementById('update').value = "False";
      }
    });

    form = dialog.find( "form" );

    $( "#create-card" ).click(function() {
      dialog.dialog( "open" );
    });
  });