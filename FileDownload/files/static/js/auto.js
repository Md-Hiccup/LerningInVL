$(function () {
    var availableTags = [
        "ActionScript",
        "AppleScript",
        "Asp",
        "BASIC",
        "C",
        "C++",
        "Clojure",
        "COBOL",
        "ColdFusion",
        "Erlang",
        "Fortran",
        "Groovy",
        "Haskell",
        "Java",
        "JavaScript",
        "Lisp",
        "Perl",
        "PHP",
        "Python",
        "Ruby",
        "Scala",
        "Scheme"
    ];
    $('#search').click(function () {
        alert('hello');
    })
    $("#search-book").autocomplete({
        // source = "/",
        source = availableTags,
        // minLength: 2,
        // select: function (event, ui) {
        //     AutoCompleteSelectHandler(event, ui)
        // },
    });
});

// function AutoCompleteSelectHandler(event, ui) {
//     var selectedObj = ui.item;
// }

//   keeps same width as box
// jQuery.ui.autocomplete.prototype._resizeMenu = function () {
//     var ul = this.menu.element;
//     ul.outerWidth(this.element.outerWidth());
// }