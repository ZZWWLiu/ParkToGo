# national parks info parser

# find a way to get national parks data
# http://us-national-parks.findthedata.org/l/16/North-Cascades-National-Park
# http://us-national-parks.findthedata.org/l/59/Acadia-National-Park
# crawl 1-59 

import re
import urllib2
from bs4 import BeautifulSoup
import time
import json
import os

# url = "http://us-national-parks.findthedata.org/l/32"
# html= 
"""
<!DOCTYPE html>
<html lang="en-us">
	<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
					<link rel="canonical" href="http://us-national-parks.findthedata.org/l/58/National-Park-of-American-Samoa" />
				<meta http-equiv="X-UA-Compatible" content="IE=edge" />
		<meta name="verify-v1" content="lNYmjN6pYU0M7ekDOEFtHhvT6hR/namYD7ZkWvOoKYI=" />
		<meta name="google-site-verification" content="iWjsCDlyBgKJBtoMZUnCL-gtg8wt9c6T0QmKov8eMhA" /><meta name="google-site-verification" content="Y4z9UsySdOSDMsyW_KtR9F4kydwHRjF6tI8RFZlTu-Y" />		<meta property="fb:page_id" content="115658481864067" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
		<link rel="shortcut icon" href="/rx/img/ftd-favicon.ico" type="image/x-icon" />
		<title>U.S. National Parks | National Park of American Samoa</title>
		<link rel='stylesheet' media='all' href='http://cdn2.findthebest.com/rx/core.225.css'/><link rel='stylesheet' media='all' href='http://cdn2.findthebest.com/rx/desktop.225.css'/><link rel='stylesheet' media='all' href='http://cdn2.findthebest.com/rx/detail.225.css'/>		<link type="text/css" rel="stylesheet" media="all" href="http://cdn1.findthebest.com/sites/default/files/css/css_f2dec9ff40a8aeae84a69be4356c93f1.ver.d8f162ea1dfb42dd5f1ad63055978fc68d60a79b-S.css" />
<!--[if IE]>
<link type="text/css" rel="stylesheet" media="all" href="/sites/all/themes/ftb1/ie.css?S" />
<![endif]-->
<!--[if IE 7]>
<link type="text/css" rel="stylesheet" media="all" href="/sites/all/themes/ftb1/ie7.css?S" />
<![endif]-->
		<style>.thm-color {color:#1D6660;}.thm-hover:hover {color:#1D998F;}.thm-bg,.thm-on.thm-on-bg {background-color:#1D6660;}.thm-bg-hover:hover {background-color:#1D6660;}.thm-btn {background-color:#1D6660;border-color:#1D6660;color:#fff;}.thm-btn:hover {background-color:#1D998F;border-color:#1D998F;}.thm-border,.thm-on .thm-on-border,.thm-border-hover:hover {border-color:#1D6660;}.thm-bt,.thm-bt-hover:hover,.thm-on .thm-on-bt,.thm-abt:after,.thm-habt:hover:after {border-top-color:#1D6660;}.thm-br,.thm-on .thm-on-br,.thm-abr:after {border-right-color:#1D6660;}.thm-bb,.thm-on .thm-on-bb,.thm-abb:after {border-bottom-color:#1D6660;}.thm-bl,.thm-on .thm-on-bl,.thm-abl:after {border-left-color:#1D6660;}input.thm-focus-border:focus {border-color:#1D6660;}.thm-stroke,.thm-on .thm-on-stroke {stroke:#1D6660;}.thm-fill {fill:#1D6660 !important;}a,.link,.thm-link {color:#1D6660;}a:hover,.link:hover {color:#1D998F;}::selection {background:#1D6660;}::-moz-selection{background:#1D6660;}input[type="text"]:focus, input[type="password"]:focus, textarea:focus, select:focus {border:1px solid #1D6660;}</style><meta property ="og:image" content="http://img3.findthebest.com/sites/default/files/721/media/images/National_Park_of_American_Samoa_59598.JPG" />
<meta property ="og:type" content="product" />
<meta property="fb:app_id" content="117946838285450" />
<meta name="keywords" content="national park, yosemite, yellowstone, denali, us national park, us national parks, national parks, national park service, camping, hiking, backpacking, compare U.S. national parks" /><meta name="description" content="National Park of American Samoa National Park. See information on park hours, location, and activities offered by National Park of American Samoa. Compare National Park of American Samoa with other parks in National Park of American Samoa." />
<meta property="og:description" content="National Park of American Samoa National Park. See information on park hours, location, and activities offered by National Park of American Samoa. Compare National Park of American Samoa with other parks in National Park of American Samoa." />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="http://img1.findthebest.com/sites/all/themes/ftb1/favicon.ico" type="image/x-icon" />
<!--[if lt IE 9]><script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script><![endif]--><!--[if gte IE 9]><!--><script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script><![endif]--><!--[if lt IE 8]><script src="/sites/all/modules/custom/lib/json.ftb.min.js"></script><![endif]-->
	<script>
	setTimeout(function () {
		var node = document.getElementsByTagName('script')[0],
		gads = document.createElement('script'),
		useSSL = 'https:' === document.location.protocol;
		gads.async = true;
		gads.type = 'text/javascript';
		gads.src = (useSSL ? 'https:' : 'http:') + '//www.googletagservices.com/tag/js/gpt.js';
		node.parentNode.insertBefore(gads, node);
	}, 1);
	</script>
	<script>/*<![CDATA[*/_gaq=window._gaq||[];FTB={"configurations":null,"IS_EMPLOYEE":false,"IS_ODESKER":false,"IS_DEVELOPER":false,"IS_FTB_OWNED":1,"GOOGLE_LOGIN":null,"login_delay":10,"tld":"findthedata.org","gatekeeper":["Pageviews Pseudo Field","Widget Designer","find unused fields","Memory Tracking","Bulbasaur","Cache From Master","Comp Quality Msg","detail-fixed-ad","new-related-comparision","Related Views","CBG"],"IS_FTB":false,"IS_FTD":true,"IS_FTC":false,"IS_ENGLISH":true,"use_image_cdn":true,"cdn_domain":".findthebest.com","IS_WIDGET":false,"IS_LOCAL":false,"net_name":"FindTheData","app_id":721,"app_name":"US National Parks","singular_item":"National Park","app_singular":"National Park","app_plural":"National Parks","subdomain":"us-national-parks","clone_of":0,"intl_of":0,"swap_commas":0,"has_images":true,"lang":1,"t":{"dict":null},"rev_type":"review","js_ver":225,"partner_tweet":null,"app_img":"_584598_i0.jpg","page_type":"detail","sponsored_id":58,"sponsored":false,"cmap":{"m1":{"type":"m","coords":["ad:Superintendent  National Park of American Samoa  Pago Pago, AS  96799-0001"],"titles":["Superintendent  National Park of American Samoa  Pago Pago, AS<br\/> 96799-0001"],"zoom":null,"lid":"58"}},"fb_app_id":"117946838285450","fb_scope":"email,user_education_history,user_work_history,user_activities,user_interests,user_groups,user_hometown,user_location","ads":{"singleRequest":false,"page_url":"http:\/\/us-national-parks.findthedata.org\/l\/58\/National-Park-of-American-Samoa"},"ad_units":[{"unit_id":"ATF_728x90","div_id":"all-header","sizes":[728,90],"manual":false,"range":{"min":750,"max":null}},{"unit_id":"ATF_468x60","div_id":"all-header-mid","sizes":[468,60],"manual":false,"range":{"min":500,"max":750}},{"unit_id":"M_ATF_320x50","div_id":"all-header-mobile","sizes":[320,50],"manual":false,"range":{"min":null,"max":500}},{"unit_id":"ATF_300x250","div_id":"middle-square-1","sizes":[[300,250],[300,600]],"manual":false,"range":{"min":1040,"max":null}},{"unit_id":"BTF_728x90_SB","div_id":"middle-ad-large","sizes":[728,90],"manual":false,"range":{"min":765,"max":1040}},{"unit_id":"BTF_468x60_SB","div_id":"middle-ad-mid","sizes":[468,60],"manual":false,"range":{"min":500,"max":765}},{"unit_id":"M_TOP_300x250","div_id":"middle-ad-mobile","sizes":[300,250],"manual":false,"range":{"min":0,"max":500}},{"unit_id":"BTF_728x90","div_id":"all-footer","sizes":[728,90],"manual":false,"range":{"min":750,"max":null}},{"unit_id":"BTF_468x60","div_id":"all-footer-mid","sizes":[468,60],"manual":false,"range":{"min":500,"max":750}},{"unit_id":"M_MID_300x250","div_id":"all-footer-mobile","sizes":[300,250],"manual":false,"range":{"min":null,"max":500}}],"ad_targeting":[{"name":"sd","value":"us-national-parks"},{"name":"d","value":"findthedata.org"},{"name":"c","value":"Society"},{"name":"pt","value":"DD"},{"name":"lid","value":"58"},{"name":"o","value":"ftb"}],"lazy_items":{"d3":{"js":["sites\/all\/modules\/custom\/lib\/d3\/d3.custom.min.js"]},"gfx":{"deps":["d3"],"core":"gfx"},"edit":{"core":"edit"},"full_edit":{"core":"full_edit"},"sic_naics_edit":{"core":"sic_naics_edit"},"widget_designer":{"core":"widget_designer"},"jquery-svg":{"js":["sites\/all\/modules\/custom\/lib_ftb\/jquery.svg-util.js"]},"smart_rating":{"deps":["jquery-svg"],"js":["sites\/all\/modules\/custom\/viz\/SmartPie.js","sites\/all\/modules\/custom\/helpful_question\/helpful_polling.js"],"css":["sites\/all\/modules\/custom\/viz\/SmartPie.css"]},"gmaps":{"js":["\/\/maps.googleapis.com\/maps\/api\/js?libraries=places&sensor=false&region=US&key=AIzaSyAEzMisxyvRaMFBNqMq9a5EP_6c93ngTWc&callback=init_gmaps"],"def":"init_gmaps"},"ImgShare":{"js":["sites\/all\/modules\/custom\/widgets\/ImgShare.js"],"css":["sites\/all\/modules\/custom\/widgets\/ImgShare.js"],"stub":["ImgShare.show"]}},"user":{"uid":0}};go_soon_timeout=100;default_imgs={"mountain":{"file_name":"default_mountain.svg","width":100,"height":100},"person":{"file_name":"default_avatar_hi.png","width":100,"height":100}};dd_imgs=[{"src":"http:\/\/img3.findthebest.com\/sites\/default\/files\/721\/media\/images\/National_Park_of_American_Samoa_59598.JPG","thumbnail_url":"http:\/\/img3.findthebest.com\/sites\/default\/files\/721\/media\/images\/t2\/National_Park_of_American_Samoa_59598.JPG","w":"508","h":"480","caption":"The Many-coloured Fruit-dove may be found in the park."},{"src":"http:\/\/img1.findthebest.com\/sites\/default\/files\/721\/media\/images\/National_Park_of_American_Samoa_1_59599.jpg","thumbnail_url":"http:\/\/img1.findthebest.com\/sites\/default\/files\/721\/media\/images\/t2\/National_Park_of_American_Samoa_1_59599.jpg","w":"640","h":"480"},{"src":"http:\/\/img2.findthebest.com\/sites\/default\/files\/721\/media\/images\/National_Park_of_American_Samoa_2_59600.jpg","thumbnail_url":"http:\/\/img2.findthebest.com\/sites\/default\/files\/721\/media\/images\/t2\/National_Park_of_American_Samoa_2_59600.jpg","w":"415","h":"286"}];detail={"id":58,"title":"National Park of American Samoa","sections":[{"title":"Overview","id":0},{"title":"Activities","id":2},{"title":"Hours and Fees","id":3},{"title":"Contact","id":4}]};related_imgs=[{"src":"http:\/\/img3.findthebest.com\/sites\/default\/files\/721\/media\/images\/Carlsbad_Caverns_National_Park_59557.jpg","thumbnail_url":"http:\/\/img3.findthebest.com\/sites\/default\/files\/721\/media\/images\/t2\/Carlsbad_Caverns_National_Park_59557.jpg","caption":"Carlsbad Caverns","attr":null,"w":"640","h":"437","link":"<a class = \"srch\" href=\"http:\/\/us-national-parks.findthedata.org\/compare\/49-58\/Carlsbad-Caverns-National-Park-vs-National-Park-of-American-Samoa\">Carlsbad Caverns National Park vs National Park of American Samoa<\/a>"},{"src":"http:\/\/img1.findthebest.com\/sites\/default\/files\/721\/media\/images\/Hot_Springs_National_Park_59336.JPG","thumbnail_url":"http:\/\/img1.findthebest.com\/sites\/default\/files\/721\/media\/images\/t2\/Hot_Springs_National_Park_59336.JPG","caption":"Remaining natural hot springs","attr":null,"w":"640","h":"480","link":"<a class = \"srch\" href=\"http:\/\/us-national-parks.findthedata.org\/compare\/28-58\/Hot-Springs-National-Park-vs-National-Park-of-American-Samoa\">Hot Springs National Park vs National Park of American Samoa<\/a>"}];location_range="200";rev_form={"REVIEW_MIN_LENGTH_WORDS":15,"user_name":null,"val":0,"item_id":58,"item_url":["http:\/\/us-national-parks.findthedata.org\/l\/58\/National-Park-of-American-Samoa","National Park of American Samoa"],"type":"review","is_standard":true,"is_inline":true};helpful_html="<div id=\"helpful-page-wrapper\"><div class=\"grid-wrap\"><div class=\"helpful-message\">Was this page helpful?<\/div><div class=\"helpful-choices-container\"><div data-choice=\"Yes\" class=\"helpful-btn helpful-yes thm-btn\">Yes<\/div><div data-choice=\"Somewhat\" class=\"helpful-btn helpful-somewhat thm-btn\">Somewhat<\/div><div data-choice=\"No\" class=\"helpful-btn helpful-no thm-btn\">No<\/div><\/div><\/div><\/div>";/*]]>*/</script><script>window.google_analytics_uacct = "UA-9929225-7";</script>
<style></style>		<script id='check-cbg'>(function (document) {
	var publishers = FTB.CBG ? FTB.CBG.publishers : '',
		hash = window.location.hash,
		pid_vals = hash ? hash.match(/pid=([^&]*)/) : '',
		pid_param = pid_vals ? pid_vals[1] : '',
		pid = '',
		valid_pid = false,
		cbg_cookie,
		valid_cookie;

	if (pid_param) {
		pid = checkValidCBG(pid_param, publishers);
		valid_pid = !!pid;
	}
	cbg_cookie = getCbgCookie();
	valid_cookie = !!publishers[cbg_cookie];

	if (valid_pid || valid_cookie) {
		var curr_pid = pid || cbg_cookie;
		FTB.CBG.current = publishers ? publishers[curr_pid] : '';
	}

	function getCbgCookie() {
		var cbg_cookie = document.cookie.match('(?:^|;) ?_ftb_cbg=([^;]*)(?:;|$)');
		if (!cbg_cookie) {
			return '';
		} else {
			return cbg_cookie[1];
		}
	}

	function checkValidCBG(pid_param, publishers) {
		if (publishers[pid_param]) {
			return pid_param;
		}
		else {
			for (var pub_id in publishers) {
				if (publishers.hasOwnProperty(pub_id)) {
					var temp_pub = publishers[pub_id];
					if (temp_pub.alias === pid_param) {
						return pub_id;
					}
				}
			}
		}
		return '';
	}

}(document));</script>		<script data-analytics='{"ga_code":"UA-9929225-7","ga_code_2":null,"comp_ga_id":"","domain_name":".findthedata.org","is_widget":false}' id='analytics-code'>(function (document) {

	var ga, curr_domain,
		data = $('#analytics-code').data('analytics'),
		ga_code = data.ga_code,
		ga_code_2 = data.ga_code_2,
		comp_ga_id = data.comp_ga_id,
		domain_name = data.domain_name,
		is_widget = data.is_widget,
		curr_publisher = FTB.CBG ? FTB.CBG.current : [],
		ga_id = curr_publisher ? curr_publisher.ga_id : ''
		;

	if (!ga_id) {
		_gaq.push(['_setAccount', ga_code]);
		_gaq.push(['_setDomainName', domain_name]);
		_gaq.push(['_setSiteSpeedSampleRate', 10]); // Track sitespeed on 10% of pageviews
		_gaq.push(['_trackPageview']);
	} else {
		curr_domain = window.location.hostname;
		_gaq.push(['_setAccount', ga_id]);
		_gaq.push(['_setDomainName', curr_domain]);
		_gaq.push(['_trackPageview']);
	}

	// Add tracking for publisher's account
	if (ga_code_2 && !is_widget) {
		_gaq.push(['b._setAccount', ga_code_2]);
		_gaq.push(['b._setDomainName', domain_name]);
		_gaq.push(['b._trackPageview']);
	}

	// Add tracking for comp specific account
	if (comp_ga_id) {
		_gaq.push(['c._setAccount', comp_ga_id]);
		_gaq.push(['c._setDomainName', domain_name]);
		_gaq.push(['c._trackPageview']);
	}

	ga = document.createElement('script');
	ga.type = 'text/javascript';
	ga.async = true;
	ga.src = ('https:' === document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
	var s = document.getElementsByTagName('script')[0];
	s.parentNode.insertBefore(ga, s);

}(document));</script>			</head>

	<body class="not-front not-logged-in no-sidebars page-l-58-national-park-of-american-samoa section-l ftb-owned detail ftd">
				<div id="loading"></div>
		<div id="loading-msg">Loading</div>
				<div id="page">
			<div id="page-inner">

									<div id='pub-header-wrap'></div>
					<div id="p-header" class="clearfix">
						<div class="grid-wrap">
														<a id="p-logo" href="http://www.findthedata.org" title="Compare public datasets at FindTheData.org"></a>

							<div id="p-user-menu">
								<div id="p-join" class="thm-hover"><span id="p-join-icon" class="color-sprite"></span><span class="text link">Join</span></div>
								<div id="p-sign-in" class="thm-hover"><span id="p-sign-in-icon" class="color-sprite"></span><span class="text">Sign in</span></div>
								<div class='my-account-menu'><span class='login_join' onclick='FTB.show_registration();'>Join</span><span class='site-login-link login_link popup_login_dlg'>Sign In</span></div>							</div>

							<div id="mob-tog-wrap" class='nosel'>
								<div id="mob-search-tog"><span id="search-tog-icon" class="color-sprite"></span><span class="remove">&times;</span></div>
								<div id="mob-menu-tog">
										<span class="line thm-bg"></span>
										<span class="line thm-bg"></span>
										<span class="line thm-bg"></span>
										<span class="remove thm-color">&times;</span>
								</div>
							</div>
							<div id="p-searchbar">
								<input id="search_input">
								<div id="p-sb-button" class="ss_but stnd-btn thm-btn">
									<div class="mag-glass-icon color-sprite"></div>
								</div>
								<div id="searchbar-dropdown" class="thm-bt thm-arrow-up s-results-list"></div>
							</div>
							<div id="p-menu" class="nosel">
								<span class="text thm-hover">Browse<span class="arrow thm-on-bt"></span></span>
							</div>
							<div id='p-cat-drop' data-init='false'></div>
						</div>
					</div>
					
					<div id='header-ad'>
						<div class='ad' id='all-header-massive'></div>
						<div class='ad' id='all-header'></div>
						<div class='ad' id='all-header-mid'></div>
						<div style='display: none;' id='mobile-ad-x'>
							<div class='ad-x-wrap'>
								<span class='ad-x'>close ad</span>
							</div>
						</div>
						<div class='ad' id='all-header-mobile'></div>
					</div><script>
					(function () {
						var width = window.innerWidth || $(window).width, i, on;
						for (i = 0; i < FTB.ad_units.length; i = i + 1) {
							on = FTB.ad_units[i];
							if (on.div_id.indexOf('all-header') === 0) {
								if (width > (on.range.min || 0) && width <= (on.range.max  || Number.MAX_VALUE)) {
									$('#' + on.div_id).addClass('active');
									return;
								}
							}
						}
					}());
				</script>				
				<div class="grid-wrap">
																							<div id="bread-crumb">
								<span class="bread-wrap" ><a class="bread" href="http://www.findthedata.org">Home</a></span><span class="bread-sep">&raquo;</span><span class="bread-wrap" ><a class="bread" href="http://www.findthedata.org/category/Society">Society</a></span><span class="bread-sep">&raquo;</span><span class="bread-wrap" ><a class="bread" href="http://us-national-parks.findthedata.org">US National Parks</a></span><span class="bread-sep">&raquo;</span><span class="bread-wrap" >Detail</span>															</div>
															</div>

				<div id="main">
					<div id="main-inner" class="clearfix">
						<div id='pub-left-wrap'></div>
						<div id='pub-right-wrap'></div>
						<div class="grid-wrap clearfix">
														<div id="share_buttons" class="clearfix">
			<div id="embed_butt" style="width:77px" class="open ico detail">
				<span class="embw">&nbsp;&nbsp;&nbsp;&nbsp;</span>
				<label id="embed_butt_label">Embed</label>
				<div class="tip">Embed a widget version of this page</div>
			</div><div class='shr-wrap'><div class='shr shr-facebook'><div class='shr-icon'></div></div><div class='shr shr-twitter'><div class='shr-icon'></div></div><div class='shr shr-googleplus'><div class='shr-icon'></div></div><div class='shr shr-email'><div class='shr-icon'></div></div></div></div>																												</div>
												
						<div id="content">
							<div id="content-inner">
								<div id="content-inner-wrapper" class="grid-wrap">

																											<div id="content-area"><div id='detail-float'>
	<div class='grid-wrap'>
		<div class='float-inner clearfix'>
			<div class='float-item'>
				<div id='main-img-thumb'><img src='http://img3.findthebest.com/sites/default/files/721/media/images/National_Park_of_American_Samoa_59598.JPG'></div>				<div class='name'>National Park of American Samoa</div>
			</div>
			<div class='section-summary'>
				<div data-section-id='0' class='section-nav first active id-0'><span class='title-text'>Overview</span><div class='current'></div></div><div data-section-id='2' class='section-nav id-2'><span class='title-text'>Activities</span><div class='current'></div></div><div data-section-id='3' class='section-nav id-3'><span class='title-text'>Hours and Fees</span><div class='current'></div></div><div data-section-id='4' class='section-nav id-4'><span class='title-text'>Contact</span><div class='current'></div></div>			</div>
		</div>
	</div>
</div>
<div id='detail-wrap' class='hreview'>
		<a id='detail-top-nav' href='/'>
		<span class='lsaquo'>&lsaquo;</span>&nbsp;See all National Parks	</a>
		<div id='detail-full-edit'>
		Last edited Nov 14th 2013 by FindTheData	</div>
		<div id='detail-page' class='clearfix'>
		<div id='detail-main'>
			
				<div id='editable-detail-header'>
					<div id='detail-header' class='clearfix horizontal-image item'>
						<div id='detail-info'>
							<div class='detail-info-title'>
								<h1 class='fn'>National Park of American Samoa, American Samoa</h1>
								
							</div>
							
							<div id='detail-actions'>
			<span class='link detail-action add-to'><span id='save-icon'>&nbsp;</span>Add to List</span><span id='write-a-review' class='detail-action link add-review-button'><span id='review-icon'>&nbsp;</span>Write a Review</span><span id='edit-listing' class='detail-action link'><span id='edit-icon'>&nbsp;</span>Edit</span>
		</div>
						</div>
						<div id='detail-image' style='max-width: 100%' class='clearfix'><div id='img-large-wrap' style='max-height: 280px; max-width: 100%;'>
				<div id='img-large'>
				<div class='img-wrap' style='max-height: 280px; max-width: 100%'>
				<div class='img-attr-wrap'>
				<img alt='The Many-coloured Fruit-dove may be found in the park.' class='detail-image dd-img photo' style='max-width: 100%; max-height: 280px;' src='http://img3.findthebest.com/sites/default/files/721/media/images/t2/National_Park_of_American_Samoa_59598.JPG'/>
				<div class='img-attr t02'><div class='img-attr-alt'>The Many-coloured Fruit-dove may be found in the park.</div><div class='img-attr-attr'></div></div>
				</div>
				</div>
				</div>
				</div><div id='img-thumbs-wrap'><div id='img-thumbs'><div data-attr='' data-alt='The Many-coloured Fruit-dove may be found in the park.' class='dd-thumb selected'><div class='thumb-wrap'><div class='thumb-wrap-inner'><img alt='The Many-coloured Fruit-dove may be found in the park.' src='http://img3.findthebest.com/sites/default/files/721/media/images/t2/National_Park_of_American_Samoa_59598.JPG'/></div></div></div><div data-attr='' data-alt='' class='dd-thumb'><div class='thumb-wrap'><div class='thumb-wrap-inner'><img alt='National Park of American Samoa' src='http://img1.findthebest.com/sites/default/files/721/media/images/t2/National_Park_of_American_Samoa_1_59599.jpg'/></div></div></div><div data-attr='' data-alt='' class='dd-thumb'><div class='thumb-wrap'><div class='thumb-wrap-inner'><img alt='National Park of American Samoa' src='http://img2.findthebest.com/sites/default/files/721/media/images/t2/National_Park_of_American_Samoa_2_59600.jpg'/></div></div></div></div></div></div>
						<div id='detail-user-ftb-rating' class='clearfix'>
				
				
				<div id='detail-your-rating'>
					<span class='rating-name'>Be the first to review</span>
					<div class='add-stars-container'>
					<div class='rateable'>
					
			
			<div class='rating-container stars clearfix med'>
				
				<div class='rating-bar ' style='width: 0%'></div>
				<div class='rating-bar-back js-stared'></div>
				<span data-star='1' class='star'> <span class='star-icon'></span><span class='tl'></span><span class='tr'></span><span class='bl'></span><span class='br'></span></span><span data-star='1' class='spacer'></span><span data-star='2' class='star'> <span class='star-icon'></span><span class='tl'></span><span class='tr'></span><span class='bl'></span><span class='br'></span></span><span data-star='2' class='spacer'></span><span data-star='3' class='star'> <span class='star-icon'></span><span class='tl'></span><span class='tr'></span><span class='bl'></span><span class='br'></span></span><span data-star='3' class='spacer'></span><span data-star='4' class='star'> <span class='star-icon'></span><span class='tl'></span><span class='tr'></span><span class='bl'></span><span class='br'></span></span><span data-star='4' class='spacer'></span><span data-star='5' class='star'> <span class='star-icon'></span><span class='tl'></span><span class='tr'></span><span class='bl'></span><span class='br'></span></span>
			</div>
					</div>
					<div class='add-stars-text'>click stars to begin review</div>
					</div>
					</div>
			</div>
					</div>
				</div>			<div id='detail-section-wrapper'><div id='detail-section-nav' style='width: 100%;'><div data-section-id='0' class='section-nav first active id-0'><span class='title-text'>Overview</span><div class='current'></div></div><div data-section-id='2' class='section-nav id-2'><span class='title-text'>Activities</span><div class='current'></div></div><div data-section-id='3' class='section-nav id-3'><span class='title-text'>Hours and Fees</span><div class='current'></div></div><div data-section-id='4' class='section-nav id-4'><span class='title-text'>Contact</span><div class='current'></div></div></div></div><div id='s-mobile'><div class='fs-wrap'>
			<div class='fs-window'>
				<div class='fs-val'>Navigate To...</div>
				<div class='fs-arrow'></div>
			</div>
			<div class='fs-opts'>
				<div class='fs-opt top-link'>Top</div>
				<div class='fs-opt section-nav' data-section-id='0'>Overview</div><div class='fs-opt section-nav' data-section-id='2'>Activities</div><div class='fs-opt section-nav' data-section-id='3'>Hours and Fees</div><div class='fs-opt section-nav' data-section-id='4'>Contact</div>
			</div>
			<div class='fs-mask'></div>
		</div></div>			<div id='detail-sections'><div data-section-id='0' class='id-0 detail-section   open'><h2 class='section-title'><span class='title-text'>About National Park of American Samoa</span><div class='section-edit'><span class='edit-off'><span class='icon'></span><span class='thm-link words'>Edit</span></span></div></h2><div class='section-body'><div class='detail-col full-split-row'>
				<div class='data-block is-editable' data-id='9'>
				<div class='full-split-wrapper clearfix'><div class='full-split-top'>
					<table class='data-block-body'><tbody><tr class='component one-column first overview odd'>
			<td colspan='2' class='fullrow fdata'><div class='dd-overview-visuals'><div style='width:33.3333333333%' class='dd-overview-box field-popup' data-field='visitors' data-val='3'><div class='dd-overview-label-wrap'><div class='dd-overview-label'><div class='tip'>Number of visitors that visited the park in the given year.</div>Visitors (2012)</div></div><span id='vz1'></span></div><div style='width:33.3333333333%' class='dd-overview-box field-popup' data-field='area_acres' data-val='9000'><div class='dd-overview-label-wrap'><div class='dd-overview-label'><div class='tip'>If vast, untouched and astonishing views are your thing, definitely look for the parks with immense size.  These parks will most likely have hidden gems that no other person has yet to see.  And maybe, if you&#039;re lucky, you&#039;ll see that wild grizzly, soaring eagle, or beautiful rainbow after a rain storm.</div>Area</div></div><span id='vz2'></span></div><div style='width:33.3333333333%' class='dd-overview-box field-popup' data-field='price_vehicle' data-val='0'><div class='dd-overview-label-wrap'><div class='dd-overview-label'><div class='tip'>You might consider (safely and legally) cramming as many people into a vehicle as possible because some parks charge per vehicle (as opposed to per person).</div>Entrance Fee</div></div><span id='vz3'></span></div></div></td>
		</tr></tbody></table>
				</div>
					<div class='full-split-left'>
						<table class='data-block-body'><tbody><tr class='component two-column first fieldmledit even'>
			<td class='fname'> Climate</td>
			<td class='fdata'>Samoa is warm, humid and rainy year-round with a long, wet summer (October - May) and a slightly cooler and drier season (June - September). A tropical climate prevails. Temperatures are warm year-round (high 70's to low 90's F) with high humidity. Rain showers are frequent and may last only for a few minutes, or last all day. Average annual rainfall is 125 inches at the airport and 200 inches elsewhere.</td>
		</tr><tr class='component two-column fieldcombo odd'>
			<td class='fname'> State</td>
			<td class='fdata'>American Samoa <br /><a class="dir" href="/d/a/American-Samoa">Compare  American Samoa National Parks</a></td>
		</tr><tr data-field='year_established' data-val='1988' class='component two-column fieldeditnumber even'>
			<td class='fname'> Year Established</td>
			<td class='fdata'>1988</td>
		</tr><tr class='component two-column fieldedit odd'>
			<td class='fname'> Governing Body</td>
			<td class='fdata'><a href="http://www.nps.gov/index.htm">National Park Service</a></td>
		</tr></tbody></table>
					</div>
					<div class='full-split-right'>
						<table class='data-block-body'><tbody><tr class='component one-column center first map even'>
			<td colspan='2' class='fullrow fdata'><div><div class='cmap js-render' data-cmap-id='m1' style='width:100%;height:300px'></div><div style='margin-top:4px;'><a href='http://us-national-parks.findthedata.org/#map' rel='nofollow'>View a map of all US National Parks</a></div></div></td>
		</tr></tbody></table>
					</div></div></div></div> </div></div>
				<div id='dd-ad-mid'>
					<div class='ad' id='middle-ad-large'></div>
					<div class='ad' id='middle-ad-mid'></div>
					<div class='ad' id='middle-ad-mobile'></div>
				</div><div data-section-id='2' class='id-2 detail-section   '><h2 class='section-title'><span class='title-text'>What to Do in National Park of American Samoa</span><div class='section-edit'><span class='edit-off'><span class='icon'></span><span class='thm-link words'>Edit</span></span></div></h2><div class='section-body'><div class='detail-col full-split-row'>
				<div class='data-block is-editable' data-id='28'>
				<div class='full-split-wrapper clearfix'>
					<div class='full-split-left'>
						<table class='data-block-body'><tbody><tr class='component two-column first fieldlist even'>
			<td class='fname'> <div class='has-help-text'>Activities
					<div class='info-icon'><div class='tip'>Knowing which activities you can do while at the park is important to know if you have members of your party that have different interests.  While Aunt Sue might only want to go on day hikes, little Bobby might want to go on overnight hiking trips.  Just make sure everybody has something to do and you'll have a great time!</div></div></div></td>
			<td class='fdata'><div class="list_scroll"><table class="list_table" id="rep_activities"><tr class="odd"><td>General Tours</td></tr><tr class="even"><td>Hiking</td></tr><tr class="odd"><td>Scuba Diving</td></tr><tr class="even"><td>Snorkeling</td></tr><tr class="odd"><td>Trails</td></tr></table></div></td>
		</tr><tr class='component two-column fieldmledit odd'>
			<td class='fname'> Popular Features</td>
		</tr></tbody></table>
					</div>
					<div class='full-split-right'>
						<table class='data-block-body'><tbody><tr class='component one-column first center imagenew even'>
			<td colspan='2' class='fullrow fdata'><div class='img-wrap'><img style='max-width:300px;max-height:300px;' class='dd-inline-img dd-img' alt='National Park of American Samoa' src='http://img1.findthebest.com/sites/default/files/721/media/images/National_Park_of_American_Samoa_1_59599.jpg'/></div></td>
		</tr></tbody></table>
					</div></div></div></div> </div></div><div data-section-id='3' class='id-3 detail-section   '><h2 class='section-title'><span class='title-text'>Getting to National Park of American Samoa</span><div class='section-edit'><span class='edit-off'><span class='icon'></span><span class='thm-link words'>Edit</span></span></div></h2><div class='section-body'><div class='split-2 detail-col split-row clearfix'><div class='detail-split-left'><div class='data-block is-editable' data-id='37'><h3 class='data-block-header'>Hours</h3><table class='data-block-body'><tbody><tr class='component two-column first fieldmledit odd'>
			<td class='fname'> Hours of Operation</td>
			<td class='fdata'>The park is open year-round.<br/><br/>The temporary Visitor Center in Ottoville is open weekdays 8:00 am to 4:30 pm.  Closed weekends and federal holidays.</td>
		</tr><tr class='component two-column fieldediturl even'>
			<td class='fname'> Hours URL</td>
			<td class='fdata'><a href='http://www.nps.gov/npsa/planyourvisit/hours.htm'  class='outbound_lnk' target='_blank'>Hours URL</a> <small>(nps.gov)</small></td>
		</tr><tr class='component two-column fieldediturl odd'>
			<td class='fname'> Directions URL</td>
			<td class='fdata'><a href='http://www.nps.gov/npsa/planyourvisit/hours.htm'  class='outbound_lnk' target='_blank'>Directions URL</a> <small>(nps.gov)</small></td>
		</tr></tbody></table></div></div><div class='detail-split-right'><div class='data-block is-editable' data-id='42'><h3 class='data-block-header'>Fees</h3><table class='data-block-body'><tbody><tr data-field='price_vehicle' data-val='0' class='component two-column first fieldeditnumber even'>
			<td class='fname'> <div class='has-help-text'>Entrance Fee
					<div class='info-icon'><div class='tip'>You might consider (safely and legally) cramming as many people into a vehicle as possible because some parks charge per vehicle (as opposed to per person).</div></div></div></td>
			<td class='fdata'>$0 Per Private Vehicle</td>
		</tr><tr data-field='price_person' data-val='0' class='component two-column fieldeditnumber odd'>
			<td class='fname'> <div class='has-help-text'>Entrance Fee
					<div class='info-icon'><div class='tip'>Some parks charge an entrance fee per person and others by the vehicle.</div></div></div></td>
			<td class='fdata'>$0 Per Person </td>
		</tr><tr class='component two-column fieldediturl even'>
			<td class='fname'> Fees URL</td>
			<td class='fdata'><a href='http://www.nps.gov/npsa/planyourvisit/feesandreservations.htm'  class='outbound_lnk' target='_blank'>Fees URL</a> <small>(nps.gov)</small></td>
		</tr></tbody></table></div></div></div> </div></div><div data-section-id='4' class='id-4 detail-section   '><h2 class='section-title'><span class='title-text'>Contact Information</span><div class='section-edit'><span class='edit-off'><span class='icon'></span><span class='thm-link words'>Edit</span></span></div></h2><div class='section-body'><div class='detail-col full-split-row'>
				<div class='data-block is-editable' data-id='47'>
				<div class='full-split-wrapper clearfix'>
					<div class='full-split-left'>
						<table class='data-block-body'><tbody><tr class='component two-column first fieldediturlmain odd'>
			<td class='fname'> Official Website</td>
			<td class='fdata'><a href='http://www.nps.gov/npsa/'  class='outbound_lnk' target='_blank'>National Park of American Samoa</a> <small>(nps.gov)</small></td>
		</tr><tr class='component two-column fieldediturl even'>
			<td class='fname'> Email Page</td>
			<td class='fdata'><a href='http://www.nps.gov/PWR/sendmail.htm?o=19%3B7HFJ%2BZ%409J%5BFSV%3FREFLHE%20%20%0A&amp;amp;amp;amp;r=/npsa/index.htm'  class='outbound_lnk' target='_blank'>Email Page</a> <small>(nps.gov)</small></td>
		</tr><tr class='component two-column fieldeditphone odd'>
			<td class='fname'> Phone</td>
			<td class='fdata'><span class='phone_number'>(684) 633-7082</span></td>
		</tr><tr class='component two-column fieldeditphone even'>
			<td class='fname'> Fax</td>
			<td class='fdata'><span class='phone_number'>(684) 633-7085</span></td>
		</tr></tbody></table>
					</div>
					<div class='full-split-right'>
						<table class='data-block-body'><tbody><tr class='component one-column first center imagenew odd'>
			<td colspan='2' class='fullrow fdata'><div class='img-wrap'><img style='max-width:300px;max-height:300px;' class='dd-inline-img dd-img' alt='National Park of American Samoa' src='http://img2.findthebest.com/sites/default/files/721/media/images/National_Park_of_American_Samoa_2_59600.jpg'/></div></td>
		</tr></tbody></table>
					</div></div></div></div> </div></div><div id='rf-review-wrap'>
	<div id='rf-head' class='clearfix'>
				<div id='rf-listing-img'><img src='http://img3.findthebest.com/sites/default/files/721/media/images/t/National_Park_of_American_Samoa_59598.JPG'/></div>
				<div id='rf-title'>Review National Park of American Samoa</div>
	</div>

	<div id='rf-message'>
		Please add a rating and a written review.You will need to be logged in to submit.	</div>

	<div class='rf-wrap rf-error-sec clearfix'></div>

		<div class='rf-wrap rf-rating-sec clearfix'>
		<div class='rf-subtitle rf-left'>
			<span class='rf-st-icon'></span>
			Rate this National Park		</div>

		<div id='rf-o-rating' class='rf-right'>
			<div class='rf-missed-wrap rf-missed-rating'><span class='rf-missed-icon color-sprite'></span></div>
			<div id='rf-o-stars' class='ur-star-container active'>
			
			<div class='rating-container stars clearfix large'>
				
				<div class='rating-bar ' style='width: 0%'></div>
				<div class='rating-bar-back js-stared'></div>
				<span data-star='1' class='star'> <span class='star-icon'></span><span class='tl'></span><span class='tr'></span><span class='bl'></span><span class='br'></span></span><span data-star='1' class='spacer'></span><span data-star='2' class='star'> <span class='star-icon'></span><span class='tl'></span><span class='tr'></span><span class='bl'></span><span class='br'></span></span><span data-star='2' class='spacer'></span><span data-star='3' class='star'> <span class='star-icon'></span><span class='tl'></span><span class='tr'></span><span class='bl'></span><span class='br'></span></span><span data-star='3' class='spacer'></span><span data-star='4' class='star'> <span class='star-icon'></span><span class='tl'></span><span class='tr'></span><span class='bl'></span><span class='br'></span></span><span data-star='4' class='spacer'></span><span data-star='5' class='star'> <span class='star-icon'></span><span class='tl'></span><span class='tr'></span><span class='bl'></span><span class='br'></span></span>
			</div></div>
						<span id='rf-click-text'>click stars to rate</span>
					</div>
	</div>
	
	<div class='rf-wrap rf-review-sec clearfix'>
		<div class='rf-subtitle rf-left'><span class='rf-st-icon'></span>Write your review</div>

		<div id='rf-review-box' class='rf-right'>

						<div class='rf-missed-wrap rf-missed-title'>
				<span class='rf-missed-icon color-sprite'></span>
			</div>
			<input id='rf-review-title' maxlength='100' class='rf-input' placeholder='Add a title'/>
						<div class='rf-missed-wrap rf-missed-review'>
				<span class='rf-missed-icon color-sprite'></span>
			</div>
			<textarea id='rf-review-body' maxlength='20000'class='rf-input' placeholder='Add a review'></textarea>

				  		<div id='rf-help-review'>
				<span class='rf-help-title'>A good review is:</span>Both detailed and specific
				<span class='rf-help-title' style='margin-top: 10px;'>Consider writing about:</span><ul><li>Pros and cons</li><li>Some things people might not know about the listing</li></ul>
			</div>
			
			<div id='rf-word-count'>15words to go</div>
		</div>
	</div>

	
	<div id='rf-input-wrap' class='rf-wrap clearfix'>
		<div class='rf-left'>&nbsp;</div>
		<div id='rf-submit' class='rf-right'>
			<div class='rf-user-post'>Your display name is set to <b class='rf-name'> </b> <span class='link'>[Edit]</span></div>
			<div class='rf-display-name clearfix'>
				<div class='rf-dn-error'></div>
				<input class='rf-dn-input rf-input' maxlength='60' value=''/>
				<div class='rf-dn-save bg-blue stnd-btn'>
					<span class='spin'></span>
					<span class='save'>Save</span>
					<span class='saving'>Saving</span>
				</div>
				<div class='rf-dn-help'>Your display name will be displayed on your profile page and next to your reviews.</div>
			</div>
			<div id='rf-post-review' class='stnd-btn bg-blue'>Post Review</div>
		</div>
	</div>
</div>
</div>
		</div>
		<div id='detail-sidebar'><div class='data-block not-editable' data-id=''><table class='data-block-body'><tbody><tr class='component one-column first center active ad even'>
			<td colspan='2' class='fullrow fdata'><div id='middle-square-1' class='ad-unit'></div><span class='ad-text'>Advertisement</span></td>
		</tr></tbody></table></div><div class='data-block not-editable' data-id='6'><table class='data-block-body'><tbody><tr class='component one-column first related odd'>
			<td colspan='2' class='fullrow fdata'><div id='related' class='related-block'><div><h4 class='data-block-header'>Compare Related National Parks</h4></div><ol><li><a class = "srch" href="http://us-national-parks.findthedata.org/compare/49-58/Carlsbad-Caverns-National-Park-vs-National-Park-of-American-Samoa">Carlsbad Caverns National Park vs National Park of American Samoa</a></li><li><a class = "srch" href="http://us-national-parks.findthedata.org/compare/28-58/Hot-Springs-National-Park-vs-National-Park-of-American-Samoa">Hot Springs National Park vs National Park of American Samoa</a></li></ol></div><div id='related-comps' class='related-block'><h4 class='data-block-header'>Related Topics</h4><ul><li><a class='related' title='Find and compare the best campgrounds for tent and RV camping based on location, activities, amenities and more.' href='http://campgrounds.findthebest.com'>Campgrounds</a></li><li><a class='related' title='Find and compare the best guest ranches and dude ranches based on location, nightly rates, activities, horseback riding options, lodging, amenities, specialty events and more.' href='http://dude-ranches.findthebest.com'>Dude and Guest Ranches</a></li><li><a class='related' title='Compare tents and bivy sacks. Our tents comparison helps you find the best tents by manufacturer, weight, size, price, seasons used, user reviews, and more.' href='http://tents.findthebest.com'>Tents</a></li><li><a class='related' title='Compare backpacking and travel backpacks. See brands like North Face side by side and compare by manufacturer, weight, capacity, size, features, reviews, and more.' href='http://backpacks.findthebest.com'>Backpacking & Travel Backpacks</a></li></ul></div></td>
		</tr></tbody></table></div><div id='sidebar-bottom'></div></div>
	</div>
	<div id='detail-below'>
		<div id="listing_answers">
										<table class = "questions_block">
											<tr>
											 <td class="faq_detail"><h2 class="faq-title-text section-title">FAQ for National Park of American Samoa</h2><ul><li><span class="rsaquo">&rsaquo;</span><a href="http://us-national-parks.findthedata.org/q/58/2571/How-big-is-the-US-National-Park-National-Park-of-American-Samoa-in-American-Samoa" class="questions">How big is the US National Park National Park of American Samoa in American Samoa?</a></li><li><span class="rsaquo">&rsaquo;</span><a href="http://us-national-parks.findthedata.org/q/58/2572/When-was-the-US-National-Park-National-Park-of-American-Samoa-in-American-Samoa-established" class="questions">When was the US National Park National Park of American Samoa in American Samoa established?</a></li><li><span class="rsaquo">&rsaquo;</span><a href="http://us-national-parks.findthedata.org/q/58/2573/What-activities-can-you-do-at-the-US-National-Park-National-Park-of-American-Samoa-in-American-Samoa" class="questions">What activities can you do at the US National Park National Park of American Samoa in American Samoa?</a></li><li><span class="rsaquo">&rsaquo;</span><a href="http://us-national-parks.findthedata.org/q/58/2574/How-many-visitors-did-the-US-National-Park-National-Park-of-American-Samoa-in-American-Samoa-get" class="questions">How many visitors did the US National Park National Park of American Samoa in American Samoa get?</a></li><li><span class="rsaquo">&rsaquo;</span><a href="http://us-national-parks.findthedata.org/q/58/2575/What-is-the-weather-like-at-the-US-National-Park-National-Park-of-American-Samoa-in-American-Samoa" class="questions">What is the weather like at the US National Park National Park of American Samoa in American Samoa?</a></li></ul></div></td>
											</tr>
										</table>
									</div>					</div>
</div>

</div>
									
					<div id='footer-ad'>
						<div class='ad' id='all-footer'></div>
						<div class='ad' id='all-footer-mid'></div>
						<div class='ad' id='all-footer-mobile'></div>
					</div>									
									
									
																			<div class="app_footer">
																						<div class='app_footer_text'>US National Park Service</div>										</div>
									
									
								</div>
							</div>
						</div>

																		
					</div>
				</div>

									<div id='pub-footer-wrap'></div>

			</div>
		</div>

					<div id="closure-blocks" class="region region-closure"><div id="block-main-0" class="block block-main region-odd odd region-count-1 count-1"><div class="block-inner">

  
  <div class="content">
    <a rel="nofollow" style="display: none;" href="/blkhol/email">BlkHol Email</a><div class="popup_login_box round3 popup_frame" style="display:none">
	<div class="popup_login_dlg_body clearfix">
		<div class="login-loading t02"></div>
		<div id="login-title">Welcome to FindTheData<h6>a <a href="http://www.findthebest.com/" target="_blank" rel="nofollow"><strong>FindThe<span>Best</span></strong></a> powered site</h6></div>
		<div id="login-message" style="display:none;">Hi! We see you would like to submit a rating. Please login or create an account to do so. Thank you!</div>
		<div id="return-login">
			<div id="reveal-login" class="round3">
				<div id="ftb-sign-in-lnk">Sign in through the <strong>FindTheBest</strong> network</div>
				<div id="reveal-login-form">
					<form action="/l/58/National-Park-of-American-Samoa"  accept-charset="UTF-8" method="post" id="user-login-small-form" class="ajax-form ajax-form">
<div><div class="form-item" id="edit-name-wrapper">
 <input type="text" maxlength="128" name="name" id="edit-name" size="30" value="" placeholder="Email" autocapitalize="off" autocorrect="off" class="form-text required" />
</div>
<div class="form-item" id="edit-pass-wrapper">
 <input type="password" name="pass" id="edit-pass"  maxlength="128"  size="30"  placeholder="Password" class="form-text required" />
</div>
<a href="/user/password" class="thm-link forgot-password" rel="NOFOLLOW">Forgot your Email / Password?</a><input type="submit" name="op" id="edit-submit" value="Login"  class="form-submit ajax-trigger stnd-btn bg-blue" />
<input type="hidden" name="dest" id="edit-dest" value=""  />
<input type="hidden" name="form_build_id" id="form-4ce1f3034386c43ea9a2e4b20a36dc3d" value="form-4ce1f3034386c43ea9a2e4b20a36dc3d"  />
<input type="hidden" name="form_id" id="edit-user-login-small-form" value="user_login_small_form"  />

</div></form>
				</div>
			</div>
			<div class="login-or">or</div>
			<div class="social-logins">
				<div class="google-login-btn stnd-btn bg-bright-red" onclick="FTB.perform_login('google', 'https://accounts.google.com/o/oauth2/auth?response_type=code&redirect_uri=http%3A%2F%2Fwww.findthebest.com%2Fgoogle-login%2Foauth2callback&client_id=118409257978.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&state=us-national-parks.findthedata.org');"><span class="btn-icon-wrap"><span class="gp">&nbsp;</span></span>Sign in with Google</div><div class="fb_login_button large stnd-btn bg-darkblue"><span class="btn-icon-wrap"><span class="fb">&nbsp;</span></span>Sign in with Facebook</div>				<span class="social-claus">Don't worry, we never post without your permission.</span>
			</div>
		</div>
		<div id="new-login">
			<div id="create-account-title">Don't have an account?</div>
			<div class="create-account-section">
				<div id="create-account-btn">
					<a class="stnd-btn" href="javascript:void(0);" onclick="FTB.show_registration(); return false;"><span>&nbsp;</span>Sign Up</a>
				</div>
			</div>
		</div>
	</div>
	<div id="login-footer">
		<ul>
			<li><a rel='nofollow' href='http://www.findthebest.com/add_edit_policy'>Content Policy</a></li>
			<li><a rel='nofollow' href='http://www.findthebest.com/privacy'>Privacy</a></li>
			<li><a rel='nofollow' href='http://www.findthebest.com/terms'>Terms & Conditions</a></li>
		</ul>
	</div>
</div><div id="fb-root"></div>
		<!-- open footer -->
			<div id='footer'>
				<div id='mob-footer-tog'>More info about this site</div>
				<div class='grid-wrap'>
					<div class='ft-nav'>
						<div class='ft-col-wrap'>
							<h5 class='ft-title'>Company</h5>
							<div class='ft-col'>
								<ul class='ft-list'>
									<li><a href='http://www.findthebest.com/about-us' rel="nofollow" class='ft-link'>About</a></li>
									<li><a href='http://www.findthebest.com/contact-us' rel="nofollow" class='ft-link'>Contact Us</a></li>
									<li><a href='http://blog.findthebest.com' rel="nofollow" class='ft-link'>Blog</a></li>
									<li><a href='http://press.findthebest.com' rel="nofollow" class='ft-link'>Press</a></li>
								</ul>
								<ul class='ft-list'>
									<li><a href='http://www.findthebest.com/partner-with-us' rel="nofollow" class='ft-link'>Partner With Us</a></li>
									<li><a href='http://www.findthebest.com/business' rel="nofollow" class='ft-link'>Businesses</a></li>
									<li><a href='http://www.findthebest.com/advertising' rel="nofollow" class='ft-link'>Advertisers</a></li>
									<li><a href='http://www.findthebest.com/jobs' rel="nofollow" class='ft-link'>Jobs</a></li>
								</ul>
								<ul class='ft-list'>
									<li><a href='http://team.findthebest.com' rel="nofollow" class='ft-link'>Team</a></li>
									<li><a href='http://www.findthebest.com/add_edit_policy' rel="nofollow" class='ft-link'>Content Policy</a></li>
									<li><a href='http://www.findthebest.com/privacy' rel="nofollow" class='ft-link'>Privacy</a></li>
									<li><a href='http://www.findthebest.com/terms' rel="nofollow" class='ft-link'>Terms</a></li>
								</ul>
							</div>
						</div>
						<div class='ft-col-wrap'>
							<h5 class='ft-title'>Network</h5>
							<div class='ft-col'>
								<ul class='ft-list'><li><a href='http://www.findthebest.com' rel="nofollow" class='ft-link'>FindTheBest</a></li><li><a href='http://www.findthecompany.com' rel="nofollow" class='ft-link'>FindTheCompany</a></li><li><a href='http://www.findthecoupons.com' rel="nofollow" class='ft-link'>FindTheCoupons</a></li></ul>
											<ul class='ft-list'><li><a href='http://www.death-record.com' rel="nofollow" class='ft-link'>Death-Record</a></li><li><a href='http://www.locategrave.org' rel="nofollow" class='ft-link'>LocateGrave</a></li><li><a href='http://www.weatherdb.com' rel="nofollow" class='ft-link'>WeatherDB</a></li></ul>
							</div>
						</div>
						<div class='ft-col-wrap connect'>
							<h5 class='ft-title'>Connect</h5>
							<div class='ft-col'>
								<ul class='ft-list'>
									<li>
										<a href='https://www.facebook.com/FindTheBest' rel="nofollow" class='ft-link'>
										<span class='facebook'>Facebook<strong></strong></span>
										Follow us on Facebook</a>
									</li>
									<li>
										<a href='http://www.twitter.com/FindTheBest' rel="nofollow" class='ft-link'>
										<span class='twitter'>Twitter<strong></strong></span>
										Follow us on Twitter</a>
									</li>
									<li>
										<a href='https://plus.google.com/109983372437179990715/posts' rel="nofollow" class='ft-link'>
										<span class='googleplus'>+1<strong></strong></span>
										Follow us on Google+</a>
									</li>
									<li>
										<a href='http://www.linkedin.com/company/findthebest' rel="nofollow" class='ft-link'>
										<span class='linkedin'>in<strong></strong></span>
										Follow us on LinkedIn</a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div class='ft-b clearfix'>
						<div class='copyright'>&copy; 2013 FindTheBest.com, Inc. All Rights Reserved.</div>
						<div class='fs-wrap'>
							<div class='fs-window'><div class='fs-val'>FindTheData</div>
					<div class='fs-arrow'></div>
				</div>
						<div class='fs-opts'>
							
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- close footer -->
	  </div>

  
</div></div> <!-- /block-inner, /block -->
</div>
		
		<script src='http://cdn1.findthebest.com/rx/core.225.js'></script><script src='http://cdn1.findthebest.com/rx/desktop.225.js'></script><script src='http://cdn1.findthebest.com/rx/detail.225.js'></script>		<script src="http://cdn2.findthebest.com/sites/default/files/js/js_6ab6f7becdd1a32237635709939a9232.ver.d8f162ea1dfb42dd5f1ad63055978fc68d60a79b-S.js"></script>
					<script>
				$('#loading,#loading-msg').css('display', 'none');
			</script>
				<script>
dataLayer = [];
dataLayer.push({subcat:'Places'});dataLayer.push({'sd':'us-national-parks'});dataLayer.push({'d':'findthedata.org'});dataLayer.push({'c':'Society'});dataLayer.push({'pt':'DD'});dataLayer.push({'lid':'58'});dataLayer.push({'o':'ftb'});dataLayer.push({mobile:$(window).width()<=750?'yes':'no'});dataLayer.push({appname:'US National Parks'});
</script><noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-8XMN"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-8XMN');</script>		<script>
			/*<![CDATA[*/
			/*]]>*/
			</script>
	</body>
</html>

"""

