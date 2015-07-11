(function() {
    'use strict';
    //var website = openerp.website;
    //website.openerp_website = {};

    openerp.website.snippet.options["background_ex"] = openerp.website.snippet.Option.extend({
        onFocus: function() {
            alert("On focus!");
        }
    })
})();