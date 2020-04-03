jQuery(document).ready(function () {
    "use strict";
    jQuery('.accordion-header').toggleClass('inactive-header');
    jQuery('.accordion-header').click(function () {
        if (jQuery(this).is('.inactive-header')) {
            jQuery('.active-header').toggleClass('active-header').toggleClass('inactive-header').next().slideToggle().toggleClass('open-content');
            jQuery(this).toggleClass('active-header').toggleClass('inactive-header');
            jQuery(this).next().slideToggle().toggleClass('open-content');
        }
        else {
            jQuery(this).toggleClass('active-header').toggleClass('inactive-header');
            jQuery(this).next().slideToggle().toggleClass('open-content');
        }
    });
    return false;
});