def read_data(filename):
    """
    Used to read all tweets from the json file.
    """
    data = []
    try:
        with open(filename) as f:
            for line in f:
                data.append(json.loads(line.strip()))
    except:
        print "Failed to read data!"
        return []
    print "The json file has been successfully read!"
    return data


def getHtml(url):
	req = urllib2.Request(url, headers={'User-Agent' : "Chrome/31.0.1650.57"})
	urlfile = urllib2.urlopen(req)
	data = urlfile.read()
	urlfile.close()
	return data

def getHtml2(url):
	urlfile = urllib2.urlopen(url)
	data = urlfile.read()
	urlfile.close()
	return data

def getDescription(gov):
	print "get des"
	html = getHtml(gov)
	# print html
	soup = BeautifulSoup(html)
	# div = soup.find("div", {'class':"landing-intro intro clearfix"})
	div = soup.find_all("div", class_="two-third-col")
	# print len(div)
	if div:
		p = div[0].findAll('p')
		# print p
		# return None
		# return div
		string = p[0].stripped_strings
		des = ""
		for s in string:
			des += s
		return des

# match = re.search(r'coords":.+' , html, re.M|re.I)
def getCoords(html):
	match = re.search(r'coords":\["ll:(-?\d+\.?\d+):(-?\d+\.?\d+)"' , html, re.M|re.I)
	if match:
	    lat = float(match.group(1))
	    lon = float(match.group(2))
	    coords = {'lat': lat, 'lon': lon}
	    return coords
	else:
	    print "did not found coords"
	    return None

