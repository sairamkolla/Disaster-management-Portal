var menuSource = document.getElementById( 'menu-template' ).innerHTML;
var menuTemplate = Handlebars.compile( menuSource );
var menuData = {
    linkName1 : "Link 1",
    linkName2 : "Link 2",
    linkName3 : "Link 3",
    linkName4 : "Link 4",
    linkName5 : "Link 5",
    linkURL1 : "http://google.com",
    linkURL2 : "http://jaskokoyn.com",
    linkURL3 : "http://yahoo.com",
    linkURL4 : "http://youtube.com",
    linkURL5 : "http://twitter.com"
};

document.getElementById( 'menu-placeholder' ).innerHTML = menuTemplate( menuData );