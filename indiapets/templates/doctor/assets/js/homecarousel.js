/* HOMEPAGE CAROUSEL SLIDER */
$(function () {
    var $carousel = $('body').find('#caroufredsel-main');
    var $items = $carousel.find(".carousel-item");
    var $headlineWrapper = $('body').find('#caroufredsel-main-wrapper');
    var $outerWrapper = $headlineWrapper.parent();
    var $window = $(window);
    var imgHeight = 460;
    var imgWidth = 1200;

    var isResponsive = (window.innerWidth <= imgWidth);

    $outerWrapper.height(imgHeight);

    $window.resize(function () {
        setTimeout(function () {
            if (window.innerWidth <= 1200) {
                $items.css("height", "auto");
                $outerWrapper.height($carousel.find(".carousel-item").height());
            } else {
                $outerWrapper.height(imgHeight);
                $items.css("height", imgHeight + "px");
            }
            if (isResponsive != (window.innerWidth <= imgWidth)) {
                isResponsive = window.innerWidth <= imgWidth;
                $carousel.trigger("destroy");
                createCarousel();
            }
        }, 10);
    }).resize();

    function createCarousel() {
        $carousel.carouFredSel({
            width: '100%',
            height: imgHeight,
            responsive: isResponsive,
            items: {
                visible: isResponsive ? 1 : 3,
                start: isResponsive ? 0 : -1,
                width: imgWidth,
                height: imgHeight
            },
            auto: {
                play: true,
                pauseOnHover: true,
                timeoutDuration:4000
            },
            scroll: {
                items: 1,
                duration: 1000,
                easing: "quadratic",
                onBefore: function (data) {
                    $(data.items.visible.get(isResponsive ? 0 : 1)).find(".slidetext").animate({ right: 100, opacity: 0 }, 500);
                },
                onAfter: function (data) {
                    $(data.items.visible.get(isResponsive ? 0 : 1)).find(".slidetext").animate({ right: 0, opacity: 0.9 }, 500);
                    $(data.items.visible.get(isResponsive ? 1 : 0)).find(".slidetext").animate({ right: 100, opacity: 0 }, 500);

                }
            },
            prev: '.car-prev',
            next: '.car-next'
        });
    };
    createCarousel();
    $items.first().find('img').load(function() {
        $window.resize();
    });
});