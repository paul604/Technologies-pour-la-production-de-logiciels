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
            content.html("");
            $.ajax({
                url : 'http://localhost:1234/data/installations',
                type : 'get',
                dataType : 'json',
                data : 'ville='+ville.val(),
                success : function(out, statut){

                    $.each(out.data, function(index, val) {
                        console.log(val);
                        content.append(
                            '<li> nom: '+val.nom
                            +"<ul>"
                                +"<li> ville: "+val.ville+"</li>"
                                +"<li> adresse: "+val.adresse+"</li>"
                            +"</ul>"
                            +"</li>"
                            +"</br>")
                    });
                }
            });
            //activite
        }else if(ville.val() == '' && activite.val()!=''){
            content.html("unsupported");
            // $.ajax({
            //     url : 'http://localhost:1234/data/equipements',
            //     type : 'get',
            //     dataType : 'json',
            //     data : 'activite='+activite.val(),
            //     success : function(out, statut){
            //         console.log(activite.val());
            //         $.each(out.data, function(index, val) {
            //             console.log(val);
                        // content.append(
                        //     '<li> nom: '+val.nom
                        //     +"<ul>"
                        //         +"<li> ville: "+val.ville+"</li>"
                        //         +"<li> adresse: "+val.adresse+"</li>"
                        //     +"</ul>"
                        //     +"</li>"
                        //     +"</br>")
            //         });
            //     }
            // });

            //ville et activiter
        }else if (ville.val() != '' && activite.val()!='') {
            content.html("unsupported");
            // var equipementID=[];
            //
            // //array contenant les equipement en fonction de l'id de linstatlation.
            // var installationID = [];
            //
            // var insatallation_array = [];
            //
            // $.ajax({
            //     url : 'http://localhost:1234/data/equipements',
            //     type : 'get',
            //     dataType : 'json',
            //     data : 'ville='+ville.val()+"&activite="+activite.val(),
            //     success : function(out, statut){
            //         content.html("");
            //         $.each(out.data, function(index, val) {
            //             equipementID.push(val.numero_equipements);
            //         });
            //
            //         $.each(equipementID, function(index, val){
            //             var installation, equipement = getinstallationAvecIdEquipement(val);
            //             var idOfInstallation=installation.id;
            //
            //             if(insatallation_array[idOfInstallation]==null){
            //                 console.log(idOfInstallation);
            //                 insatallation_array[idOfInstallation]=installation;
            //             }
            //
            //         });
            //     }
            // });
        }
    });

}
//////////////////////////////////////////






////////////////////////////////////////// get installation avec id de l'equipement
// function getinstallationAvecIdEquipement(id){
//     $.ajax({
//         url : 'http://localhost:1234/data/equipements',
//         type : 'get',
//         dataType : 'json',
//         data : 'id='+id,
//         success : function(out, statut){
//             var installation = getinstallation(out.data);
//             return installation, out.data;
//         }
//     });
// }
//////////////////////////////////////////





////////////////////////////////////////// get installation avec l'equipement
// function getinstallation(equipement){
//     $.ajax({
//         url : 'http://localhost:1234/data/installations',
//         type : 'get',
//         dataType : 'json',
//         data : 'id='+equipement.numero_installation,
//         success: function(out, statut){
//             return out.data;
//         }
//     });
// }
//////////////////////////////////////////
