$(function () {
    // window.tdata = JSON.parse('{{content}}')
    // var data = {{ book.name }}
    console.log('data : ', (data))
    const a = []
    for (var i = 0; i < data.length; i++) {
        console.log(data)
    }
    var availableTags = [
        "ActionScript",
        "AppleScript",
        "Artificial Intelligence",
        "Asp",
        "Api",
        "BASIC",
        "C",
        "C++",
        "Clojure",
        "COBOL",
        "ColdFusion",
        "Django",
        "Erlang",
        "Fortran",
        "Groovy",
        "Haskell",
        "Java",
        "JavaScript",
        "jQuery",
        "Lisp",
        "Machine Learning",
        "Node js",
        "Perl",
        "PHP",
        "Python",
        "Ruby",
        "Ruby on Rails",
        "Scala",
        "Scheme"
    ];
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
    
    // $('#search').click(function () {
    //     alert('hello');
    // })
});

function AutoCompleteSelectHandler(event, ui) {
    var selectedObj = ui.item;
    console.log(selectedObj, ui)
}

//   keeps same width as box
// jQuery.ui.autocomplete.prototype._resizeMenu = function () {
//     var ul = this.menu.element;
//     ul.outerWidth(this.element.outerWidth());
// }