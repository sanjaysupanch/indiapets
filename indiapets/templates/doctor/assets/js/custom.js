/* MAIN MENU */
var ww = document.body.clientWidth;

jQuery(window).load(function () {
    "use strict";
    jQuery('body').find(".nav-container").css('pointer-events', 'auto');
});

jQuery(document).ready(function () {
    "use strict";
    jQuery('body').find(".nav li a").each(function () {
        if (jQuery(this).next().length > 0) {
            jQuery(this).addClass("parent");
        }
    });
    jQuery('body').find(".toggleMenu").click(function (e) {
        e.preventDefault();
        jQuery(this).toggleClass("active");
        jQuery('body').find(".nav").toggle();
    });
    adjustMenu();
});

jQuery(window).bind('resize orientationchange', function () {
    "use strict";
    ww = document.body.clientWidth;
    adjustMenu();
});

var adjustMenu = function () {
    "use strict";
    if (ww < 900) {
        jQuery('body').find(".toggleMenu").css("display", "inline-block");
        if (!jQuery('body').find(".toggleMenu").hasClass("active")) {
            jQuery('body').find(".nav").hide();
        } else {
            jQuery('body').find(".nav").show();
        }
        jQuery('body').find(".nav li").unbind('mouseenter mouseleave');
        jQuery('body').find(".nav li a.parent").unbind('click').bind('click', function (e) {
            e.preventDefault();
            jQuery(this).parent("li").toggleClass("hover");
        });
    } else if (ww >= 900) {
        jQuery('body').find(".toggleMenu").css("display", "none");
        jQuery('body').find(".nav").show();
        jQuery('body').find(".nav li").removeClass("hover");
        jQuery('body').find(".nav li a").unbind('click');
        jQuery('body').find(".nav li").unbind('mouseenter mouseleave').bind('mouseenter mouseleave', function () {
            jQuery(this).toggleClass('hover');
            jQuery(this).toggleClass('activelink');
            jQuery(this).find("ul").toggleClass('animatedfast');
            jQuery(this).find("ul").toggleClass('fadeInDown');
        });
        jQuery('body').find(".nav ul li").unbind('mouseenter mouseleave').bind('mouseenter mouseleave', function () {
            jQuery(this).toggleClass('hover');
            jQuery(this).find("ul li").toggleClass('animatedfast');
            jQuery(this).find("ul li").toggleClass('fadeInLeft');
        });
    }
};

/* STICKY MENU */
jQuery(document).ready(function () {
    "use strict";
    fixnav();
});

var nav = jQuery('body').find('.nav-container');

function fixnav() {
    "use strict";
    jQuery(window).bind("scroll", function () {
        if (jQuery(this).scrollTop() > 120 && ww >= 900) {
            nav.addClass("f-nav");
        } else {
            nav.removeClass("f-nav");
        }
    });
}

/* BACK TO TOP BUTTON */

jQuery(document).ready(function () {
    "use strict";
    var offset = 220;
    var duration = 500;
    if (ww >= 1200) {
    jQuery(window).scroll(function () {
        if (jQuery(this).scrollTop() > offset) {
            jQuery('.back-to-top').fadeIn(duration);
        } else {
            jQuery('.back-to-top').fadeOut(duration);
        }
    });
    }

    jQuery('.back-to-top').click(function (event) {
        event.preventDefault();
        jQuery('html, body').animate({
            scrollTop: 0
        }, duration);
        return false;
    });
});

/* ICON EFFECT */

jQuery('body').find(".icon-container a").hover(
    function () {
        "use strict";
        jQuery(this).addClass('animated pulse');
    }, function () {
        "use strict";
        jQuery(this).removeClass('animated pulse');
    }
);

/* CAROUSEL FIXES */
jQuery('a').on('dragstart', function (event) {
    "use strict";
    event.preventDefault();
});

jQuery(document).ready(function () {
    "use strict";
    jQuery(".owl-prev:empty").parent().hide();
});

/* Info Box */

jQuery('body').find('.vet-message-close').on("click", function () {
    "use strict";
    jQuery(this).parent().fadeOut();
});