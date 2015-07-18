(function(){

    "use strict";

    var _t = openerp._t;
    openerp.web_tweak = {};

    openerp.web.UserMenu.include({
        on_menu_help: function() {
            window.open('http://www.moco.co/help', '_blank');
        },
        on_menu_about: function() {
            window.open('http://www.moco.co/about', '_blank');
        },
        on_menu_support: function() {
            window.open('http://www.moco.co/support', '_blank');
        },
    });

})();