def getActivities(html):
	soup = BeautifulSoup(html)
	acti = soup.find("table", {'id':"rep_activities"})
	records = []
	for row in acti.findAll('tr'):
		col = row.findAll('td')
		act = col[0].string
		records.append(act)
	return records

def getUrlandTitle(html):
	soup = BeautifulSoup(html)
	urls = soup.find_all("a",{'class':'outbound_lnk'}, href=True)
	gov = urls[3]['href']
	print gov
	p = getDescription(gov)
	datadict = {'facility': urls[3].string, 'description': p}
	# print p
	return datadict

def getNationalParkInfo(html):
	coords = getCoords(html)
	amenities = getActivities(html)
	UrlandTitle = getUrlandTitle(html)
	info = {'coords': coords, 'amenity':amenities}
	info.update(UrlandTitle)
	return info


# html = getHtml(url)
# print getCoords(html)
# print getUrlandTitle(html)

def writeInfoToJson(start, num, filename = 'NparkDetails.json'):
	f = open(filename, "w")
	for i in xrange(start, num):
		url = "http://us-national-parks.findthedata.org/l/"+str(i)
		html = getHtml(url)
		info = getNationalParkInfo(html)
		f.write(json.dumps(info) + '\n')
		time.sleep(5)
	f.close()

def getImg(html):
	soup = BeautifulSoup(html)
	img_divs = soup.find_all("div",{'class':'thumb-wrap-inner'})
	# print img_divs
	srcs = []
	for div in img_divs:
		img = div.findAll('img')
		src = img[0]['src']
		srcs.append(src)
	return srcs

# getImg(html)

#32, 37
#37 is gone , 32 seems normal
if __name__ == "__main__":
	data = read_data(os.path.join(os.getcwd(),'NparkDetails.json'))
	print "start..."
	baseurl = "http://us-national-parks.findthedata.org/l/"
	filename = "NparkDetailsNew.json"
	f = open(filename, "w")
	for idx, park in enumerate(data):
		if idx < 36:
			url = baseurl+str(idx+1)
		else:
			url = baseurl+str(idx+2)
		html = getHtml(url)
		srcs = getImg(html)
		# print type(park)
		print idx
		park['img'] = srcs
		f.write(json.dumps(park)+'\n')
		time.sleep(5)
	f.close()
# 	writeInfoToJson(1, 60)
# 	print "finished..."
	




