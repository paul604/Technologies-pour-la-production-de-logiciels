////////////////////////////////////////// s'exécute après le chargement du HTML
$(document).ready(function(){

    autocomplete();
    recherche();

});
//////////////////////////////////////////





////////////////////////////////////////// gère l'autocomplet
function autocomplete(){

    //ville
    var champ_ville = $("#ville");

    champ_ville.autocomplete({
        minLength: 1,
        source:function(ville, response){
          getVille(ville.term, response);
        }
    });


    //activite
    var champ_activite = $("#activite");

    champ_activite.autocomplete({
        minLength: 1,
        source:function(activite, response){
          getActivite(activite.term, response);
        }
    });

}
//////////////////////////////////////////





////////////////////////////////////////// perme de get les vill matchant avec `ville`
function getVille(ville, response){
    console.log("auto comp vill");
  var outData='suggestions='+ville;
  $.ajax({
      url : 'http://localhost:1234/data/villes',
      type : 'get',
      dataType : 'json',
      data : outData,
      success : function(out, statut){response(out.data); }
  });
};
//////////////////////////////////////////





////////////////////////////////////////// perme de get les activité matchant avec `activite`
function getActivite(activite, response){
    var outData='suggestions='+activite;
    $.ajax({
        url : 'http://localhost:1234/data/activites',
        type : 'get',
        dataType : 'json',
        data : outData,
        success : function(out, statut){ response(out.data); }
    });
};
//////////////////////////////////////////





////////////////////////////////////////// recherche
function recherche() {

    var ville = $('#ville');
    var activite = $('#activite');
    var content = $('#content');

    // selement ville
    $('#submit').click(function(event) {
        if (ville.val() == '' && activite.val()=='') {
            content.html("404");
        }else if (ville.val() != '' && activite.val()=='') {
            $.ajax({
                url : 'http://localhost:1234/data/installations',
                type : 'get',
                dataType : 'json',
                data : 'ville='+ville.val(),
                success : function(out, statut){
                    content.html("");
                    $.each(out.data, function(index, val) {
                        console.log(val);
                        content.append(
                            '<li> nom: '+val.nom
                            +"<ul>"
                                +"<li> ville: "+val.ville+"</li>"
                                +"<li> adresse: "+val.adresse+"</li>"
                            +"</ul>"
                            +"</li>")
                    });
                }
            });
            //ville et activiter
        }else if (ville.val() != '' && activite.val()!='') {
            $.ajax({
                url : 'http://localhost:1234/data/equipements',
                type : 'get',
                dataType : 'json',
                data : 'ville='+ville.val()+"&activite="+activite.val(),
                success : function(out, statut){
                    content.html("");
                    $.each(out.data, function(index, val) {
                        console.log(val);
                        // content.append(
                        //     '<li> nom: '+val.nom
                        //     +"<ul>"
                        //         +"<li> ville: "+val.ville+"</li>"
                        //         +"<li> adresse: "+val.adresse+"</li>"
                        //     +"</ul>"
                        //     +"</li>")
                    });
                }
            });
        }
    });

}
//////////////////////////////////////////
