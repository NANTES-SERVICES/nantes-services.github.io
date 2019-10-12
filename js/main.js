$("<select />").appendTo("nav");

// Create default option "Go to..."
$("<option />", {
  "selected": "selected",
  "value"   : "",
  "text"    : "Go to..."
}).appendTo("nav select");

// Populate dropdown with menu items
$("nav a").each(function() {
  var el = $(this);
  $("<option />", {
    "value"   : el.attr("href"),
    "text"    : el.text()
  }).appendTo("nav select");
});

$("nav select").change(function() {
  window.location = $(this).find("option:selected").val();
});

function afficheMenu(obj){
  var idMenu     = obj.id;
  var idSousMenu = 'sous' + idMenu;
  var sousMenu   = document.getElementById(idSousMenu);


  for(var i = 1; i <= 4; i++){
    if(document.getElementById('sousmenu' + i) && document.getElementById('sousmenu' + i) != sousMenu){
      document.getElementById('sousmenu' + i).style.display = "none";
    }
  }

  if(sousMenu){
    //alert(sousMenu.style.display);
    if(sousMenu.style.display == "block"){
      sousMenu.style.display = "none";
    }
    else{
      sousMenu.style.display = "block";
    }
  }


}

function cacheMain(obj) {
  var idMenu     = obj.id;
  var idSousMenu = 'sous' + idMenu;
  var sousMenu   = document.getElementById(idSousMenu);
  var main       = document.getElementById('main')

  if (sousMenu.style.display == "block") {
    main.style.display = "none";
    TweenMax.to(".btnmenu", 0.5, {rotation:90})
  }
  else if (sousMenu.style.display == "none") {
    main.style.display = "block";
    TweenMax.to(".btnmenu", 0.5, {rotation:0})
  }
}
