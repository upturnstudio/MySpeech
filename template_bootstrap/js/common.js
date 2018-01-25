
$(document).ready(function() {
	$('.track').on('mousemove', function(e){
		e = e.target;
		if(e.className == 'track active-track'){
			return true;
		}
		if(e.className != 'track') {
			e =  $(e).offsetParent();
        }
		$(e).addClass('active-track');
        var r_inf = $(e).children().filter('.right-info');
        r_inf.children('.time-of-track').css('display', 'none');
        r_inf.children('.active-right').css('display', 'block');
	});
	$('.track').on('mouseleave', function(e){
		e = e.target;
		if(e.className != 'track active-track') {
			e =  $(e).offsetParent();
        }
		$(e).removeClass('active-track');
      	var r_inf = $(e).children().filter('.right-info');
		r_inf.children('.time-of-track').css('display', 'block');
		r_inf.children('.active-right').css('display', 'none');
	});
	$('.block-music').on('mousemove', function(e){
		e = e.target;
		if(e.className == 'block-music block-active-on'){
			return true;
		}
		if(e.className != 'block-music') {
			e =  $(e).offsetParent();
        }
        e.children('.info').children('#redline').css('background', '#FF3434');
        e.addClass('block-music-on');
        var r_inf = $(e).children().filter('.wrap-img');
        var nab = r_inf.children('.no-active-block-music');
		nab.removeClass('no-active-block-music');
        nab.addClass('active-block-music');
	});
	$('.block-music').on('mouseleave', function(e){
		e = e.target;
		if(e.className != 'block-music block-music-on') {
			e =  $(e).offsetParent();
        }
        e.children('.info').children('#redline').css('background', '#fff');
        e.removeClass('block-music-on');
        var r_inf = $(e).children().filter('.wrap-img');
        var nab = r_inf.children('.active-block-music');
		nab.removeClass('active-block-music');
        nab.addClass('no-active-block-music');
	});

    $('.signup-input').on('focus', function(e){
        $(this).parent().css('background', '#EAEAEA');
    });
    $('.signup-input').on('blur', function(e){
       $(this).parent().css('background', '#FFF');
    });
	//Таймер обратного отсчета
	//Документация: http://keith-wood.name/countdown.html
	//<div class="countdown" date-time="2015-01-07"></div>
	var austDay = new Date($(".countdown").attr("date-time"));
	$(".countdown").countdown({until: austDay, format: 'yowdHMS'});

	//Попап менеджер FancyBox
	//Документация: http://fancybox.net/howto
	//<a class="fancybox"><img src="image.jpg" /></a>
	//<a class="fancybox" data-fancybox-group="group"><img src="image.jpg" /></a>
	$(".fancybox").fancybox();

	//Навигация по Landing Page
	//$(".top_mnu") - это верхняя панель со ссылками.
	//Ссылки вида <a href="#contacts">Контакты</a>
	$(".top_mnu").navigation();

	//Добавляет классы дочерним блокам .block для анимации
	//Документация: http://imakewebthings.com/jquery-waypoints/
	$(".block").waypoint(function(direction) {
		if (direction === "down") {
			$(".class").addClass("active");
		} else if (direction === "up") {
			$(".class").removeClass("deactive");
		};
	}, {offset: 100});

	//Плавный скролл до блока .div по клику на .scroll
	//Документация: https://github.com/flesler/jquery.scrollTo
	$("a.scroll").click(function() {
		$.scrollTo($(".div"), 800, {
			offset: -90
		});
	});

	//Каруселька
	//Документация: http://owlgraphic.com/owlcarousel/
	var owl = $(".carousel");
	owl.owlCarousel({
		items : 4
	});
	owl.on("mousewheel", ".owl-wrapper", function (e) {
		if (e.deltaY > 0) {
			owl.trigger("owl.prev");
		} else {
			owl.trigger("owl.next");
		}
		e.preventDefault();
	});
	$(".next_button").click(function(){
		owl.trigger("owl.next");
	});
	$(".prev_button").click(function(){
		owl.trigger("owl.prev");
	});

	//Кнопка "Наверх"
	//Документация:
	//http://api.jquery.com/scrolltop/
	//http://api.jquery.com/animate/
	$("#top").click(function () {
		$("body, html").animate({
			scrollTop: 0
		}, 800);
		return false;
	});
	
	//Аякс отправка форм
	//Документация: http://api.jquery.com/jquery.ajax/
	$("form").submit(function() {
		$.ajax({
			type: "GET",
			url: "mail.php",
			data: $("form").serialize()
		}).done(function() {
			alert("Спасибо за заявку!");
			setTimeout(function() {
				$.fancybox.close();
			}, 1000);
		});
		return false;
	});

});