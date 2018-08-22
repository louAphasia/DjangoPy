(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src='https://747e7cef.ngrok.io/static/js/gallery.js?r=' +Math.floor(Math.random()*99999999999999999999);
    }
})();