$(function () {
    var d = JSON.parse(data)
    // console.log('data : ', d)
    const availableTags = []
    for (var i = 0; i < d.length; i++) {
        availableTags.push(d[i].fields.name)
    }
    // var availableTags = ["ActionScript","AppleScript","Artificial Intelligence","Asp","Api","BASIC","C","C++","Clojure","COBOL","ColdFusion","Django","Erlang","Fortran",
        // "Groovy","Haskell","Java","JavaScript","jQuery","Lisp","Machine Learning","Node js","Perl","PHP","Python","Ruby","Ruby on Rails","Scala", "Scheme" ];
    $("#search-book").autocomplete({
        source: function( request, response ) {
            var matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( request.term ), "i" );
            response( $.grep( availableTags, function( item ){
                return matcher.test( item );
            }) );
        },
        // source: "/",
        // minLength: 2,
        select: function (event, ui) {
            AutoCompleteSelectHandler(event, ui)
        },
    });
    $('#print').on('click', function(){
        $("#home-content").css("display",'none')
        window.print('#mytable')
        $("#home-content").css("display", 'block')
    })
    
});

function AutoCompleteSelectHandler(event, ui) {
    var selectedObj = ui.item;
    console.log(selectedObj, ui)
}
