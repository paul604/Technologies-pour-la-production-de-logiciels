////////////////////////////////////////// s'exécute après le chargement du HTML
$(document).ready(function(){

    autocomplete();

});
//////////////////////////////////////////





////////////////////////////////////////// gère l'autocomplet
function autocomplete(){

    //ville
    var champ_ville = $("#ville");

    console.log(champ_ville.val());
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
  var outData='suggestions='+ville;
  $.ajax({
      url : 'http://localhost:1234/data/villes',
      type : 'get',
      dataType : 'json',
      data : outData,
      success : function(out, statut){
        var tab = [];
        $.each(out, function (i, val) {
          tab[tab.length]=val;
        });
        response(tab);
      }
  });
};
//////////////////////////////////////////




function getActivite(activite, response){
    var outData='suggestions='+activite;
    $.ajax({
        url : 'http://localhost:1234/data/activites',
        type : 'get',
        dataType : 'json',
        data : outData,
        success : function(out, statut){
          var tab = [];
          $.each(out, function (i, val) {
            tab[tab.length]=val;
          });
          response(tab);
        }
    });
}
