# extract HTML data from BeautifulSoup
# website: https://parade.com/1039985/marynliles/pick-up-lines/
from bs4 import BeautifulSoup
html_data = """
<!DOCTYPE HTML>
<html xmlns="https://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<!--[if lt IE 9]><link rel="stylesheet" href="/wp-content/themes/wp-theme/css/parade/compiled/bootstrap-fixed.css?v=8" type="text/css" media=""/>
		<link rel="stylesheet" href="/wp-content/themes/wp-theme/css/parade/compiled/bootstrap-desktop.css?v=8" type="text/css" media=""/><![endif]-->
<script type="text/javascript">
/* Modernizr 2.6.2 (Custom Build) | MIT & BSD
 * Build: http://modernizr.com/download/#-fontface-backgroundsize-borderimage-borderradius-boxshadow-flexbox-flexboxlegacy-hsla-multiplebgs-opacity-rgba-textshadow-cssanimations-csscolumns-generatedcontent-cssgradients-cssreflections-csstransforms-csstransforms3d-csstransitions-applicationcache-canvas-canvastext-draganddrop-hashchange-history-audio-video-indexeddb-input-inputtypes-localstorage-postmessage-sessionstorage-websockets-websqldatabase-webworkers-geolocation-inlinesvg-smil-svg-svgclippaths-touch-webgl-shiv-mq-cssclasses-teststyles-testprop-testallprops-hasevent-prefixes-domprefixes-load
 */
;window.Modernizr=function(a,b,c){function D(a){j.cssText=a}function E(a,b){return D(n.join(a+";")+(b||""))}function F(a,b){return typeof a===b}function G(a,b){return!!~(""+a).indexOf(b)}function H(a,b){for(var d in a){var e=a[d];if(!G(e,"-")&&j[e]!==c)return b=="pfx"?e:!0}return!1}function I(a,b,d){for(var e in a){var f=b[a[e]];if(f!==c)return d===!1?a[e]:F(f,"function")?f.bind(d||b):f}return!1}function J(a,b,c){var d=a.charAt(0).toUpperCase()+a.slice(1),e=(a+" "+p.join(d+" ")+d).split(" ");return F(b,"string")||F(b,"undefined")?H(e,b):(e=(a+" "+q.join(d+" ")+d).split(" "),I(e,b,c))}function K(){e.input=function(c){for(var d=0,e=c.length;d<e;d++)u[c[d]]=c[d]in k;return u.list&&(u.list=!!b.createElement("datalist")&&!!a.HTMLDataListElement),u}("autocomplete autofocus list placeholder max min multiple pattern required step".split(" ")),e.inputtypes=function(a){for(var d=0,e,f,h,i=a.length;d<i;d++)k.setAttribute("type",f=a[d]),e=k.type!=="text",e&&(k.value=l,k.style.cssText="position:absolute;visibility:hidden;",/^range$/.test(f)&&k.style.WebkitAppearance!==c?(g.appendChild(k),h=b.defaultView,e=h.getComputedStyle&&h.getComputedStyle(k,null).WebkitAppearance!=="textfield"&&k.offsetHeight!==0,g.removeChild(k)):/^(search|tel)$/.test(f)||(/^(url|email)$/.test(f)?e=k.checkValidity&&k.checkValidity()===!1:e=k.value!=l)),t[a[d]]=!!e;return t}("search tel url email datetime date month week time datetime-local number range color".split(" "))}var d="2.6.2",e={},f=!0,g=b.documentElement,h="modernizr",i=b.createElement(h),j=i.style,k=b.createElement("input"),l=":)",m={}.toString,n=" -webkit- -moz- -o- -ms- ".split(" "),o="Webkit Moz O ms",p=o.split(" "),q=o.toLowerCase().split(" "),r={svg:"http://www.w3.org/2000/svg"},s={},t={},u={},v=[],w=v.slice,x,y=function(a,c,d,e){var f,i,j,k,l=b.createElement("div"),m=b.body,n=m||b.createElement("body");if(parseInt(d,10))while(d--)j=b.createElement("div"),j.id=e?e[d]:h+(d+1),l.appendChild(j);return f=["&#173;",'<style id="s',h,'">',a,"</style>"].join(""),l.id=h,(m?l:n).innerHTML+=f,n.appendChild(l),m||(n.style.background="",n.style.overflow="hidden",k=g.style.overflow,g.style.overflow="hidden",g.appendChild(n)),i=c(l,a),m?l.parentNode.removeChild(l):(n.parentNode.removeChild(n),g.style.overflow=k),!!i},z=function(b){var c=a.matchMedia||a.msMatchMedia;if(c)return c(b).matches;var d;return y("@media "+b+" { #"+h+" { position: absolute; } }",function(b){d=(a.getComputedStyle?getComputedStyle(b,null):b.currentStyle)["position"]=="absolute"}),d},A=function(){function d(d,e){e=e||b.createElement(a[d]||"div"),d="on"+d;var f=d in e;return f||(e.setAttribute||(e=b.createElement("div")),e.setAttribute&&e.removeAttribute&&(e.setAttribute(d,""),f=F(e[d],"function"),F(e[d],"undefined")||(e[d]=c),e.removeAttribute(d))),e=null,f}var a={select:"input",change:"input",submit:"form",reset:"form",error:"img",load:"img",abort:"img"};return d}(),B={}.hasOwnProperty,C;!F(B,"undefined")&&!F(B.call,"undefined")?C=function(a,b){return B.call(a,b)}:C=function(a,b){return b in a&&F(a.constructor.prototype[b],"undefined")},Function.prototype.bind||(Function.prototype.bind=function(b){var c=this;if(typeof c!="function")throw new TypeError;var d=w.call(arguments,1),e=function(){if(this instanceof e){var a=function(){};a.prototype=c.prototype;var f=new a,g=c.apply(f,d.concat(w.call(arguments)));return Object(g)===g?g:f}return c.apply(b,d.concat(w.call(arguments)))};return e}),s.flexbox=function(){return J("flexWrap")},s.flexboxlegacy=function(){return J("boxDirection")},s.canvas=function(){var a=b.createElement("canvas");return!!a.getContext&&!!a.getContext("2d")},s.canvastext=function(){return!!e.canvas&&!!F(b.createElement("canvas").getContext("2d").fillText,"function")},s.webgl=function(){return!!a.WebGLRenderingContext},s.touch=function(){var c;return"ontouchstart"in a||a.DocumentTouch&&b instanceof DocumentTouch?c=!0:y(["@media (",n.join("touch-enabled),("),h,")","{#modernizr{top:9px;position:absolute}}"].join(""),function(a){c=a.offsetTop===9}),c},s.geolocation=function(){return"geolocation"in navigator},s.postmessage=function(){return!!a.postMessage},s.websqldatabase=function(){return!!a.openDatabase},s.indexedDB=function(){return!!J("indexedDB",a)},s.hashchange=function(){return A("hashchange",a)&&(b.documentMode===c||b.documentMode>7)},s.history=function(){return!!a.history&&!!history.pushState},s.draganddrop=function(){var a=b.createElement("div");return"draggable"in a||"ondragstart"in a&&"ondrop"in a},s.websockets=function(){return"WebSocket"in a||"MozWebSocket"in a},s.rgba=function(){return D("background-color:rgba(150,255,150,.5)"),G(j.backgroundColor,"rgba")},s.hsla=function(){return D("background-color:hsla(120,40%,100%,.5)"),G(j.backgroundColor,"rgba")||G(j.backgroundColor,"hsla")},s.multiplebgs=function(){return D("background:url(https://),url(https://),red url(https://)"),/(url\s*\(.*?){3}/.test(j.background)},s.backgroundsize=function(){return J("backgroundSize")},s.borderimage=function(){return J("borderImage")},s.borderradius=function(){return J("borderRadius")},s.boxshadow=function(){return J("boxShadow")},s.textshadow=function(){return b.createElement("div").style.textShadow===""},s.opacity=function(){return E("opacity:.55"),/^0.55$/.test(j.opacity)},s.cssanimations=function(){return J("animationName")},s.csscolumns=function(){return J("columnCount")},s.cssgradients=function(){var a="background-image:",b="gradient(linear,left top,right bottom,from(#9f9),to(white));",c="linear-gradient(left top,#9f9, white);";return D((a+"-webkit- ".split(" ").join(b+a)+n.join(c+a)).slice(0,-a.length)),G(j.backgroundImage,"gradient")},s.cssreflections=function(){return J("boxReflect")},s.csstransforms=function(){return!!J("transform")},s.csstransforms3d=function(){var a=!!J("perspective");return a&&"webkitPerspective"in g.style&&y("@media (transform-3d),(-webkit-transform-3d){#modernizr{left:9px;position:absolute;height:3px;}}",function(b,c){a=b.offsetLeft===9&&b.offsetHeight===3}),a},s.csstransitions=function(){return J("transition")},s.fontface=function(){var a;return y('@font-face {font-family:"font";src:url("https://")}',function(c,d){var e=b.getElementById("smodernizr"),f=e.sheet||e.styleSheet,g=f?f.cssRules&&f.cssRules[0]?f.cssRules[0].cssText:f.cssText||"":"";a=/src/i.test(g)&&g.indexOf(d.split(" ")[0])===0}),a},s.generatedcontent=function(){var a;return y(["#",h,"{font:0/0 a}#",h,':after{content:"',l,'";visibility:hidden;font:3px/1 a}'].join(""),function(b){a=b.offsetHeight>=3}),a},s.video=function(){var a=b.createElement("video"),c=!1;try{if(c=!!a.canPlayType)c=new Boolean(c),c.ogg=a.canPlayType('video/ogg; codecs="theora"').replace(/^no$/,""),c.h264=a.canPlayType('video/mp4; codecs="avc1.42E01E"').replace(/^no$/,""),c.webm=a.canPlayType('video/webm; codecs="vp8, vorbis"').replace(/^no$/,"")}catch(d){}return c},s.audio=function(){var a=b.createElement("audio"),c=!1;try{if(c=!!a.canPlayType)c=new Boolean(c),c.ogg=a.canPlayType('audio/ogg; codecs="vorbis"').replace(/^no$/,""),c.mp3=a.canPlayType("audio/mpeg;").replace(/^no$/,""),c.wav=a.canPlayType('audio/wav; codecs="1"').replace(/^no$/,""),c.m4a=(a.canPlayType("audio/x-m4a;")||a.canPlayType("audio/aac;")).replace(/^no$/,"")}catch(d){}return c},s.localstorage=function(){try{return localStorage.setItem(h,h),localStorage.removeItem(h),!0}catch(a){return!1}},s.sessionstorage=function(){try{return sessionStorage.setItem(h,h),sessionStorage.removeItem(h),!0}catch(a){return!1}},s.webworkers=function(){return!!a.Worker},s.applicationcache=function(){return!!a.applicationCache},s.svg=function(){return!!b.createElementNS&&!!b.createElementNS(r.svg,"svg").createSVGRect},s.inlinesvg=function(){var a=b.createElement("div");return a.innerHTML="<svg/>",(a.firstChild&&a.firstChild.namespaceURI)==r.svg},s.smil=function(){return!!b.createElementNS&&/SVGAnimate/.test(m.call(b.createElementNS(r.svg,"animate")))},s.svgclippaths=function(){return!!b.createElementNS&&/SVGClipPath/.test(m.call(b.createElementNS(r.svg,"clipPath")))};for(var L in s)C(s,L)&&(x=L.toLowerCase(),e[x]=s[L](),v.push((e[x]?"":"no-")+x));return e.input||K(),e.addTest=function(a,b){if(typeof a=="object")for(var d in a)C(a,d)&&e.addTest(d,a[d]);else{a=a.toLowerCase();if(e[a]!==c)return e;b=typeof b=="function"?b():b,typeof f!="undefined"&&f&&(g.className+=" "+(b?"":"no-")+a),e[a]=b}return e},D(""),i=k=null,function(a,b){function k(a,b){var c=a.createElement("p"),d=a.getElementsByTagName("head")[0]||a.documentElement;return c.innerHTML="x<style>"+b+"</style>",d.insertBefore(c.lastChild,d.firstChild)}function l(){var a=r.elements;return typeof a=="string"?a.split(" "):a}function m(a){var b=i[a[g]];return b||(b={},h++,a[g]=h,i[h]=b),b}function n(a,c,f){c||(c=b);if(j)return c.createElement(a);f||(f=m(c));var g;return f.cache[a]?g=f.cache[a].cloneNode():e.test(a)?g=(f.cache[a]=f.createElem(a)).cloneNode():g=f.createElem(a),g.canHaveChildren&&!d.test(a)?f.frag.appendChild(g):g}function o(a,c){a||(a=b);if(j)return a.createDocumentFragment();c=c||m(a);var d=c.frag.cloneNode(),e=0,f=l(),g=f.length;for(;e<g;e++)d.createElement(f[e]);return d}function p(a,b){b.cache||(b.cache={},b.createElem=a.createElement,b.createFrag=a.createDocumentFragment,b.frag=b.createFrag()),a.createElement=function(c){return r.shivMethods?n(c,a,b):b.createElem(c)},a.createDocumentFragment=Function("h,f","return function(){var n=f.cloneNode(),c=n.createElement;h.shivMethods&&("+l().join().replace(/\w+/g,function(a){return b.createElem(a),b.frag.createElement(a),'c("'+a+'")'})+");return n}")(r,b.frag)}function q(a){a||(a=b);var c=m(a);return r.shivCSS&&!f&&!c.hasCSS&&(c.hasCSS=!!k(a,"article,aside,figcaption,figure,footer,header,hgroup,nav,section{display:block}mark{background:#FF0;color:#000}")),j||p(a,c),a}var c=a.html5||{},d=/^<|^(?:button|map|select|textarea|object|iframe|option|optgroup)$/i,e=/^(?:a|b|code|div|fieldset|h1|h2|h3|h4|h5|h6|i|label|li|ol|p|q|span|strong|style|table|tbody|td|th|tr|ul)$/i,f,g="_html5shiv",h=0,i={},j;(function(){try{var a=b.createElement("a");a.innerHTML="<xyz></xyz>",f="hidden"in a,j=a.childNodes.length==1||function(){b.createElement("a");var a=b.createDocumentFragment();return typeof a.cloneNode=="undefined"||typeof a.createDocumentFragment=="undefined"||typeof a.createElement=="undefined"}()}catch(c){f=!0,j=!0}})();var r={elements:c.elements||"abbr article aside audio bdi canvas data datalist details figcaption figure footer header hgroup mark meter nav output progress section summary time video",shivCSS:c.shivCSS!==!1,supportsUnknownElements:j,shivMethods:c.shivMethods!==!1,type:"default",shivDocument:q,createElement:n,createDocumentFragment:o};a.html5=r,q(b)}(this,b),e._version=d,e._prefixes=n,e._domPrefixes=q,e._cssomPrefixes=p,e.mq=z,e.hasEvent=A,e.testProp=function(a){return H([a])},e.testAllProps=J,e.testStyles=y,g.className=g.className.replace(/(^|\s)no-js(\s|$)/,"$1$2")+(f?" js "+v.join(" "):""),e}(this,this.document),function(a,b,c){function d(a){return"[object Function]"==o.call(a)}function e(a){return"string"==typeof a}function f(){}function g(a){return!a||"loaded"==a||"complete"==a||"uninitialized"==a}function h(){var a=p.shift();q=1,a?a.t?m(function(){("c"==a.t?B.injectCss:B.injectJs)(a.s,0,a.a,a.x,a.e,1)},0):(a(),h()):q=0}function i(a,c,d,e,f,i,j){function k(b){if(!o&&g(l.readyState)&&(u.r=o=1,!q&&h(),l.onload=l.onreadystatechange=null,b)){"img"!=a&&m(function(){t.removeChild(l)},50);for(var d in y[c])y[c].hasOwnProperty(d)&&y[c][d].onload()}}var j=j||B.errorTimeout,l=b.createElement(a),o=0,r=0,u={t:d,s:c,e:f,a:i,x:j};1===y[c]&&(r=1,y[c]=[]),"object"==a?l.data=c:(l.src=c,l.type=a),l.width=l.height="0",l.onerror=l.onload=l.onreadystatechange=function(){k.call(this,r)},p.splice(e,0,u),"img"!=a&&(r||2===y[c]?(t.insertBefore(l,s?null:n),m(k,j)):y[c].push(l))}function j(a,b,c,d,f){return q=0,b=b||"j",e(a)?i("c"==b?v:u,a,b,this.i++,c,d,f):(p.splice(this.i++,0,a),1==p.length&&h()),this}function k(){var a=B;return a.loader={load:j,i:0},a}var l=b.documentElement,m=a.setTimeout,n=b.getElementsByTagName("script")[0],o={}.toString,p=[],q=0,r="MozAppearance"in l.style,s=r&&!!b.createRange().compareNode,t=s?l:n.parentNode,l=a.opera&&"[object Opera]"==o.call(a.opera),l=!!b.attachEvent&&!l,u=r?"object":l?"script":"img",v=l?"script":u,w=Array.isArray||function(a){return"[object Array]"==o.call(a)},x=[],y={},z={timeout:function(a,b){return b.length&&(a.timeout=b[0]),a}},A,B;B=function(a){function b(a){var a=a.split("!"),b=x.length,c=a.pop(),d=a.length,c={url:c,origUrl:c,prefixes:a},e,f,g;for(f=0;f<d;f++)g=a[f].split("="),(e=z[g.shift()])&&(c=e(c,g));for(f=0;f<b;f++)c=x[f](c);return c}function g(a,e,f,g,h){var i=b(a),j=i.autoCallback;i.url.split(".").pop().split("?").shift(),i.bypass||(e&&(e=d(e)?e:e[a]||e[g]||e[a.split("/").pop().split("?")[0]]),i.instead?i.instead(a,e,f,g,h):(y[i.url]?i.noexec=!0:y[i.url]=1,f.load(i.url,i.forceCSS||!i.forceJS&&"css"==i.url.split(".").pop().split("?").shift()?"c":c,i.noexec,i.attrs,i.timeout),(d(e)||d(j))&&f.load(function(){k(),e&&e(i.origUrl,h,g),j&&j(i.origUrl,h,g),y[i.url]=2})))}function h(a,b){function c(a,c){if(a){if(e(a))c||(j=function(){var a=[].slice.call(arguments);k.apply(this,a),l()}),g(a,j,b,0,h);else if(Object(a)===a)for(n in m=function(){var b=0,c;for(c in a)a.hasOwnProperty(c)&&b++;return b}(),a)a.hasOwnProperty(n)&&(!c&&!--m&&(d(j)?j=function(){var a=[].slice.call(arguments);k.apply(this,a),l()}:j[n]=function(a){return function(){var b=[].slice.call(arguments);a&&a.apply(this,b),l()}}(k[n])),g(a[n],j,b,n,h))}else!c&&l()}var h=!!a.test,i=a.load||a.both,j=a.callback||f,k=j,l=a.complete||f,m,n;c(h?a.yep:a.nope,!!i),i&&c(i)}var i,j,l=this.yepnope.loader;if(e(a))g(a,0,l,0);else if(w(a))for(i=0;i<a.length;i++)j=a[i],e(j)?g(j,0,l,0):w(j)?B(j):Object(j)===j&&h(j,l);else Object(a)===a&&h(a,l)},B.addPrefix=function(a,b){z[a]=b},B.addFilter=function(a){x.push(a)},B.errorTimeout=1e4,null==b.readyState&&b.addEventListener&&(b.readyState="loading",b.addEventListener("DOMContentLoaded",A=function(){b.removeEventListener("DOMContentLoaded",A,0),b.readyState="complete"},0)),a.yepnope=k(),a.yepnope.executeStack=h,a.yepnope.injectJs=function(a,c,d,e,i,j){var k=b.createElement("script"),l,o,e=e||B.errorTimeout;k.src=a;for(o in d)k.setAttribute(o,d[o]);c=j?h:c||f,k.onreadystatechange=k.onload=function(){!l&&g(k.readyState)&&(l=1,c(),k.onload=k.onreadystatechange=null)},m(function(){l||(l=1,c(1))},e),i?k.onload():n.parentNode.insertBefore(k,n)},a.yepnope.injectCss=function(a,c,d,e,g,i){var e=b.createElement("link"),j,c=i?h:c||f;e.href=a,e.rel="stylesheet",e.type="text/css";for(j in d)e.setAttribute(j,d[j]);g||(n.parentNode.insertBefore(e,n),m(c,0))}}(this,document),Modernizr.load=function(){yepnope.apply(window,[].slice.call(arguments,0))};

window.parade = (function( app ) { app.styles = {"phone":"https:\/\/parade.com\/wp-content\/themes\/wp-theme\/css\/parade\/compiled\/bootstrap-phone--article.css?v=8","tablet":"https:\/\/parade.com\/wp-content\/themes\/wp-theme\/css\/parade\/compiled\/bootstrap-tablet--article.css?v=8","desktop":"https:\/\/parade.com\/wp-content\/themes\/wp-theme\/css\/parade\/compiled\/bootstrap-desktop--article.css?v=8"}; return app; })( window.parade || {} );
window.parade = (function (app) {
    var config = app.styles;
    var d = document,
        css = document.createElement('link'),
        is_phone = window.Modernizr.mq('(max-device-width: 767px),(max-device-width: 480px)'),
        is_tablet = (window.Modernizr.mq('(min-device-width: 768px) and (max-device-width: 1024px)') && Modernizr.touch),
        is_desktop = window.Modernizr.mq('only screen and (min-device-width: 1024px)'),
        is_old_ie = navigator.userAgent.match(/MSIE [678]\..*?(?!.*Trident\/[5-9])/),
        is_oldest_ie = navigator.userAgent.match(/MSIE [67]\..*?(?!.*Trident\/[5-9])/),
        is_retina = window.Modernizr.mq("only screen and (-moz-min-device-pixel-ratio: 1.3), only screen and (-o-min-device-pixel-ratio: 2.6/2), only screen and (-webkit-min-device-pixel-ratio: 1.3), only screen  and (min-device-pixel-ratio: 1.3), only screen and (min-resolution: 1.3dppx)"),
        is_recipe_print = document.location.pathname.match(/\/print\/?$/),
        is_landscape = null,
        is_iphone5 = null;

    if (null !== is_old_ie && is_old_ie.length > 0) {
        is_old_ie = true;
    } else {
        is_old_ie = false;
    }
    if (null !== is_oldest_ie && is_oldest_ie.length > 0) {
        is_oldest_ie = true;
    } else {
        is_oldest_ie = false;
    }
	if ( false === is_desktop && false === is_phone && false === is_tablet ) {
		is_tablet = window.Modernizr.mq('(max-width:800px),(device-aspect-ratio: 3/4)');
		if ( !is_tablet ) {
			is_phone =  window.Modernizr.mq('(orientation: landscape),(orientation: landscape),(device-aspect-ratio: 40/71),(device-aspect-ratio: 2/3),(max-device-width: 1136px)');
			if ( !is_phone ) {
				is_desktop = true;
			}
		}
	}
    var isLandscape = function () {
        return ('undefined' !== typeof window.orientation && (90 === Math.abs(window.orientation) || 270 === Math.abs(window.orientation))) ? true : false;
    },
        addE = window.addEventListener || window.attachEvent,
        callB = function (e) {
            var l1 = window.parade.is_landscape,
                l2 = isLandscape();
            if (l1 !== l2 && false === window.parade.orientationChanged) {
                window.parade.orientationChanged = true;
                if ('function' === typeof window.parade.displayOrientationChangeAds) {
                    window.parade.displayOrientationChangeAds();
                }
            }
			if ( true === window.parade.modalOverlayed && true !== isLandscape() ) {
				googletag.pubads().refresh( [ window.parade.adInstances[ '300_modal' ] ] );
			}
            return l2;
        };
    if ('function' === typeof addE) {
        addE("orientationchange", callB);
    }
    is_landscape = isLandscape();
    var isiPhone5 = function () {
        var agent = window.navigator.userAgent,
            start = agent.indexOf('OS '),
            version = 0,
            availHeight = 0;
        if ((agent.indexOf('iPhone') > -1) && start > -1) {
            version = window.Number(agent.substr(start + 3, 3).replace('_', '.'));
        }
        if ('undefined' !== typeof window.screen) {
            availHeight = window.screen.availHeight;
        }
        return (version >= 6 && window.devicePixelRatio >= 2 && availHeight == 548) ? true : false;
    };
    is_iphone5 = isiPhone5();

    // Properly detects phones in landscape orientation & with a width larger than 768px.
    // Mainly for iPhone X
    if(is_tablet && is_landscape) {
        if(window.screen.width/window.screen.height > 16/9) {
            is_tablet = false;
            is_phone = true;
        }
    }

    // Determines which style sheet to load.
    css.rel = 'stylesheet';
    css.media = 'screen, print';
    if (is_phone) {
        css.href = config.phone;
    } else if (is_tablet) {
        css.href = config.tablet;
    } else if (is_desktop && !is_recipe_print) {
        css.href = config.desktop;
    }

    // @todo: remove when tested on all browsers.
    css.rel = 'stylesheet';
    css.media = 'screen, print';
    (d.head || d.getElementsByTagName('head')[0]).appendChild(css);
    if (is_phone) {
        css.href = config.phone;
    } else if (is_tablet) {
        css.href = config.tablet;
    } else if (is_desktop && !is_recipe_print) {
        css.href = config.desktop;
    }

    if (true === is_old_ie) {
        is_desktop = true;
    }

    d.getElementsByTagName('html')[0].style.display = "block";

    app.is_phone = is_phone;
    app.is_iphone5 = is_iphone5;
    app.is_tablet = is_tablet;
    app.is_landscape = is_landscape;
    app.is_desktop = is_desktop;
    app.is_old_ie = is_old_ie;
    app.is_oldest_ie = is_oldest_ie;
    app.is_retina = is_retina;
	app.content300Disabled = false;
	app.content300Enabled = true;
    app.platform = function () {
        if (true === this.is_phone) {
            return 'phone';
        } else if (true === this.is_tablet) {
            return 'tablet';
        }
        return 'desktop';
    }

    //@todo: cleanup
    //app.supportedAds = {"desktop":[],"phone":[],"tablet":[]};
    //app.adSlot = function () {
    //    return ('desktop' === app.platform()) ? '' : '';
    //};
    //app.adSizes = function (type) {
    //    var ads = app.supportedAds
    //    	, result = []
	//		, platform = app.platform()
    //    	, supported_ads = ads[ platform ];
    //    if ('undefined' !== typeof supported_ads) {
    //        var supported_ad = supported_ads[type];
    //        result = ('undefined' !== typeof supported_ad) ? supported_ad : [];
    //    }
	//	if ( '300_content' === type ) {
	//		if ( true !== this.content300Enabled && true === this.is_desktop) {
	//			result = [];
	//		} else if ( true === this.content300Disabled ) {
	//			result = [];
	//		}
	//	}
    //    return result;
    //};
    //app.adInstances = {};
    //app.isSupportedAd = function (type) {
    //    var supported_ad = app.adSizes(type);
    //    return ('undefined' !== typeof supported_ad && supported_ad.length > 0) ? true : false;
    //};
    app.takeoverAd = function (obj) {
        app.takeover = obj;
		if ("function" === app.doTakeover) {
			app.doTakeover();
		}
    };
    return app;

})(window.parade || {});

		</script>
<meta property="article:published_time" content="2020-10-01T15:15:30-04:00" />
<meta property="article:modified_time" content="2020-12-10T11:42:04-04:00" />
<link rel="dns-prefetch" href="//s7.addthis.com">
<link rel="publisher" ref="https://plus.google.com/+parademagazine">

<meta name="author" content="Maryn Liles">
<meta name="keywords" content="Cheesy Pick Up Lines, Funny Pick Up Lines, Pick Up Lines">
<meta name="description" content="Whether you need cheesy pick up lines or corny pick-up lines, here are 101 funny, clever, cute, mildly cringy pick up lines that actually work for guys and girls.">
<meta name="news_keywords" content="Cheesy Pick Up Lines, Funny Pick Up Lines, Pick Up Lines">
<link rel="canonical" href="https://parade.com/1039985/marynliles/pick-up-lines/">
<meta name="twitter:title" content="101 Cheesy-But-Cute Pick Up Lines That'll Kick Your Flirting Game Into High Gear">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@ParadeMagazine">
<meta name="twitter:creator" content="@ParadeMagazine">
<meta name="twitter:description" content="The best pick-up lines—whether they’re cheesy, funny pick-up lines that’ll get someone laughing or clever pick-up lines that’ll make you stand out—will make breaking the ice and getting the conversation started a little bit easier.Plus, using corny pick-up lines shows off what a playful personality you have, too—and who doesn’t like that! So whether you’re [...]">
<meta name="twitter:image" content="https://parade.com/wp-content/uploads/2020/05/pickup-lines-ftr-1024x640.jpg">
<title>101 Best Pick Up Lines - Funny Pick Up Lines for Guys, Girls</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link rel="icon" type="image/png" href="/wp-content/themes/wp-theme/img/ico/favicon-16x16.png?v=7k4a9AlWgN" sizes="16x16">
<link rel="icon" type="image/png" href="/wp-content/themes/wp-theme/img/ico/favicon-32x32.png?v=7k4a9AlWgN" sizes="32x32">
<link rel="icon" type="image/png" href="/wp-content/themes/wp-theme/img/ico/favicon-128.png?v=7k4a9AlWgN" sizes="128x128">
<link rel="icon" type="image/png" href="/wp-content/themes/wp-theme/img/ico/favicon-192.png?v=7k4a9AlWgN" sizes="192x192">

<link rel="icon" href="/wp-content/themes/wp-theme/img/ico/android-chrome-192x192.png?v=7k4a9AlWgN" sizes="192x192">
<link rel="icon" href="/wp-content/themes/wp-theme/img/ico/android-chrome-256x256.png?v=7k4a9AlWgN" sizes="256x256">

<link rel="apple-touch-icon" href="/wp-content/themes/wp-theme/img/ico/apple-touch-icon-120.png?v=7k4a9AlWgN" sizes="120x120">
<link rel="apple-touch-icon" href="/wp-content/themes/wp-theme/img/ico/apple-touch-icon-152.png?v=7k4a9AlWgN" sizes="152x152">
<link rel="apple-touch-icon" href="/wp-content/themes/wp-theme/img/ico/apple-touch-icon-167.png?v=7k4a9AlWgN" sizes="167x167">
<link rel="apple-touch-icon" href="/wp-content/themes/wp-theme/img/ico/apple-touch-icon.png?v=7k4a9AlWgN" sizes="180x180">

<meta name="msapplication-config" content="/wp-content/themes/wp-theme/img/ico/browserconfig.xml?v=7k4a9AlWgN" />

<link rel="manifest" href="wp-content/themes/wp-theme/img/ico/site.webmanifest?v=7k4a9AlWgN">

<link rel="mask-icon" href="wp-content/themes/wp-theme/img/ico/safari-pinned-tab.svg?v=7k4a9AlWgN" color="#30b4cf">
<link rel="shortcut icon" type="image/ico" href="/wp-content/themes/wp-theme/img/ico/favicon.ico?v=7k4a9AlWgN">
<meta name="theme-color" content="#ffffff">
<meta property="og:title" content="101 Cheesy-But-Cute Pick Up Lines That'll Kick Your Flirting Game Into High Gear">
<meta property="og:url" content="https://parade.com/1039985/marynliles/pick-up-lines/">
<meta property="og:type" content="article">
<meta property="og:image" content="https://static.parade.com/wp-content/uploads/2020/05/pickup-lines-ftr.jpg">
<link rel="image_src" href="https://static.parade.com/wp-content/uploads/2020/05/pickup-lines-ftr.jpg">
<link rel="thumbnail" href="https://static.parade.com/wp-content/uploads/2020/05/pickup-lines-ftr.jpg">
<meta property="og:site_name" content="Parade: Entertainment, Recipes, Health, Life, Holidays">
<meta property="og:description" content="The best pick-up lines—whether they’re cheesy, funny pick-up lines that’ll get someone laughing or clever pick-up lines that’ll make you stand out—will make breaking the ice and getting the conversation started a little bit easier.Plus, using corny pick-up lines shows off what a playful personality you have, too—and who doesn’t like that! So whether you’re [...]">
<meta property="fb:app_id" content="134158690266891">
<meta name="google-site-verification" content="XliNoL7daDHEXs-2PccR30eVWdl_cbTSTBdoAl8jm_M">
<meta name="orginal-source" content="https://parade.com/1039985/marynliles/pick-up-lines/">
<link rel="dns-prefetch" href="//use.typekit.net">
<link rel="dns-prefetch" href="//static.chartbeat.com">
<link rel="dns-prefetch" href="//ping.chartbeat.com">
<link rel="dns-prefetch" href="//m.addthis.com">
<link rel="dns-prefetch" href="//api.native.ai">
<link rel="dns-prefetch" href="//ajax.googleapis.com">
<link rel="dns-prefetch" href="//www.google-analytics.com">
<link rel="dns-prefetch" href="//www.zergnet.com">
<link rel="dns-prefetch" href="//main.pubexchange.com">
<link rel="dns-prefetch" href="//static.parade.com">
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests"> <meta name="p:domain_verify" content="a04f6b64e346423c0987137b666a9a76" /><script>
if (typeof window.LogBuilder === "undefined") {
    window.LogBuilder = function(prefix, enabled) {
        return {
            buffer: [],
            debugOn : enabled,
            prefix: prefix,

            log: function (label, value) {
                if (this.debugOn !== true) {
                    this.bufferItem('log')
                    return;
                }

                console.log(this.prefix + label);

                if (typeof value === "undefined") {
                    return;
                }

                console.log(value);
            },
            table: function(label, value) {
                if (this.debugOn !== true) {
                    this.bufferItem('table', arguments)
                    return;
                }

                console.log(this.prefix + label);

                if (typeof console.table === "function") {
                    console.table(value);
                } else {
                    // ie doesn't have console.table
                    console.log(value);
                }

            },
            info: function(label, value) {
                if (this.debugOn !== true) {
                    this.bufferItem('info', arguments);
                    return;
                }
                console.info(this.prefix + label);

                if (typeof value !== "undefined") {
                    console.info(value);
                }
            },
            warn: function(label, value) {
                if (this.debugOn !== true) {
                    this.bufferItem('warn', arguments);
                    return;
                }
                console.warn(this.prefix + label);

                if (typeof value !== "undefined") {
                    console.warn(value);
                }
            },
            error: function(label, value) {
                if (this.debugOn !== true) {
                    this.bufferItem('error', arguments);
                    return;
                }
                console.error("AMG_ADS -- " + label);

                if (typeof value !== "undefined") {
                    console.error(value);
                }
            },
            enable: function() {
                if (this.debugOn !== true) {
                    this.debugOn = true;
                    this.dumpBuffer();
                }

                return this;
            },
            disable: function() {
                if (this.debugOn !== false) {
                    this.debugOff = true;
                    this.buffer = [];
                }

                return this;
            },
            bufferItem : function(type, arguments) {
                this.buffer.push({'type' : type, 'arguments' : arguments});
                return this;
            },
            dumpBuffer: function() {
                if (this.debugOn !== true) {
                    return this;
                }

                while (this.buffer.length > 0) {
                    var item = this.buffer.shift();
                    this[item['type']].apply(this, item['arguments']);
                }
            },
            queryStringExists: function(targetString) {
                var regex = new RegExp(targetString);
                if (regex.exec(window.location.search.toLowerCase()) === null) {
                    // string doesn't exist in query string
                    return false;
                }
                // string exists in query string
                return true;
            }

        };
    };
}
</script>

<link rel="stylesheet" href="https://cdn.consentmanager.mgr.consensu.org/delivery/cmp.min.css" />
<script type="text/javascript" async=true>
    /** PROMISE POLYFILL **/
    !function(e,n){"object"==typeof exports&&"undefined"!=typeof module?n():"function"==typeof define&&define.amd?define(n):n()}(0,function(){"use strict";function e(e){var n=this.constructor;return this.then(function(t){return n.resolve(e()).then(function(){return t})},function(t){return n.resolve(e()).then(function(){return n.reject(t)})})}function n(e){return!(!e||"undefined"==typeof e.length)}function t(){}function o(e){if(!(this instanceof o))throw new TypeError("Promises must be constructed via new");if("function"!=typeof e)throw new TypeError("not a function");this._state=0,this._handled=!1,this._value=undefined,this._deferreds=[],c(e,this)}function r(e,n){for(;3===e._state;)e=e._value;0!==e._state?(e._handled=!0,o._immediateFn(function(){var t=1===e._state?n.onFulfilled:n.onRejected;if(null!==t){var o;try{o=t(e._value)}catch(r){return void f(n.promise,r)}i(n.promise,o)}else(1===e._state?i:f)(n.promise,e._value)})):e._deferreds.push(n)}function i(e,n){try{if(n===e)throw new TypeError("A promise cannot be resolved with itself.");if(n&&("object"==typeof n||"function"==typeof n)){var t=n.then;if(n instanceof o)return e._state=3,e._value=n,void u(e);if("function"==typeof t)return void c(function(e,n){return function(){e.apply(n,arguments)}}(t,n),e)}e._state=1,e._value=n,u(e)}catch(r){f(e,r)}}function f(e,n){e._state=2,e._value=n,u(e)}function u(e){2===e._state&&0===e._deferreds.length&&o._immediateFn(function(){e._handled||o._unhandledRejectionFn(e._value)});for(var n=0,t=e._deferreds.length;t>n;n++)r(e,e._deferreds[n]);e._deferreds=null}function c(e,n){var t=!1;try{e(function(e){t||(t=!0,i(n,e))},function(e){t||(t=!0,f(n,e))})}catch(o){if(t)return;t=!0,f(n,o)}}var a=setTimeout;o.prototype["catch"]=function(e){return this.then(null,e)},o.prototype.then=function(e,n){var o=new this.constructor(t);return r(this,new function(e,n,t){this.onFulfilled="function"==typeof e?e:null,this.onRejected="function"==typeof n?n:null,this.promise=t}(e,n,o)),o},o.prototype["finally"]=e,o.all=function(e){return new o(function(t,o){function r(e,n){try{if(n&&("object"==typeof n||"function"==typeof n)){var u=n.then;if("function"==typeof u)return void u.call(n,function(n){r(e,n)},o)}i[e]=n,0==--f&&t(i)}catch(c){o(c)}}if(!n(e))return o(new TypeError("Promise.all accepts an array"));var i=Array.prototype.slice.call(e);if(0===i.length)return t([]);for(var f=i.length,u=0;i.length>u;u++)r(u,i[u])})},o.resolve=function(e){return e&&"object"==typeof e&&e.constructor===o?e:new o(function(n){n(e)})},o.reject=function(e){return new o(function(n,t){t(e)})},o.race=function(e){return new o(function(t,r){if(!n(e))return r(new TypeError("Promise.race accepts an array"));for(var i=0,f=e.length;f>i;i++)o.resolve(e[i]).then(t,r)})},o._immediateFn="function"==typeof setImmediate&&function(e){setImmediate(e)}||function(e){a(e,0)},o._unhandledRejectionFn=function(e){void 0!==console&&console&&console.warn("Possible Unhandled Promise Rejection:",e)};var l=function(){if("undefined"!=typeof self)return self;if("undefined"!=typeof window)return window;if("undefined"!=typeof global)return global;throw Error("unable to locate global object")}();"Promise"in l?l.Promise.prototype["finally"]||(l.Promise.prototype["finally"]=e):l.Promise=o});

    // separately set the cmp_id to allow for different CMP configurations
    var _consentAdapterConfig = {"recheckTime":10,"initSettings":[],"ccpaVendors":[80,240,"s1"],"defaultCcpaConsent":true,"defaultGdprConsent":false};
    window.cmp_id = _consentAdapterConfig.cmp_id || 5474; 

    /** START CONSENTMANAGER.NET TAG */
    window.gdprAppliesGlobally=false;if(!("cmp_id" in window)){window.cmp_id=5474}if(!("cmp_params" in window)){window.cmp_params=""}window.cmp_host="consentmanager.mgr.consensu.org";window.cmp_cdn="cdn.consentmanager.mgr.consensu.org";function cmp_getlang(j){if(typeof(j)!="boolean"){j=true}if(j&&typeof(cmp_getlang.usedlang)=="string"&&cmp_getlang.usedlang!==""){return cmp_getlang.usedlang}var g=["DE","EN","FR","IT","NO","DA","FI","ES","PT","RO","BG","ET","EL","GA","HR","LV","LT","MT","NL","PL","SV","SK","SL","CS","HU","RU","SR","ZH","TR","UK"];var c=[];var f=location.hash;var e=location.search;var a="languages" in navigator?navigator.languages:[];if(f.indexOf("cmplang=")!=-1){c.push(f.substr(f.indexOf("cmplang=")+8,2))}else{if(e.indexOf("cmplang=")!=-1){c.push(e.substr(e.indexOf("cmplang=")+8,2))}else{if("cmp_setlang" in window&&window.cmp_setlang!=""){c.push(window.cmp_setlang.toUpperCase())}else{if(a.length>0){for(var d=0;d<a.length;d++){c.push(a[d])}}}}}if("language" in navigator){c.push(navigator.language)}if("userLanguage" in navigator){c.push(navigator.userLanguage)}var h="";for(var d=0;d<c.length;d++){var b=c[d].toUpperCase();if(b.indexOf("-")!=-1){b=b.substr(0,2)}if(g.indexOf(b)!=-1){h=b;break}}if(h==""&&typeof(cmp_getlang.defaultlang)=="string"&&cmp_getlang.defaultlang!==""){return cmp_getlang.defaultlang}else{if(h==""){h="EN"}}h=h.toUpperCase();return h}(function(){var a="";var c="_en";if("cmp_getlang" in window){a=window.cmp_getlang().toLowerCase();c="_"+a}var b=document.createElement("script");b.src="https://"+window.cmp_host+"/delivery/cmp.php?id="+window.cmp_id+"&h="+encodeURIComponent(location.href)+"&"+window.cmp_params+(document.cookie.length>0?"&__cmpfcc=1":"")+"&l="+a+"&o="+(new Date()).getTime();b.type="text/javascript";b.setAttribute("data-cmp-ab",1);b.async=true;if(document.body){document.body.appendChild(b)}else{if(document.currentScript){document.currentScript.parentElement.appendChild(b)}else{document.write(b.outerHTML)}}var b=document.createElement("script");b.src="https://"+window.cmp_cdn+"/delivery/cmp"+c+".min.js";b.type="text/javascript";b.setAttribute("data-cmp-ab",1);b.async=true;if(document.body){document.body.appendChild(b)}else{if(document.currentScript){document.currentScript.parentElement.appendChild(b)}else{document.write(b.outerHTML)}}window.cmp_addFrame=function(e){if(!window.frames[e]){if(document.body){var d=document.createElement("iframe");d.style.cssText="display:none";d.name=e;document.body.appendChild(d)}else{window.setTimeout('window.cmp_addFrame("'+e+'")',10)}}};window.cmp_rc=function(k){var d=document.cookie;var h="";var f=0;while(d!=""&&f<100){f++;while(d.substr(0,1)==" "){d=d.substr(1,d.length)}var j=d.substring(0,d.indexOf("="));if(d.indexOf(";")!=-1){var e=d.substring(d.indexOf("=")+1,d.indexOf(";"))}else{var e=d.substr(d.indexOf("=")+1,d.length)}if(k==j){h=e}var g=d.indexOf(";")+1;if(g==0){g=d.length}d=d.substring(g,d.length)}return(h)};window.cmp_stub=function(){var d=arguments;__cmapi.a=__cmapi.a||[];if(!d.length){return __cmapi.a}else{if(d[0]==="ping"){if(d[1]===2){d[2]({gdprApplies:gdprAppliesGlobally,cmpLoaded:false,cmpStatus:"stub",displayStatus:"hidden",apiVersion:"2.0",cmpId:31},true)}else{d[2]({gdprAppliesGlobally:gdprAppliesGlobally,cmpLoaded:false},true)}}else{if(d[0]==="getUSPData"){d[2]({version:1,uspString:window.cmp_rc("")},true)}else{if(d[0]==="getTCData"){__cmapi.a.push([].slice.apply(d))}else{if(d[0]==="addEventListener"){__cmapi.a.push([].slice.apply(d))}else{if(d.length==4&&d[3]===false){d[2]({},false)}else{__cmapi.a.push([].slice.apply(d))}}}}}}};window.cmp_msghandler=function(h){var d=typeof h.data==="string";try{var g=d?JSON.parse(h.data):h.data}catch(j){var g=null}if(typeof(g)==="object"&&g!==null&&"__cmpCall" in g){var f=g.__cmpCall;window.__cmp(f.command,f.parameter,function(k,i){var e={__cmpReturn:{returnValue:k,success:i,callId:f.callId}};h.source.postMessage(d?JSON.stringify(e):e,"*")})}if(typeof(g)==="object"&&g!==null&&"__cmapiCall" in g){var f=g.__cmapiCall;window.__cmapi(f.command,f.parameter,function(k,i){var e={__cmapiReturn:{returnValue:k,success:i,callId:f.callId}};h.source.postMessage(d?JSON.stringify(e):e,"*")})}if(typeof(g)==="object"&&g!==null&&"__uspapiCall" in g){var f=g.__uspapiCall;window.__uspapi(f.command,f.version,function(k,i){var e={__uspapiReturn:{returnValue:k,success:i,callId:f.callId}};h.source.postMessage(d?JSON.stringify(e):e,"*")})}if(typeof(g)==="object"&&g!==null&&"__tcfapiCall" in g){var f=g.__tcfapiCall;window.__tcfapi(f.command,f.version,function(k,i){var e={__tcfapiReturn:{returnValue:k,success:i,callId:f.callId}};h.source.postMessage(d?JSON.stringify(e):e,"*")},f.parameter)}};window.cmp_setStub=function(d){if(!(d in window)||(typeof(window[d])!=="function"&&typeof(window[d])!=="object"&&(typeof(window[d])==="undefined"||window[d]!==null))){window[d]=window.cmp_stub;window[d].msgHandler=window.cmp_msghandler;if(window.addEventListener){window.addEventListener("message",window.cmp_msghandler,false)}else{window.attachEvent("onmessage",window.cmp_msghandler)}}};window.cmp_addFrame("__cmapiLocator");window.cmp_addFrame("__cmpLocator");window.cmp_addFrame("__uspapiLocator");window.cmp_addFrame("__tcfapiLocator");window.cmp_setStub("__cmapi");window.cmp_setStub("__cmp");window.cmp_setStub("__tcfapi");window.cmp_setStub("__uspapi")})();    /** END CONSENTMANANGER.NET TAG */

    window.ConsentAdapter = (function (_adapterConfig) {

        var __logger = LogBuilder("AMG_CMNET -- ", false);

        var cmpmngrLoaded = function () {
            return ('cmpmngr' in window && 'status' in cmpmngr && cmpmngr.status >= 2);
        };

        // @todo move this to a generic position?  It's pretty much abstract as it is
        var Adapter = {
            __consentsRetrieved: false,  // used if no model applies
            consentStatus: false, // true means consents have been retrieved
            defaultConsent: null, // for when no consentModel applies
            userRequiresConsent: null,
            markLoaded: null,
            loadedPromise: null, 
            activeModel: null,
            consentModels: [],
            pendingModels: 0,

            logger : null, //for ease of access

            init: function (_consentModels, logger) {
                this.logger = logger || __logger;

                this.logger.info("initializing  ConsentManager.net facade adapter");

                if (typeof _consentModels === 'undefined' || typeof _consentModels.forEach !== 'function') {
                    this.logger.warn("No consent models supplied to ConsentManager.net facade adapter");
                    return;
                }

                this.loadPromise = new Promise(function(resolve){ this.markLoaded = resolve}.bind(this));
                this.pendingModels = _consentModels.length;

                _consentModels.forEach(this.registerConsentModel.bind(this));
            },
            registerConsentModel : function (consentModel) {
                if (typeof consentModel.init !== 'function') {
                    this.logger.error("Unable to register consent model as does not supply the required interface", consentModel);
                }

                consentModel.init().then(this.markModelLoaded.bind(this));
                this.consentModels.push(consentModel);
            },
            markModelLoaded : function(consentModel) {
                if (this.activeModel !== null) {
                    this.logger.warn(
                        "CMnet adapter already selected, refraning from loading secondary adapter",
                        {"active": this.activeModel, "new" : consentModel}
                    );

                    return;
                }

                if (!consentModel || typeof consentModel.needsConsent !== "function") {
                    this.logger.error("Attempting to mark an undefined model as loaded", consentModel);
                    return;
                }

                if (consentModel.needsConsent() === true) {
                    this.logger.info("Marking consent model as active", consentModel);
                    this.activeModel = consentModel;
                    this.pendingModels = 0;
                    this.markLoaded();
                    return;
                }

                this.pendingModels--;

                if (this.pendingModels <= 0) {
                    // if no models apply, we don't need consent.
                    this.defaultConsent = true;
                    this.__consentsRetrieved = true;
                    this.markLoaded();
                }
            },
            /* facade methods */
            loadPreExistingConsent: function () {
                return (this.activeModel === null) ? false : this.activeModel.loadPreExistingConsent();
            },
            checksCountry: function () {
                return (this.activeModel === null) ?  true : this.activeModel.checksCountry();
            },
            consentsRetrieved: function () {
                return (this.activeModel === null) ? this.__consentsRetrieved : this.activeModel.consentsRetrieved();
            },
            retrieveConsents: function (callback, cancelRetrievalTimeout) {
                if (typeof cancelRetrievalTimeout !== 'function') {
                    cancelRetrievalTimeout = function () {};
                }

                this.loadPromise.then(function() {
                    cancelRetrievalTimeout(); // ensure immediate cancellation

                    if (this.activeModel === null) {
                        __logger.info("CMNet adapter loaded, no consent model applies");
                        return callback();
                    }

                    __logger.info("CMNet adapter loaded, retrieving consent from model", this.activeModel);
                    return this.activeModel.retrieveConsents(callback);
                }.bind(this));
            },

            refreshConsents: function (callback) {
                if (this.activeModel !== null) { 
                    return this.activeModel.refreshConsents(callback);
                }
            },
            needsConsent: function () {
                return (this.activeModel === null) ? this.defaultConsent : this.activeModel.needsConsent();
            },
            getConsentForPurpose: function (purpose, defaultConsent) {
                if (this.consentsRetrieved() && this.activeModel !== null) {
                    return this.activeModel.getConsentForPurpose(purpose, defaultConsent);
                }

                return defaultConsent;
            },
            getConsentForVendor: function (vendorId, defaultConsent) {
                if (this.consentsRetrieved() && this.activeModel !== null) {
                    return this.activeModel.getConsentForVendor(vendorId, defaultConsent);
                }
                
                return defaultConsent;
            },
            getConsentForPublisher: function (purpose, defaultConsent) {
                if (this.consentsRetrieved() && this.activeModel !== null) {
                    return this.activeModel.getConsentForPublisher(purpose, defaultConsent);
                }
                
                return defaultConsent;
            },
            manageConsents: function (callback, modelName) {
                if (modelName === "gdpr") {
                    gdprAdapter.manageConsents(callback);
                    return;
                } else if (modelName == "ccpa") {
                    ccpaAdapter.manageConsents(callback);
                    return;
                }

                __logger.info("No active consent model, no known model specified to open.");

            }
            /* end facade methods */
        };


        var gdprAdapter = (function() {
            return {
            consentStatus: false, // true means consents have been retrieved
            loadedPromise: null,
            userRequiresConsent: null,
            purposeConsents: {},
            vendorConsents: {},
            publisherConsents: {},
            init: function () {

                var consentsComplete;
                var completedPromise = new Promise(function(resolve, reject) { consentsComplete = resolve;})
                    .then(function() { return this;}.bind(this) );

                this.loadedPromise = new Promise(function(resolve, reject){
                        this.startLoadWatcher(resolve);
                    }.bind(this)
                ).then(function() {
                    // this will fire after the load watcher completes
                    this.checkIfAdapterApplies(function() { 
                        __logger.info("Initial GDPR load complete");
                        consentsComplete();
                    });
                }.bind(this));


                return completedPromise;
            },
            startLoadWatcher: function(resolveLoadPromise) {
                // this anon function handles the __tcfapi status check.  Usually will be not loaded
                var pingHandler = function(results, success) {
                    if (results.cmpLoaded === false || !cmpmngrLoaded()) {
                        // retry as the 'init' event will not work as expected
                        setTimeout(ping, 10);
                        return;
                    }
                    __logger.info("GDPR adapter loaded");

                    if (typeof resolveLoadPromise === "function") {
                        resolveLoadPromise();
                    }
                }.bind(this);

                var ping = function() {
                    window.__tcfapi('ping', 2, pingHandler);
                }.bind(this);

                // start the process
                ping();
            },
            loadPreExistingConsent: function () {
                return false;
            },
            checksCountry: function () {
                return true;
            },
            consentsRetrieved: function () {
                return this.consentStatus;
            },
            checkIfAdapterApplies : function (completionCallback) {
                __logger.info("Checking GDPR applicability");
                window.__tcfapi('getTCData', 2, function() {
                    __logger.info("Checking if GDPR applies");

                    this.userRequiresConsent = (window.cmpmngr && window.cmpmngr.getRegulation && window.cmpmngr.getRegulation() === 1);

                    if (this.userRequiresConsent) {
                        __logger.info("GDPR applies");
                    } else {
                        // setting default gdpr consent to true as it doesn't apply (edge case)
                        _adapterConfig.defaultGdprConsent = true;
                        __logger.info("GDPR does not apply");
                    }

                    completionCallback();
                }.bind(this), false);
            },
            retrieveConsents: function (callback, cancelRetrievalTimeout) {
                if (typeof cancelRetrievalTimeout !== 'function') {
                    cancelRetrievalTimeout = function () {
                    };
                }

                var checkAndRetrieve = function() {

                    cancelRetrievalTimeout();
                    if (cmpmngr.isLayerShown) {
                        // consent layer open, wait for selection
                        __logger.info("GDPR consent layer open, registering listener");
                        __tcfapi('addEventListener', 2, function(tcData, success) {
                            if (window.cmpmngr.isLayerShown && tcData.eventStatus !== "useractioncomplete") {
                                // window still open don't do anything
                                return;
                            }

                            __logger.info("GDPR consent layer closed, notifying callback");
                            this.consentStatus = true;
                            this.refreshConsents(callback);
                            if (tcData.listenerId != undefined && tcData.listenerId != null) { 
                                // prevent from firing again
                                __tcfapi('removeEventListener', 2, () => __logger.info("removed GDPR consent layer listener", tcData));
                            }
                        }.bind(this));
                        return;
                    }

                    __logger.info("GDPR consent layer closed");
                    this.consentStatus = true;
                    
                    callback();
                }.bind(this);

                this.loadedPromise.then(function() {
                    var delay = _adapterConfig.bannerCheckDelay || 100;

                    if (Object.keys(this.vendorConsents).length == 0) {
                        __logger.info('Delaying consent refresh to give dialog a chance to open');
                        // empty consents may imply the cmp needs to show the screen.  Delay once to give it a chance
                        setTimeout(checkAndRetrieve, delay);    
                        return;
                    } 
                    
                    // no need to delay
                    checkAndRetrieve();
                }.bind(this));
            },
            refreshConsents: function (callback) {
                // No need to refresh, tcf v2 is easier just passing through
                callback();
            },
            needsConsent: function () {
                return this.userRequiresConsent;
            },
            getConsentForPurpose: function (purpose, defaultConsent) {
                if (!this.consentsRetrieved()) {
                    return defaultConsent;
                }

                var results = __tcfapi('getTCData', 2, null, false);
               
                if (results.purpose === undefined && results.purpose.consents === undefined) {
                    return _adapterConfig.defaultGdprConsent;
                }
                
                return (results.purpose.consents[purpose] !== undefined) ? results.purpose.consents[purpose] : _adapterConfig.defaultGdprConsent;
            },
            getConsentForVendor: function (vendorId, defaultConsent) {
                if (!this.consentsRetrieved()) {
                    return defaultConsent;
                }

                var results = __tcfapi('getTCData', 2, null, false);

                if (results.vendor.consents.hasOwnProperty(vendorId)) {
                    // TCF signitory vendors
                    return results.vendor.consents[vendorId];
                }

                if (results.customVendorConsents.hasOwnProperty(vendorId)) {
                    // Custom vendors
                    return results.customVendorConsents[vendorId];
                }    

                // vendor not found, returning default
                return _adapterConfig.defaultGdprConsent;
            },
            getConsentForPublisher: function (purpose, defaultConsent) {
                if (!this.consentsRetrieved()) {
                    return defaultConsent;
                }

                return (this.publisherConsents.hasOwnProperty(purpose)) ? this.publisherConsents[purpose] : _adapterConfig.defaultGdprConsent;
            },
            manageConsents: function (callback) {
                __logger.info("Displaying GDPR Consent Management screen");

                if (window.cmpmngr.cnf.regulation == 1) {
                    window.__cmp('showScreen');
                } else {
                    window.__cmp('showScreenAdvanced');
                }
            }
        };
        })();


        var ccpaAdapter = (function() {
            return {
            consentStatus: false, // true means consents have been retrieved
            loadedPromise: null,
            userRequiresConsent: null,
            userGivesConsent: null,
            purposeConsents: {},
            vendorConsents: {},
            publisherConsents: {},
            settings: {
                usConsentDoesNotApply: '1---',
                revokedPos: 2 // position in string that says the user has revoked consent
            },
            init: function () {
                var consentsComplete;
                var completedPromise = new Promise(function(resolve, reject) { consentsComplete = resolve;})
                    .then(function() { return this;}.bind(this) );

                this.loadedPromise = new Promise(function(resolve, reject){
                        this.startLoadWatcher(resolve);
                    }.bind(this)
                ).then(function() {
                    this.refreshConsents(function() {
                        consentsComplete();
                    });
                
                    }.bind(this)
                );

                return completedPromise;
            },
            startLoadWatcher: function(callback) {
                if (typeof __uspapi === "undefined") {
                    // Create uspapi object so our ping check works.
                    __uspapi = function(action,b, stubCB, d) {
                        if (action === "ping") {
                            stubCB({'cmpLoaded' : false});
                        }
                    };
                }

                // this anon function handles the __uspapi status check.  Usually will be not loaded
                var pingHandler = function(results, success) {
                    if (cmpmngrLoaded()) {
                        __logger.info("CCPA adapter loaded");
                        this.consentStatus = true;
                        if(typeof callback === "function") {
                            callback();
                        }

                        return;
                    }

                    // retry as the 'init' event will not work as expected
                    setTimeout(ping, 10);
                }.bind(this);

                var ping = function() {
                    window.__uspapi('ping', null, pingHandler);
                }.bind(this);

                // start the process
                ping();
            },
            loadPreExistingConsent: function () {
                return false;
            },
            checksCountry: function () {
                return true;
            },
            consentsRetrieved: function () {
                return this.consentStatus;
            },
            retrieveConsents: function (callback, cancelRetrievalTimeout) {
                __logger.info("retrieving CCPA consents")
                if (typeof cancelRetrievalTimeout !== 'function') {
                    cancelRetrievalTimeout = function () {};
                }

                this.loadedPromise.then(function() {
                    cancelRetrievalTimeout();
                    this.refreshConsents(callback)
                }.bind(this));
            },
            refreshConsents: function (callback) {
                __logger.info("retrieving CCPA consents");
                var consentRefresh = function (result, success) {
                    if (success !== true) {
                        __logger.error("Unable to retrive CCPA consents!");
                        return;
                    }

                    if (!result || result.uspString === undefined || result.uspString === null) {
                        __logger.error("Unable to retrive CCPA consent string");
                        return;
                    }

                    var regulationIndex = (window.cmpmngr&& window.cmpmngr.getRegulation) ? window.cmpmngr.getRegulation() : false;
                    
                    if (regulationIndex === 2) {
                        __logger.info("CCPA applies");
                        this.userRequiresConsent = true;
                        this.userGivesConsent = (result.uspString[this.settings.revokedPos] === "N");
                    } else {
                        this.userRequiresConsent = false;
                        __logger.info("CCPA does not apply");
                    }

                    callback();
                }.bind(this);

                window.__uspapi('getUSPData', null, consentRefresh.bind(this), true);

            },
            needsConsent: function () {
                return this.userRequiresConsent;
            },
            userHasGivenConsent: function() {
                return (this.userGivesConsent === null) ? _adapterConfig.defaultCcpaConsent : this.userGivesConsent;
            },
            getConsentForPurpose: function (purpose, defaultConsent) {
                if (!this.consentsRetrieved()) {
                    return defaultConsent;
                }

                if (isGdprPurpose(purpose)) {
                    return true;
                }

                return this.needsConsent()? this.userHasGivenConsent() : true;
            },
            getConsentForVendor: function (vendorId, defaultConsent) {
                if (!this.consentsRetrieved()) {
                    return defaultConsent;
                }

                return this.vendorNeedsConsent(vendorId) ? this.userHasGivenConsent() : true;
            },
            getConsentForPublisher: function (purpose, defaultConsent) {
                if (gdprPurpose(purpose)) {
                    return true;
                }

                return this.userHasGivenConsent(defaultConsent);
            },

            vendorNeedsConsent: function(vendorId) {
                if (_adapterConfig.ccpaVendors && _adapterConfig.ccpaVendors[vendorId]) {
                    return true;                    
                }

                return false;
            },
            manageConsents: function (callback) {
                __logger.info("Displaying CCPA consent management screen");
       
                // hackaround while waiting on cmnet fix
                window.cmpmngr.cnf.regulation = 2;
                __cmp('showScreenAdvanced');
            }
        };
        })();

        
        // Bring the wrapper online, with both consent model adapaters 
        Adapter.init([gdprAdapter, ccpaAdapter], __logger);

        return Adapter;
    })(_consentAdapterConfig);

</script>

<script>
    var ConsentManager = window.ConsentManager || {};
    var consentParams = {"adapterName":"consentManagerNet","defaultConsent":true,"usePurposeMap":true,"allowConsentTimeout":true,"consentCheckDelay":1500,"purposeMap":{"storage":1,"personalization":2,"ad_selection":3,"content_selection":4,"measurement":5,"ccpa--sells_data":-1},"prebidConfig":{"cmpApi":"iab","timeout":8000,"allowAuctionWithoutConsent":true},"requiredCountries":{"BE":"Belgium","BG":"Bulgaria","CZ":"Czech Republic","DK":"Denmark","DE":"Germany","EE":"Estonia","IE":"Ireland","EL":"Greece","ES":"Spain","FR":"France","HR":"Croatia","IT":"Italy","CY":"Cyprus","LV":"Latvia","LT":"Lithuania","LU":"Luxembourg","HU":"Hungary","MT":"Malta","NL":"Netherlands","AT":"Austria","PL":"Poland","PT":"Portugal","RO":"Romania","SI":"Slovenia","SK":"Slovakia","FI":"Finland","SE":"Sweden","UK":"United Kingdom","be":"Belgium","bg":"Bulgaria","cz":"Czech Republic","dk":"Denmark","de":"Germany","ee":"Estonia","ie":"Ireland","el":"Greece","es":"Spain","fr":"France","hr":"Croatia","it":"Italy","cy":"Cyprus","lv":"Latvia","lt":"Lithuania","lu":"Luxembourg","hu":"Hungary","mt":"Malta","nl":"Netherlands","at":"Austria","pl":"Poland","pt":"Portugal","ro":"Romania","si":"Slovenia","sk":"Slovakia","fi":"Finland","se":"Sweden","uk":"United Kingdom"},"countryCodeHeader":"http_cf_ipcountry","countryCheckUri":"\/country-code"} 
    window.dataLayer = window.dataLayer || [];

    if (typeof window.isGdprPurpose !== 'function') {
        window.isGdprPurpose = function(purpose) {
            // this is a sorta fragile check.  If purposes expand beyond gdpr
            // it will need to be expanded.
            return (purpose >= 0);
        };
    }

    (function (_consentSettings, _adapter, gtagDataLayer) {
        var consentFlowComplete;

        ConsentManager = {
            settings : {
                debugQueryString: 'amgconsentdebug',
                defaultConsent : false,
                defaultPrebidConfig: {
                    cmpApi: 'iab',
                    timeout: 8000,
                    allowAuctionWithoutConsent: false
                },
                allowConsentTimeout: false,  // if false, consentCheckDelay no longer applies
                consentCheckDelay : 500,
                requiredCountries: [],
                countryCodeHeader: '',
                consentEventName: "AMGConsentsRetrieved",  //really shouldn't mess with this one
                consentManagementClass: "amgmanageconsent",
                consentManagementModelAttribute: "data-consent-model"
            },
            initDone: false,
            logger: LogBuilder('AMG_CONSENT -- ', false),

            // START PUBLIC INTERFACE METHODS
            registerVendorHandler: function(vendorId, consentMethod, nonConsentMethod, label) {
                this.checkVendorConsent(vendorId)

                this.logger.info("Registering vendor consent handler for vendor:\n" + vendorId + " -- " + label);
                this.registerHandlerSet(vendorId, consentMethod, nonConsentMethod, label + "-- vendor handler", this.checkVendorConsent.bind(this));
            },
            registerPurposeHandler: function(purposes, consentMethod, nonConsentMethod, label) {
                if (typeof label == 'undefined') {
                    label = '';
                }

                this.logger.info("Registering purpose handler:\n" + label, purposes);
                this.registerHandlerSet(purposes, consentMethod, nonConsentMethod, label + "-- purpose handler", this.checkPurposeConsent.bind(this));
            },
            registerPublisherHandler: function(purposes, consentMethod, nonConsentMethod, label) {
                if (typeof label === 'undefined') {
                    label = '';
                }

                this.logger.info("Registering publisher purpose handler:\n" + label, purposes);
                this.registerHandlerSet(purposes, consentMethod, nonConsentMethod, label + "-- publisher handler", this.checkPublisherConsent.bind(this));
            },
            registerHandlerSet: function(criteria, consentMethod, nonConsentMethod, label, checkMethod) {
                if (typeof consentMethod !== 'function') {
                    this.logger.error(
                        'Unable to register consent handler, incorrect types given',
                        {"critera": critera, "handler": consentMethod, "nonConsentMethod" : nonConsentMethod, "label": label}
                    );
                }

                this.registerHandler(function() {
                    if (checkMethod(criteria)) {
                        this.logger.info("Calling consent handler:\n" + label, criteria);
                        consentMethod();
                        return;
                    }

                    if (typeof nonConsentMethod === "function") {
                        this.logger.info("Calling nonconsent handle:\n" + label, criteria);
                        nonConsentMethod();
                    } else {
                        this.logger.info("Not calling handler as consent is not given:\n" + label, criteria);
                    }
                }.bind(this));
            },
            registerHandler: function(handlerMethod) {
                // register the handler for ongoing use
                window.addEventListener(this.getRetrievedEventName(), handlerMethod);

                // if the consents have already been retrived, call the handler immediately
                if (this.consentsRetrieved() || this.useConsentDefault === true) {
                    this.logger.info("Handler registered after consents have already been retrieved, calling handler immediately");
                    handlerMethod();
                }
            },
            consentsRetrieved: function() {
                return this.adapter.consentsRetrieved();
            },
            checkPurposeConsent: function (purposes) {
                if (this.useConsentDefault === true) {
                    return this.getDefaultConsent();
                }

                if (!this.consentsRetrieved()) {
                    return null;
                }

                if (!Array.isArray(purposes)) {
                    // no point in looping over a single item.
                    return this.checkSinglePurposeConsent(purposes);
                }

                for (var purpose = 0; purpose < purposes.length; purpose++) {
                    if (this.checkSinglePurposeConsent(purposes[purpose]) !== true) {
                        this.logger.warn("No consent for purpose, bailing:\n" + purposes[purpose]);
                        return false;
                    }
                }

                return true;
            },
            checkSinglePurposeConsent: function(purpose) {
                var purpose = this.mapPurpose(purpose);
                if (purpose === false) {
                    return this.getDefaultConsent();
                }

                if (!this.consentsRetrieved()) {
                    this.logger.info("Unable to determine consent as consent data has not been retrieved");
                    // we don't know yet
                    return null;
                }

                return this.adapter.getConsentForPurpose(purpose, this.getDefaultConsent());
            },

            checkPublisherConsent: function (purposes) {
                if (this.useConsentDefault === true) {
                    return this.getDefaultConsent();
                }

                if (!this.consentsRetrieved()) {
                    return null;
                }

                if (!Array.isArray(purposes)) {
                    // no point in looping over a single item.
                    return this.checkSinglePublisherConsent(purposes);
                }

                for (var purpose = 0; purpose < purposes.length; purpose++) {
                    if (this.checkSinglePublisherConsent(purposes[purpose]) !== true) {
                        this.logger.warn("No consent for publisher purpose, bailing:\n" + purposes[purpose]);
                        return false;
                    }
                }

                return true;
            },
            checkSinglePublisherConsent: function(purpose) {
                var purpose = this.mapPurpose(purpose);
                if (purpose === false) {
                    return this.getDefaultConsent();
                }

                if (!this.consentsRetrieved()) {
                    this.logger.info("Unable to determine publisher consent as consent data has not been retrieved");
                    // we don't know yet
                    return null;
                }

                return this.adapter.getConsentForPublisher(purpose, this.getDefaultConsent());
            },

            mapPurpose: function(purpose) {
                if (!this.settings.usePurposeMap) {
                    return purpose;
                }

                if (!this.settings.purposeMap.hasOwnProperty(purpose)) {
                    this.logger.error("Cannot find specified purpose in the purpose map",
                        {"purposeMap" : this.settings.purposeMap, "purpose": purpose}
                    );
                    return false;
                }

                return this.settings.purposeMap[purpose];
            },

            checkVendorConsent: function (vendorId) {
                if (this.useConsentDefault === true) {
                    this.logger.info("Using default consent for vendor id:\n" + vendorId);
                    return this.getDefaultConsent();
                }

                if (this.consentsRetrieved()) {
                    this.logger.info("Checking consent for vendor:\n" +  vendorId);
                    return this.adapter.getConsentForVendor(vendorId, this.getDefaultConsent());
                }

                return null;
            },
            // This is the event that will be sent out on the window object when consents are retrieved
            getRetrievedEventName: function() {
                return this.settings.consentEventName;
            },
            gdprApplies: function() {
                return this.adapter.needsConsent();
            },
            setDebug: function(enable) {
                if (enable !== true && !this.logger.queryStringExists(this.settings.debugQueryString)) {
                    return;
                }

                this.logger.enable();

                if (this.Adapter && this.Adapter.logger) {
                    this.logger.enable();
                }
            },
            // END PUBLIC INTERFACE METHODS

            init: function () {
                if (this.initDone === true) {
                    return;
                }

                this.setDebug();
                this.setManagerParams(_consentSettings);
                this.setAdapter(_adapter);
                this.hookManageConsent();

                this.initConsentFlow();

                this.initDone = true;
            },
            // @todo I really really want to refactor this into a settings obj
            setManagerParams: function (managerParams) {
                this.logger.table("Setting Consent Manager params", managerParams);
                for (var paramName in managerParams) {
                    if (managerParams.hasOwnProperty(paramName)) {
                        this.settings[paramName] = managerParams[paramName];
                    }
                }

                return this;
            },
            // @todo I think it'd be good to have some ducktyping in here for the adapter
            setAdapter: function(_adapter) {
                this.adapter = _adapter;

                if (this.logger.debugOn && _adapter.logger) {
                    _adapter.logger.enable();
                }

                return this;
            },
            initConsentFlow: function() {
                this.logger.info('Starting consent check flow');
                if (this.adapter.loadPreExistingConsent()) {
                    this.logger.info('Consent Manager detected pre-existing consent information');
                    // Sending event just in case something else loaded prior.  Shouldn't happen, but...
                    this.sendConsentRetrievedEvent();
                    return;
                }

                this.logger.info('No pre-existing consent information detected, checking consent');
                this.retrieveConsents();
            },

            retrieveConsents: function() {
                this.logger.info(
                    "Instructing adapter to retrieve consents, no notification of user managment available"
                );


                if (!this.settings.allowConsentTimeout) {
                    this.logger.info("Consent retrieval with no timeout");
                    this.adapter.retrieveConsents(this.notifyConsentsRetrieved.bind(this));

                    return;
                }

                var retrievalTimer;
                var timerCanceled = false;

                // This is called if the adapter can notify when users are doing inital consent management.
                var cancelRetrievalTimeout = function() {
                    this.logger.info("Adapter is in user consent management flow, canceling consent retrieval timeout");
                    timerCanceled = true;
                    clearTimeout(retrievalTimer);
                }.bind(this);

                this.logger.info("Consent retrieval with timeout");
                this.adapter.retrieveConsents(
                    this.notifyConsentsRetrieved.bind(this),
                    cancelRetrievalTimeout
                );

                // setting timeout first in case the adapter is blocking or has an error
                retrievalTimer = setTimeout(function() {
                    if (timerCanceled) {
                        return; // early exit due to backup cancelation
                    }                    
                    this.logger.info("Consent retrieval timed out, setting defaults");
                    
                    this.markConsentDefault();
                    this.sendConsentRetrievedEvent();
                    
                    var timeoutLength = this.settings.consentCheckDelay;
                    var errorEvent = function() {
                        if (window.parade.contribEventReporter  && window.parade.contribEventReporter.sendCmpTimeoutEvent) {
                            window.parade.contribEventReporter.sendCmpTimeoutEvent(timeoutLength);
                            return;
                        }

                        setTimeout(errorEvent, timeoutLength);
                    };

                    errorEvent();
                }.bind(this), this.settings.consentCheckDelay);
            },
            manageConsents: function(e) {
                if (e && typeof e.preventDefault === "function") {
                    e.preventDefault();
                }

                this.logger.info("Instructing adapter to get user modification of consents");
                // no timeout on this one, as it is expected to take a long time.
                this.adapter.manageConsents(this.notifyConsentsRetrieved.bind(this), e.srcElement.getAttribute(this.settings.consentManagementModelAttribute));

                return false;
            },
            hookManageConsent: function() {
                document.addEventListener('DOMContentLoaded', function() {
                    var elements = document.getElementsByClassName(this.settings.consentManagementClass);
                    if (elements.length == 0) {
                        this.logger.warn("No elements matching the consent management selector were found: " + this.settings.consentManagementClass);
                        return;
                    }

                    for (var element in elements) {
                        if (typeof elements[element].addEventListener === "function") {
                            this.logger.info("Binding object click event to 'manageConsents()'", elements[element]);
                            elements[element].addEventListener("click", this.manageConsents.bind(this));
                        }
                    }
                }.bind(this));
            },
            notifyConsentsRetrieved: function() {
                this.logger.info("Consent Provider has retrieved or updated consents");

                if (this.adapter.needsConsent() === false) {
                    this.logger.info("Adapter specifies that we don't need consent");
                    this.markConsentDefault(true);
                    this.sendConsentRetrievedEvent();
                    return;
                }

                if (this.useConsentDefault === true) {
                    this.logger.info(
                        "Default Consents were previously being used, clearing to use specific consents."
                    );

                    this.useConsentDefault = false;
                }

                gtagDataLayer.push({"event":"ConsentFinished"});
                this.sendConsentRetrievedEvent();
            },
            sendConsentRetrievedEvent: function() {
                this.logger.info("Sending consent retrieved event");
                var consentEvent = new Event(this.getRetrievedEventName());
                window.dispatchEvent(consentEvent);
            },
            getDefaultConsent: function() {
                return this.settings.defaultConsent;
            },
            markConsentDefault: function(newDefaultConsent) {
                this.logger.info("Marking that manager should use it's default consent value", {"defaultConsent" : this.settings.defaultConsent});
                this.useConsentDefault = true;

                if (typeof newDefaultConsent !== "undefined") {
                    this.logger.info("New default consent value supplied", newDefaultConsent);
                    this.settings.defaultConsent = (newDefaultConsent);
                }

                return this;
            },
            getPrebidConfig: function() {
                if (this.adapter.needsConsent() === false) {
                    // if we don't need consent, allow without it
                    this.settings.prebidConfig.allowAuctionWithoutConsent = true;
                }

                return this.settings.prebidConfig;
            },
        };

        ConsentManager.init();
    })(consentParams, window.ConsentAdapter, window.dataLayer);
</script>

<script data-cfasync="false" data-pagespeed-no-defer>//<![CDATA[
	var gtm4wp_datalayer_name = "dataLayer";
	var dataLayer = dataLayer || [];
//]]>
</script>
<link rel='dns-prefetch' href='//s.w.org' />

<script data-cfasync="false" data-pagespeed-no-defer>//<![CDATA[
	var dataLayer_content = {"pagePostType":"post","pagePostType2":"single-post","pageCategory":["entertainment"],"pageAttributes":["cheesy-pick-up-lines","funny-pick-up-lines","pick-up-lines"],"pagePostAuthor":"Maryn Liles"};
	dataLayer.push( dataLayer_content );//]]>
</script>
<script data-cfasync="false">//<![CDATA[
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'//www.googletagmanager.com/gtm.'+'js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-NQNX3LZ');//]]>
</script>

 <script type="text/javascript">
			window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/12.0.0-1\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/12.0.0-1\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/parade.com\/wp-includes\/js\/wp-emoji-release.min.js"}};
			/*! This file is auto-generated */
			!function(e,a,t){var r,n,o,i,p=a.createElement("canvas"),s=p.getContext&&p.getContext("2d");function c(e,t){var a=String.fromCharCode;s.clearRect(0,0,p.width,p.height),s.fillText(a.apply(this,e),0,0);var r=p.toDataURL();return s.clearRect(0,0,p.width,p.height),s.fillText(a.apply(this,t),0,0),r===p.toDataURL()}function l(e){if(!s||!s.fillText)return!1;switch(s.textBaseline="top",s.font="600 32px Arial",e){case"flag":return!c([127987,65039,8205,9895,65039],[127987,65039,8203,9895,65039])&&(!c([55356,56826,55356,56819],[55356,56826,8203,55356,56819])&&!c([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]));case"emoji":return!c([55357,56424,55356,57342,8205,55358,56605,8205,55357,56424,55356,57340],[55357,56424,55356,57342,8203,55358,56605,8203,55357,56424,55356,57340])}return!1}function d(e){var t=a.createElement("script");t.src=e,t.defer=t.type="text/javascript",a.getElementsByTagName("head")[0].appendChild(t)}for(i=Array("flag","emoji"),t.supports={everything:!0,everythingExceptFlag:!0},o=0;o<i.length;o++)t.supports[i[o]]=l(i[o]),t.supports.everything=t.supports.everything&&t.supports[i[o]],"flag"!==i[o]&&(t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&t.supports[i[o]]);t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&!t.supports.flag,t.DOMReady=!1,t.readyCallback=function(){t.DOMReady=!0},t.supports.everything||(n=function(){t.readyCallback()},a.addEventListener?(a.addEventListener("DOMContentLoaded",n,!1),e.addEventListener("load",n,!1)):(e.attachEvent("onload",n),a.attachEvent("onreadystatechange",function(){"complete"===a.readyState&&t.readyCallback()})),(r=t.source||{}).concatemoji?d(r.concatemoji):r.wpemoji&&r.twemoji&&(d(r.twemoji),d(r.wpemoji)))}(window,document,window._wpemojiSettings);
		</script>
<style type="text/css">
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 .07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
<link rel='stylesheet' id='wp-block-library-css' href='https://parade.com/wp-includes/css/dist/block-library/style.min.css' type='text/css' media='all' />
<link rel='stylesheet' id='rate-my-post-css' href='https://parade.com/wp-content/plugins/rate-my-post/public/css/rate-my-post.css' type='text/css' media='all' />
<link rel='stylesheet' id='easyazonpro-popovers-css' href='https://parade.com/wp-content/plugins/easyazon-pro/components/popovers/resources/popovers.css' type='text/css' media='all' />
<script type='text/javascript' src='//ajax.googleapis.com/ajax/libs/jquery/1.12.4-wp/jquery.min.js'></script>
<link rel='https://api.w.org/' href='https://parade.com/wp-json/' />
<link rel='shortlink' href='https://bit.ly/3g5YKYs' />
<link rel="alternate" type="application/json+oembed" href="https://parade.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fparade.com%2F1039985%2Fmarynliles%2Fpick-up-lines%2F" />
<link rel="alternate" type="text/xml+oembed" href="https://parade.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fparade.com%2F1039985%2Fmarynliles%2Fpick-up-lines%2F&#038;format=xml" />
<script type="text/javascript">
(function(doc) {
    window.cnxps = window.cnxps || {cmd: []};
    window.cnx = window.cnx || {cmd: []};
    const outstreamVideoListener = function (e) {
        const { disableThirdPartyAds, disabledOutstreamVideo } = e.detail;
        if (disableThirdPartyAds) {
            return;
        }
        // Include the Elements script when outstream video is disabled
        // On future iteration, have a disable setting for Elements specifically
        !function(n){if(!window.cnxflag){window.cnxflag = true;var t=n.createElement('iframe');t.style.display='none',t.onload=function(){var n=t.contentWindow.document,c=n.createElement('script');c.src='//cd.connatix.com/connatix.player.js',c.setAttribute('async','1'),c.setAttribute('type','text/javascript'),n.body.appendChild(c)},n.head.appendChild(t)}}(document);
        if (disabledOutstreamVideo) {
            return;
        }
        !function (n) { if (!window.cnxpsFlag) { window.cnxpsFlag = true; var t = n.createElement('iframe'); t.style.display = 'none', t.onload = function () { var n = t.contentWindow.document, c = n.createElement('script'); c.src = '//cd.connatix.com/connatix.playspace.js', c.setAttribute('async', '1'), c.setAttribute('type', 'text/javascript'), n.body.appendChild(c) }, n.head.appendChild(t) } }(document);
    }
    doc.addEventListener('outstreamVideoConsent', outstreamVideoListener);
})(document);
</script>

<script>
    var pbjs = pbjs || {};
    pbjs.que = pbjs.que || [];

    var googletag = googletag || {};
    googletag.cmd = googletag.cmd || [];
    googletag.cmd.push(function () {
        googletag.pubads().disableInitialLoad();
    });

</script>

<script type="text/javascript">
    window.parade = window.parade || {};
    window.parade.adSettings = {
        slots : {"728_top":{"slotId":"div-gpt-ad-728-top-0","defineSlot":{"slotName":"728_top","slotId":"div-gpt-ad-728-top-0","localTargets":{"pos":"728","loc":"top"},"outOfPage":false},"html":"<div class=\"ad-wrapper\">\n    <div id='div-gpt-ad-728-top-0' class=\"ad-728-top\">\n        <script type='text\/javascript'>\n            window.AdManager.displaySlot(\"728_top\", \"div-gpt-ad-728-top-0\");\n        <\/script>\n    <\/div>\n<\/div>\n"},"728_bottom":{"slotId":"div-gpt-ad-728-bottom-1","defineSlot":{"slotName":"728_bottom","slotId":"div-gpt-ad-728-bottom-1","localTargets":{"pos":"728","loc":"bottom"},"outOfPage":false},"html":"<div class=\"ad-wrapper\">\n    <div id='div-gpt-ad-728-bottom-1' class=\"ad-728-bottom\">\n        <script type='text\/javascript'>\n            window.AdManager.displaySlot(\"728_bottom\", \"div-gpt-ad-728-bottom-1\");\n        <\/script>\n    <\/div>\n<\/div>\n"},"300_top":{"slotId":"div-gpt-ad-300-top-2","defineSlot":{"slotName":"300_top","slotId":"div-gpt-ad-300-top-2","localTargets":{"pos":"300","loc":"top"},"outOfPage":false},"html":"<div class=\"ad-wrapper\">\n    <div id='div-gpt-ad-300-top-2' class=\"ad-300-top\">\n        <script type='text\/javascript'>\n            window.AdManager.displaySlot(\"300_top\", \"div-gpt-ad-300-top-2\");\n        <\/script>\n    <\/div>\n<\/div>\n"},"300_bottom":{"slotId":"div-gpt-ad-300-bottom-3","defineSlot":{"slotName":"300_bottom","slotId":"div-gpt-ad-300-bottom-3","localTargets":{"pos":"300","loc":"bottom"},"outOfPage":false},"html":"<div class=\"ad-wrapper\">\n    <div id='div-gpt-ad-300-bottom-3' class=\"ad-300-bottom\">\n        <script type='text\/javascript'>\n            window.AdManager.displaySlot(\"300_bottom\", \"div-gpt-ad-300-bottom-3\");\n        <\/script>\n    <\/div>\n<\/div>\n"},"300_content":{"slotId":"div-gpt-ad-300-content-4","defineSlot":{"slotName":"300_content","slotId":"div-gpt-ad-300-content-4","localTargets":{"pos":"300","loc":"content"},"outOfPage":false},"html":"<div class=\"ad-wrapper\">\n    <div id='div-gpt-ad-300-content-4' class=\"ad-300-content\">\n        <script type='text\/javascript'>\n            window.AdManager.displaySlot(\"300_content\", \"div-gpt-ad-300-content-4\");\n        <\/script>\n    <\/div>\n<\/div>\n"},"ditto_background":{"slotId":"div-gpt-ad-ditto-background-5","defineSlot":{"slotName":"ditto_background","slotId":"div-gpt-ad-ditto-background-5","localTargets":{"pos":"ditto","loc":"background"},"outOfPage":true},"html":"<div class=\"ad-wrapper\">\n    <div id='div-gpt-ad-ditto-background-5' class=\"ad-ditto-background\">\n        <script type='text\/javascript'>\n            window.AdManager.displaySlot(\"ditto_background\", \"div-gpt-ad-ditto-background-5\");\n        <\/script>\n    <\/div>\n<\/div>\n"}},
        globalTargets: {"en":"production","id":"1039985","mem":"marynliles","lo":"1","cat":"entertainment","sec":"","pa":"article","fo":"article","tags":"Cheesy Pick Up Lines,Funny Pick Up Lines,Pick Up Lines","hasRecipe":"no","package":""}    };
</script>
<script>
window.amgAds = window.amgAds || {};

window.amgAds.SlotMapper = window.amgAds.SlotMapper || (function() {
    var debugQueryString = "amgaddebug";
    var logger = LogBuilder("AMG_AD_MAPPER -- ", false);

    slotMap = {};
    nameMap = {};

    return {
        setDebug : function(enable) {
            if (enable === true || logger.queryStringExists(debugQueryString)) {
                logger.enable();
            }
        },
        addMap : function(slotName, slotId) {
            logger.info(`Adding map ${slotName} : ${slotId}`);
            slotMap[slotId] = slotName;
            nameMap[slotName] = slotId;
        },
        getSlotId : function(slot) {
            if (typeof slot.getSlotElementId !== "function") {
                logger.error("Attempting to get the slot id of a non-slot object");
                return false;
            }
            
            return slot.getSlotEvelementId();
        },
        getSlotName : function(slot) {
            slotId = (typeof slot.getSlotElementId === "function") ? slot.getSlotElementId() : slot;

            if (!slotMap[slotId]) {
                return false;
            }

            return slotMap[slotId];
        },
        getSlotId : function(slot) {
            return (typeof slot.getSlotElementId === "function") ? slot.getSlotElementId() : false;
        },
        getSlotDomElement: function(slotName) {
            if (!nameMap[slotName]) {
                return false;
            }

            return document.getElementById(nameMap[slotName]) || false;
        }
    }
})();


window.amgAds.AdSlotTracker = window.AdSlotTracker || (function(SlotMapper) {
    var hasInitialized = false;
    var pendingInitialCount = true;
    var logger = LogBuilder("AMG_AD_TRACK -- ");
    var slotMap = {};
    var trackOnce = {};
    var contribTrackedSlots = {};
    var siteTrackedSlots = {};
    var slotsLoading = false;

    // @todo make these slots dynamic

    // Slots 
    var settings = {
        'analyticsRunDelay' : 150,
        'neverTrack' : ['fset_slot'],
        'trackOnce' : [
            '728_top',
            '728_bottom',
            '300_top',
            '300_bottom',
            '300_stream',
            '300_content',
            '300_modal',
            'toolbar_background',
        ],
        'alwaysTrack' : ['728_gallery', '300_gallery', 'interstitial_gallery'],
        'debugQueryString' : "amgaddebug"
    };

    // return a new promise that delays for delayLength.  Useful in the middle of a chain
    var delayPromise = function(delayLength) {
        return new Promise((resolve) => {
            setTimeout(
                function() {
                    logger.info("Delay complete");
                    resolve();
                },
                delayLength
            );
        });
    };

    var noteTrackability = function(slotName) {
        if (trackOnce.hasOwnProperty(slotName)) {
            // no need to 
            return;
        }

        trackOnce[slotName] = true;
    }

    var countSlots = function(slotTracker) {
        var count = 0;
        
        for (var slotName in slotTracker) {
            if (slotTracker.hasOwnProperty(slotName)) {
                count++;
            }
        }

        return count;
    }
    
    // send the contrib events to ga
    var sendContribSlotCount = function () {
        var count = countSlots(contribTrackedSlots);

        logger.info("Starting contrib analytics run");

        if (count === 0) {
            logger.info("No contrib slots noted, refraining from sending ga event");
            return;
        }

        if (pendingInitialCount) {
            logger.info(`Sending initial contrib count: ${count}`);
            window.parade.contribEventReporter.queueInitialContribEvents(count);
            pendingInitialCount = false;
        } else {
            logger.info(`Sending secondary contrib count: ${count}`);
            window.parade.contribEventReporter.sendContributorEvent(count, window.document.location.pathname);
        }

        contribTrackedSlots = {}; // reset so as to not recount
    };

    var sendSiteSlotCount = function() {
        var adCount = countSlots(siteTrackedSlots);

        logger.info(`Starting site analytics run ${adCount}`);
        if (adCount) {
            // @todo move this implementation to the analytics tool
            ga('amgTracker.send', 'event', 'displayed-ads', 'total', window.document.location.pathname, adCount, {'nonInteraction': true});
            siteTrackedSlots = {};
        }
    };

    var trackSlot = function(slotName) {
        if (settings.neverTrack.includes(slotName)) {
            logger.info(`Declining to mark 'never track' slot ${slotName}`);
            return;
        }

        // non "never track" slots are always counted for the site
        siteTrackedSlots[slotName] = true;
        
        if (settings.alwaysTrack.includes(slotName)) {
            logger.info(`marking 'always track' contrib slot ${slotName}`);
            contribTrackedSlots[slotName] = true;
            return;

        }
        
        if (trackOnce.hasOwnProperty(slotName)) {
            logger.info(`marking 'track once' contrib slot ${slotName}`);
            contribTrackedSlots[slotName] = true;
            // slot is deleted from trackOnce in noteSlotLoaded()
            return;
        }

        logger.info(`not marking slot ${slotName}`);
    };

    var triggerAnalyticsRun = function() 
    {
        if (slotsLoading instanceof Promise) {
            logger.info("Not triggering analytics, run already pending");
            // already going, leave it alone
            return;
        }

        logger.info("Triggering analytics run");
        // create promise and save the resolution object 
      
        slotsLoading = delayPromise(settings.analyticsRunDelay) // buffer so all slots have a chance to load
            .then(sendContribSlotCount)
            .then(sendSiteSlotCount)
            .then(() => {
                slotsLoading = false;
                logger.info("Analytics run complete");
            });
    };

    var noteSlotLoaded = function(loadEvent) {
        // Analytics run will delay, then send out both
        triggerAnalyticsRun();
        
        // use the slot element id to walk back to the name
        var slotName = SlotMapper.getSlotName(loadEvent.slot);
        
        if (slotName === false) {
            logger.warn(`Refusing to note slot load for unknown slot with id ${SlotMapper.getSlotId(loadEvent.slot)}`, loadEvent);
            return;
        }

        if (!loadEvent.isEmpty) {
            trackSlot(slotName);
        }

        // clear trackOnce slots after first attempt to load an ad in them.
        // no need to check if it is set, delete will not error if not there.
        delete trackOnce[slotName];
    };

    // Public functions
    return {
        init : function(incomingSettings) {
            this.setDebug();

            if (hasInitialized === true) {
                logger.info("Refraining from initializing SlotTracker twice");
                return;
            }

            googletag.cmd.push(function() { googletag.pubads().addEventListener('slotRenderEnded', noteSlotLoaded);})

            logger.info("Initialzing SlotTracker");
            settings = {...settings, ...incomingSettings};
            this.allowSingleTrack(settings.trackOnce);

            hasInitialized = true;
        },
        setDebug: function(enable) {
            if (enable === true || logger.queryStringExists(settings.debugQueryString)) {
                logger.enable();
            }
        },
        allowSingleTrack(slots) {
            if (!Array.isArray(slots)) {
                // single slot
                noteTrackability(slots);
            }

            slots.forEach(noteTrackability);
        },
        manualSlotLoaded(slotName) {
            // housekeeping
            triggerAnalyticsRun();
            delete trackOnce[slotName];
            
            // force tracking regardless of settings
            siteTrackedSlots[slotName] = true;
            contribTrackedSlots[slotName] = true;
        }
    }
})(window.amgAds.SlotMapper);

window.amgAds.AdSlotTracker.init();
</script><script>
    var AdManager = window.AdManager || {};
    window.parade.adSettings.managerParams = {"prebidEnable":true,"slots":{"728_top":{"desktop":[[728,90],[970,90],[1,1]],"tablet":[[728,90]],"phone":[[300,50],[320,50]]},"728_bottom":{"desktop":[[728,90],[970,90],[970,250]],"tablet":[[728,90]],"phone":[[300,50],[320,50]]},"300_top":{"desktop":[[300,250],[300,600],[300,1050],[160,600]],"tablet":[[300,250],[300,600],[160,600]],"phone":[[320,50]]},"300_bottom":{"desktop":[[300,250],[300,600],[300,1050],[160,600]],"tablet":[[300,250],[300,50],[300,600],[160,600]],"phone":[[320,50]]},"300_content":{"desktop":[[300,250],[1,1]],"tablet":[[300,250],[320,50],[300,50],[1,1]],"phone":[[300,250],[320,50],[300,50],[1,1]]},"ditto_background":{"desktop":[],"tablet":[],"phone":[]}},"prebid":{"timeout":1400,"granularity":"auto","slots":{"desktop":[{"code":"div-gpt-ad-728-top-0","bids":[{"bidder":"sonobi","sizes":[[728,90]],"params":{"ad_unit":"\/84077725\/Parade\/entertainment\/contrib\/marynliles\/728_top"}},{"bidder":"sovrn","sizes":[[728,90]],"params":{"tagid":"414066"}},{"bidder":"sovrn","sizes":[[970,90]],"params":{"tagid":"414067"}},{"bidder":"sovrn","sizes":[[970,250]],"params":{"tagid":"414069"}},{"bidder":"appnexusAst","sizes":[[300,250]],"params":{"placementId":"10538285"}},{"bidder":"appnexusAst","sizes":[[300,250]],"params":{"placementId":"10538285"}},{"bidder":"appnexusAst","sizes":[[300,250]],"params":{"placementId":"10538285"}},{"bidder":"gumgum","sizes":[[728,90]],"params":{"inSlot":"5371"}},{"bidder":"optimera","sizes":[[728,90],[970,250],[970,90]],"params":{"clientID":"13"}}],"sizes":[[728,90],[970,90],[1,1]]},{"code":"div-gpt-ad-728-bottom-1","bids":[{"bidder":"sonobi","sizes":[[728,90]],"params":{"ad_unit":"\/84077725\/Parade\/entertainment\/contrib\/marynliles\/728_bottom"}},{"bidder":"sovrn","sizes":[[728,90]],"params":{"tagid":"414066"}},{"bidder":"appnexusAst","sizes":[[300,1050]],"params":{"placementId":"10538303"}},{"bidder":"gumgum","sizes":[[728,90]],"params":{"inSlot":"5372"}},{"bidder":"optimera","sizes":[[728,90],[970,250],[970,90]],"params":{"clientID":"13"}}],"sizes":[[728,90],[970,90],[970,250]]},{"code":"div-gpt-ad-300-top-2","bids":[{"bidder":"sonobi","sizes":[[300,250],[300,600]],"params":{"ad_unit":"\/84077725\/Parade\/entertainment\/contrib\/marynliles\/300_top"}},{"bidder":"sovrn","sizes":[[300,250]],"params":{"tagid":"414033"}},{"bidder":"appnexusAst","sizes":[[300,250]],"params":{"placementId":"10538285"}},{"bidder":"appnexusAst","sizes":[[300,600]],"params":{"placementId":"10538306"}},{"bidder":"appnexusAst","sizes":[[729,90]],"params":{"placementId":"10538312"}},{"bidder":"gumgum","sizes":[[300,250]],"params":{"inSlot":"5366"}},{"bidder":"optimera","sizes":[[300,250],[300,600],[300,1050]],"params":{"clientID":"13"}}],"sizes":[[300,250],[300,600],[300,1050],[160,600]]},{"code":"div-gpt-ad-300-bottom-3","bids":[{"bidder":"sonobi","sizes":[[300,250],[300,600]],"params":{"ad_unit":"\/84077725\/Parade\/entertainment\/contrib\/marynliles\/300_bottom"}},{"bidder":"sovrn","sizes":[[300,250]],"params":{"tagid":"414033"}},{"bidder":"appnexusAst","sizes":[[300,250]],"params":{"placementId":"10538285"}},{"bidder":"appnexusAst","sizes":[[300,600]],"params":{"placementId":"10538306"}},{"bidder":"appnexusAst","sizes":[[729,90]],"params":{"placementId":"10538312"}},{"bidder":"gumgum","sizes":[[300,250]],"params":{"inSlot":"5367"}},{"bidder":"optimera","sizes":[[300,250],[300,600],[300,1050]],"params":{"clientID":"13"}}],"sizes":[[300,250],[300,600],[300,1050],[160,600]]},{"code":"div-gpt-ad-300-content-4","bids":[{"bidder":"sonobi","sizes":[[300,250],[300,600]],"params":{"ad_unit":"\/84077725\/Parade\/entertainment\/contrib\/marynliles\/300_content"}},{"bidder":"sovrn","sizes":[[300,250]],"params":{"tagid":"414033"}},{"bidder":"appnexusAst","sizes":[[300,600]],"params":{"placementId":"10538306"}},{"bidder":"appnexusAst","sizes":[[970,90]],"params":{"placementId":"10538320"}},{"bidder":"gumgum","sizes":[[300,250]],"params":{"inSlot":"5369"}},{"bidder":"optimera","sizes":[[300,250],[300,600]],"params":{"clientID":"13"}}],"sizes":[[300,250],[1,1]]}],"phone":[{"code":"div-gpt-ad-728-top-0","bids":[{"bidder":"appnexusAst","sizes":[[300,50]],"params":{"placementId":"10538305"}},{"bidder":"appnexusAst","sizes":[[320,50]],"params":{"placementId":"10538309"}},{"bidder":"gumgum","sizes":[[320,50]],"params":{"inSlot":"5378"}},{"bidder":"optimera","sizes":[[320,50]],"params":{"clientID":"13"}}],"sizes":[[300,50],[320,50]]},{"code":"div-gpt-ad-728-bottom-1","bids":[{"bidder":"appnexusAst","sizes":[[300,50]],"params":{"placementId":"10538305"}},{"bidder":"appnexusAst","sizes":[[320,50]],"params":{"placementId":"10538309"}},{"bidder":"gumgum","sizes":[[320,50]],"params":{"inSlot":"5379"}},{"bidder":"optimera","sizes":[[320,50]],"params":{"clientID":"13"}}],"sizes":[[300,50],[320,50]]},{"code":"div-gpt-ad-300-top-2","bids":[{"bidder":"gumgum","sizes":[[300,250]],"params":{"inSlot":"5373"}}],"sizes":[[320,50]]},{"code":"div-gpt-ad-300-bottom-3","bids":[{"bidder":"sovrn","sizes":[[300,250]],"params":{"tagid":"414033"}},{"bidder":"gumgum","sizes":[[300,250]],"params":{"inSlot":"5374"}},{"bidder":"optimera","sizes":[[300,250]],"params":{"clientID":"13"}}],"sizes":[[320,50]]},{"code":"div-gpt-ad-300-content-4","bids":[{"bidder":"sonobi","sizes":[[300,250]],"params":{"ad_unit":"\/84077725\/Parade\/entertainment\/contrib\/marynliles\/300_content"}},{"bidder":"sovrn","sizes":[[300,250]],"params":{"tagid":"414033"}},{"bidder":"appnexusAst","sizes":[[300,250]],"params":{"placementId":"10538285"}},{"bidder":"gumgum","sizes":[[300,250]],"params":{"inSlot":"5376"}}],"sizes":[[300,250],[320,50],[300,50],[1,1]]}],"tablet":[{"code":"div-gpt-ad-728-top-0","bids":[{"bidder":"sonobi","sizes":[[300,250]],"params":{"ad_unit":"\/84077725\/Parade\/entertainment\/contrib\/marynliles\/300_gallery"}},{"bidder":"sovrn","sizes":[[728,90]],"params":{"tagid":"414066"}},{"bidder":"sonobi","sizes":[[728,90]],"params":{"ad_unit":"\/84077725\/Parade\/entertainment\/contrib\/marynliles\/728_gallery"}},{"bidder":"appnexusAst","sizes":[[300,600]],"params":{"placementId":"10538306"}},{"bidder":"gumgum","sizes":[[300,250]],"params":{"inSlot":"5381"}},{"bidder":"gumgum","sizes":[[728,90]],"params":{"inSlot":"5385"}},{"bidder":"optimera","sizes":[[728,90]],"params":{"clientID":"13"}}],"sizes":[[728,90]]},{"code":"div-gpt-ad-728-bottom-1","bids":[{"bidder":"appnexusAst","sizes":[[300,250]],"params":{"placementId":"10538285"}},{"bidder":"appnexusAst","sizes":[[728,90]],"params":{"placementId":"10538312"}},{"bidder":"gumgum","sizes":[[728,90]],"params":{"inSlot":"5386"}},{"bidder":"optimera","sizes":[[728,90]],"params":{"clientID":"13"}}],"sizes":[[728,90]]},{"code":"div-gpt-ad-300-top-2","bids":[{"bidder":"sovrn","sizes":[[300,250]],"params":{"tagid":"414033"}},{"bidder":"appnexusAst","sizes":[[300,250]],"params":{"placementId":"10538285"}},{"bidder":"optimera","sizes":[[300,250],[300,600]],"params":{"clientID":"13"}}],"sizes":[[300,250],[300,600],[160,600]]},{"code":"div-gpt-ad-300-bottom-3","bids":[{"bidder":"sonobi","sizes":[[300,600]],"params":{"ad_unit":"\/84077725\/Parade\/entertainment\/contrib\/marynliles\/300_top"}},{"bidder":"sovrn","sizes":[[300,250]],"params":{"tagid":"414033"}},{"bidder":"sonobi","sizes":[[728,90]],"params":{"ad_unit":"\/84077725\/Parade\/entertainment\/contrib\/marynliles\/728_top"}},{"bidder":"appnexusAst","sizes":[[300,250]],"params":{"placementId":"10538285"}}],"sizes":[[300,250],[300,50],[300,600],[160,600]]},{"code":"div-gpt-ad-300-content-4","bids":[{"bidder":"sonobi","sizes":[[300,250]],"params":{"ad_unit":"\/84077725\/Parade\/entertainment\/contrib\/marynliles\/300_stream"}},{"bidder":"sovrn","sizes":[[728,90]],"params":{"tagid":"414066"}},{"bidder":"sonobi","sizes":[[728,90]],"params":{"ad_unit":"\/84077725\/Parade\/entertainment\/contrib\/marynliles\/728_bottom"}},{"bidder":"appnexusAst","sizes":[[300,600]],"params":{"placementId":"10538306"}},{"bidder":"appnexusAst","sizes":[[728,90]],"params":{"placementId":"10538312"}},{"bidder":"gumgum","sizes":[[300,250]],"params":{"inSlot":"5383"}},{"bidder":"optimera","sizes":[[300,250]],"params":{"clientID":"13"}}],"sizes":[[300,250],[320,50],[300,50],[1,1]]}]}},"adSlotId":"\/84077725\/Parade\/entertainment\/contrib\/marynliles","firstLoadSlotTarget":false,"disableThirdPartyAds":false,"disableActionButton":false,"disabledOutstreamVideo":false};
    window.dataLayer = window.dataLayer || [];

    (function (adSettings, app, SlotTracker, SlotMapper, gtagDataLayer) {
        // stub with no-op
        var SlotRefresher = {setDontRefresh : function(){}}

        var initTasks = null;
        var promiseCompletions = {
            "pbjs" : null,
            "managerInit" : null,
            "consent" : null,
            "gptComplete" : null
        };

        AdManager = {
            debugQueryString: "amgaddebug",
            logger: LogBuilder("AMG_ADS -- ", false),
            debugOn: true,
            abOn: true,
            abGptName: 'ab',
            abGroups: 'ab',
            abCookie: 'pjs_ab',
            abCookieExpiration: 365,
            adSlotId: null,
            platform: 'desktop',
            adInstances: {},
            slotsBuilt: false,
            slots: [],
            managerInitializedPromise : null,
            slotSize: null,
            prebidEnable: false,
            prebidGranularity: 'auto',
            slotMarkerClass: 'ad-slot-marker',
            wallpaperInfo: {
                'slotName' : 'wallpaper_background',
                'rendered' : false,
                'delayedRender' : false,
                'minWidth' : 1024,
                'slotDetails' : {
                    'outOfPage' : true,
                    'slotId' : 'div-gpt-wallpaper-background-99',
                    'localTargets' : {pos : "wallpaper", loc: "background"}
                },
                'fromFSET' : false,
                'hasBeenTracked' : false
            },
            immediateDisplaySlots: ['728_gallery', '300_gallery'],
            slotExclusionMap: {
                'wallpaper_background': {
                    slots: ['728_top'],
                    conditionCheck: function () { return this.platform !== 'phone'; }
                }
            },
            blacklistedSlots: {},
            slotDisplayQueue: [],
            requiredPurposes: [1, 2, 7, 9, 10],

            // Handles initial configuration of the AdManager and the related libraries
            init: function () {
                this.initPromises();
                this.setDebug();
                this.setEnvironment();
                this.setAdManagerParams(adSettings.managerParams);
                this.modifyAdManagerTargeting(adSettings.globalTargets);
                this.initGpt(this.platform, adSettings.globalTargets);

                this.manageWallpaperBlacklisting();
                this.enableAdManager(adSettings);
                
            },

            initPromises: function() {
                initTasks = [
                    new Promise(function(resolve) { promiseCompletions.pbjs = resolve; }),
                    new Promise(function(resolve) { promiseCompletions.managerInit = resolve; }),
                    new Promise(function(resolve) { promiseCompletions.consent = resolve; }),
                    new Promise(function(resolve) { promiseCompletions.gptComplete = resolve; })
                ];

                if (window.ConsentManager.consentsRetrieved()) {
                    this.logger.info("consents already retrieved, marking as complete");
                    // consent retrieved already somehow
                    promiseCompletions.consent();
                    promiseCompletions.consent = true;
                } else {
                    // add a completion when consent done
                    window.addEventListener(
                        window.ConsentManager.getRetrievedEventName(),
                        function() {
                            this.logger.info("marking consents as complete");
                            promiseCompletions.consent();
                        }.bind(this)
                    );
                }

                this.managerInitalizedPromise = Promise.all(initTasks)
                    .then(function() { this.logger.info("all promises complete")}.bind(this))
                    .then(this.makeInitialRequest.bind(this));
            },

            handleConsent: function() {
                if (!window.ConsentManager.checkPurposeConsent(this.requiredPurposes)) {
                    this.logger.info("Consents not granted, refraining from making ad request");
                    return;
                }

                this.makeInitialRequest();
            },

            // Enables the ad manager and injects the GPT tag.
            enableAdManager: function(adSettings) {
                this.logger.info("Enabling Ad Manager");
                if (!this.adsEnabled) {
                    this.enableGpt();
                    this.adsEnabled = true;

                    this.logger.info("AdManager enabled");
                }
                
                
                this.buildSlots(adSettings.slots);
                this.executeSlotDisplayQueue();

                this.logger.info("Marking AdManager Initalized");
                promiseCompletions.managerInit();
                promiseCompletions.managerInit = true;
                gtagDataLayer.push({"event": "AdManagerLoaded"});
            },
            setDebug: function(enable) {
                if (enable === true || this.logger.queryStringExists(this.debugQueryString)) {
                    this.logger.enable();
                }
            },
            setEnvironment: function () {
                if (typeof app !== 'undefined' && typeof app.platform !== 'undefined') {
                    this.platform = app.platform();
                }
            },
            modifyAdManagerTargeting: function(globalTargets) {
                this.logger.table("Modifying globalTargets", globalTargets);
                if(this.abOn) {
                    var abGroup = this.getCookie(this.abCookie);
                    if(!abGroup || 0 === abGroup.length){
                        var random = Math.floor(Math.random() * Math.floor(2));
                        var groups = this.abGroups.split('');
                        abGroup = groups[random];
                        this.logger.info("AB Group: " + abGroup);
                        this.setCookie(this.abCookie, abGroup, this.abCookieExpiration);
                    }else{
                        this.logger.info("AB cookie already set.  Group " + abGroup);
                    }
                    
                    globalTargets[this.abGptName] = abGroup;
                }
            },
            setCookie: function(cookieName, value, exDays) {
               var exDate = new Date();
                exDate.setDate(exDate.getDate() + exDays);
                var cookieValue = escape(value) + ((exDays === null) ? "": "; expires=" + exDate.toUTCString());
                document.cookie = cookieName + "=" + cookieValue;
            },
            getCookie: function(cookieName) {
                var i, x, y, ARRcookies = document.cookie.split(";");
                for (i = 0; i < ARRcookies.length; i++) {
                    x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
                    y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
                    x = x.replace(/^\s+|\s+$/g, "");
                    if (x == cookieName) {
                        return unescape(y);
                    }
                }
                return "";
            },
            setAdManagerParams: function (adManagerParams) {
                this.logger.table("Setting Ad Manager params", adManagerParams);
                for (var adManagerParam in adManagerParams) {
                    if (adManagerParams.hasOwnProperty(adManagerParam)) {
                        AdManager[adManagerParam] = adManagerParams[adManagerParam];
                    }
                }
            },
            // Add initial configuration to the googletag command queue
            initGpt: function(platform, globalTargets) {
                googletag.cmd.push(function() {
                    if (!globalTargets.platform) {
                        globalTargets.platform = platform;
                    }

                    this.addGlobalTargeting(globalTargets);

                    googletag.pubads().enableSingleRequest();
                    googletag.pubads().collapseEmptyDivs();
                    googletag.pubads().addEventListener('slotOnload', this.markInitialLoadComplete.bind(this));
                    
                    googletag.enableServices();
                    this.logger.info("GoogleTag Enabled");

                }.bind(this));
            },
            dispatchOutstreamVideoConsentEvent: function(doc, managerParams) {
                const event = new CustomEvent('outstreamVideoConsent', {
                    detail: {
                        disabledOutstreamVideo: managerParams.disabledOutstreamVideo,
                        disableThirdPartyAds: managerParams.disableThirdPartyAds
                    }
                })

                doc.dispatchEvent(event);
            },
            // This function builds the tag for the GPT script and inserts it into the head
            // We are doing this such that consent management can control when GPT loads.
            // This is a bit of a pain, but Google has not integrated with the IAB consent
            // framework as of yet.
            enableGpt: function() {
                this.logger.info("Inserting GPT script");
                // build and insert the GPT script
                var gads = document.createElement('script');
                gads.async = true;
                gads.type = 'text/javascript';
                var useSSL = 'https:' == document.location.protocol;
                gads.src = (useSSL ? 'https:' : 'http:') + '//www.googletagservices.com/tag/js/gpt.js';
                var node = document.getElementsByTagName('script')[0];
                node.parentNode.insertBefore(gads, node);
            },

            // This function is the callback supplied to PBJS.  It will be called if pbjs fails to load,
            // if the pbjs auction times out, and on the PBJS auction's successful completion
            markInitialPbjs: function(bids, timeout) {
                if (typeof promiseCompletions.pbjs !== "function") {
                    this.logger.info("Avoiding second completion of pbjs");
                }

                this.logger.info(
                    "Initial PBJS auction complete",
                    {
                        'bids' : bids,
                        'auction timed out' : timeout
                    }
                );

                // Marking complete for later use
                this.logger.info("Marking PBJS as complete");
                promiseCompletions.pbjs();
                promiseCompletions.pbjs = true;
            },

            // This is trigger for the normal ad request flow.  It is called by either markInitialPbjs()
            // or at the end of the FSET check, if FSET is not determined to be needed.  It does not use
            // refreshAllAds() in order to avoid triggering a PBJS auction or an optimera refresh alert
            makeInitialRequest: function() {
                this.logger.info("asked to make initial request");

                if (this.initialRequestSent === true) {
                    this.logger.info("Avoiding second 'initial' ad request as one has already been sent");
                    return;
                }

                this.dispatchOutstreamVideoConsentEvent(document, adSettings.managerParams);

                // marking initial request complete to avoid double-calls
                this.initialRequestSent = true;

                var execute = function() {
                    this.logger.info("Making inital ad request");
                    // manual refresh to avoid a second PBJS auction
                    if (this.prebidEnable) {
                        this.logger.info("Setting Prebid targeting");
                        pbjs.setTargetingForGPTAsync();
                    }

                    googletag.pubads().refresh();
                    this.logger.info("Initial Ad request complete");
                }.bind(this);

                // using queues ensure both gpt and pbjs are fully loaded prior to call
                if (this.prebidEnabled) {
                    googletag.cmd.push(function () {
                        pbjs.que.push(execute);
                    });
                } else {
                    googletag.cmd.push(execute);
                }
            },
            addGlobalTargeting: function(keyList) {
                this.logger.table("Setting Global Targets", keyList);

                for (var keyName in keyList) {
                    googletag.pubads().setTargeting(keyName, keyList[keyName]);
                }
            },
            buildSlots: function(slots) {
                // check to see if slots should exclude others.  This loop is done
                // ahead of the pushed function as blacklists need to be set first.
                for (var slotName in slots) {
                    this.manageSlotExclusions(slotName);
                }

                if (slots.length === 0) {
                    return;
                }

                googletag.cmd.push(function() {
                    if (this.slotsBuilt) {
                        return;
                    }

                    var slotDef;
                    for (var slotName in slots) {
                        if (!this.isBlacklisted(slotName)) {
                            slotDef = this.buildSlotDef(slots[slotName].defineSlot);

                            if (slotDef) {
                                this.adInstances[slotName] = slotDef;
                            } else {
                                this.logger.warn("Skipping slot as there are no defined sizes: " + slotName);
                            }
                        }
                    }

                    this.slotsBuilt = true;
                    this.logger.info("Marking gpt complete, ad slots built.");
                    promiseCompletions.gptComplete();
                    promiseCompletions.gptComplete = true;
                }.bind(this));
            },
            buildSlotDef: function (slotInfo) {
                this.logger.info("Building slot with details", slotInfo);

                var slotDef, slotSizes;
                if (slotInfo.outOfPage) {
                    slotDef = googletag.defineOutOfPageSlot(this.adSlotId, slotInfo.slotId);
                } else {
                    slotSizes = this.getAdSizesBySlotName(slotInfo.slotName);
                    if (!slotSizes || slotSizes.length === 0) {
                        // no defined sizes for this ad, don't add slot.
                        return false;
                    }
                    slotDef = googletag.defineSlot(this.adSlotId, slotSizes, slotInfo.slotId);
                }

                slotDef.addService(googletag.pubads());

                if (slotInfo.hasOwnProperty("localTargets")) {
                    for (var slotTarget in slotInfo.localTargets) {
                        slotDef.setTargeting(slotTarget, slotInfo.localTargets[slotTarget]);
                    }
                }

                return slotDef;
            },
            displaySlot: function(slotName, slotId) {
                this.logger.info("Registering slot for display: " + slotId);
                SlotMapper.addMap(slotName, slotId);

                var execution = function() {
                    googletag.cmd.push(function() {
                        if (this.isBlacklisted(slotName)) {
                            this.logger.info("Skipping display call for slot as it is blacklisted: " + slotName);
                            return;
                        }

                        this.logger.info('Displaying slot: ' + slotId);
                        googletag.display(slotId);
                    }.bind(this));
                }.bind(this);
                execution.slotName = slotName;
                execution.slotId = slotId;

                if (this.readyToDisplayAds()) {
                    // not in first site entry takeover check, just display the thing.
                    this._actuallyDisplaySlot(execution);
                } else {
                    // we are in the middle of checking a site entry takeover,
                    // this slot is likely not defined yet, so don't display it.
                    this.slotDisplayQueue.push(execution);
                }
            },
            executeSlotDisplayQueue: function() {
                this.logger.info("Executing slot display queue");
                while (this.slotDisplayQueue.length > 0) {
                    this._actuallyDisplaySlot(this.slotDisplayQueue.shift());
                }

                //once the queue is empty, swap out the push method to prevent orphans
                this.slotDisplayQueue.push = this._actuallyDisplaySlot.bind(this);
            },
            _actuallyDisplaySlot: function(execution) {
                // execution is a function object that will correctly call googletag.
                // It also has some information attached to it.
                if (this.isBlacklisted(execution.slotName)) {
                    return; // slot has been excluded, don't display
                }

                if (this.immediateDisplaySlots.indexOf(execution.slotName) !== -1) {
                    // this slot is in our "display immediately" list
                    execution();

                } else if (window.addEventListener) {
                    window.addEventListener('load', execution);

                } else if (window.attachEvent) {
                    window.attachEvent('onload', execution);
                }
            },
            moveSlotToMarker: function(slotMarker) {

                // slotMarker should be a dom element with a data-slotname attribute
                if (typeof slotMarker === "undefined"
                    || typeof slotMarker.dataset === "undefined"
                    || typeof slotMarker.dataset.slotname == "undefined"
                    || typeof slotMarker.appendChild !== "function"
                ) {
                    this.logger.error("Attempting to move a slot to an invalid target", slotMarker);
                    return;
                }

                var slotName = slotMarker.dataset.slotname;
                var slotContainer;

                if (!adSettings.slots.hasOwnProperty(slotName) || !adSettings.slots[slotName].hasOwnProperty('slotId')) {
                    this.logger.error("Attempting to move an unknown slot to marker", slotMarker);
                    return;
                }

                slotContainer = document.getElementById(adSettings.slots[slotName].slotId);

                if (slotContainer === null) {
                    this.logger.error("Unable to find a rendered slot container for slot marker", slotMarker);
                    return;
                }

                if (slotContainer === slotMarker) {
                    this.logger.info("Ad slot already contined in marker, skipping the move", slotMarker);
                    return;
                }

                // Make sure we can move it back to the old container if we need too
                if (!slotContainer.classList.contains(this.slotMarkerClass)) {
                    slotContainer.classList.add(this.slotMarkerClass);
                }

                if (typeof slotContainer.dataset.slotname === "undefined") {
                    slotContainer.dataset.slotname = slotName;
                }

                // Everything is good, move the slot over
                slotMarker.appendChild(slotContainer);
                this.logger.info("Moved " + slotName + " to new dom node");
            },
            manageSlotExclusions: function (slotName) {
                if (!this.slotExclusionMap.hasOwnProperty(slotName)) {
                    return;
                }

                var conditionCheck = this.slotExclusionMap[slotName].hasOwnProperty('conditionCheck');
                if (!conditionCheck) {
                    this.addBlacklistedSlots(this.slotExclusionMap[slotName].slots, true);
                    return;
                }

                if (this.slotExclusionMap[slotName]['conditionCheck'].apply(this)) {
                    this.addBlacklistedSlots(this.slotExclusionMap[slotName].slots, true);
                }
            },
            addBlacklistedSlots: function (slotNames, remove) {
                remove = remove || false;
                for (var slotKey in slotNames) {
                    var slot = slotNames[slotKey];
                    if (!this.blacklistedSlots.hasOwnProperty(slot)) {
                        this.logger.info("Blacklisting slot: " + slot);
                        this.blacklistedSlots[slot] = true;
                    }

                    if (remove) {
                        this.removeSlot(slot);
                    }
                }
            },
            removeSlot: function(slotName) {
                var instance = this.getAdInstance(slotName);

                if (instance === null) {
                    this.logger.warn("Attempting to remove unknown slot: " + slotName);
                    // no slot found by that name, or slot instance was supplied as null
                    return;
                }

                try {
                    this.logger.info("Destroying slot : " + slotName);
                    googletag.destroySlots([instance]);
                } catch (e) {
                    // hackaround for googletag not wanting to remove an empty oop slot
                    // for some reason the second call works.
                    this.logger.warn("Attempting second destruction of slot : " + slotName);
                    googletag.destroySlots([instance]);
                }

                this.logger.info("Removing slot from map: " + slotName);
                delete this.adInstances[slotName];
            },
            getAdInstance: function(slotName) {
                if (!this.adInstances.hasOwnProperty(slotName)) {
                    return null;
                }

                return this.adInstances[slotName];
            },
            removeBlacklist: function (slotName) {
                this.logger.info("Removing slot blacklist: " + slotName);
                delete this.blacklistedSlots[slotName];
            },
            isBlacklisted: function (slotName) {
                return this.blacklistedSlots.hasOwnProperty(slotName);
            },
            shouldAttemptTakeover: function () {
                return (this.firstLoadSlotTarget !== false);
            },
            readyToDisplayAds: function() {
                return this.slotsBuilt && (!this.shouldAttemptTakeover() || this.firstLoadChecked !== false);
            },
            buildWallpaperSlot: function() {
                googletag.cmd.push(function() {
                    var slotName = this.wallpaperInfo.slotName;
                    var slotId = this.wallpaperInfo.slotDetails.slotId;

                    if (this.adInstances.hasOwnProperty(slotName)) {
                        // wallpaper slot has already been built, skip this.
                        return;
                    }

                    this.logger.info("Building wallpaper slot");

                    // make sure 728_top is excluded
                    this.manageSlotExclusions(slotName);

                    // adding a DOM element for the takeover
                    var container = document.createElement('div');
                    container.id = slotId;
                    document.body.appendChild(container);

                    this.adInstances[slotName] = this.buildSlotDef(this.wallpaperInfo.slotDetails);

                    this.displaySlot(slotName, slotId);
                }.bind(this));
            },
            activateWallpaper: function(wallpaperDetails, renderMethod) {
                this.manageSlotExclusions('wallpaper_background', true);
                var wallpaperCallback = function() {
                    if (!this.checkShouldRenderWallpaper()) {
                        this.logger.info("Skipping Wallpaper render as window is not wide enough (" + window.innerWidth
                            + "px < " + this.wallpaperInfo.minWidth + "px)");
                        return;
                    }
                    if (this.wallpaperInfo.rendered === true) {
                        this.logger.info("Skipping wallpaper activation as it has already been rendered");
                        return;
                    }

                    this.logger.info("Rendering wallpaper with info: ", wallpaperDetails);
                    this.wallpaperInfo.rendered = true;

                    // not tracking wallpaper unless it is actually rendered.
                    SlotTracker.manualSlotLoaded(this.wallpaperInfo.slotName);
                    // no refreshing while we have a wallpaper active.
                    SlotRefresher.setDontRefresh(true);

                    window.parade.takeover = wallpaperDetails;
                };

                if (this.checkShouldRenderWallpaper()) {
                    this.logger.info("Immediate wallpaper render detected");
                    wallpaperCallback.apply(this);
                } else {
                    this.logger.info("Wallpaper not rendered as window is not wide enough, registering callback.");
                    this.wallpaperInfo.delayedRender = true;
                    window.addEventListener('resize', this.debounce(wallpaperCallback.bind(this), 150));
                }
            },
            manageWallpaperBlacklisting : function() {
                if (this.wallpaperInfo.rendered === true || this.wallpaperInfo.fromFSET === true || app.is_phone == true) {
                    return;
                }

                // @todo set wallpaper breakpoint in ad admin
                if (!this.checkShouldRenderWallpaper()) {
                    this.logger.info("Blacklisting wallpaper slot, width (" + window.innerWidth
                        + "px) smaller than breakpoint (" + this.wallpaperInfo.minWidth + "px)");
                    this.addBlacklistedSlots([this.wallpaperInfo.slotName]);
                    this.preventWallpaperSlot();
                    this.wallpaperInfo.delayedRender = true;
                    // listen for resize
                    window.addEventListener('resize', this.debounce(this.manageWallpaperBlacklisting.bind(this), 150));

                } else if (this.isBlacklisted(this.wallpaperInfo.slotName)) {
                    this.removeBlacklist(this.wallpaperInfo.slotName);
                    this.buildWallpaperSlot();
                    this.refreshAllAds();
                }
            },
            checkShouldRenderWallpaper: function() {
                // only render wallpaper if window it is bigger than the minwidth
                return (window.innerWidth >= this.wallpaperInfo.minWidth);
            },
            preventWallpaperSlot: function() {
                if (adSettings.slots.hasOwnProperty(this.wallpaperInfo.slotName)) {
                    delete adSettings.slots[this.wallpaperInfo.slotName];
                }
            },
            setSlotRefresher: function(refresher) {
                SlotRefresher = refresher;
            },
            handleSlotRendered: function(event) {
                if (this.checkSlotFirstLoad === true) {
                    this.handleTakeoverLoad(event);
                }

                SlotTracker.noteSlotLoaded(event);
            },
            getAdSizesBySlotName: function (slotName) {
                if (typeof this.slots[slotName] !== 'undefined' && typeof this.slots[slotName][this.platform] !== undefined) {
                    return this.slots[slotName][this.platform];
                }

                return [];
            },
            getPrebidSlots: function () {
                if (typeof this.prebid !== 'undefined' && typeof this.prebid.slots !== 'undefined') {
                    return this.prebid.slots[this.platform];
                }

                return [];
            },
            getPrebidTimeout: function () {
                if (typeof this.prebid !== 'undefined' && typeof this.prebid.timeout !== 'undefined') {
                    return this.prebid.timeout;
                }

                return null;
            },
            getPrebidFailsafeTimeout: function () {
                // @todo add this to the prebid config in the ad manager
                if (typeof this.prebid !== 'undefined' && typeof this.prebid.failsafeTimeout !== 'undefined') {
                    return this.prebid.failsafeTimeout;
                }

                return null;
            },
            getPrebidGranularity: function () {
                if (typeof this.prebid !== 'undefined' && typeof this.prebid.granularity !== 'undefined') {
                    return this.prebid.granularity;
                }

                return this.prebidGranularity;
            },
            markInitialLoadComplete: function() {
                if (this.initialAdsLoaded === true) {
                    return;
                }

                this.logger.info("Marking initial ads loaded");
                this.initialAdsLoaded = true;
                return;
            },
            forceRefresh: function() {
                if (this.initialAdsLoaded === true) {
                    return;
                }

                this.logger.warn("Forcing ad refresh");
                this.refreshAllAds();
            },
            refreshAllAds: function () {
                if (!this.adsEnabled) {
                    // ad manager not fully initialized, make the call later
                    googletag.cmd.push(this.refreshAllAds.bind(this));
                    return;
                }

                this.refreshAdsBySlotName(Object.keys(this.adInstances));
            },
            refreshAdsBySlotName : function(slotNames) {
                var refreshSlots = this.buildSlotsByName(slotNames);

                if (refreshSlots.length == 0) {
                    this.logger.warn("Attempting to refresh slots, unable to match any defined slots!");
                    return;
                } else {
                    this.logger.info("Refreshing slots, count: " + refreshSlots.length);
                    this.refreshAds(refreshSlots);
                }
            },
            refreshAds: function (ads) {
                if (!ads) {
                    return false;
                }

                var slotIds = this.buildRefreshIds(ads);

                if (this.prebidEnable === true && typeof pbjs !== 'undefined') {
                    this.logger.info("Prebid exists, using it for refresh");
                    this.triggerPrebidRefresh(ads, slotIds);
                    return;
                }

                this.logger.info("PBJS not active, using GPT");
                this.triggerGptRefresh(ads, slotIds);
            },
            buildSlotsByName(slotNames){
                var refreshSlots = [];
                slotNames.forEach((slotName) => {
                    var instance = this.getAdInstance(slotName);
                    if (instance) {
                        refreshSlots.push(instance);
                    }
                });

                return refreshSlots;
            },
            buildRefreshIds: function(ads) {
                var slotIds = [];
                for (var i = 0; i < ads.length; i++) {
                    if (ads[i]) {
                        slotIds.push(ads[i].getSlotElementId());
                    }
                }

                return slotIds;
            },
            // Trigger a PBJS auction and refresh on completion
            triggerPrebidRefresh: function(ads, slotIds) {
                
                var handler = function() {
                    this.logger.info("Setting pbjs targeting");
                    pbjs.setTargetingForGPTAsync(slotIds);
                    this.triggerGptRefresh(ads, slotIds);
                };

                // using que as pbjs may not be fully loaded
                pbjs.que.push(function () {
                    this.logger.info("Refreshing PBJS slots", slotIds);

                    pbjs.requestBids({
                        timeout: this.getPrebidTimeout(),
                        adUnitCodes: slotIds,
                        bidsBackHandler: function () {
                            this.logger.info("PBJS bids returned");
                            // gpt must be loaded prior to setting targeting, queue it
                            googletag.cmd.push(handler.bind(this));
                        }.bind(this)
                    });
                }.bind(this));
            },
            triggerGptRefresh: function(ads, slotIds) {

                this.logger.info("Pubads is not ready, queuing refresh");
                googletag.cmd.push(function() {
                    try {
                        this.logger.info("GPT refresh triggered", ads);
                        googletag.pubads().refresh(ads);
                        if (slotIds) {
                            // potentially no ids defined (i.e. FSET)
                            this.optimeraRefresh(slotIds);
                        }
                    } catch (err) {
                        this.logger.error("Optimera refresh encountered an error", err);
                    }
                }.bind(this));
            },
            optimeraRefresh: function(slotIds) {
                if (typeof window.oPageUnload !== 'function') {
                        this.logger.info('Not performing optimera refresh as optimera has not loaded yet');
                        return;
                }

                this.logger.info('Starting optimera refresh for slots', slotIds);
                var slotId;

                for (var i = 0; i < slotIds.length; i++) {
                    slotId = slotIds[i];

                    this.logger.info("Checking that slot with ID exists in DOM: " + slotId);
                    if (document.getElementById(slotId) !== null) {
                        this.logger.info("Triggering optimera refresh for slot: " + slotId);
                        oPageUnload(slotId);
                    }
                }

            },
            updateTargetingOnAllAdUnits: function (targetName, targetValue) {
                for (var slotName in this.adInstances) {
                    this.addSlotTargeting(slotName, targetName, targetValue);
                }
            },
            addSlotTargeting(slotName, targetName, targetValue) {
                if (this.adInstances.hasOwnProperty(slotName)) {
                    this.adInstances[slotName].setTargeting(targetName, targetValue);
                }
            },
            shouldDisplay3rdPartyAds: function () {
                if (!this.readyToDisplayAds()) {
                    return null;
                }

                // don't show 3rd party ads when manually disabled in admin 
                if (app.disableThirdPartyAds === true
                    || adSettings.managerParams.disableThirdPartyAds === true
                    || this.hasAd(this.wallpaperInfo.slotName)
                ) {
                    return false;
                }
                // nothing blocking it, lets display!
                return true;
            },
            shouldDisplayActionButton: function() {
                if (!this.readyToDisplayAds()) {
                    return null;
                }

                if (app.disableActionButton === true || adSettings.managerParams.disableActionButton === true
                ) {
                    return false;
                }

                return true;
            },
            hasAd: function (adName) {
                var hasAd = false;
                if (this.adInstances[adName]) {
                    hasAd = true;
                }

                return hasAd;
            },
            displayOrientationChangeAds: function () {
                var tabletRefreshableSizes = [];
                for (var adInstance in this.adInstances) {
                    if (this.adInstances.hasOwnProperty(adInstance) && (adInstance === '300_top' || adInstance === '300_bottom')) {
                        tabletRefreshableSizes.push(this.adInstances[adInstance]);
                    }
                }

                this.refreshAds(tabletRefreshableSizes);
            },
            listenSingle: function(target, eventName, eventCallback) {
                target.addEventListener(eventName, function(e) {
                    // remove the event
                    e.target.removeEventListener(e.type, arguments.callee);

                    // call the actual event handler.
                    eventCallback(e);
                });
            },
            // Debounce from underscore.js
            debounce: function(func, wait, immediate) {
                var timeout;
                return function() {
                    var context = this;
                    var args = arguments;

                    var later = function() {
                        timeout = null;
                        if (!immediate) {
                            func.apply(context, args);
                        }
                    };

                    var callNow = immediate && !timeout;
                    clearTimeout(timeout);

                    timeout = setTimeout(later, wait);
                    if (callNow){
                        func.apply(context, args);
                    }
                };
            }
        };

        AdManager.init();
    })( window.parade.adSettings, window.parade, window.amgAds.AdSlotTracker, window.amgAds.SlotMapper, window.dataLayer);

    // @todo: cleanup this is legacy code used to detect if function calls are being made that shouldn't be at this point.
    window.parade = (function (app, AdManager) {
        app.trackAdDisplays = function (ads) {
            console.log('legacy track ad displays ads call............');
        };

        app.displayInitialAds = function () {
            console.log('legacy display initial ads call............');
        };

        app.orientationChanged = false;
        app.displayOrientationChangeAds = function () {
            console.log('legacy display orientation change call............');
            if (typeof app.is_tablet !== 'undefined' && (app.is_tablet === true && app.is_landscape === false)) {
                AdManager.displayOrientationChangeAds();
            }
        };

        app.adsReady = true;
        app.refreshAds = function (ads) {
            console.log('legacy refresh ads call............');
        };

        return app;
    })(window.parade || {}, AdManager);
</script>
<script type="text/javascript">
window.amgAds = window.amgAds || {};

window.amgAds.PageVisibility = window.amgAds.PageVisibility || (function() {
    // from MDN
    var hidden; 
    if (document.hidden !== undefined) { // Opera 12.10 and Firefox 18 and later support 
        hidden = "hidden";
    } else if (document.msHidden !== undefined) {
        hidden = "msHidden";
    } else if (document.webkitHidden !== undefined) {
        hidden = "webkitHidden";
    }

    

    return {
        isVisible: function() {
            if (!hidden) {
                // if we can't determine the proper field, say we are visible
                return true;
            }
            return (!document[hidden]);
        },
        isActive: function()
        {
           return document.hasFocus(); 
        }
    }
})();

window.amgAds.SlotAutoRefresher = window.amgAds.SlotAutoRefresher || (function(AdManager, SlotMapper, PageVisibility) {
    var settings = {
        refreshIntervals : {
            'default' : 30000,
            'fset_slot' : false,
            '300_gallery' : false,
            '728_gallery' : false,
            'gallery_interstitial' : false,
        },
        failedRefreshInterval : 30000,
        autoRefreshCheckInterval: 2500,
        slotCooldown: 900, // must be under the "visible impression" time threshold
        inactivePageDelay: 120000, // delay between refreshes when tab is inactive 
        visibilityThresholds: { // visibility percentags for refrshes
            'out' : 4,  // what triggers "out of page"
            'in' : 6 // what triggers "back in page"
        },
        refreshTargetName: "rf",
        maxRefreshCount: 10,
        noRefreshSelector: ".amg-norefresh",
        debugQueryString: "amgaddebug"
    };
    var refreshCount = {};
    var scheduled = {};
    var readyForRefresh = {};
    var slotCooldowns = {};
    var intervalToken = false;
    var dontRefresh = false;
    var refreshPaused = false;
    var logger = LogBuilder("AMG_AD_REFRESH -- ", false);

    var isSlotVisible = function(slotName) {
        var slot = AdManager.getAdInstance(slotName);
        var el = SlotMapper.getSlotDomElement(slotName);

        if (slot !== null && slot.getOutOfPage()) {
            // out of slot pages are visible by definition.
            return true;
        }

        if (el === false) {
            return false;
        }

        // use parent's bounding, slot is all 0's
        var rect = el.parentElement.getBoundingClientRect();

        if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
            return true;
        }

        if (rect.height === 0) {
            return false;
        }


        //rect.top is position of box re: to viewport, - means out of view above
        var hidden = (rect.top < 0) ? hidden = rect.top : 0;
            
        // rect.bottom being greater than window.innerheight means that it is off the bottom
        hidden += (rect.bottom > window.innerHeight) ? rect.bottom - window.innerHeight : 0;
        
        // check to see if percent hidden is greater than threshold
        return ((hidden / rect.height) * 100 < settings.visibilityThresholds.in); 

     }

    var getSlotRefreshTime = function(slotName) {
        if (slotName === false) {
            return false;
        } 
        
        if (settings.refreshIntervals[slotName] === undefined) {
            slotName = 'default';
        }

        return settings.refreshIntervals[slotName];
    };

    var handleImpressionVisble = function (slotEvent) {
        var slotName = SlotMapper.getSlotName(slotEvent.slot);
        var refreshTime = getSlotRefreshTime(slotName);

        // no refresh or refresh already scheduled somehow
        if (!shouldScheduleRefresh(slotName) || refreshTime === false) {
            logger.info(`Auto-refresher Ignoring slot impression: ${SlotMapper.getSlotId(slotEvent.slot)}`);
            return;
        }

        logger.info(`Scheduled slot for refresh after impression: ${slotName}`, slotEvent);
        scheduleSlot(slotName, refreshTime);
    };

    var handleNoRefresh = function (slot, slotName = null) {
        if (!slotName) {
            slotName = SlotMapper.getSlotName(slot);
        }

        // find iframe
        var iframe = document.querySelector('#' + slot.getSlotElementId() + ' iframe');      
        var iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
        var noRefresh = iframeDoc.querySelector(settings.noRefreshSelector);

        logger.info(`No Refresh check for ${slotName}`, noRefresh);
        
        //check for no-refresh class
        if (noRefresh) {
            Refresher.setRefreshForSlot(slotName, false);
        }
    }

    var scheduleSlot = function(slotName, slotRefreshDelay) {
        addRefreshCount(slotName);

        if (!PageVisibility.isActive() && settings.inactivePageDelay > slotRefreshDelay) {
            slotRefreshDelay = settings.inactivePageDelay;
        }

        logger.info(`Scheduled slot for refresh ${slotName} : ${slotRefreshDelay}ms`);

        var timeoutToken = setTimeout(() =>{
            logger.info(`Marking slot ${slotName} as ready for refresh`);
            readyForRefresh[slotName] = true;
        }, slotRefreshDelay);

        scheduled[slotName] = {'token' : timeoutToken, 'hasBeenOutOfSight' : false};
    };

    var clearScheduleData = function(slotName) 
    {
        logger.info(`Clearing refresh schedule for ${slotName}`);
        if (scheduled[slotName] !== undefined){
            clearTimeout(scheduled[slotName].token);
        }

        delete scheduled[slotName];
        delete readyForRefresh[slotName];
    }

    var slotRefreshTick = function() {
        if (refreshActive() === false || !PageVisibility.isVisible()) {
            logger.info(`Window hidden or refresher not active, skipping tick`);
            return;
        }

        var keys = Object.keys(readyForRefresh);
        if (keys.length === 0) {
            // nothing to do
            return;
        }

        // only refresh visible slots ready for refresh
        var visible = keys.filter(perSlotTickFilter);

        if (visible.length > 0) {
            logger.info(`found ${visible.length} slots ready for refresh`, visible);
            AdManager.refreshAdsBySlotName(visible);
        }
    };

    var perSlotTickFilter = function(slotName) {
        if (!isSlotVisible(slotName)) {
            return false;
        }

        clearScheduleData(slotName);

        return (refreshCount[slotName] < settings.maxRefreshCount);
    };

    // Keep an eye on all rendered slots. If they are one we are tracking, and the
    // slot was filled, clear it out. Otherwise, try again after a delay.
    var handleSlotRendered = function(slotEvent) {
        var slotName = SlotMapper.getSlotName(slotEvent.slot);
        var slotRefresh = getSlotRefreshTime(slotName);
        logger.info(`Slot rendered: {${slotName}`, slotEvent);

        clearScheduleData(slotName);

        if (!slotEvent.isEmpty) {
            handleNoRefresh(slotEvent.slot, slotName);
            logger.info(`Slot rendered successfully ${slotName}, not scheduling auto-refresh`);
            startSlotCooldown(slotName, settings.slotCooldown);
            return;
        }

        if (slotRefresh === false || !shouldScheduleRefresh(slotName)) {
            logger.info(`Slot not eligible for auto refresh, refusing to schedule: ${slotName}`);
            return;
        }

        scheduleSlot(slotName, settings.failedRefreshInterval, "Unfilled slot render");
        startSlotCooldown(slotName, settings.slotCooldown);
    };

    var handleVisibilityChange = function(slotEvent) {
        var slotName = SlotMapper.getSlotName(slotEvent.slot);
        if (slotName === false || typeof scheduled[slotName] === "undefined" || readyForRefresh[slotName]) {
            // no refresh for this slot, or slot is aready marked as ready
            return;
        }

        var slot = scheduled[slotName];
        

        // If slot is marked for refresh when it becomes visible again, and is now visible, mark it for immediate refresh.
        if (slot.hasBeenOutOfSight === true && slotEvent.inViewPercentage > settings.visibilityThresholds.in) {
            logger.log("Scheduled slot has returned into view, marking it for immediate refresh")
            readyForRefresh[slotName] = true;
            return;
        }


        // slot is being tracked for refresh
        slot.lastVisibility = slotEvent.inViewPercentage;

        // If slot is not marked as needing an immediate refresh when it becomes visible,
        // and just qualified as "not visible", mark it.
        if (slot.lastVisibility <= settings.visibilityThresholds.out && readyForRefresh[slotName] !== true) {
            logger.log("Marking scheduled slot as having left view");
            slot.hasBeenOutOfSight = true;
        }
    };

    var shouldScheduleRefresh = function(slotName) 
    {
        return (
            (refreshCount[slotName] === undefined || refreshCount[slotName] < settings.maxRefreshCount)
            && !isSlotOnCooldown(slotName) 
        );
    };

    var addRefreshCount = function(slotName, label = "unknown") {
        logger.info(`Adding refresh count for ${slotName}, from ${label}`);
        refreshCount[slotName] = (refreshCount[slotName] === undefined) ? 1 : refreshCount[slotName] + 1;

        // add targeting showing refresh count
        AdManager.addSlotTargeting(slotName, settings.refreshTargetName, 1);
    };

    var refreshActive = function() {
        return (dontRefresh !== true && refreshPaused !== true);
    };

    var startSlotCooldown = function(slotName, length) {
        logger.info(`Starting slot cooldown for ${slotName} : ${length}`);
        slotCooldowns[slotName] = Date.now() + length;
    };

    var isSlotOnCooldown = function(slotName) {
        // if slot is unset, or cooldown has already ended
        return (slotCooldowns[slotName] && slotCooldowns[slotName] > Date.now());
    };

    var Refresher = {
        init : function(incomingSettings) {
            if (intervalToken !== false) {
                // we have already initialized
                return;
            }

            this.setDebug();
            logger.info("Initializing Auto Refresher");
            AdManager.setSlotRefresher(this);
            settings = {...settings, ...incomingSettings};
            intervalToken = setInterval(slotRefreshTick, settings.autoRefreshCheckInterval);

            googletag.cmd.push(function() {
                logger.info("Hooking refresh listeners");                 
                
                googletag.pubads().addEventListener('slotVisibilityChanged', handleVisibilityChange);
                googletag.pubads().addEventListener('impressionViewable', handleImpressionVisble);
                googletag.pubads().addEventListener('slotRenderEnded', handleSlotRendered);
            });
        },
        setDebug: function(enable) {
            if (enable === true || logger.queryStringExists(settings.debugQueryString)) {
                logger.enable();
            }
        },
        setDontRefresh: function(status) {
            dontRefresh = (!!status);
        },
        setRefreshForSlot: function(slotName, refreshVal) {
            logger.info(`Setting refresh for ${slotName} to ${refreshVal}`);

            settings.refreshIntervals[slotName] = refreshVal;

            if (refreshVal === false) {
                clearScheduleData(slotName);
            }
        },
        pauseRefresh: function() {
            logger.info("Pausing refresh");
            refreshPaused = true;
        },
        unpauseRefresh: function() {
            logger.info("Unpausing refresh");
            refreshPaused = false;  
        }
    };

    return Refresher;
})(window.AdManager, window.amgAds.SlotMapper, window.amgAds.PageVisibility);

// self init
window.amgAds.SlotAutoRefresher.init();
</script><script type="text/javascript" src="https://parade.com/wp-content/plugins/amg_ads/assets/js/lib/Prebid/build/dist/prebid.js" async></script>
<script>
    window.adUnits = [];

    (function() {
        if (typeof window.AdManager === "undefined") {
            console.error("Attempting to configure PBJS before AdManager loaded!");
            return;
        }

        if (typeof window.ConsentManager === "undefined") {
            console.error("Attempting to configure PBJS before ConsentManager loaded!");
        }

        if (AdManager.prebidEnable === false) {
            AdManager.logger.info("Skipping PBJS config as AdManager says it is not enabled");
            return;
        }

        adUnits = AdManager.getPrebidSlots();

        var pbjsAuctionTimeout = AdManager.getPrebidTimeout() || 500;
        var failsafeTimeout = AdManager.getPrebidFailsafeTimeout() || 3000;
        var pbjsGranularity = AdManager.getPrebidGranularity() || 'auto';

        var pbjsConsentConfig = ConsentManager.getPrebidConfig();

        var configurePBJS = function() {
            AdManager.logger.info("Configuring PBJS");

            pbjs.setConfig({
                priceGranularity: pbjsGranularity,
                consentManagement: pbjsConsentConfig
            });

            pbjs.addAdUnits(adUnits);
            pbjs.requestBids({
                timeout: pbjsAuctionTimeout,
                bidsBackHandler: AdManager.markInitialPbjs.bind(window.AdManager)
            });
        };

        if (pbjs.libLoaded === true) {
            // pbjs has already loaded, need to just configure!
            pbjs.que.push(configurePBJS);
        } else {
            // pbjs not loaded yet, make sure we are at the front of the line.
            // using unshift to make sure that this is the first callback executed
            pbjs.que.unshift(configurePBJS);
        }

        // Set callback to trigger ad load if PBJS does not correctly load
        setTimeout(function(){
            if (AdManager.prebidInitialComplete === false) {
                AdManager.logger.info("PBJS failed to load, manually triggering ads");
                AdManager.markInitialPbjs();
            }
        }, failsafeTimeout);
    })();
</script>
<script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"Article","mainEntityOfPage":"https:\/\/parade.com\/1039985\/marynliles\/pick-up-lines\/","publisher":{"@type":"Organization","name":"Parade: Entertainment, Recipes, Health, Life, Holidays","logo":{"type":"ImageObject","url":"https:\/\/ath-clients.s3.amazonaws.com\/parade\/logo\/parade-logo-amp.png","height":60,"width":600}},"headline":"101 Best Pick Up Lines - Funny Pick Up Lines for Guys, Girls","articleBody":"The best pick-up lines\u2014whether they're cheesy, funny pick-up lines that'll get someone laughing or clever pick-up lines that'll make you stand out\u2014will make breaking the ice and getting the conversation started a little bit easier.\r\n\r\nPlus, using corny pick-up lines shows off what a playful personality you have, too\u2014and who doesn't like that!\r\n\r\nSo whether you're looking for cute pick-up lines to tell a girl you like her or need some cheesy pick-up lines to text to a guy you're into, these 101 best funny pick up lines can help you get your flirt on.\r\nBest Pick Up Lines\r\n1. I hope you know CPR, because you just took my breath away!\r\n\r\n2. So, aside from taking my breath away, what do you do for a living?\r\n\r\n3. I ought to complain to Spotify for you not being named this week\u2019s hottest single.\r\n\r\n4. Are you a parking ticket? \u2018Cause you\u2019ve got \u2018fine\u2019 written all over you.\r\n\r\n5. Your eyes are like the ocean; I could swim in them all day.\r\n\r\n6. When I look in your eyes, I see a very kind soul.\r\n\r\n7. If you were a vegetable, you\u2019d be a \u2018cute-cumber.\u2019\r\n\r\n8. Do you happen to have a Band-Aid? \u2018Cause I scraped my knees falling for you.\r\n\r\n9. I never believed in love at first sight, but that was before I saw you.\r\n\r\n10. I didn\u2019t know what I wanted in a woman until I saw you.\r\n\r\n\r\n\r\n11. I was wondering if you could tell me: If you\u2019re here, who\u2019s running Heaven?\r\n\r\n12. No wonder the sky is gray (or dark, if at night)\u2014all the color is in your eyes.\r\n\r\n13. You\u2019ve got everything I\u2019ve been searching for, and believe me\u2014I\u2019ve been looking a long time.\r\n\r\n14. You\u2019re like a fine wine. The more of you I drink in, the better I feel.\r\n\r\n15. You\u2019ve got a lot of beautiful curves, but your smile is absolutely my favorite.\r\n\r\n16. Are you as beautiful on the inside as you are on the outside?\r\n\r\n17. If being sexy was a crime, you\u2019d be guilty as charged.\r\n\r\n18. I was wondering if you\u2019re an artist because you were so good at drawing me in.\r\n\r\n19. It says in the Bible to only think about what\u2019s pure and lovely\u2026 So I\u2019ve been thinking about you all day long.\r\n\r\n20. Do you have a map? I just got lost in your eyes.\r\nFunny Pick Up Lines\r\n21. I\u2019d like to take you to the movies, but they don\u2019t let you bring in your own snacks.\r\n\r\n22. You know what you would look really beautiful in? My arms.\r\n\r\n23. I would never play hide and seek with you because someone like you is impossible to find.\r\n\r\n24. Are you a magician? It\u2019s the strangest thing, but every time I look at you, everyone else disappears.\r\n\r\n25. I think there\u2019s something wrong with my phone. Could you try calling it to see if it works?\r\n\r\n26. Hi, I just wanted to thank you for the gift. (pause) I\u2019ve been wearing this smile ever since you gave it to me.\r\n\r\n27. Are you an electrician? Because you\u2019re definitely lighting up my day\/night!\r\n\r\n28. I\u2019ve heard it said that kissing is the \u2018language of love.\u2019 Would you care to have a conversation with me about it sometime?\r\n\r\n29. I always thought happiness started with an \u2018h,\u2019 but it turns out mine starts with \u2018u.\u2019\r\n\r\n30. I believe in following my dreams. Can I have your Instagram?\r\n\r\n\r\n\r\n31. Do you know what the Little Mermaid and I have in common? We both want to be part of your world.\r\n\r\n32. If you were a song, you\u2019d be the best track on the album.\r\n\r\n33. On a scale of 1 to America, how free are you tonight?\r\n\r\n34. You know, I always thought that Disneyland was the \u2018happiest place on Earth,\u2019 but that was before I got a chance to stand here next to you.\r\n\r\n35. Want to go outside and get some fresh air with me? You just took my breath away.\r\n\r\n36. If you were a taser, you\u2019d be set to \u2018stun.\u2019\r\n\r\n37. If you were a Transformer, you\u2019d be \u2018Optimus Fine.\u2019\r\n\r\n38. Is your name Google? Because you have everything I\u2019m searching for.\r\n\r\n39. Do you ever get tired from running through my thoughts all night?\r\n\r\n40. You know, they say that love is when you don\u2019t want to sleep because reality is better than your dreams. And after seeing you, I don\u2019t think I ever want to sleep again.\r\nCheesy Pick Up Lines for Guys\r\n41. Your hand looks heavy\u2014can I hold it for you?\r\n\r\n42. Are you a time traveler? Because I absolutely see you in my future.\r\n\r\n43. Do you know what my shirt is made of? Boyfriend material.\r\n\r\n44. I thought this was a (bar\/restaurant\/etc.), but I must be in a museum because you\u2019re a piece of art.\r\n\r\n45. You know, your smile has been lighting up the room all night and I just had to come and say hello.\r\n\r\n46. Hi, I\u2019m (your name). Do you remember me? Oh, that\u2019s right\u2014we\u2019ve only met in my dreams.\r\n\r\n47. What does it feel like to be the most gorgeous girl in the room?\r\n\r\n48. I can\u2019t tell if that was an earthquake, or if you just seriously rocked my world.\r\n\r\n49. I just had to tell you, your beauty made me truly appreciate being able to see.\r\n\r\n50. If you were a fruit, you\u2019d be a \u2018fine-apple.\u2019\r\n\r\n\r\n\r\n51. I don\u2019t know your name, but I\u2019m sure it\u2019s as beautiful as you are. I\u2019m (your name).\r\n\r\n52. You are astoundingly gorgeous, but I can tell that\u2019s the least interesting thing about you. I\u2019d love to know more.\r\n\r\n53.\u00a0The sparkle in your eyes is so bright, the sun must be jealous.\r\n\r\n54. One night I looked up at the stars and thought, \u2018Wow, how beautiful.\u2019 But now that I\u2019m looking at you, nothing else can compare.\r\n\r\n55. If I had a nickel for every time I saw someone as beautiful as you, I\u2019d still only have five cents.\r\n\r\n56.\u00a0If beauty were time, you\u2019d be eternity.\r\n\r\n57. I think the only way you could possibly be more beautiful is if I got to know you.\r\n\r\n58. I don\u2019t know which is prettier today\u2014the weather, or your eyes.\r\n\r\n59. I swear someone stole the stars from the sky and put them in your eyes.\r\n\r\n60. In my opinion, there are three kinds of beautiful: Cute, pretty, and sexy. Somehow, you manage to be all three.\r\n\r\n\r\nCute Pick Up Lines for Girls\r\n61. I\u2019m not usually religious, but when I saw you, I knew you were the answer to my prayers.\r\n\r\n62. (Hold out your hand) Hey, I\u2019m going for a walk. Would you mind holding this for me?\r\n\r\n63. Do you believe in love at first sight, or should I try walking by again?\r\n\r\n64. I\u2019m really glad I just bought life insurance, because when I saw you, my heart stopped.\r\n\r\n65. I\u2019m not photographer, but I can definitely picture us together.\r\n\r\n66. Would you mind giving me a pinch? You\u2019re so cute, I must be dreaming.\r\n\r\n67. Wow, when God made you, he was seriously showing off.\r\n\r\n68. Excuse me, do you have the time? I just want to remember the exact minute I got a crush on you.\r\n\r\n69. Kiss me if I\u2019m wrong but, dinosaurs still exist, right?\r\n\r\n70.\u00a0If I were a cat, I\u2019d spend all nine of my lives with you.\r\n\r\n\r\n\r\n71. You know, I had a pickup line ready to go, but you\u2019re so hot it just left my mind.\r\n\r\n72. When I text you goodnight later, what phone number should I use?\r\n\r\n73. I saw you walking by and I had to come say hello. I love your style. My name\u2019s (your name).\r\n\r\n74. I\u2019m not currently an organ donor, but I\u2019d be happy to give you my heart.\r\n\r\n75. I was going to say something really sweet about you, but when I saw you, I became speechless.\r\n\r\n76.You know, I believe that honesty is the best policy, so to be perfectly honest, you\u2019re the sexiest man I\u2019ve ever seen.\r\n\r\n77. I\u2019d say, \u2018God bless you,\u2019 but it looks like he already did.\r\n\r\n78. You must be a hell of a thief, because you managed to steal my heart from across the room.\r\n\r\n79. There must be something wrong with my eyes\u2014I can\u2019t seem to take them off of you.\r\n\r\n80. If you let me borrow a kiss, I promise I\u2019ll give it right back.\r\nCute Pick Up Lines to Use at a Bar\r\n81. My friends bet me I couldn\u2019t talk to the prettiest girl in the bar. Want to use their money to buy some drinks?\r\n\r\n82. Trust me, I\u2019m not drunk; I\u2019m just intoxicated by you.\r\n\r\n83. I seem to have lost my number\u2014can I have yours?\r\n\r\n84. I was just trying to buy a drink here, but you\u2019re very distracting.\r\n\r\n85. I started reading\/watching an interesting book\/show last week, and I\u2019d love to discuss it with someone. Have you heard of it?\r\n\r\n86. You see my friend over there? S\/he wants to know if you think I\u2019m cute.\r\n\r\n87. I was going to call you beautiful, but then I realized I don\u2019t have your number yet.\r\n\r\n88. You: Are you good at math?\r\nThem: No (or Yes)\r\nYou: Me neither (or Me too). But the only number I care about is yours.\r\n\r\n89. I\u2019m surprised the restaurant\/bar\/etc. hasn\u2019t asked you to leave yet. You\u2019re so beautiful you\u2019re making all the other girls look bad.\r\n\r\n90. Excuse me, I don\u2019t mean to intrude, but you owe me a drink (pause), because when I saw you, I dropped mine.\r\n\r\n\r\n\r\n91. Are you any good at boxing? Because you look like a knockout.\r\n\r\n92. It\u2019s never easy meeting a complete stranger\u2014especially one as beautiful as you\u2014without being properly introduced. But can we try anyway?\r\n\r\n93. I wish I\u2019d paid more attention to science in high school, because you and I\u2019ve got chemistry and I want to know all about it.\r\n\r\n94. Hi, my name is (your name), but you can call me tonight or tomorrow.\r\n\r\n95. Do I know you? (pause) Oh, sorry, it\u2019s just that you look just like my next girlfriend.\r\n\r\n96. If I were to ask you out on a date, would your answer be the same as the answer to this question?\r\n\r\n97. Hey, do you mind if we take a picture together? I just want to show my mom what my next girlfriend looks like.\r\n\r\n98.\u00a0You look like you know how to have a good time. Been on any adventures lately?\r\n\r\n99. You know, I\u2019m actually terrible at flirting. How about you try to pick me up instead?\r\n\r\n100. Do you have a name, or can I just call you \u2018mine?\u2019\r\n\r\n101. I\u2019m not sure what it is yet, but something about you seems really interesting.\r\n\r\nCheck out:\r\n\r\n250 Questions to Ask a Guy\r\n250 Never Have I Ever Questions\r\n250 \"Would You Rather..?\" Questions\r\n250 Truth or Dare Questions","description":"Whether you need cheesy pick up lines or corny pick-up lines, here are 101 funny, clever, cute, mildly cringy pick up lines that actually work for guys and girls.","wordCount":2088,"datePublished":"2020-10-01T15:15:30-04:00","dateModified":"2020-12-10T11:42:04-04:00","author":{"@type":"Person","name":"Maryn Liles","jobTitle":"editor"},"image":{"@type":"ImageObject","url":"https:\/\/parade.com\/wp-content\/uploads\/2020\/05\/pickup-lines-ftr.jpg","width":1240,"height":775},"keywords":"\"entertainment\",\"cheesy pick up lines\",\"funny pick up lines\",\"pick up lines\""}</script>
<link rel="amphtml" href="https://parade.com/1039985/marynliles/pick-up-lines/amp/"><script type='text/javascript'>
    var _sf_async_config = _sf_async_config || {};
    /** CONFIGURATION START **/
    _sf_async_config.uid = 17212;
    _sf_async_config.domain = 'parade.com';
    _sf_async_config.useCanonical = true;
    _sf_async_config.flickerControl= true;
    _sf_async_config.useCanonicalDomain = true;
    var flickerTimeout = 1000;
    var flickerCss = 'body, .wf-active h1, .wf-active h2, ' +
        '.wf-active h3, .wf-active h4, .wf-active h5, ' +
        '.wf-active h6, .wf-active p, .wf-active blockquote, ' +
        '.wf-active span, .wf-active q, .wf-active a { visibility: hidden !important; }';
    /** CONFIGURATION END **/

    (function() {

        function chartbeatConsentActions() {
            //Loads Chartbeat Headline Testing javascript
            window._sf_endpt = (new Date()).getTime();
            var e = document.createElement('script');
            e.setAttribute('language', 'javascript');
            e.setAttribute('type', 'text/javascript');
            e.setAttribute('async', '');
            e.setAttribute('src', '//static.chartbeat.com/js/chartbeat_mab.js');
            document.head.appendChild(e);
        }

        function chartbeatNonConsentActions() {
            flickerControlRemoval();
        }

        /**
         * Loads style element that hides all page elements
         */
        function loadFlickerControlStyle() {
            var style = document.createElement('style');
            style.setAttribute('id', 'chartbeat-flicker-control-style');
            style.setAttribute('type', 'text/css');
            style.innerHTML = flickerCss;
            document.head.appendChild(style);
        }

        /**
         * Removes style element that hides page elements
         */
        function flickerControlRemoval() {
            var hider = document.getElementById('chartbeat-flicker-control-style');
            if (hider) {
                hider.parentNode.removeChild(hider);
            }
        }

        loadFlickerControlStyle();

        window.setTimeout(flickerControlRemoval, flickerTimeout);

        window.ConsentManager.registerVendorHandler("s28", chartbeatConsentActions, chartbeatNonConsentActions, "Chartbeat Mab & Style add");
    })();
</script>

<script src="https://use.typekit.net/fpk3xgr.js"></script>
<script>try{Typekit.load({ async: true });}catch(e){}</script>
<style type="text/css">
.wf-loading h1, .wf-loading h2, .wf-loading h3, .wf-loading h4, .wf-loading h5, .wf-loading h6, .wf-loading p, .wf-loading blockquote,
.wf-loading span, .wf-loading q, .wf-loading div, .wf-loading a { color: transparent; visibility: hidden; }

.wf-active h1, .wf-active h2, .wf-active h3, .wf-active h4, .wf-active h5, .wf-active h6, .wf-active p, .wf-active blockquote,
.wf-active span, .wf-active q, .wf-active a { visibility: visible; }

.wf-in-active h1, .wf-in-active h2, .wf-in-active h3, .wf-in-active h4, .wf-in-active h5, .wf-in-active h6, .wf-in-active p, .wf-in-active blockquote,
.wf-in-active span, .wf-in-active q, .wf-in-active a { visibility: visible; }</style>

</head>
<body class="page_article without_gallery post-template-default single single-post postid-1039985 single-format-standard logged_out unstyled">
<div class="globalwrapper">
<header class="global ">
<div class="nav-hidden closed">
<div class="hamburger-container">
<input type="checkbox" class="hamburger-indicator" autocomplete="off">
<label for="hamburger">
<span class="hamburger-line"></span>
<span class="hamburger-line"></span>
<span class="hamburger-line"></span>
</label>
</div>
<div class="brand-logo featured" id="logo">
<a href="/" class="logo">
<svg role="img" aria-label="Parade Logo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 118.99 26"><path d="M108,16.31h12c.33,0,.48-.12.48-.38-.27-4.4-3.32-7.55-8.42-7.55h0c-4.87,0-9.12,3.79-9.12,9.62s3.42,9,9.54,9a9.75,9.75,0,0,0,4.32-1h0a5.61,5.61,0,0,0,3.47-4.79,2.66,2.66,0,0,0-2.88-2.68,2.76,2.76,0,0,0,0,5.51,2.57,2.57,0,0,0,1.1-.21,4.38,4.38,0,0,1-1.88,1.76h0a6.41,6.41,0,0,1-2.91.62c-3.69,0-5.74-3.7-5.74-8.09V17.8C108,17.27,108,16.8,108,16.31Zm4.06-7.52c2.61,0,3.43,3.12,3.45,7.05H108c.3-4.6,1.78-7,4-7Z" transform="translate(-1.5 -1.32)" style="fill:#212121" /><path d="M100,22.14V1.93c0-.34,0-.61-.39-.61s-1.11.28-2.42.48a35.79,35.79,0,0,1-5.48.49v.44c3.16,0,3.67.28,3.67,3.71v6.11c-.74-2.86-2.33-4.61-5.13-4.61-3.82,0-7.43,3-7.43,9.94s3.37,9.37,7.25,9.37c2.41,0,3.87-1.32,4.85-3.87h0c.07-.17.13-.34.19-.52v1.21c0,2.2.87,2.89,2.41,2.89h5.14v-.48C100.41,26.48,100,25.85,100,22.14ZM95.41,18a15.11,15.11,0,0,1-.93,5.22h0c-.68,1.73-1.69,3-2.92,3-1.88,0-3.7-1.47-3.7-8.49,0-6.84,1.91-8.8,3.82-8.8,1.39,0,2.61,1.42,3.25,3.78a15.46,15.46,0,0,1,.48,4Z" transform="translate(-1.5 -1.32)" style="fill:#212121" /><path d="M78.8,22.13V14.7c0-4.29-3.13-6.32-8.61-6.32-.42,0-.85,0-1.27.06h0c-3.63.32-5.93,2-5.93,4.2a2.76,2.76,0,0,0,3,2.79,2.73,2.73,0,0,0,2.84-2.73A2.63,2.63,0,0,0,66.14,10a3.07,3.07,0,0,0-.73.11A6.77,6.77,0,0,1,69,8.88h0a8.83,8.83,0,0,1,.89,0c2.51,0,4.15,1.36,4.15,3.92v.76c0,1.39-1,2.11-2.36,2.62l-.36.13c-2.09.66-4.42,1-6.2,1.79A4.46,4.46,0,0,0,62,22.5c0,3.25,2.36,4.5,5.63,4.5,2.69,0,4.63-.83,5.87-2.75l.18-.31s.15-.27.22-.43h0v.27c0,2.17.9,2.87,2.42,2.87h5.17v-.46C79.31,26.19,78.77,25.64,78.8,22.13ZM74,20.88a6.12,6.12,0,0,1-.82,2.95,1.78,1.78,0,0,0-.12.18,3.59,3.59,0,0,1-2.85,1.79c-1.79,0-2.94-1.07-2.94-3.59,0-3.45,1.19-4.53,4.12-5.48l.43-.14A5.6,5.6,0,0,0,74,15.26Z" transform="translate(-1.5 -1.32)" style="fill:#212121" /><path d="M12.81,17.65h.62c8.18,0,11.87-2.58,11.87-7.4S21.07,3,13.58,3H1.68V3.5C5.46,3.5,6,4,6,7.57v15c0,3.41-.77,4-4.5,4V27H15.23V26.5c-3.57-.09-4.43-.59-4.41-4V17.65Zm-2-14.15h2c5,0,7.43,2,7.43,6.58s-2.6,7.07-7.43,7.06h-2Z" transform="translate(-1.5 -1.32)" style="fill:#212121" /><path d="M58.77,8.43a6,6,0,0,0-4.58,2.35h0a7.25,7.25,0,0,0-1.25,2.44V9.17c0-.33,0-.59-.39-.59s-.93.15-2,.3a35.11,35.11,0,0,1-5.12.41v.44c2.55,0,3,.33,3,3.49v9.26c0,3.39-.49,4-2.5,4.05h0c-1.94,0-2.38-.66-2.35-4.11V14.81c0-4.37-3-6.43-8.32-6.43-.42,0-.83,0-1.24.06-3.51.33-5.73,2.07-5.73,4.28a2.84,2.84,0,0,0,5.67.06A2.62,2.62,0,0,0,31.29,10a2.69,2.69,0,0,0-.7.11A6.23,6.23,0,0,1,34,8.89a8.12,8.12,0,0,1,.86,0,3.68,3.68,0,0,1,4,4v.77c0,1.41-.95,2.15-2.29,2.67l-.34.13c-2,.68-4.28,1-6,1.83a4.53,4.53,0,0,0-3,4.52c0,3.3,2.28,4.57,5.44,4.57,2.57,0,4.42-.82,5.63-2.71,0-.06.07-.12.1-.19l.19-.38.14-.26V24c0,2.22.88,2.93,2.35,2.93H55.52v-.48c-2.11,0-2.64-.56-2.61-4.13V17.11A9.62,9.62,0,0,1,54.65,11,4.85,4.85,0,0,1,57.8,9.15a2.51,2.51,0,0,0-1.35,2.44,2.75,2.75,0,0,0,2.82,2.71A2.72,2.72,0,0,0,62,11.38,3,3,0,0,0,58.77,8.43ZM38.91,21.09a6.29,6.29,0,0,1-.7,2.82h0l-.21.37a3.48,3.48,0,0,1-2.76,1.83c-1.73,0-2.84-1.1-2.84-3.66,0-3.51,1.15-4.6,4-5.58l.41-.14a5.39,5.39,0,0,0,2.11-1.36Z" transform="translate(-1.5 -1.32)" style="fill:#212121" /></svg>
</a>
</div>
<ul class="items vertical menu accordion-menu" data-accordion-menu data-parent-link="true" data-multi-open="false">
<li class="accordion subnav loginNav">
<a href="javascript:void(0);" class="nav-link">LOGIN</a>
<div class="user_login login panel menu vertical nested secondary-links">
<div class="login_form login-signup">
<div class="login_form_content">
<form name="loginform" id="loginform" action="" method="post">
<form>
<fieldset>
<div class="input_group">
<input type="text" name="log" id="user_login--login" class="field" value="" placeholder="Email or Username" data-parade-type="email" autocomplete="username">
<div class="error_message">
Please enter a valid email address.
</div>
</div>
<div class="input_group">
<input type="password" name="pwd" id="user_pass" value="" placeholder="Password" class="field" autocomplete="current-password">
<div class="error_message">
Incorrect email or username/password combination.
</div>
</div>
<div class="submit_container">
<input type="submit" name="wp-submit" class="submit" value="Log in" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="login-submit" data-parade-views="false" data-parade-touches="true" data-parade-clicks="true" data-parade-mouseovers="false">
<input type="hidden" name="redirect_to" value="https://parade.com/1039985/marynliles/pick-up-lines/">
<input type="hidden" name="testcookie" value="1">
<input type="hidden" name="isfrontnedlogin" value="1">
<p>
<a class="password" href="https://parade.com/reset/">Forgot Password?</a> | <a class="signup" href="https://parade.com/register/">Sign Up</a>
</p>
</div>
<span class="loading_spinner" style="display:none;">
<span class="bar bar_1"></span>
<span class="bar bar_2"></span>
<span class="bar bar_3"></span>
<span class="bar bar_4"></span>
<span class="bar bar_5"></span>
<span class="bar bar_6"></span>
<span class="bar bar_7"></span>
<span class="bar bar_8"></span>
<span class="bar bar_9"></span>
<span class="bar bar_10"></span>
<span class="bar bar_11"></span>
<span class="bar bar_12"></span>
</span>
</fieldset>
</form>
</form>
</div>
</div>
</div>
</li>
<li class="accordion subnav ">
<a href="javascript:void(0);" class="nav-link">ENTERTAINMENT</a>
 <ul class="panel menu vertical nested secondary-links">
<li class=""><a class="secondary-link" href="https://parade.com/entertainment/">LATEST</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/books/">READ</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/movies-tv/">WATCH</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/music-podcasts/">LISTEN</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/magazine/">MAGAZINE</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/cinema-sins/">CINEMA SINS</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/video-games/">GAME ON!</a></li>
</ul>
</li>
<li class="accordion subnav ">
<a href="javascript:void(0);" class="nav-link">POP CULTURE</a>
<ul class="panel menu vertical nested secondary-links">
<li class=""><a class="secondary-link" href="https://parade.com/culture/">LATEST</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/celebrities/">CELEBS</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/royal-family/">ROYALS</a></li>
</ul>
</li>
<li class="accordion subnav ">
<a href="javascript:void(0);" class="nav-link">FOOD &amp; DRINK</a>
<ul class="panel menu vertical nested secondary-links">
<li class=""><a class="secondary-link" href="https://parade.com/food/">LATEST</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/tag/recipes/">RECIPES</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/969844/parade/weight-watchers-recipes/">WEIGHT WATCHERS RECIPES</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/chicken/">CHICKEN RECIPES</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/budget-meals/">ON A BUDGET</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/easy-meals/">EASY MEALS</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/healthy-recipes/">HEALTHY RECIPES</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/easy-dinners/">DIN FOR THE WIN</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/dessert/">DESSERT</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/baking/">BAKING ADVENTURE</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/st-patricks-day/">ST. PATRICK'S DAY</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/pop-kitchen/">POP KITCHEN</a></li>
<li class=""><a class="secondary-link" href="https://www.youtube.com/channel/UCH0nW7Z_xsKQmVL1rml36Vg">VIDEOS</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/tag/plate-it-perfect/">PLATE IT PERFECT</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/what-america-eats/">WHAT AMERICA EATS</a></li>
</ul>
</li>
<li class="accordion subnav ">
<a href="javascript:void(0);" class="nav-link">WELLNESS</a>
<ul class="panel menu vertical nested secondary-links">
<li class=""><a class="secondary-link" href="https://parade.com/health/">LATEST</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/cold-and-flu/">COLD AND FLU STARTER KIT</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/heart-health/">HEART HEALTH STARTER KIT</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/super-survivors/">SUPER SURVIVORS STARTER KIT</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/covid-vaccine/">COVID-19 VACCINE STARTER KIT</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/healthy-now/">HEALTHY NOW</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/mental-health/">MENTAL HEALTH</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/self-care/">SELF-CARE</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/caregiver-boot-camp/">CAREGIVING</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/numbrix/">NUMBRIX</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/986848/nancy_henderson/types-of-diets/">TYPES OF DIETS</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/970087/lisamulcahy/keto-diet-food-list/">KETO APPROVED FOODS</a></li>
</ul>
</li>
<li class="accordion subnav ">
<a href="javascript:void(0);" class="nav-link">LIFE</a>
<ul class="panel menu vertical nested secondary-links">
<li class=""><a class="secondary-link" href="https://parade.com/living/">LATEST</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/parade-picks/">SHOPPING, DEALS & FREEBIES</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/family/">PARENT VS. PANDEMIC</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/pets-animals/">PET PARENT CENTRAL</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/books/">BOOKS</a></li>
<li class=""><a class="secondary-link" href="https://www.youtube.com/playlist?list=PLs2k2TJZZt8npapRxMtbwopZatKJY32p5">DELUXE VS. DUPE</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/travel/">TRAVEL</a></li>
<li class=""><a class="secondary-link" href="https://parade.com/970149/ashleylauretta/best-workout-apps/">BEST FREE WORKOUT APPS</a></li>
</ul>
</li>
</ul>
<div class="newsletter-signup">
<form>
<h5>Subscribe to our Newsletter</h5>
<fieldset>
<input class="field" type="text" name="email" placeholder="Email Address">
<input class="submit" type="submit" value="">
<span class="loading_spinner" style="display:none;">
<span class="bar bar_1"></span>
<span class="bar bar_2"></span>
<span class="bar bar_3"></span>
<span class="bar bar_4"></span>
<span class="bar bar_5"></span>
<span class="bar bar_6"></span>
<span class="bar bar_7"></span>
<span class="bar bar_8"></span>
<span class="bar bar_9"></span>
<span class="bar bar_10"></span>
<span class="bar bar_11"></span>
<span class="bar bar_12"></span>
</span>
</fieldset>
<p class="error_message" style="display:none;">
There was an error in your submission. Please try again.
</p>
<p class="note" style="display:none;"></p>
</form>
<p><a href="/user-agreement">Terms & Conditions</a> and <a href="/privacy-policy">Privacy Policy</a></p>
</div>
<div class="social-links">
<span class="instagram"><a href="https://www.instagram.com/parade.media/" target="_blank"></a></span>
<span class="pinterest"><a href="https://www.pinterest.com/parademag/" target="_blank"></a></span>
<span class="youtube"><a href="https://www.youtube.com/user/ParadeMagazine/" target="_blank"></a></span>
<span class="facebook"><a href="https://www.facebook.com/parademag/" target="_blank"></a></span>
<span class="twitter"><a href="https://twitter.com/ParadeMagazine" target="_blank"></a></span>
</div>
<div class="footer-content">
<ul class="sitemap-items">
</ul>
<div class="legal-notice">
<p>
© 2020 AMG/Parade. All rights reserved.
</p>
<p class="policy">
Your use of this website constitutes and manifests your acceptance of our <strong><a href="/user-agreement">User Agreement</a></strong>, <strong><a href="/privacy-policy">Privacy Policy</a></strong>, <strong><a href="/cookie-policy">Cookie Notification</a></strong>, and awareness of the <strong><a href="/privacy-policy/#cpr">California Privacy Rights</a></strong>. Pursuant to U.S. Copyright law, as well as other applicable federal and state laws, the content on this website may not be reproduced, distributed, displayed, transmitted, cached, or otherwise used, without the prior, express, and written permission of Athlon Media Group. <strong><a href="/privacy-policy/#third-party">Ad Choices</a></strong>
</p>
</div>
</div>
</div>
<div class="nav-overlay hidden"></div>
</header>
<nav class="grid-x main-navigation nav-down" id="main-navigation">
<div class="hamburger-container">
<input type="checkbox" class="hamburger-indicator" autocomplete="off">
<label for="hamburger">
<span class="hamburger-line"></span>
<span class="hamburger-line"></span>
<span class="hamburger-line"></span>
</label>
</div>
<div class="brand-logo featured" id="logo">
<a href="/" class="logo">
<svg role="img" aria-label="Parade Logo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 118.99 26"><path d="M108,16.31h12c.33,0,.48-.12.48-.38-.27-4.4-3.32-7.55-8.42-7.55h0c-4.87,0-9.12,3.79-9.12,9.62s3.42,9,9.54,9a9.75,9.75,0,0,0,4.32-1h0a5.61,5.61,0,0,0,3.47-4.79,2.66,2.66,0,0,0-2.88-2.68,2.76,2.76,0,0,0,0,5.51,2.57,2.57,0,0,0,1.1-.21,4.38,4.38,0,0,1-1.88,1.76h0a6.41,6.41,0,0,1-2.91.62c-3.69,0-5.74-3.7-5.74-8.09V17.8C108,17.27,108,16.8,108,16.31Zm4.06-7.52c2.61,0,3.43,3.12,3.45,7.05H108c.3-4.6,1.78-7,4-7Z" transform="translate(-1.5 -1.32)" style="fill:#212121" /><path d="M100,22.14V1.93c0-.34,0-.61-.39-.61s-1.11.28-2.42.48a35.79,35.79,0,0,1-5.48.49v.44c3.16,0,3.67.28,3.67,3.71v6.11c-.74-2.86-2.33-4.61-5.13-4.61-3.82,0-7.43,3-7.43,9.94s3.37,9.37,7.25,9.37c2.41,0,3.87-1.32,4.85-3.87h0c.07-.17.13-.34.19-.52v1.21c0,2.2.87,2.89,2.41,2.89h5.14v-.48C100.41,26.48,100,25.85,100,22.14ZM95.41,18a15.11,15.11,0,0,1-.93,5.22h0c-.68,1.73-1.69,3-2.92,3-1.88,0-3.7-1.47-3.7-8.49,0-6.84,1.91-8.8,3.82-8.8,1.39,0,2.61,1.42,3.25,3.78a15.46,15.46,0,0,1,.48,4Z" transform="translate(-1.5 -1.32)" style="fill:#212121" /><path d="M78.8,22.13V14.7c0-4.29-3.13-6.32-8.61-6.32-.42,0-.85,0-1.27.06h0c-3.63.32-5.93,2-5.93,4.2a2.76,2.76,0,0,0,3,2.79,2.73,2.73,0,0,0,2.84-2.73A2.63,2.63,0,0,0,66.14,10a3.07,3.07,0,0,0-.73.11A6.77,6.77,0,0,1,69,8.88h0a8.83,8.83,0,0,1,.89,0c2.51,0,4.15,1.36,4.15,3.92v.76c0,1.39-1,2.11-2.36,2.62l-.36.13c-2.09.66-4.42,1-6.2,1.79A4.46,4.46,0,0,0,62,22.5c0,3.25,2.36,4.5,5.63,4.5,2.69,0,4.63-.83,5.87-2.75l.18-.31s.15-.27.22-.43h0v.27c0,2.17.9,2.87,2.42,2.87h5.17v-.46C79.31,26.19,78.77,25.64,78.8,22.13ZM74,20.88a6.12,6.12,0,0,1-.82,2.95,1.78,1.78,0,0,0-.12.18,3.59,3.59,0,0,1-2.85,1.79c-1.79,0-2.94-1.07-2.94-3.59,0-3.45,1.19-4.53,4.12-5.48l.43-.14A5.6,5.6,0,0,0,74,15.26Z" transform="translate(-1.5 -1.32)" style="fill:#212121" /><path d="M12.81,17.65h.62c8.18,0,11.87-2.58,11.87-7.4S21.07,3,13.58,3H1.68V3.5C5.46,3.5,6,4,6,7.57v15c0,3.41-.77,4-4.5,4V27H15.23V26.5c-3.57-.09-4.43-.59-4.41-4V17.65Zm-2-14.15h2c5,0,7.43,2,7.43,6.58s-2.6,7.07-7.43,7.06h-2Z" transform="translate(-1.5 -1.32)" style="fill:#212121" /><path d="M58.77,8.43a6,6,0,0,0-4.58,2.35h0a7.25,7.25,0,0,0-1.25,2.44V9.17c0-.33,0-.59-.39-.59s-.93.15-2,.3a35.11,35.11,0,0,1-5.12.41v.44c2.55,0,3,.33,3,3.49v9.26c0,3.39-.49,4-2.5,4.05h0c-1.94,0-2.38-.66-2.35-4.11V14.81c0-4.37-3-6.43-8.32-6.43-.42,0-.83,0-1.24.06-3.51.33-5.73,2.07-5.73,4.28a2.84,2.84,0,0,0,5.67.06A2.62,2.62,0,0,0,31.29,10a2.69,2.69,0,0,0-.7.11A6.23,6.23,0,0,1,34,8.89a8.12,8.12,0,0,1,.86,0,3.68,3.68,0,0,1,4,4v.77c0,1.41-.95,2.15-2.29,2.67l-.34.13c-2,.68-4.28,1-6,1.83a4.53,4.53,0,0,0-3,4.52c0,3.3,2.28,4.57,5.44,4.57,2.57,0,4.42-.82,5.63-2.71,0-.06.07-.12.1-.19l.19-.38.14-.26V24c0,2.22.88,2.93,2.35,2.93H55.52v-.48c-2.11,0-2.64-.56-2.61-4.13V17.11A9.62,9.62,0,0,1,54.65,11,4.85,4.85,0,0,1,57.8,9.15a2.51,2.51,0,0,0-1.35,2.44,2.75,2.75,0,0,0,2.82,2.71A2.72,2.72,0,0,0,62,11.38,3,3,0,0,0,58.77,8.43ZM38.91,21.09a6.29,6.29,0,0,1-.7,2.82h0l-.21.37a3.48,3.48,0,0,1-2.76,1.83c-1.73,0-2.84-1.1-2.84-3.66,0-3.51,1.15-4.6,4-5.58l.41-.14a5.39,5.39,0,0,0,2.11-1.36Z" transform="translate(-1.5 -1.32)" style="fill:#212121" /></svg>
</a>
</div>
<div class="left-nav">
<div class="desktop-display scrollable">
<ul class="items secondary-nav-items">
<li>
<a href="https://parade.com/entertainment/" class="nav-link">ENTERTAINMENT</a>
</li>
<li>
<a href="https://parade.com/food/" class="nav-link">FOOD & DRINK</a>
</li>
<li>
<a href="https://parade.com/easter/" class="nav-link">EASTER IDEAS</a>
</li>
<li>
<a href="https://parade.com/tag/outlander/" class="nav-link">DROUGHTLANDER</a>
</li>
<li>
<a href="https://parade.com/cold-and-flu/" class="nav-link">COLD & FLU</a>
</li>
<li>
<a href="https://parade.com/covid-vaccine/" class="nav-link">COVID-19 INFO</a>
</li>
<li>
<a href="https://parade.com/super-survivors/" class="nav-link">SUPER SURVIVORS</a>
</li>
</ul>
</div>
</div>
<div class="desktop-display">
<div class="right-nav">
<ul class="items">
<li class="newsletter">
<a href="/newsletter" class="nav-link"></a>
</li>
<li class="user-login">
<a href="/login" class="nav-link avatar logged-out"></a>
</li>
<li class="search">
<div class="header_button nav-item nav-item--search">
<div class="expanding-menu mobile-search same-template">
<div class="content">
<form method="get" action="https://parade.com/" data-parade-type="menu-item" data-parade-menu-id="search" data-parade-location-types="menu-item" data-parade-location-ids="header" data-parade-views="false" data-parade-touches="true" data-parade-clicks="true" data-parade-mouseovers="true">
<fieldset>
<img src="https://ath-clients.s3.amazonaws.com/parade/assets/search.svg" class="svg" alt="" data-parade-image-inlining="true" data-parade-image="">
<input type="text" class="field" name="q" placeholder="Search Parade">
</fieldset>
</form>
</div>
</div>
<a href="#" class="action action--search" data-target="mobile-search"><img src="https://ath-clients.s3.amazonaws.com/parade/assets/search.svg" alt="Search Icon"></a>
</div>
</li>
<div class="main-nav--dropdown">
<div class="nav-dropdown--mobile-user">
<div class="expanding_menu mobile_user">
<div class="header_login" data-state="logged_out">
<div class="user-pointer"></div>

<div class="header_login_content" data-state="logged_out" style="display: block;">

<div class="login_parade">
<div class="login_parade_content">
<a href="https://parade.com/login/?redirect_to=https%3A%2F%2Fparade.com%2F1039985%2Fmarynliles%2Fpick-up-lines%2F">Log In</a> or <a href="https://parade.com/register/?redirect_to=https%3A%2F%2Fparade.com%2F1039985%2Fmarynliles%2Fpick-up-lines%2F">Sign Up</a> with Parade.com
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</ul>
</div>
</div>
</nav>

<div class="page_wrapper">
<div class="page_content">
<div class="leaderboard_ad">
<div class="ad-wrapper">
<div id='div-gpt-ad-728-top-0' class="ad-728-top">
<script type='text/javascript'>
            window.AdManager.displaySlot("728_top", "div-gpt-ad-728-top-0");
        </script>
</div>
</div>
</div>
<section class="row">
<article class="span8 page_article   entertainment ">
<section class='main_content'>
<section class='body_column'>
<header class="page_header" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="article-header" data-parade-views="false" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="article-header" data-parade-views="false" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">
<h3>
<a class="category" href="https://parade.com/entertainment/" title="Go to the Entertainment channel.">Entertainment</a>
</h3>
<h1 data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="article-headline" data-parade-views="false" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="article-headline" data-parade-views="false" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">
<span class="text">101 Cheesy-But-Cute Pick Up Lines That'll Kick Your Flirting Game Into High Gear&nbsp;</span>
</h1>
<div class="details">
<time pubdate>October 1, 2020 &ndash; 3:15 PM</time>
<span class="comment_count">&nbsp;&ndash;&nbsp;0&nbsp;Comments</span>
<div class="clear"></div>
</div>
<div class="sharing" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="article-header-social" data-parade-views="false" data-parade-touches="true" data-parade-clicks="true" data-parade-mouseovers="true" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="article-header-social" data-parade-views="false" data-parade-touches="true" data-parade-clicks="true" data-parade-mouseovers="true">
<div class="addthis_toolbox addthis_default_style addthis_32x32_style">
<a href='#addthis' class="addthis_button_facebook" data-parade-type="social" data-parade-location-types="social"></a>
<a href='#addthis' class="addthis_button_twitter" data-parade-type="social" data-parade-location-types="social"></a>
<a href='#addthis' class="addthis_button_pinterest_share at300b" data-parade-type="social" data-parade-location-types="social" target="_self"></a>
<a href="#addthis" class="addthis_button_compact" data-parade-type="social" data-parade-location-types="social" data-parade-location-ids="counter"></a>
<a href="#addthis" class="addthis_counter addthis_bubble_style" data-parade-type="social" data-parade-location-types="social" data-parade-location-ids="bubble"></a>
</div>
</div>
</header>
<section class="author_block collapsed">
<article>
<header>
<figure>
<a href="https://parade.com/member/marynliles/" rel="author" data-parade-type="member" data-parade-member-id="687561" data-parade-location-types="member" data-parade-location-ids="article-header" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<img class="authorblock-avatar photo" data-parade-avatar-image="https://secure.gravatar.com/avatar/0f1cd734d2ae976089b5f960fa1887c3?s=136&amp;d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D136&amp;r=G" data-parade-avatar-image-placeholding="" src="https://secure.gravatar.com/avatar/0f1cd734d2ae976089b5f960fa1887c3?s=136&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D136&r=G" alt="Maryn Liles" nopin="nopin">
</a>
</figure>
<h3 class="author_byline">
<span class="by">By&nbsp;</span><a href="https://parade.com/member/marynliles/" rel="author"><span class="authorblock-display-name name fn" data-parade-type="member" data-parade-member-id="687561" data-parade-location-types="member" data-parade-location-ids="article-header" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Maryn Liles</span></a>&nbsp;
<span class="role"></span><span class="org" style="display:none">Parade</span></span>
</h3>
</header>
<section class="more_articles">
<h3>
More by
<span class="nickname">Maryn</span>
</h3>
<ul><li><a href='https://parade.com/1181867/marynliles/how-long-does-it-take-to-get-divorced/' data-parade-type="article" data-parade-post-id="1181867" data-parade-author-id="687561" data-parade-post-description="" data-parade-post-title="How Long Does It Take to Get a Divorce? Here&#039;s What You Should Know About a Typical Divorce Timeline" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/How-Long-Does-It-Take-to-Get-a-Divorce.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="article-header" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">How Long Does It Take to Get a Divorce? Here&#8217;s What You Should Know About a Typical Divorce Timeline</a></li><li><a href='https://parade.com/1181864/marynliles/should-i-get-a-divorce/' data-parade-type="article" data-parade-post-id="1181864" data-parade-author-id="687561" data-parade-post-description="" data-parade-post-title="Should You Get a Divorce? 10 Signs Your Marriage Might Be Over" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/should-i-get-a-divorce.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="article-header" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Should You Get a Divorce? 10 Signs Your Marriage Might Be Over</a></li><li><a href='https://parade.com/1172098/marynliles/cricut-easter-projects/' data-parade-type="article" data-parade-post-id="1172098" data-parade-author-id="687561" data-parade-post-description="" data-parade-post-title="50 of the Cutest Easter Craft Ideas (Made Using a Cricut!) We&#039;ve Ever Seen" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/Cricut-Easter-Crafts-3.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="article-header" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">50 of the Cutest Easter Craft Ideas (Made Using a Cricut!) We&#8217;ve Ever Seen</a></li></ul>
</section>
<div class="toggle">
<a href="#" class="button" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="article-header" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="icon"></span>
</a>
</div>
</article>
</section>
<section class="body">

<div class="figure_block feature" data-parade-type="media" data-parade-location-types="media" data-parade-location-ids="featured-image" data-parade-views="false" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">
<figure>
<a href="https://parade.com/1041982/pickup-lines-ftr/">
<img class="addthis_shareable" src="https://static.parade.com/wp-content/uploads/2020/05/pickup-lines-ftr.jpg" alt="pickup-lines-ftr" data-parade-image="" data-parade-image-placeholding="">
</a>
</figure>
<figcaption>
<span class="credit">(iStock)</span>
</figcaption>
</div>
<span data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="article" data-parade-views="false" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">
<p class="first">The <strong>best pick-up lines</strong>&mdash;whether they&rsquo;re cheesy, funny pick-up lines that&rsquo;ll get someone laughing or clever pick-up lines that&rsquo;ll make you stand out&mdash;will make breaking the ice and <a href="https://parade.com/969981/parade/conversation-starters/" target="_blank" rel="noopener noreferrer">getting the conversation started</a> a little bit easier.</p><p>Plus, using <a href="https://parade.com/965742/parade/corny-jokes/" target="_blank" rel="noopener noreferrer">corny</a> pick-up lines shows off what a playful personality you have, too&mdash;and who doesn&rsquo;t like that!</p><div class="content_ad_container">
<div class="content_ad" data-parade-type="ad" data-parade-ad-position="300" data-parade-ad-location="content" data-parade-location-types="ad" data-parade-views="true" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="true">
<div class="ad-wrapper">
<div id="div-gpt-ad-300-content-4" class="ad-300-content">
<script type="text/javascript">
            window.AdManager.displaySlot("300_content", "div-gpt-ad-300-content-4");
        </script></div>
</div>
</div>
</div><p>So whether you&rsquo;re looking for cute pick-up lines to tell a girl you like her or need some cheesy pick-up lines to text to a guy you&rsquo;re into, these 101 best funny pick up lines can help you get your flirt on.</p><h2>Best Pick Up Lines</h2><p>1. I hope you know CPR, because you just took my breath away!</p><p>2. So, aside from taking my breath away, what do you do for a living?</p><p>3. I ought to complain to Spotify for you not being named this week&rsquo;s hottest single.</p><p>4. Are you a parking ticket? &lsquo;Cause you&rsquo;ve got &lsquo;fine&rsquo; written all over you.</p><p>5. Your eyes are like the ocean; I could swim in them all day.</p><p>6. When I look in your eyes, I see a very kind soul.</p><p>7. If you were a vegetable, you&rsquo;d be a &lsquo;cute-cumber.&rsquo;</p><p>8. Do you happen to have a Band-Aid? &lsquo;Cause I scraped my knees falling for you.</p><p>9. I never believed in love at first sight, but that was before I saw you.</p><p>10. I didn&rsquo;t know what I wanted in a woman until I saw you.</p><div class="figure_block paradeImage wp-media-selected size-100 aligncenter wp-image-1040103"> <figure><img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="Unsplash" class="addthis_shareable at_include" title="Clever pick up lines" data-parade-image-placeholding="true" data-parade-image-inlining="" data-parade-image="https://static.parade.com/wp-content/uploads/2020/05/pick-up-lines-1.jpg"></figure><figcaption><span class="credit">(Unsplash)</span></figcaption></div><p>11. I was wondering if you could tell me: If you&rsquo;re here, who&rsquo;s running Heaven?</p><p>12. No wonder the sky is gray (or dark, if at night)&mdash;all the color is in your eyes.</p><p>13. You&rsquo;ve got everything I&rsquo;ve been searching for, and believe me&mdash;I&rsquo;ve been looking a long time.</p><p>14. You&rsquo;re like a fine wine. The more of you I drink in, the better I feel.</p><p>15. You&rsquo;ve got a lot of beautiful curves, but your <a href="https://parade.com/1045449/marynliles/smile-quotes/" target="_blank">smile</a> is absolutely my favorite.</p><p>16. Are you as beautiful on the inside as you are on the outside?</p><p>17. If being sexy was a crime, you&rsquo;d be guilty as charged.</p><p>18. I was wondering if you&rsquo;re an artist because you were so good at drawing me in.</p><p>19. It says in the Bible to only think about what&rsquo;s pure and lovely&hellip; So I&rsquo;ve been thinking about you all day long.</p><p>20. Do you have a map? I just got lost in your eyes.</p><h2>Funny Pick Up Lines</h2><p>21. I&rsquo;d like to take you to the movies, but they don&rsquo;t let you bring in your own snacks.</p><p>22. You know what you would look really beautiful in? My arms.</p><p>23. I would never play hide and seek with you because someone like you is impossible to find.</p><p>24. Are you a magician? It&rsquo;s the strangest thing, but every time I look at you, everyone else disappears.</p><p>25. I think there&rsquo;s something wrong with my phone. Could you try calling it to see if it works?</p><p>26. Hi, I just wanted to thank you for the gift. (pause) I&rsquo;ve been wearing this smile ever since you gave it to me.</p><p>27. Are you an electrician? Because you&rsquo;re definitely lighting up my day/night!</p><p>28. I&rsquo;ve heard it said that kissing is the &lsquo;language of love.&rsquo; Would you care to have a conversation with me about it sometime?</p><p>29. I always thought happiness started with an &lsquo;h,&rsquo; but it turns out mine starts with &lsquo;u.&rsquo;</p><p>30. I believe in following my dreams. Can I have your Instagram?</p><div class="figure_block paradeImage wp-media-selected size-100 aligncenter wp-image-1040106"> <figure><img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="Unsplash" class="addthis_shareable at_include" title="Funny pick up lines" data-parade-image-placeholding="true" data-parade-image-inlining="" data-parade-image="https://static.parade.com/wp-content/uploads/2020/05/pick-up-lines-61.jpg"></figure><figcaption><span class="credit">(Unsplash)</span></figcaption></div><p>31. Do you know what the Little Mermaid and I have in common? We both want to be part of your world.</p><p>32. If you were a song, you&rsquo;d be the best track on the album.</p><p>33. On a scale of 1 to America, how free are you tonight?</p><p>34. You know, I always thought that Disneyland was the &lsquo;happiest place on Earth,&rsquo; but that was before I got a chance to stand here next to you.</p><p>35. Want to go outside and get some fresh air with me? You just took my breath away.</p><p>36. If you were a taser, you&rsquo;d be set to &lsquo;stun.&rsquo;</p><p>37. If you were a Transformer, you&rsquo;d be &lsquo;Optimus Fine.&rsquo;</p><p>38. Is your name Google? Because you have everything I&rsquo;m searching for.</p><p>39. Do you ever get tired from running through my thoughts all night?</p><p>40. You know, they say that love is when you don&rsquo;t want to sleep because reality is better than your dreams. And after seeing you, I don&rsquo;t think I ever want to sleep again.</p><h2>Cheesy Pick Up Lines for Guys</h2><p>41. Your hand looks heavy&mdash;can I hold it for you?</p><p>42. Are you a time traveler? Because I absolutely see you in my future.</p><p>43. Do you know what my shirt is made of? Boyfriend material.</p><p>44. I thought this was a (bar/restaurant/etc.), but I must be in a museum because you&rsquo;re a piece of art.</p><p>45. You know, your smile has been lighting up the room all night and I just had to come and say hello.</p><p>46. Hi, I&rsquo;m (your name). Do you remember me? Oh, that&rsquo;s right&mdash;we&rsquo;ve only met in my dreams.</p><p>47. What does it feel like to be the most gorgeous girl in the room?</p><p>48. I can&rsquo;t tell if that was an earthquake, or if you just seriously rocked my world.</p><p>49. I just had to tell you, your beauty made me truly appreciate being able to see.</p><p>50. If you were a fruit, you&rsquo;d be a &lsquo;fine-apple.&rsquo;</p><div class="figure_block paradeImage wp-media-selected size-100 aligncenter wp-image-1040104"> <figure><img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="Unsplash" class="addthis_shareable at_include" title="Cute pick up line" data-parade-image-placeholding="true" data-parade-image-inlining="" data-parade-image="https://static.parade.com/wp-content/uploads/2020/05/pick-up-lines-21.jpg"></figure><figcaption><span class="credit">(Unsplash)</span></figcaption></div><p>51. I don&rsquo;t know your name, but I&rsquo;m sure it&rsquo;s as beautiful as you are. I&rsquo;m (your name).</p><p>52. You are astoundingly gorgeous, but I can tell that&rsquo;s the least interesting thing about you. I&rsquo;d love to know more.</p><p>53.&nbsp;The sparkle in your eyes is so bright, the sun must be jealous.</p><p>54. One night I looked up at the stars and thought, &lsquo;Wow, how beautiful.&rsquo; But now that I&rsquo;m looking at you, nothing else can compare.</p><p>55. If I had a nickel for every time I saw someone as beautiful as you, I&rsquo;d still only have five cents.</p><p>56.&nbsp;If beauty were time, you&rsquo;d be eternity.</p><p>57. I think the only way you could possibly be more beautiful is if I got to know you.</p><p>58. I don&rsquo;t know which is prettier today&mdash;the weather, or your eyes.</p><p>59. I swear someone stole the stars from the sky and put them in your eyes.</p><p>60. In my opinion, there are three kinds of beautiful: Cute, pretty, and sexy. Somehow, you manage to be all three.</p><div class="connatix_wrapper"> <script id="e4d29110661e4c899ecdd35094daaf63">    cnxps.cmd.push(function () {      var jsTargeting = {};      if (parade.current !== undefined) {        if(parade.current.categories){          for (const category of parade.current.categories){            var targetingCat = "category_" + category.slug;            jsTargeting[targetingCat] = 1;          }        }        if(parade.current.tags){          for (const tag of parade.current.tags){            var targetingTag = "tag_" + tag.slug;            jsTargeting[targetingTag] = 1;          }        }      }      if (parade.post !== undefined) {        if(parade.post.ID){          jsTargeting["post_id"] = parade.post.ID;        }        if(parade.post.post_type){          jsTargeting["post_type"] = parade.post.post_type;        }      }      if (parade.adSettings !== undefined && parade.adSettings.globalTargets !== undefined) {        if(parade.adSettings.globalTargets.en){          jsTargeting["env"] = parade.adSettings.globalTargets.en;        }      }      var settings = {};      if(Object.keys(jsTargeting).length){        settings["queryJsTargeting"] = jsTargeting;      }      cnxps({        playerId: "5602a962-6662-4ad2-85fb-4518b2e55487",        customParam1: window.location.pathname,          storyId: "9edbf7a5-6744-47d5-8b37-8d491d342981",        settings      }).render("e4d29110661e4c899ecdd35094daaf63");    });  </script></div><h2>Cute Pick Up Lines for Girls</h2><p>61. I&rsquo;m not usually religious, but when I saw you, I knew you were the answer to my prayers.</p><p>62. (Hold out your hand) Hey, I&rsquo;m going for a walk. Would you mind holding this for me?</p><p>63. Do you believe in love at first sight, or should I try walking by again?</p><p>64. I&rsquo;m really glad I just bought life insurance, because when I saw you, my heart stopped.</p><p>65. I&rsquo;m not photographer, but I can definitely picture us together.</p><p>66. Would you mind giving me a pinch? You&rsquo;re so cute, I must be dreaming.</p><p>67. Wow, when God made you, he was seriously showing off.</p><p>68. Excuse me, do you have the time? I just want to remember the exact minute I got a crush on you.</p><p>69. Kiss me if I&rsquo;m wrong but, dinosaurs still exist, right?</p><p><span class="Apple-converted-space">70.&nbsp;If I were a cat, I&rsquo;d spend all nine of my lives with you.</span></p><div class="figure_block paradeImage wp-media-selected size-100 aligncenter wp-image-1040107"> <figure><img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="Unsplash" class="addthis_shareable at_include" title="Funny pick-up lines" data-parade-image-placeholding="true" data-parade-image-inlining="" data-parade-image="https://static.parade.com/wp-content/uploads/2020/05/pick-up-lines-81.jpg"></figure><figcaption><span class="credit">(Unsplash)</span></figcaption></div><p>71. You know, I had a pickup line ready to go, but you&rsquo;re so hot it just left my mind.</p><p>72. When I text you goodnight later, what phone number should I use?</p><p>73. I saw you walking by and I had to come say hello. I love your style. My name&rsquo;s (your name).</p><p>74. I&rsquo;m not currently an organ donor, but I&rsquo;d be happy to give you my heart.</p><p>75. I was going to say something really sweet about you, but when I saw you, I became speechless.</p><p>76.You know, I believe that honesty is the best policy, so to be perfectly honest, you&rsquo;re the sexiest man I&rsquo;ve ever seen.</p><p>77. I&rsquo;d say, &lsquo;God bless you,&rsquo; but it looks like he already did.</p><p>78. You must be a hell of a thief, because you managed to steal my heart from across the room.</p><p>79. There must be something wrong with my eyes&mdash;I can&rsquo;t seem to take them off of you.</p><p>80. If you let me borrow a kiss, I promise I&rsquo;ll give it right back.</p><h2>Cute Pick Up Lines to Use at a Bar</h2><p>81. My friends bet me I couldn&rsquo;t talk to the prettiest girl in the bar. Want to use their money to buy some drinks?</p><p>82. Trust me, I&rsquo;m not drunk; I&rsquo;m just intoxicated by you.</p><p>83. I seem to have lost my number&mdash;can I have yours?</p><p>84. I was just trying to buy a drink here, but you&rsquo;re very distracting.</p><p>85. I started reading/watching an interesting book/show last week, and I&rsquo;d love to discuss it with someone. Have you heard of it?</p><p>86. You see my friend over there? S/he wants to know if you think I&rsquo;m cute.</p><p>87. I was going to call you beautiful, but then I realized I don&rsquo;t have your number yet.</p><p>88. You: Are you good at math?<br>Them: No (or Yes)<br>You: Me neither (or Me too). But the only number I care about is yours.</p><p>89. I&rsquo;m surprised the restaurant/bar/etc. hasn&rsquo;t asked you to leave yet. You&rsquo;re so beautiful you&rsquo;re making all the other girls look bad.</p><p>90. Excuse me, I don&rsquo;t mean to intrude, but you owe me a drink (pause), because when I saw you, I dropped mine.</p><div class="figure_block paradeImage wp-media-selected size-100 aligncenter wp-image-1040108"> <figure><img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="Unsplash" class="addthis_shareable at_include" title="Cheesy pick-up lines" data-parade-image-placeholding="true" data-parade-image-inlining="" data-parade-image="https://static.parade.com/wp-content/uploads/2020/05/pick-up-lines-100.jpg"></figure><figcaption><span class="credit">(Unsplash)</span></figcaption></div><p>91. Are you any good at boxing? Because you look like a knockout.</p><p>92. It&rsquo;s never easy meeting a complete stranger&mdash;especially one as beautiful as you&mdash;without being properly introduced. But can we try anyway?</p><p>93. I wish I&rsquo;d paid more attention to science in high school, because you and I&rsquo;ve got chemistry and I want to know all about it.</p><p>94. Hi, my name is (your name), but you can call me tonight or tomorrow.</p><p>95. Do I know you? (pause) Oh, sorry, it&rsquo;s just that you look just like my next girlfriend.</p><p>96. If I were to ask you out on a date, would your answer be the same as the answer to this question?</p><p>97. Hey, do you mind if we take a picture together? I just want to show my mom what my next girlfriend looks like.</p><p>98.&nbsp;You look like you know how to have a good time. Been on any adventures lately?</p><p>99. You know, I&rsquo;m actually terrible at flirting. How about you try to pick me up instead?</p><p>100. Do you have a name, or can I just call you &lsquo;mine?&rsquo;</p><p>101. I&rsquo;m not sure what it is yet, but something about you seems really interesting.</p><p><em>Check out:</em></p><p><strong>250 <a href="https://parade.com/968403/parade/questions-to-ask-a-guy/" target="_blank" rel="noopener noreferrer">Questions to Ask a Guy</a><br>250 <a href="https://parade.com/966617/parade/never-have-i-ever-questions/" target="_blank" rel="noopener noreferrer">Never Have I Ever Questions</a><br></strong><strong>250 &ldquo;<a href="https://parade.com/964027/parade/would-you-rather-questions/" target="_blank" rel="noopener noreferrer">Would You Rather..?&rdquo; Questions</a></strong><br><strong>250 <a href="https://parade.com/966507/parade/truth-or-dare-questions/" target="_blank" rel="noopener noreferrer">Truth or Dare Questions</a></strong></p>
</span>
<div id="action_button_container"></div>
<div class="sharing sharing_article_bottom">
<div class="addthis_toolbox addthis_default_style addthis_32x32_style">
<a href='#addthis' class="addthis_button_facebook" data-parade-type="social" data-parade-location-types="social"></a>
<a href='#addthis' class="addthis_button_twitter" data-parade-type="social" data-parade-location-types="social"></a>
<a href='#addthis' class="addthis_button_pinterest_share at300b" data-parade-type="social" data-parade-location-types="social" target="_self"></a>
<a href="#addthis" class="addthis_button_compact" data-parade-type="social" data-parade-location-types="social" data-parade-location-ids="counter"></a>
<a href="#addthis" class="addthis_counter addthis_bubble_style" data-parade-type="social" data-parade-location-types="social" data-parade-location-ids="bubble"></a>
</div>
</div>
</section>
<div class="genesis_inpage_wrapper"></div>
<section class="more_stories">
<div class="OUTBRAIN" data-src="https://parade.com/1039985/marynliles/pick-up-lines/" data-widget-id="AR_2" data-ob-template="Parade.com"></div>
<div class="clear"></div>
</section>
<section class="comments ">
<section class="content">
<ol class="commentlist" id="comments">
</ol>
</section>
<form action="" method="post" id="commentform">
<div id="respond">
<h6 id="reply-title">Leave A Comment</h6>
<section id="comment-group">
<div class="input_group">
<p class="comment-form-comment">
<textarea placeholder="Leave A Comment" id="comment" name="comment" cols="45" rows="8" aria-required="true" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="comment-box" data-parade-views="false" data-parade-touches="true" data-parade-clicks="true" data-parade-mouseovers="false"></textarea>
<span class="error_message empty">Uh-oh! Empty comment.</span>
<span class="error_message duplicate">It looks as though you&#8217;ve already said that.</span>
<span class="error_message logged_out">You seem to be logged out. Refresh your page, login and try again.</span>
<span class="error_message closed">Whoops! Sorry, comments are currently closed. </span>
<span class="error_message comment_flood">You are posting comments too quickly. Slow down.</span>
</p>
</div>
</section>
<div id="parade_comments_login"><div class="user_login login">
<header>
<h3>Login</h3>
</header>
<div class="login_form login-signup">
<div class="login_form_content">
<form name="loginform" id="loginform" action="" method="post">
<form>
<fieldset>
<div class="input_group">
<input type="text" name="log" id="user_login--login" class="field" value="" placeholder="Email or Username" data-parade-type="email" autocomplete="username">
<div class="error_message">
Please enter a valid email address.
</div>
</div>
<div class="input_group">
<input type="password" name="pwd" id="user_pass" value="" placeholder="Password" class="field" autocomplete="current-password">
<div class="error_message">
Incorrect email or username/password combination.
</div>
</div>
<div class="submit_container">
<input type="submit" name="wp-submit" class="submit" value="Log in" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="login-submit" data-parade-views="false" data-parade-touches="true" data-parade-clicks="true" data-parade-mouseovers="false">
<input type="hidden" name="redirect_to" value="https://parade.com/1039985/marynliles/pick-up-lines/">
<input type="hidden" name="testcookie" value="1">
<input type="hidden" name="isfrontnedlogin" value="1">
<p>
<a class="password" href="https://parade.com/reset/">Forgot Password?</a> | <a class="signup" href="https://parade.com/register/">Sign Up</a>
</p>
</div>
<span class="loading_spinner" style="display:none;">
<span class="bar bar_1"></span>
<span class="bar bar_2"></span>
<span class="bar bar_3"></span>
<span class="bar bar_4"></span>
<span class="bar bar_5"></span>
<span class="bar bar_6"></span>
<span class="bar bar_7"></span>
<span class="bar bar_8"></span>
<span class="bar bar_9"></span>
<span class="bar bar_10"></span>
<span class="bar bar_11"></span>
<span class="bar bar_12"></span>
</span>
</fieldset>
</form>
</form>
</div>
</div>
</div>
</div>
<div id="parade_comments_registration"><div class="user_login register">
<header>
<h3>Sign up</h3>
</header>
<div class="login_form">
<div class="login_form_content">
<h4>Create a Parade.com account</h4>
<form method="post" action="" id="registerform" name="registerform">
<fieldset>
<div class="note message" style="display:none">Your account was created. An email has been sent to you.</div>
<div class="input_group">
<label for="user_email">Email Address</label>
<input type="text" value="" placeholder="Email Address" class="username" id="user_email" name="user_email" data-parade-type="email" autocomplete="username">
<div class="error_message">
Please enter a valid email address.
</div>
</div>
<div class="input_group">
<label for="user_password">Password</label>
<input type="password" value="" placeholder="Password" class="username" id="user_password" name="user_password" autocomplete="new-password">
<div class="error_message">
Incorrect email/password combination.
</div>
</div>
<div class="register_option">
<input type="checkbox" id="newsletter_signup" value="" class="newsletter_signup" data-parade-type="default" data-parade-slug="parade">
<label for="newsletter_signup">
<strong>Get the Parade Daily:</strong>
celebrity interviews, recipes and
health tips in your inbox.
</label>
<br />
<input type="checkbox" id="channel_food_newsletter" value="" checked="checked" class="newsletter_signup channel_food_newsletter" data-parade-type="channel" data-parade-slug="food">
<label for="channel_food_newsletter" class="newsletter_signup channel_food_newsletter">
<strong>Get the Pop Kitchen Newsletter:</strong> recipes and handy kitchen tips in your inbox.
</label>
<br />
<input type="checkbox" id="channel_health_newsletter" value="" checked="checked" class="newsletter_signup channel_health_newsletter" data-parade-type="channel" data-parade-slug="health">
<label for="channel_health_newsletter" class="newsletter_signup channel_health_newsletter">
<strong>Get the Healthy Now Newsletter:</strong> good vibes and health tips delivered right to your inbox!
</label>
<br />
<input type="checkbox" id="subcategory_parade-picks_newsletter" value="" checked="checked" class="newsletter_signup subcategory_parade-picks_newsletter" data-parade-type="subcategory" data-parade-slug="parade-picks">
<label for="subcategory_parade-picks_newsletter" class="newsletter_signup subcategory_parade-picks_newsletter">
<strong>Get the Pop Shop Newsletter:</strong> fabulous finds delivered right to your inbox!
</label>
</div>
<input class="has_newsletter multiple" type="submit" value="Sign Up" name="wp-submit" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="register-submit" data-parade-views="false" data-parade-touches="true" data-parade-clicks="true" data-parade-mouseovers="false" />
<input type="hidden" value="https://parade.com/1039985/marynliles/pick-up-lines/?registered=1" name="redirect_to">
<input type="hidden" value="1" name="is_parade_registration" />
<span class="loading_spinner" style="display:none">
<span class="bar bar_1"></span>
<span class="bar bar_2"></span>
<span class="bar bar_3"></span>
<span class="bar bar_4"></span>
<span class="bar bar_5"></span>
<span class="bar bar_6"></span>
<span class="bar bar_7"></span>
<span class="bar bar_8"></span>
<span class="bar bar_9"></span>
<span class="bar bar_10"></span>
<span class="bar bar_11"></span>
<span class="bar bar_12"></span>
</span>
<div class="note terms">
By creating an account, you accept the terms and
conditions of our <a href="/privacy-policy/">User Agreement</a> and
<a href="/privacy-policy/#privacy-policy">Privacy Policy</a>.
</div>
</fieldset>
</form>
<div class="account_link">
Already have an account? <a href="https://parade.com/login/">Log In</a>.
</div>
</div>
</div>
</div>
</div>
<div id="parade_comments_lost_password"><div class="user_login reset">
<header>
<h3>Reset Password</h3>
</header>
<div class="login_form">
<div class="login_form_content">
<h4>Enter Your Email Address:</h4>
<form name="lostpasswordform" id="lostpasswordform" action="" method="post">
<fieldset>
<div class="note message" style="display:none"></div>
<div class="input_group">
<label for="user_login--forgot">Email Address:</label>
<input type="text" id="user_login--forgot" name="log" value="" placeholder="Email Address" class="username" data-parade-type="email">
<div class="error_message"></div>
</div>
<input type="hidden" name="redirect_to" value="https://parade.com/1039985/marynliles/pick-up-lines/" />
<input type="submit" value="Reset Password">
<span class="loading_spinner" style="display:none;">
<span class="bar bar_1"></span>
<span class="bar bar_2"></span>
<span class="bar bar_3"></span>
<span class="bar bar_4"></span>
<span class="bar bar_5"></span>
<span class="bar bar_6"></span>
<span class="bar bar_7"></span>
<span class="bar bar_8"></span>
<span class="bar bar_9"></span>
<span class="bar bar_10"></span>
<span class="bar bar_11"></span>
<span class="bar bar_12"></span>
</span>
<div class="note back">
<a href="https://parade.com/login/">Back to Login</a>
</div>
</fieldset>
</form>
<div class="account_link back">
Don't have an account?&nbsp;<a href="https://parade.com/register/">Sign up</a>.
</div>
</div>
</div>
</div>
</div>
<input type="hidden" name="comment_parent" id="comment_parent" value="" />
<input type="hidden" name="comment_post_ID" value="1039985" id="comment_post_ID" />
<div class="comments_submit">
<div class="submit_button">
<input type="submit" id="parade_comment_submit" name="parade_comment_submit" value="Post A Comment" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="comment-submit" data-parade-views="false" data-parade-touches="true" data-parade-clicks="true" data-parade-mouseovers="false">
</div>
<span class="loading_spinner comment_spinner">
<span class="bar bar_1"></span>
<span class="bar bar_2"></span>
<span class="bar bar_3"></span>
<span class="bar bar_4"></span>
<span class="bar bar_5"></span>
<span class="bar bar_6"></span>
<span class="bar bar_7"></span>
<span class="bar bar_8"></span>
<span class="bar bar_9"></span>
<span class="bar bar_10"></span>
<span class="bar bar_11"></span>
<span class="bar bar_12"></span>
</span>
</div>
</div>
</form>
</section>
</section>
<aside class="span4">
<div class="ad-position-1" data-parade-type="ad" data-parade-ad-position="300" data-parade-ad-location="top" data-parade-location-types="ad" data-parade-location-slugs="top" data-parade-views="false" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">
<div class="ad-wrapper">
<div id='div-gpt-ad-300-top-2' class="ad-300-top">
<script type='text/javascript'>
            window.AdManager.displaySlot("300_top", "div-gpt-ad-300-top-2");
        </script>
</div>
</div>
</div>
<section data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">
<div id="zergnet-widget-34512"></div>
<script language="javascript" type="text/javascript">
    (function() {
        var zergnet = document.createElement('script');
        zergnet.type = 'text/javascript'; zergnet.async = true;
        zergnet.src = 'https://www.zergnet.com/zerg.js?id=34512';
        var znscr = document.getElementsByTagName('script')[0];
        znscr.parentNode.insertBefore(zergnet, znscr);
    })();
</script><article class="entertainment ">
<figure>
<a href="https://parade.com/1103425/paulettecohn/american-idol-2021/" data-parade-type="article" data-parade-post-id="1103425" data-parade-author-id="652086" data-parade-post-description="" data-parade-post-title="&lt;em&gt;American Idol&lt;/em&gt; Is Back! Here&#039;s Everything You Need to Know About the 2021 Season" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/02/american_idol_judges_156372_S4PRGROUP-2.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span>
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image-placeholding="true" data-parade-image="https://static.parade.com/wp-content/uploads/2021/02/american_idol_judges_156372_S4PRGROUP-2-300x188.jpg" nopin="nopin" data-parade-image-desktop-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/02/american_idol_judges_156372_S4PRGROUP-2-90x69.jpg" data-parade-image-desktop-wide-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/02/american_idol_judges_156372_S4PRGROUP-2-90x69.jpg" data-parade-image-tablet-landscape-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/02/american_idol_judges_156372_S4PRGROUP-2-90x69.jpg" data-parade-image-tablet-landscape-retina-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/02/american_idol_judges_156372_S4PRGROUP-2-180x138.jpg" />
</span>
</a>
</figure>
<h4>
<a href="https://parade.com/1103425/paulettecohn/american-idol-2021/" data-parade-type="article" data-parade-post-id="1103425" data-parade-author-id="652086" data-parade-post-description="" data-parade-post-title="&lt;em&gt;American Idol&lt;/em&gt; Is Back! Here&#039;s Everything You Need to Know About the 2021 Season" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/02/american_idol_judges_156372_S4PRGROUP-2.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false"><em>American Idol</em> Is Back! Here's Everything You Need to Know About the 2021&nbsp;Season</a>
</h4>
<cite>
<a class='fn url' href="https://parade.com/member/paulettecohn/" data-parade-type="member" data-parade-member-id="652086" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false" data-parade-type="member" data-parade-member-id="652086" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Paulette Cohn</a>, <span class="role">Editor</span><span class="org" style="display:none">Parade</span>
</cite>
</article>
<article class="health ">
<figure>
<a href="https://parade.com/986848/nancy_henderson/types-of-diets/" data-parade-type="article" data-parade-post-id="986848" data-parade-author-id="687262" data-parade-post-description="" data-parade-post-title="Which One of These 100 Diets Could Help You Lose Weight? We&#039;ve Got Tons of Info to Help You Decide" data-parade-post-image="https://static.parade.com/wp-content/uploads/2020/02/woman-in-kitchen-FTR.jpg" data-parade-post-format="photos" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
 <span>
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image-placeholding="true" data-parade-image="https://static.parade.com/wp-content/uploads/2020/02/woman-in-kitchen-FTR-300x188.jpg" nopin="nopin" data-parade-image-desktop-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2020/02/woman-in-kitchen-FTR-90x69.jpg" data-parade-image-desktop-wide-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2020/02/woman-in-kitchen-FTR-90x69.jpg" data-parade-image-tablet-landscape-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2020/02/woman-in-kitchen-FTR-90x69.jpg" data-parade-image-tablet-landscape-retina-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2020/02/woman-in-kitchen-FTR-180x138.jpg" />
</span>
</a>
</figure>
<h4>
<a href="https://parade.com/986848/nancy_henderson/types-of-diets/" data-parade-type="article" data-parade-post-id="986848" data-parade-author-id="687262" data-parade-post-description="" data-parade-post-title="Which One of These 100 Diets Could Help You Lose Weight? We&#039;ve Got Tons of Info to Help You Decide" data-parade-post-image="https://static.parade.com/wp-content/uploads/2020/02/woman-in-kitchen-FTR.jpg" data-parade-post-format="photos" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Which One of These 100 Diets Could Help You Lose Weight? We've Got Tons of Info to Help You&nbsp;Decide</a>
</h4>
<cite>
<a class='fn url' href="https://parade.com/member/nancy_henderson/" data-parade-type="member" data-parade-member-id="687262" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false" data-parade-type="member" data-parade-member-id="687262" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Nancy Henderson</a>, <span class="role">Contributor</span><span class="org" style="display:none">Parade</span>
</cite>
</article>
<article class="food ">
<figure>
<a href="https://parade.com/954875/parade/crock-pot-recipes/" data-parade-type="article" data-parade-post-id="954875" data-parade-author-id="6" data-parade-post-description="" data-parade-post-title="200 Best Crock Pot Recipes and Easy Slow Cooker Dinner Ideas for the Family" data-parade-post-image="https://static.parade.com/wp-content/uploads/2019/11/Crock-Pot-Recipes-Slow-cooker-125.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span>
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image-placeholding="true" data-parade-image="https://static.parade.com/wp-content/uploads/2019/11/Crock-Pot-Recipes-Slow-cooker-125-200x300.jpg" nopin="nopin" data-parade-image-desktop-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2019/11/Crock-Pot-Recipes-Slow-cooker-125-90x69.jpg" data-parade-image-desktop-wide-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2019/11/Crock-Pot-Recipes-Slow-cooker-125-90x69.jpg" data-parade-image-tablet-landscape-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2019/11/Crock-Pot-Recipes-Slow-cooker-125-90x69.jpg" data-parade-image-tablet-landscape-retina-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2019/11/Crock-Pot-Recipes-Slow-cooker-125-180x138.jpg" />
</span>
</a>
</figure>
<h4>
<a href="https://parade.com/954875/parade/crock-pot-recipes/" data-parade-type="article" data-parade-post-id="954875" data-parade-author-id="6" data-parade-post-description="" data-parade-post-title="200 Best Crock Pot Recipes and Easy Slow Cooker Dinner Ideas for the Family" data-parade-post-image="https://static.parade.com/wp-content/uploads/2019/11/Crock-Pot-Recipes-Slow-cooker-125.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">200 Best Crock Pot Recipes and Easy Slow Cooker Dinner Ideas for the&nbsp;Family</a>
</h4>
<cite>
<a class='fn url' href="https://parade.com/member/parade/" data-parade-type="member" data-parade-member-id="6" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false" data-parade-type="member" data-parade-member-id="6" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Parade</a>, <span class="role">Editor</span><span class="org" style="display:none">Parade</span>
</cite>
</article>
<article class="food ">
<figure>
<a href="https://parade.com/969844/parade/weight-watchers-recipes/" data-parade-type="article" data-parade-post-id="969844" data-parade-author-id="6" data-parade-post-description="" data-parade-post-title="100+ Weight Watchers Recipes with WW Points to Help You Lose Weight" data-parade-post-image="https://static.parade.com/wp-content/uploads/2020/01/WW-Recipe-Chili.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span>
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image-placeholding="true" data-parade-image="https://static.parade.com/wp-content/uploads/2020/01/WW-Recipe-Chili-300x201.jpg" nopin="nopin" data-parade-image-desktop-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2020/01/WW-Recipe-Chili-90x69.jpg" data-parade-image-desktop-wide-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2020/01/WW-Recipe-Chili-90x69.jpg" data-parade-image-tablet-landscape-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2020/01/WW-Recipe-Chili-90x69.jpg" data-parade-image-tablet-landscape-retina-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2020/01/WW-Recipe-Chili-180x138.jpg" />
</span>
</a>
</figure>
<h4>
<a href="https://parade.com/969844/parade/weight-watchers-recipes/" data-parade-type="article" data-parade-post-id="969844" data-parade-author-id="6" data-parade-post-description="" data-parade-post-title="100+ Weight Watchers Recipes with WW Points to Help You Lose Weight" data-parade-post-image="https://static.parade.com/wp-content/uploads/2020/01/WW-Recipe-Chili.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">100+ Weight Watchers Recipes with WW Points to Help You Lose&nbsp;Weight</a>
</h4>
<cite>
<a class='fn url' href="https://parade.com/member/parade/" data-parade-type="member" data-parade-member-id="6" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false" data-parade-type="member" data-parade-member-id="6" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Parade</a>, <span class="role">Editor</span><span class="org" style="display:none">Parade</span>
</cite>
</article>
<article class="entertainment ">
<figure>
<a href="https://parade.com/1101968/alexandra-hurtado/the-bachelor-season-25-matt-james/" data-parade-type="article" data-parade-post-id="1101968" data-parade-author-id="687370" data-parade-post-description="" data-parade-post-title="Matt James&#039; Journey for Love Has Begun! Everything You Need to Know About Season 25 of &lt;em&gt;The Bachelor&lt;/em&gt;" data-parade-post-image="https://static.parade.com/wp-content/uploads/2020/10/matt-james.png" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span>
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image-placeholding="true" data-parade-image="https://static.parade.com/wp-content/uploads/2020/10/matt-james-300x188.png" nopin="nopin" data-parade-image-desktop-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2020/10/matt-james-90x69.png" data-parade-image-desktop-wide-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2020/10/matt-james-90x69.png" data-parade-image-tablet-landscape-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2020/10/matt-james-90x69.png" data-parade-image-tablet-landscape-retina-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2020/10/matt-james-180x138.png" />
</span>
</a>
</figure>
<h4>
<a href="https://parade.com/1101968/alexandra-hurtado/the-bachelor-season-25-matt-james/" data-parade-type="article" data-parade-post-id="1101968" data-parade-author-id="687370" data-parade-post-description="" data-parade-post-title="Matt James&#039; Journey for Love Has Begun! Everything You Need to Know About Season 25 of &lt;em&gt;The Bachelor&lt;/em&gt;" data-parade-post-image="https://static.parade.com/wp-content/uploads/2020/10/matt-james.png" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Matt James' Journey for Love Has Begun! Everything You Need to Know About Season 25 of <em>The&nbsp;Bachelor</em></a>
</h4>
<cite>
<a class='fn url' href="https://parade.com/member/alexandra-hurtado/" data-parade-type="member" data-parade-member-id="687370" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false" data-parade-type="member" data-parade-member-id="687370" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Alexandra Hurtado</a>, <span class="role">Contributor</span><span class="org" style="display:none">Parade</span>
</cite>
</article>
<article class="uncategorized ">
<figure>
<a href="https://www.facebook.com/parademag" data-parade-type="article" data-parade-post-id="253103" data-parade-author-id="6" data-parade-post-description="" data-parade-post-title="Inspiration. Tips. Recipes. Get ’Em Here!" data-parade-post-image="https://static.parade.com/wp-content/uploads/2014/01/facebook-logo-parade-2-ftr.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span>
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image-placeholding="true" data-parade-image="https://static.parade.com/wp-content/uploads/2014/01/facebook-logo-parade-2-ftr-300x187.jpg" nopin="nopin" data-parade-image-desktop-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2014/01/facebook-logo-parade-2-ftr-90x69.jpg" data-parade-image-desktop-wide-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2014/01/facebook-logo-parade-2-ftr-90x69.jpg" data-parade-image-tablet-landscape-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2014/01/facebook-logo-parade-2-ftr-90x69.jpg" data-parade-image-tablet-landscape-retina-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2014/01/facebook-logo-parade-2-ftr-180x138.jpg" />
</span>
</a>
</figure>
<h4>
<a href="https://www.facebook.com/parademag" data-parade-type="article" data-parade-post-id="253103" data-parade-author-id="6" data-parade-post-description="" data-parade-post-title="Inspiration. Tips. Recipes. Get ’Em Here!" data-parade-post-image="https://static.parade.com/wp-content/uploads/2014/01/facebook-logo-parade-2-ftr.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Inspiration. Tips. Recipes. Get ’Em&nbsp;Here!</a>
</h4>
<cite>
<a class='fn url' href="https://parade.com/member/parade/" data-parade-type="member" data-parade-member-id="6" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false" data-parade-type="member" data-parade-member-id="6" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Parade</a>, <span class="role">Editor</span><span class="org" style="display:none">Parade</span>
</cite>
</article>
<article class="living ">
<figure>
<a href="https://parade.com/parade_numbrix/numbrix-9-march-20-13/" data-parade-type="article" data-parade-post-id="1156089" data-parade-author-id="78" data-parade-post-description="" data-parade-post-title="Numbrix 9 - March 20" data-parade-post-image="https://static.parade.com/wp-content/uploads/2013/04/numbrix-ftr-e1378756696914.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span>
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image-placeholding="true" data-parade-image="https://static.parade.com/wp-content/uploads/2013/04/numbrix-ftr-e1378756696914-300x187.jpg" nopin="nopin" />
</span>
</a>
</figure>
<h4>
<a href="https://parade.com/parade_numbrix/numbrix-9-march-20-13/" data-parade-type="article" data-parade-post-id="1156089" data-parade-author-id="78" data-parade-post-description="" data-parade-post-title="Numbrix 9 - March 20" data-parade-post-image="https://static.parade.com/wp-content/uploads/2013/04/numbrix-ftr-e1378756696914.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Numbrix 9 - March&nbsp;20</a>
</h4>
<cite>
<a class='fn url' href="https://parade.com/member/marilynvossavant/" data-parade-type="member" data-parade-member-id="78" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false" data-parade-type="member" data-parade-member-id="78" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Marilyn vos Savant</a>, <span class="role">Contributor</span><span class="org" style="display:none">Parade</span>
</cite>
</article>
<article class="health ">
<figure>
<a href="https://parade.com/1181874/kaitlin-vogel/benefits-of-telehealth/" data-parade-type="article" data-parade-post-id="1181874" data-parade-author-id="692301" data-parade-post-description="" data-parade-post-title="All the Things You Can Get via Telehealth, From a Much-Needed Prescription to a Therapy Session" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/benefits-of-telehealth.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span>
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image-placeholding="true" data-parade-image="https://static.parade.com/wp-content/uploads/2021/03/benefits-of-telehealth-300x200.jpg" nopin="nopin" data-parade-image-desktop-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/03/benefits-of-telehealth-90x69.jpg" data-parade-image-desktop-wide-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/03/benefits-of-telehealth-90x69.jpg" data-parade-image-tablet-landscape-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/03/benefits-of-telehealth-90x69.jpg" data-parade-image-tablet-landscape-retina-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/03/benefits-of-telehealth-180x138.jpg" />
</span>
</a>
</figure>
<h4>
<a href="https://parade.com/1181874/kaitlin-vogel/benefits-of-telehealth/" data-parade-type="article" data-parade-post-id="1181874" data-parade-author-id="692301" data-parade-post-description="" data-parade-post-title="All the Things You Can Get via Telehealth, From a Much-Needed Prescription to a Therapy Session" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/benefits-of-telehealth.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">All the Things You Can Get via Telehealth, From a Much-Needed Prescription to a Therapy&nbsp;Session</a>
</h4>
<cite>
<a class='fn url' href="https://parade.com/member/kaitlin-vogel/" data-parade-type="member" data-parade-member-id="692301" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false" data-parade-type="member" data-parade-member-id="692301" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Kaitlin Vogel</a>, <span class="role">Contributor</span><span class="org" style="display:none">Parade</span>
</cite>
</article>
<article class="health ">
<figure>
<a href="https://parade.com/1182358/korinmiller/best-peloton-desk/" data-parade-type="article" data-parade-post-id="1182358" data-parade-author-id="687379" data-parade-post-description="" data-parade-post-title="Max Out Your WFH Experience With These Desks That Clip Right on to Your Peloton" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/best-peloton-desks.png" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span>
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image-placeholding="true" data-parade-image="https://static.parade.com/wp-content/uploads/2021/03/best-peloton-desks-300x300.png" nopin="nopin" data-parade-image-desktop-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/03/best-peloton-desks-90x69.png" data-parade-image-desktop-wide-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/03/best-peloton-desks-90x69.png" data-parade-image-tablet-landscape-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/03/best-peloton-desks-90x69.png" data-parade-image-tablet-landscape-retina-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/03/best-peloton-desks-180x138.png" />
</span>
</a>
</figure>
<h4>
<a href="https://parade.com/1182358/korinmiller/best-peloton-desk/" data-parade-type="article" data-parade-post-id="1182358" data-parade-author-id="687379" data-parade-post-description="" data-parade-post-title="Max Out Your WFH Experience With These Desks That Clip Right on to Your Peloton" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/best-peloton-desks.png" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Max Out Your WFH Experience With These Desks That Clip Right on to Your&nbsp;Peloton</a>
</h4>
<cite>
<a class='fn url' href="https://parade.com/member/korinmiller/" data-parade-type="member" data-parade-member-id="687379" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false" data-parade-type="member" data-parade-member-id="687379" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Korin Miller</a>, <span class="role">Contributor</span><span class="org" style="display:none">Parade</span>
</cite>
</article>
<article class="health ">
<figure>
<a href="https://parade.com/1176077/nicolepajer/daily-harvest-reviews/" data-parade-type="article" data-parade-post-id="1176077" data-parade-author-id="655498" data-parade-post-description="" data-parade-post-title="I Eat a Plant-Based Diet and I Tried Daily Harvest for a Week—Here&#039;s My Honest Review" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/daily-harvest-reviews.png" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span>
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image-placeholding="true" data-parade-image="https://static.parade.com/wp-content/uploads/2021/03/daily-harvest-reviews-300x300.png" nopin="nopin" data-parade-image-desktop-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/03/daily-harvest-reviews-90x69.png" data-parade-image-desktop-wide-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/03/daily-harvest-reviews-90x69.png" data-parade-image-tablet-landscape-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/03/daily-harvest-reviews-90x69.png" data-parade-image-tablet-landscape-retina-featured-sidebar-image="https://static.parade.com/wp-content/uploads/2021/03/daily-harvest-reviews-180x138.png" />
</span>
</a>
</figure>
<h4>
<a href="https://parade.com/1176077/nicolepajer/daily-harvest-reviews/" data-parade-type="article" data-parade-post-id="1176077" data-parade-author-id="655498" data-parade-post-description="" data-parade-post-title="I Eat a Plant-Based Diet and I Tried Daily Harvest for a Week—Here&#039;s My Honest Review" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/daily-harvest-reviews.png" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">I Eat a Plant-Based Diet and I Tried Daily Harvest for a Week—Here's My Honest&nbsp;Review</a>
</h4>
<cite>
<a class='fn url' href="https://parade.com/member/nicolepajer/" data-parade-type="member" data-parade-member-id="655498" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false" data-parade-type="member" data-parade-member-id="655498" data-parade-location-types="member" data-parade-location-ids="sidebar" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Nicole Pajer</a>, <span class="role">Contributor</span><span class="org" style="display:none">Parade</span>
</cite>
</article>
</section>
<div class="ad-position-2" data-parade-type="ad" data-parade-ad-position="300" data-parade-ad-location="bottom" data-parade-location-types="ad" data-parade-views="true" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="true">
<div class="ad-wrapper">
<div id='div-gpt-ad-300-bottom-3' class="ad-300-bottom">
<script type='text/javascript'>
            window.AdManager.displaySlot("300_bottom", "div-gpt-ad-300-bottom-3");
        </script>
</div>
</div>
</div>
</aside>
</section>
</article>
</section>
<section class="footer_ad">
<div class="content">
<div data-parade-type="ad" data-parade-ad-position="728" data-parade-ad-location="bottom" data-parade-location-types="ad" data-parade-location-ids="728-bottom" data-parade-views="true" data-parade-touches="true" data-parade-clicks="true" data-parade-mouseovers="false">
<div class="ad-wrapper">
<div id='div-gpt-ad-728-bottom-1' class="ad-728-bottom">
<script type='text/javascript'>
            window.AdManager.displaySlot("728_bottom", "div-gpt-ad-728-bottom-1");
        </script>
</div>
</div>
</div>
</div>
</section><div class="most_popular entertainment" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="tab-box" data-parade-views="true" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">
<section class="content">
<div class="tab-group-box" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="popular-box" data-parade-views="false" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">
<section class="category most_commented tab_group" data-id="most_commented" data-count="10" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">
<header class="category_header">
<h3>
<span class="text">most commented</span>
</h3>
</header>
<section class="items">
<article class="uncategorized" data-id="1">
<figure style="background-image: url(https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif);" data-parade-background-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-1024x640.jpg" data-parade-background-image-inlining="" data-parade-background-image-placeholding="true">
<a href="https://parade.com/1174155/marilynvossavant/is-it-inappropriate-to-refer-to-electrical-cords-and-sockets-as-male-and-female/" data-parade-type="article" data-parade-post-id="1174155" data-parade-author-id="78" data-parade-post-description="" data-parade-post-title="Is It Inappropriate to Refer to Electrical Cords and Sockets as &#039;Male&#039; and &#039;Female&#039;?" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-1024x640.jpg" data-parade-image-placeholding="true" data-parade-image-desktop-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-223x223.jpg" data-parade-image-desktop-wide-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-250x250.jpg" data-parade-image-tablet-portrait-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-230x230.jpg" data-parade-image-tablet-landscape-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-225x225.jpg" data-parade-image-tablet-portrait-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-460x460.jpg" data-parade-image-tablet-landscape-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-450x450.jpg" data-parade-image-phone-portrait-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-90x90.jpg" data-parade-image-phone-landscape-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-90x90.jpg" data-parade-image-phone-portrait-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-90x90.jpg" data-parade-image-phone-landscape-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-180x180.jpg" data-parade-image-iphone-5-landscape-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR-180x180.jpg" />
</a>
</figure>
<span class="rank">
<span class="text">1</span>
</span>
<h4>
<a href="https://parade.com/1174155/marilynvossavant/is-it-inappropriate-to-refer-to-electrical-cords-and-sockets-as-male-and-female/" data-parade-type="article" data-parade-post-id="1174155" data-parade-author-id="78" data-parade-post-description="" data-parade-post-title="Is It Inappropriate to Refer to Electrical Cords and Sockets as &#039;Male&#039; and &#039;Female&#039;?" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Male-Female-plugs-FTR.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="text">Is It Inappropriate to Refer to Electrical Cords and Sockets as 'Male' and&nbsp;'Female'?</span>
</a>
</h4>
<a href="https://parade.com/member/marilynvossavant/" class="source" data-parade-type="member" data-parade-member-id="78" data-parade-location-types="member" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="source-text">Marilyn vos Savant</span>, <span class="role">Contributor</span>
</a>
</article>
<article class="living" data-id="2">
<figure style="background-image: url(https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif);" data-parade-background-image="https://static.parade.com/wp-content/uploads/2014/08/Why-Love-Is-a-Good-Drug-for-Mind-and-Body-ftr-1024x640.jpg" data-parade-background-image-inlining="" data-parade-background-image-placeholding="true">
<a href="https://parade.com/391231/lindsaylowe/inspiring-quotes-love-marriage/" data-parade-type="article" data-parade-post-id="391231" data-parade-author-id="651122" data-parade-post-description="" data-parade-post-title="100 Inspiring Quotes on Love and Marriage" data-parade-post-image="https://static.parade.com/wp-content/uploads/2014/08/Why-Love-Is-a-Good-Drug-for-Mind-and-Body-ftr.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image="https://static.parade.com/wp-content/uploads/2014/08/Why-Love-Is-a-Good-Drug-for-Mind-and-Body-ftr-1024x640.jpg" data-parade-image-placeholding="true" />
</a>
</figure>
<span class="rank">
<span class="text">2</span>
</span>
<h4>
<a href="https://parade.com/391231/lindsaylowe/inspiring-quotes-love-marriage/" data-parade-type="article" data-parade-post-id="391231" data-parade-author-id="651122" data-parade-post-description="" data-parade-post-title="100 Inspiring Quotes on Love and Marriage" data-parade-post-image="https://static.parade.com/wp-content/uploads/2014/08/Why-Love-Is-a-Good-Drug-for-Mind-and-Body-ftr.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="text">100 Inspiring Quotes on Love and&nbsp;Marriage</span>
</a>
</h4>
<a href="https://parade.com/member/lindsaylowe/" class="source" data-parade-type="member" data-parade-member-id="651122" data-parade-location-types="member" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="source-text">Lindsay Lowe</span>, <span class="role">Contributor</span>
</a>
</article>
<article class="health" data-id="3">
<figure style="background-image: url(https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif);" data-parade-background-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-1024x640.jpg" data-parade-background-image-inlining="" data-parade-background-image-placeholding="true">
<a href="https://parade.com/1012420/nicolepajer/best-online-games/" data-parade-type="article" data-parade-post-id="1012420" data-parade-author-id="655498" data-parade-post-description="" data-parade-post-title="The 35 Best Online Games to Play With Friends While Social Distancing" data-parade-post-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-1024x640.jpg" data-parade-image-placeholding="true" data-parade-image-desktop-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-223x223.jpg" data-parade-image-desktop-wide-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-250x250.jpg" data-parade-image-tablet-portrait-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-230x230.jpg" data-parade-image-tablet-landscape-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-225x225.jpg" data-parade-image-tablet-portrait-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-460x460.jpg" data-parade-image-tablet-landscape-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-450x450.jpg" data-parade-image-phone-portrait-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-90x90.jpg" data-parade-image-phone-landscape-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-90x90.jpg" data-parade-image-phone-portrait-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-90x90.jpg" data-parade-image-phone-landscape-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-180x180.jpg" data-parade-image-iphone-5-landscape-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr-180x180.jpg" />
</a>
</figure>
<span class="rank">
<span class="text">3</span>
</span>
<h4>
<a href="https://parade.com/1012420/nicolepajer/best-online-games/" data-parade-type="article" data-parade-post-id="1012420" data-parade-author-id="655498" data-parade-post-description="" data-parade-post-title="The 35 Best Online Games to Play With Friends While Social Distancing" data-parade-post-image="https://static.parade.com/wp-content/uploads/2020/03/best-online-games-ftr.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="text">The 35 Best Online Games to Play With Friends While Social&nbsp;Distancing</span>
</a>
</h4>
<a href="https://parade.com/member/nicolepajer/" class="source" data-parade-type="member" data-parade-member-id="655498" data-parade-location-types="member" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="source-text">Nicole Pajer</span>, <span class="role">Contributor</span>
</a>
</article>
<article class="uncategorized" data-id="4">
<figure style="background-image: url(https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif);" data-parade-background-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-1024x640.jpg" data-parade-background-image-inlining="" data-parade-background-image-placeholding="true">
<a href="https://parade.com/1177621/marilynvossavant/in-what-ways-has-quarantining-inside-affected-our-health/" data-parade-type="article" data-parade-post-id="1177621" data-parade-author-id="78" data-parade-post-description="" data-parade-post-title="In What Ways Has Quarantining Inside Affected Our Health?" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image-inlining="" data-parade-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-1024x640.jpg" data-parade-image-placeholding="true" data-parade-image-desktop-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-223x223.jpg" data-parade-image-desktop-wide-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-250x250.jpg" data-parade-image-tablet-portrait-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-230x230.jpg" data-parade-image-tablet-landscape-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-225x225.jpg" data-parade-image-tablet-portrait-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-460x460.jpg" data-parade-image-tablet-landscape-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-450x450.jpg" data-parade-image-phone-portrait-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-90x90.jpg" data-parade-image-phone-landscape-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-90x90.jpg" data-parade-image-phone-portrait-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-90x90.jpg" data-parade-image-phone-landscape-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-180x180.jpg" data-parade-image-iphone-5-landscape-retina-featured-most-popular-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR-180x180.jpg" />
</a>
</figure>
<span class="rank">
<span class="text">4</span>
</span>
<h4>
<a href="https://parade.com/1177621/marilynvossavant/in-what-ways-has-quarantining-inside-affected-our-health/" data-parade-type="article" data-parade-post-id="1177621" data-parade-author-id="78" data-parade-post-description="" data-parade-post-title="In What Ways Has Quarantining Inside Affected Our Health?" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/Ask-M_Vitamin-D-FTR.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="text">In What Ways Has Quarantining Inside Affected Our&nbsp;Health?</span>
</a>
</h4>
<a href="https://parade.com/member/marilynvossavant/" class="source" data-parade-type="member" data-parade-member-id="78" data-parade-location-types="member" data-parade-location-ids="most-commented" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="source-text">Marilyn vos Savant</span>, <span class="role">Contributor</span>
</a>
</article>
</section>
</section><section class="category articles selected tab_group" data-id="articles" data-count="10">
<header class="category_header">
<h3><span class="text"><span class="hide-phone">Most </span>Popular</span></h3>
</header>
<section class="items">
<article class="entertainment" data-id="1">
<figure style="background-image: url(https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif);" data-parade-background-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-1024x683.jpg" data-parade-background-image-placeholding="true" data-parade-background-image-inlining="">
<a href="https://parade.com/1177337/klconniewang/when-calls-the-heart-season-8-episode-5/" data-parade-type="article" data-parade-post-id="1177337" data-parade-author-id="10233" data-parade-post-description="" data-parade-post-title="Elizabeth and Lucas Go on a Proper Date! Get a Sneak Peek of This Week&#039;s &lt;em&gt;When Calls the Heart&lt;/em&gt;" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-scaled.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-popular" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-1024x683.jpg" data-parade-image-placeholding="true" data-parade-image-inlining="" data-parade-image-desktop-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-300x250.jpg" data-parade-image-desktop-wide-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-350x298.jpg" data-parade-image-tablet-portrait-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-354x275.jpg" data-parade-image-tablet-landscape-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-315x260.jpg" data-parade-image-tablet-portrait-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-708x550.jpg" data-parade-image-tablet-landscape-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-630x520.jpg" data-parade-image-phone-portrait-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-280x210.jpg" data-parade-image-phone-landscape-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-440x210.jpg" data-parade-image-phone-portrait-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-560x420.jpg" data-parade-image-phone-landscape-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-880x420.jpg" data-parade-image-iphone-5-landscape-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-1136x420.jpg" />
</a>
</figure>
<span class="rank"><span class="text">1</span></span>
<h4>
<a href="https://parade.com/1177337/klconniewang/when-calls-the-heart-season-8-episode-5/" data-parade-type="article" data-parade-post-id="1177337" data-parade-author-id="10233" data-parade-post-description="" data-parade-post-title="Elizabeth and Lucas Go on a Proper Date! Get a Sneak Peek of This Week&#039;s &lt;em&gt;When Calls the Heart&lt;/em&gt;" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/When-Calls-the-Heart-805-3-scaled.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-popular" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="text">Elizabeth and Lucas Go on a Proper Date! Get a Sneak Peek of This Week's <em>When Calls the&nbsp;Heart</em></span>
</a>
</h4>
<a href="https://parade.com/member/klconniewang/" class="source" data-parade-type="member" data-parade-member-id="10233" data-parade-location-types="member" data-parade-location-ids="most-popular" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="source-text">K.L. Connie Wang</span>, <span class="role">Contributor</span>
</a>
</article>
<article class="entertainment" data-id="2">
<figure style="background-image: url(https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif);" data-parade-background-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-1024x640.png" data-parade-background-image-placeholding="true" data-parade-background-image-inlining="">
<a href="https://parade.com/1181100/paulettecohn/ncis-mark-harmon-wife-pam-dawber-guest-stars/" data-parade-type="article" data-parade-post-id="1181100" data-parade-author-id="652086" data-parade-post-description="" data-parade-post-title="Mark Harmon&#039;s Real-Life Wife Pam Dawber Is Joining &lt;em&gt;NCIS&lt;/em&gt; in a Recurring Role—Find Out When!" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg.png" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-popular" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-1024x640.png" data-parade-image-placeholding="true" data-parade-image-inlining="" data-parade-image-desktop-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-300x250.png" data-parade-image-desktop-wide-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-350x298.png" data-parade-image-tablet-portrait-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-354x275.png" data-parade-image-tablet-landscape-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-315x260.png" data-parade-image-tablet-portrait-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-708x550.png" data-parade-image-tablet-landscape-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-630x520.png" data-parade-image-phone-portrait-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-280x210.png" data-parade-image-phone-landscape-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-440x210.png" data-parade-image-phone-portrait-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-560x420.png" data-parade-image-phone-landscape-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-880x420.png" data-parade-image-iphone-5-landscape-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg-1136x420.png" />
</a>
</figure>
<span class="rank"><span class="text">2</span></span>
<h4>
<a href="https://parade.com/1181100/paulettecohn/ncis-mark-harmon-wife-pam-dawber-guest-stars/" data-parade-type="article" data-parade-post-id="1181100" data-parade-author-id="652086" data-parade-post-description="" data-parade-post-title="Mark Harmon&#039;s Real-Life Wife Pam Dawber Is Joining &lt;em&gt;NCIS&lt;/em&gt; in a Recurring Role—Find Out When!" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/mark-harmon-wife-removebg.png" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-popular" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
 <span class="text">Mark Harmon's Real-Life Wife Pam Dawber Is Joining <em>NCIS</em> in a Recurring Role—Find Out&nbsp;When!</span>
</a>
</h4>
<a href="https://parade.com/member/paulettecohn/" class="source" data-parade-type="member" data-parade-member-id="652086" data-parade-location-types="member" data-parade-location-ids="most-popular" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="source-text">Paulette Cohn</span>, <span class="role">Editor</span>
</a>
</article>
<article class="culture" data-id="3">
<figure style="background-image: url(https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif);" data-parade-background-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-1024x640.png" data-parade-background-image-placeholding="true" data-parade-background-image-inlining="">
<a href="https://parade.com/1180893/jessicasager/lori-loughlin-net-worth-college-admissions-scandal/" data-parade-type="article" data-parade-post-id="1180893" data-parade-author-id="687433" data-parade-post-description="" data-parade-post-title="Lori Loughlin&#039;s Net Worth Before and After the College Admissions Scandal" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg.png" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-popular" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-1024x640.png" data-parade-image-placeholding="true" data-parade-image-inlining="" data-parade-image-desktop-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-300x250.png" data-parade-image-desktop-wide-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-350x298.png" data-parade-image-tablet-portrait-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-354x275.png" data-parade-image-tablet-landscape-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-315x260.png" data-parade-image-tablet-portrait-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-708x550.png" data-parade-image-tablet-landscape-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-630x520.png" data-parade-image-phone-portrait-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-280x210.png" data-parade-image-phone-landscape-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-440x210.png" data-parade-image-phone-portrait-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-560x420.png" data-parade-image-phone-landscape-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-880x420.png" data-parade-image-iphone-5-landscape-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg-1136x420.png" />
</a>
</figure>
<span class="rank"><span class="text">3</span></span>
<h4>
<a href="https://parade.com/1180893/jessicasager/lori-loughlin-net-worth-college-admissions-scandal/" data-parade-type="article" data-parade-post-id="1180893" data-parade-author-id="687433" data-parade-post-description="" data-parade-post-title="Lori Loughlin&#039;s Net Worth Before and After the College Admissions Scandal" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/lori-loughlin-now-removebg.png" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-popular" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="text">Lori Loughlin's Net Worth Before and After the College Admissions&nbsp;Scandal</span>
</a>
</h4>
<a href="https://parade.com/member/jessicasager/" class="source" data-parade-type="member" data-parade-member-id="687433" data-parade-location-types="member" data-parade-location-ids="most-popular" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="source-text">Jessica Sager</span>, <span class="role">Contributor</span>
</a>
</article>
<article class="entertainment" data-id="4">
<figure style="background-image: url(https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif);" data-parade-background-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-1024x640.jpg" data-parade-background-image-placeholding="true" data-parade-background-image-inlining="">
<a href="https://parade.com/1180660/paulettecohn/gibbs-arrested-suspended-on-ncis-tonight-will-he-be-back/" data-parade-type="article" data-parade-post-id="1180660" data-parade-author-id="652086" data-parade-post-description="" data-parade-post-title="Gibbs Gets Arrested! Is His &lt;em&gt;NCIS&lt;/em&gt; Career at an End?" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-popular" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<img src="https://static.parade.com/wp-content/themes/wp-theme/img/misc/tiny.gif" alt="" data-parade-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-1024x640.jpg" data-parade-image-placeholding="true" data-parade-image-inlining="" data-parade-image-desktop-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-300x250.jpg" data-parade-image-desktop-wide-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-350x298.jpg" data-parade-image-tablet-portrait-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-354x275.jpg" data-parade-image-tablet-landscape-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-315x260.jpg" data-parade-image-tablet-portrait-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-708x550.jpg" data-parade-image-tablet-landscape-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-630x520.jpg" data-parade-image-phone-portrait-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-280x210.jpg" data-parade-image-phone-landscape-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-440x210.jpg" data-parade-image-phone-portrait-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-560x420.jpg" data-parade-image-phone-landscape-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-880x420.jpg" data-parade-image-iphone-5-landscape-retina-featured-gridstream-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2-1136x420.jpg" />
 </a>
</figure>
<span class="rank"><span class="text">4</span></span>
<h4>
<a href="https://parade.com/1180660/paulettecohn/gibbs-arrested-suspended-on-ncis-tonight-will-he-be-back/" data-parade-type="article" data-parade-post-id="1180660" data-parade-author-id="652086" data-parade-post-description="" data-parade-post-title="Gibbs Gets Arrested! Is His &lt;em&gt;NCIS&lt;/em&gt; Career at an End?" data-parade-post-image="https://static.parade.com/wp-content/uploads/2021/03/ncis-mark-harmon-117258_0541b-2.jpg" data-parade-post-format="article" data-parade-location-types="article" data-parade-location-ids="most-popular" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="text">Gibbs Gets Arrested! Is His <em>NCIS</em> Career at an&nbsp;End?</span>
</a>
</h4>
<a href="https://parade.com/member/paulettecohn/" class="source" data-parade-type="member" data-parade-member-id="652086" data-parade-location-types="member" data-parade-location-ids="most-popular" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="source-text">Paulette Cohn</span>, <span class="role">Editor</span>
</a>
</article>
</section>
</section>
<div class="optional">
<section class="category voices" data-id="voices" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="voices" data-parade-views="true" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">
<header class="category_header">
<h3><span class="text">top voices</span></h3>
</header>
<section class="items">
<article class="">
<header>
<figure>
<a href="https://parade.com/member/paulettecohn/" data-parade-type="member" data-parade-member-id="652086" data-parade-location-types="member" data-parade-location-ids="voices" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<img src="https://secure.gravatar.com/avatar/84eff5c1e82dc8d009855fb5a730ccb6?s=50&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D50&r=G" data-parade-avatar-image="https://secure.gravatar.com/avatar/84eff5c1e82dc8d009855fb5a730ccb6?s=50&amp;d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D50&amp;r=G" data-parade-avatar-image-placeholding="true" alt="Paulette Cohn" nopin="nopin" />
</a>
</figure>
<h4>
<a href="https://parade.com/member/paulettecohn/" data-parade-type="member" data-parade-member-id="652086" data-parade-location-types="member" data-parade-location-ids="voices" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="fn">Paulette Cohn</span>
<span class="role">Editor</span>
<span class="org" style="display:none">Parade</span>
</a>
</h4>
</header>
<ul class="articles">
<li><a href="https://parade.com/1181784/paulettecohn/genius-aretha-franklin-courtney-b-vance-c-l-franklin/" data-parade-type="article" data-parade-location-types="article" data-parade-location-ids="voices" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false"><Em>Genius: Aretha</Em>’s Courtney B. Vance Explains Why Now Is the Time to Tell Aretha Franklin's&nbsp;Story</a></li>
</ul>
</article>
<article class="">
<header>
<figure>
<a href="https://parade.com/member/jessicasager/" data-parade-type="member" data-parade-member-id="687433" data-parade-location-types="member" data-parade-location-ids="voices" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
 <img src="https://secure.gravatar.com/avatar/f89144de761e4d02fbcaea3ff1722eee?s=50&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D50&r=G" data-parade-avatar-image="https://secure.gravatar.com/avatar/f89144de761e4d02fbcaea3ff1722eee?s=50&amp;d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D50&amp;r=G" data-parade-avatar-image-placeholding="true" alt="Jessica Sager" nopin="nopin" />
</a>
</figure>
<h4>
<a href="https://parade.com/member/jessicasager/" data-parade-type="member" data-parade-member-id="687433" data-parade-location-types="member" data-parade-location-ids="voices" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="fn">Jessica Sager</span>
<span class="role">Contributor</span>
<span class="org" style="display:none">Parade</span>
</a>
</h4>
</header>
<ul class="articles">
<li><a href="https://parade.com/1165727/jessicasager/easter-trivia/" data-parade-type="article" data-parade-location-types="article" data-parade-location-ids="voices" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Calling All Eggheads! 75 Easter Trivia Questions and Answers About the Hoppy&nbsp;Holiday</a></li>
</ul>
</article>
<article class="">
<header>
<figure>
<a href="https://parade.com/member/mikebloom/" data-parade-type="member" data-parade-member-id="656629" data-parade-location-types="member" data-parade-location-ids="voices" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<img src="https://secure.gravatar.com/avatar/1e80afc8730b232743edb1a06e5640a6?s=50&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D50&r=G" data-parade-avatar-image="https://secure.gravatar.com/avatar/1e80afc8730b232743edb1a06e5640a6?s=50&amp;d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D50&amp;r=G" data-parade-avatar-image-placeholding="true" alt="Mike Bloom" nopin="nopin" />
</a>
</figure>
<h4>
<a href="https://parade.com/member/mikebloom/" data-parade-type="member" data-parade-member-id="656629" data-parade-location-types="member" data-parade-location-ids="voices" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="fn">Mike Bloom</span>
<span class="role">Contributor</span>
<span class="org" style="display:none">Parade</span>
</a>
</h4>
</header>
<ul class="articles">
<li><a href="https://parade.com/1181022/mikebloom/who-is-piglet-on-masked-singer/" data-parade-type="article" data-parade-location-types="article" data-parade-location-ids="voices" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">Who Is Piglet on <em>The Masked Singer</em>? We Get Down and Dirty With Our&nbsp;Guesses</a></li>
</ul>
</article>
<article class="">
<header>
<figure>
<a href="https://parade.com/member/alexandra-hurtado/" data-parade-type="member" data-parade-member-id="687370" data-parade-location-types="member" data-parade-location-ids="voices" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<img src="https://secure.gravatar.com/avatar/15e101b428e4f1d76761ca88dff4feb9?s=50&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D50&r=G" data-parade-avatar-image="https://secure.gravatar.com/avatar/15e101b428e4f1d76761ca88dff4feb9?s=50&amp;d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D50&amp;r=G" data-parade-avatar-image-placeholding="true" alt="Alexandra Hurtado" nopin="nopin" />
</a>
</figure>
<h4>
<a href="https://parade.com/member/alexandra-hurtado/" data-parade-type="member" data-parade-member-id="687370" data-parade-location-types="member" data-parade-location-ids="voices" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<span class="fn">Alexandra Hurtado</span>
<span class="role">Contributor</span>
<span class="org" style="display:none">Parade</span>
</a>
</h4>
</header>
<ul class="articles">
<li><a href="https://parade.com/1159256/alexandra-hurtado/oscars-2021/" data-parade-type="article" data-parade-location-types="article" data-parade-location-ids="voices" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">The Show Will Go On! Your Guide to The 2021 Oscars, Including the&nbsp;Nominees</a></li>
</ul>
</article>
</section>
</section>
</div>
</div>
</section>
</div>
<div id="newsletter_container" class="newsletter-block">
<div class="newsletter-block__signup signup_module standalone" data-parade-type="promoarea" data-parade-location-ids="newsletter" data-parade-newsletter-type="default" data-parade-newsletter-slug="parade">
<div class="signup_content signup__content">
<form>
<span class="top-headline">Let's make it official</span>
<span class="message">Celeb interviews, recipes, wellness tips and horoscopes delivered to your inbox daily.</span>
<fieldset>
<div class="input_group">
<label>Email Address</label>
<input type="text" name="email" value="" placeholder="Email Address" data-parade-type="email">
<span class="submit_block">
<input class="has_newsletter single" type="submit" value="Sign Up">
<span class="loading_spinner">
<span class="bar bar_1"></span>
<span class="bar bar_2"></span>
<span class="bar bar_3"></span>
<span class="bar bar_4"></span>
<span class="bar bar_5"></span>
<span class="bar bar_6"></span>
<span class="bar bar_7"></span>
<span class="bar bar_8"></span>
<span class="bar bar_9"></span>
<span class="bar bar_10"></span>
<span class="bar bar_11"></span>
<span class="bar bar_12"></span>
</span>
</span>
<span class="error_message">
Please enter a valid email address.
</span>
</div>
<div class="note success">
Thanks for signing up! Please check your email to confirm your subscription.
</div>
</fieldset>
</form>
</div>
</div>
</div>
</div>
</div>
<footer data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="footer" data-parade-views="false" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">
<div class="wrapper new-footer">
<div class="container-fluid">
<div class="new-footer-logos">
<a href="https://www.parade.com"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgwIiBoZWlnaHQ9IjEwMyIgdmlld0JveD0iMCAwIDQ4MCAxMDMiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjx0aXRsZT5wYXJhZGUtbG9nbzwvdGl0bGU+PGRlZnM+PHBhdGggaWQ9ImEiIGQ9Ik0uMjAxIDc1Ljk0SDc2LjRWLjAzSC4yMDF6Ii8+PHBhdGggaWQ9ImMiIGQ9Ik0uNzYgNzUuOTRoNzUuMjZWLjAzSC43NnY3NS45MXoiLz48L2RlZnM+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48cGF0aCBkPSJNNDc5LjM4IDU3LjU2YzAgMS4wNy0uNTkgMS41NC0xLjkgMS41NGgtNDcuOHYtMS44OWgyOS44MmMtLjEyLTE1Ljk4LTMuMzItMjguNjQtMTMuNzMtMjguNjRsLjA0LTEuNjZjMjAuMzMuMDIgMzIuNSAxMi43OSAzMy41NyAzMC42NU00NjcuMDcgNjguMjFjNi44NiAwIDExLjQ4IDQuNjIgMTEuNDggMTAuODkgMCA3LjkyLTUuNDI5IDE1LjE3OS0xMy44NCAxOS40NmwtLjgxLTEuNjVjMy4yMy0xLjY2IDUuNzgtNC4wOCA3LjU1MS03LjE2LTEuMzAxLjU5LTIuNzIxLjgzLTQuMzgxLjgzLTYuMDMgMC0xMS00Ljk3LTExLTExLjAxMSAwLTYuMzg5IDQuNzMtMTEuMzU5IDExLTExLjM1OSIgZmlsbD0iI0ZGRiIvPjxwYXRoIGQ9Ik00NjMuOSA5Ni45MWwuODEgMS42NWMtNC45MSAyLjQ5LTEwLjgzIDMuOTY5LTE3LjI4IDMuOTY5LTI0LjM4IDAtMzcuOTktMTIuODk5LTM3Ljk5LTM2LjU1OSAwLTIzLjY3IDE2LjkyLTM5LjA2IDM2LjMzLTM5LjA2aC4wNGwtLjA0IDEuNjZjLTguOTkgMC0xNC45MSA5Ljk0LTE2LjA5IDI4LjY0djEuODloLS4xMmMtLjEyIDIuMDEtLjEyIDMuOTEtLjEyIDYuMDR2MS40MmMwIDE3Ljg2IDguMTcgMzIuODkgMjIuODQgMzIuODkgNC41IDAgOC40LS44OSAxMS42Mi0yLjU0TTQwNC44MzEgOTkuNjl2MS44OUgzODQuNDdjLTYuMTUgMC05LjU4LTIuNzIxLTkuNTgtMTEuMzZ2LTQuNzNjLS4yNC43MS0uNSAxLjQtLjc2IDIuMDdsLTEuNzQtLjYxYzIuMzUtNi4wMSAzLjY4LTEzLjUzIDMuNjgtMjAuNTF2LTUuMzNjMC01LjkyLS42OS0xMS4xOC0xLjktMTUuNTlsMS43ODEtLjVWMjFjMC0xMy40OS0yLjAxMS0xNC43OS0xNC41NTEtMTQuNTZWNC42N2M3LjU3IDAgMTQuNzktLjgzIDIxLjc3LTEuOSA1LjIxLS44MiA4LjQtMS44OSA5LjU5LTEuODkgMS40MiAwIDEuNTQgMS4wNyAxLjU0IDIuMzd2NzkuMzk5YzAgMTQuNTYxIDEuNjUxIDE3LjA0MSAxMC41MzEgMTcuMDQxIiBmaWxsPSIjRkZGIi8+PHBhdGggZD0iTTM3NS45NTEgNDUuMDJsLTEuNzgxLjVjLTIuNTMtOS4yOC03LjM2LTE0LjgyLTEyLjg5LTE0LjgyLTcuNTcgMC0xNS4xNSA3LjY5LTE1LjE1IDM0LjU2IDAgMjcuNTcgNy4yMiAzMy4zNyAxNC42OCAzMy4zNyA0LjkgMCA4LjktNC44OCAxMS41OC0xMS42OGwxLjc0LjYxYy0zLjkxIDEwLjAwOS05LjcgMTUuMjEtMTkuMjQgMTUuMjEtMTUuMzggMC0yOC43NS05LjM1LTI4Ljc1LTM2LjggMC0yNy40NiAxNC4zMTEtMzkuMDYgMjkuNDYtMzkuMDYgMTEuMTIgMCAxNy40IDYuODcgMjAuMzUxIDE4LjExIiBmaWxsPSIjRkZGIi8+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjQ1IDI3KSI+PG1hc2sgaWQ9ImIiIGZpbGw9IiNmZmYiPjx1c2UgeGxpbms6aHJlZj0iI2EiLz48L21hc2s+PHBhdGggZD0iTTc2LjQgNzIuNjl2MS44OUg1Ni4xN2MtNS45MiAwLTkuNDY5LTIuODQtOS40NjktMTEuNzFWNjEuOGMtLjI5Ljc0LS42MzEgMS4zOS0uOTcxIDEuOTdsLTEuNzktLjY4YzIuMDktMy42OTEgMy4yMy04LjM5IDMuMjMtMTIuMDVWMjguMDhjLTEuODYgMi4xNy00LjgxIDMuOTgtOC41MyA1LjQzbC0uNzEtMS44MWM1LjQyLTIuMDkgOS4yNC01LjA1IDkuMjQtMTAuNzJWMTcuOWMwLTEwLjQxLTYuMzktMTUuOTctMTYuMjEtMTUuOTctMS4xNiAwLTIuMzMuMDUtMy41MDkuMTZMMjcuMjYuMjdjMS42LS4xNiAzLjI3LS4yNCA1LS4yNCAyMS40MiAwIDMzLjYxMSA4LjI5IDMzLjYxMSAyNS44djMwLjI5QzY1Ljc1IDcwLjQ0IDY3Ljg4IDcyLjY5IDc2LjQgNzIuNjkiIGZpbGw9IiNGRkYiIG1hc2s9InVybCgjYikiLz48cGF0aCBkPSJNNDMuOTQgNjMuMDlsMS43OS42OGMtLjE5LjM1LS4zOS42OC0uNTY5Ljk5QzQwLjMxIDcyLjU2OSAzMi43NCA3NiAyMi4yMSA3NiA5LjQzIDc2IC4yMDEgNzAuOTEuMjAxIDU3LjY2YzAtOS45NCA0Ljk2OS0xNC45MSAxMi4wNjktMTguMSA2Ljk4LTMuMiAxNi4wOS00LjYyIDI0LjI1LTcuMzQuNDgtLjE3Ljk1LS4zNCAxLjQxLS41MmwuNzEgMS44MWMtLjUzLjIxLTEuMDguNDEtMS42NC42LTExLjQ4IDMuOTEtMTYuMSA4LjI4OS0xNi4xIDIyLjM3IDAgMTAuMjkgNC41IDE0LjY3IDExLjQ4IDE0LjY3IDQuMjYgMCA4LjQtMi45NiAxMS4xMy03LjM0LjE1MS0uMjQxLjI5LS40OC40My0uNzIiIGZpbGw9IiNGRkYiIG1hc2s9InVybCgjYikiLz48L2c+PHBhdGggZD0iTTI3Mi4yNiAyNy4yN2wuMTkxIDEuODJjLTUuMDkxLjQ2LTEwLjIzMSAxLjk3LTEzLjg4MSA1LjA0Ljk0LS4yMyAxLjc3LS40NyAyLjg0MS0uNDcgNi44NTkgMCAxMC42NDkgNS40NCAxMC42NDkgMTEgMCA2LjM5LTQuODUgMTEuMTMtMTEuMTMgMTEuMTMtNi43NCAwLTExLjgzLTQuMjYtMTEuODMtMTEuMzYgMC04LjgyIDguOTgxLTE1Ljg0IDIzLjE2LTE3LjE2TTIyNy45NyAyNy4yN2M4LjY0IDAgMTMuMDIgNi4wMyAxMy4wMiAxMS44MyAwIDcuNDYtNS4yMSAxMS43Mi0xMS4wMSAxMS43Mi02LjUgMC0xMS4zNi00Ljk3LTExLjM2LTEwLjg5IDAtNS4wOSAyLjI1LTguMjggNS40NS05LjgyLTQuOTcuNzMtOS4zNyAzLjItMTIuNzUgNy4zOGwtMS44NC0uNzljNC44Mi02LjAyIDExLjc0LTkuNDMgMTguNDktOS40MyIgZmlsbD0iI0ZGRiIvPjxwYXRoIGQ9Ik0yMTQuODQgOTkuNjl2MS44OWgtMzguODJ2LTEuNzdjOC4xNyAwIDEwLjMtMi42IDEwLjE4LTE2LjIxVjQ2LjQ0YzAtMTIuNjYtMS43Ny0xNC4wOC0xMi4wNy0xMy45NlYzMC43YzguNjQgMCAxNC41Ni0uODMgMjAuNzEtMS42NiA0LjI2LS41OSA2Ljk4LTEuMTggOC4wNS0xLjE4IDEuNDIgMCAxLjUzIDEuMDcgMS41MyAyLjM3djE2LjIxYzEuMTEtMy43MyAyLjg3LTcuMDEgNS4wNi05Ljc0bDEuODQuNzljLTQuMzUgNS4zNy03LjAxIDEzLjU4LTcuMDEgMjQuNTd2MjEuMDZjLS4xMiAxNC4zMiAyLjAxIDE2LjU3IDEwLjUzIDE2LjU3IiBmaWxsPSIjRkZGIi8+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTAwIDI3KSI+PG1hc2sgaWQ9ImQiIGZpbGw9IiNmZmYiPjx1c2UgeGxpbms6aHJlZj0iI2MiLz48L21hc2s+PHBhdGggZD0iTTc2LjAyIDcyLjgxdjEuNzdINTYuNzRjLTUuOTIgMC05LjQ3LTIuODQtOS40Ny0xMS43MVY2MS44bC0uNzIgMS4zOC0xLjYxLS44NGMxLjktMy41NjEgMi44LTcuODkgMi44LTExLjNWMjguMDhjLTEuODYgMi4xNy00LjgxIDMuOTgtOC41MyA1LjQzbC0uNzEtMS44MWM1LjQyLTIuMDkgOS4yNC01LjA1IDkuMjQtMTAuNzJWMTcuOWMwLTEwLjQxLTYuNTEtMTUuOTctMTYuMjEtMTUuOTctMS4xNSAwLTIuMzMuMDUtMy41LjE2TDI3Ljg0LjI3YzEuNi0uMTYgMy4yNi0uMjQgNC45OS0uMjQgMjEuNDIgMCAzMy42MSA4LjI5IDMzLjYxIDI1Ljh2MzAuNTI5QzY2LjMyIDcwLjIxIDY4LjEgNzIuODEgNzYuMDIgNzIuODEiIGZpbGw9IiNGRkYiIG1hc2s9InVybCgjZCkiLz48cGF0aCBkPSJNNDYuNTUgNjMuMThsLS44MiAxLjU4QzQwLjg4IDcyLjU2OSAzMy4zMSA3NiAyMi43NyA3NiA5Ljk5IDc2IC43NiA3MC45MS43NiA1Ny42NmMwLTkuOTQgNC45Ny0xNC45MSAxMi4wNy0xOC4xIDYuOTktMy4yIDE2LjEtNC42MiAyNC4yNi03LjM0LjQ4LS4xNy45NS0uMzQgMS40MS0uNTJsLjcxIDEuODFjLS41My4yMS0xLjA4LjQxLTEuNjQuNi0xMS40OCAzLjkxLTE2LjEgOC4yODktMTYuMSAyMi4zNyAwIDEwLjI5IDQuNSAxNC42NyAxMS40OCAxNC42NyA0LjI2IDAgOC40LTIuOTYgMTEuMTItNy4zNC4zMS0uNDcuNi0uOTcuODctMS40N2wxLjYxLjg0IiBmaWxsPSIjRkZGIiBtYXNrPSJ1cmwoI2QpIi8+PC9nPjxwYXRoIGQ9Ik0xMjcuODQgMjcuMjdsLjE5IDEuODJjLTUuMS40Ni0xMC4yNCAxLjk3LTEzLjg5IDUuMDQuOTQtLjIzIDEuNzctLjQ3IDIuODQtLjQ3IDYuODYgMCAxMC42NSA1LjQ0IDEwLjY1IDExIDAgNi4zOS00Ljg2IDExLjEzLTExLjEzIDExLjEzLTYuNzQgMC0xMS44My00LjI2LTExLjgzLTExLjM2IDAtOC44MyA4Ljk4LTE1Ljg0IDIzLjE3LTE3LjE2TTk1LjE0IDMzLjljMCAxOS41Mi0xNC43OSAyOS45NC00Ny40NSAyOS45NEg0NS4ydi0yLjAyYzE5LjI5IDAgMjkuNy0xMC4xNyAyOS43LTI4LjYzUzY1LjIgNi41NiA0NS4yIDYuNTZWNC42N2gzLjA4YzI5Ljk0IDAgNDYuODYgOS4zNSA0Ni44NiAyOS4yMyIgZmlsbD0iI0ZGRiIvPjxwYXRoIGQ9Ik01NC45IDk5LjY5djEuODlIMHYtMS44OWMxNC45MSAwIDE3Ljk4LTIuMjUgMTcuOTgtMTYuMDlWMjMuMDFDMTcuOTggOC42OSAxNS44NSA2LjU2LjcxIDYuNTZWNC42N0g0NS4ydjEuODloLTcuOTN2NTUuMjZoNy45M3YyLjAyaC03LjkzVjgzLjZjLS4xMiAxMy43MTkgMy4zMiAxNS43MyAxNy42MyAxNi4wOSIgZmlsbD0iI0ZGRiIvPjwvZz48L3N2Zz4=" alt="PARADE" data-parade-image-inlining="true" data-parade-image="https://local.parade.com/wp-content/themes/wp-theme/img/logos/parade.png" rel="logo" nopin="nopin"></a>
</div>
<div class="row-fluid main_row">
<div class="new-footer-social">
<ul>
<div class="social_item_instagram" data-parade-type="menu-item" data-parade-menu-id="instagram" data-parade-location-types="menu-item" data-parade-location-ids="footer" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<a href='https://www.instagram.com/parade.media' class="social_link_instagram new-footer-social-instagram" target="_blank"></a>
</div>
<div class="social_item_pinterest" data-parade-type="menu-item" data-parade-menu-id="pinterest" data-parade-location-types="menu-item" data-parade-location-ids="footer" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<a href='https://www.pinterest.com/parademag' class="social_link_pinterest new-footer-social-pinterest" target="_blank"></a>
</div>
<div class="social_item_youtube" data-parade-type="menu-item" data-parade-menu-id="youtube" data-parade-location-types="menu-item" data-parade-location-ids="footer" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<a href='https://www.youtube.com/user/ParadeMagazine' class="social_link_youtube new-footer-social-youtube" target="_blank"></a>
</div>
<div class="social_item_twitter" data-parade-type="menu-item" data-parade-menu-id="twitter" data-parade-location-types="menu-item" data-parade-location-ids="footer" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<a href='https://www.twitter.com/ParadeMagazine' class="social_link_twitter new-footer-social-twitter" target="_blank"></a>
</div>
<div class="social_item_facebook" data-parade-type="menu-item" data-parade-menu-id="facebook" data-parade-location-types="menu-item" data-parade-location-ids="footer" data-parade-views="false" data-parade-touches="false" data-parade-clicks="true" data-parade-mouseovers="false">
<a href='https://www.facebook.com/parademag' class="social_link_facebook new-footer-social-facebook" target="_blank"></a>
</div>
</ul>
</div>
<div class="category-wrap">
<div class="category-fluid">
<span class="footer-menu-group1">
<div class="categories">
<a href="https://parade.com/entertainment/" class="">Entertainment</a>
<ul class="footer-tab-up-submenu">
<li class=""><a href="https://parade.com/books/" class="footer-submenu-link">Read</a></li>
<li class=""><a href="https://parade.com/movies-tv/" class="footer-submenu-link">Watch</a></li>
<li class=""><a href="https://parade.com/music-podcasts/" class="footer-submenu-link">Listen</a></li>
<li class=""><a href="https://parade.com/magazine/" class="footer-submenu-link">Magazine</a></li>
<li class=""><a href="https://parade.com/932146/mikebloom/amazing-race-season-32/" class="footer-submenu-link">Amazing Race</a></li>
<li class=""><a href="https://parade.com/1131564/mikebloom/dancing-with-the-stars-season-30/" class="footer-submenu-link">DWTS</a></li>
<li class=""><a href="https://parade.com/1044810/mikebloom/the-masked-singer-season-4/" class="footer-submenu-link">Masked Singer</a></li>
<li class=""><a href="https://parade.com/1057230/mikebloom/survivor-season-41/" class="footer-submenu-link">Survivor</a></li>
</ul>
</div>
</span><span class="footer-menu-group1">
<div class="categories">
<a href="https://parade.com/food/" class="">Food & Drink</a>
<ul class="footer-tab-up-submenu">
<li class=""><a href="https://parade.com/986637/parade/casserole-recipes/" class="footer-submenu-link">Casserole Recipes</a></li>
<li class=""><a href="https://parade.com/chicken/" class="footer-submenu-link">Chicken Recipes</a></li>
<li class=""><a href="https://parade.com/954875/parade/crock-pot-recipes/" class="footer-submenu-link">Crock Pot Recipes</a></li>
<li class=""><a href="https://parade.com/dessert/" class="footer-submenu-link">Dessert</a></li>
<li class=""><a href="https://parade.com/easy-meals/" class="footer-submenu-link">Easy Meals</a></li>
<li class=""><a href="https://parade.com/1018830/parade/ground-beef-recipes/" class="footer-submenu-link">Ground Beef Recipes</a></li>
<li class=""><a href="https://parade.com/healthy-recipes/" class="footer-submenu-link">Healthy Recipes</a></li>
<li class=""><a href="https://parade.com/1048195/parade/pasta-recipes/" class="footer-submenu-link">Pasta Recipes</a></li>
<li class=""><a href="https://parade.com/tag/recipes/" class="footer-submenu-link">Recipes</a></li>
<li class=""><a href="https://parade.com/1133959/parade/best-soup-recipes/" class="footer-submenu-link">Soup Recipes</a></li>
<li class=""><a href="https://parade.com/1033852/parade/vegan-recipes/" class="footer-submenu-link">Vegan Recipes</a></li>
<li class=""><a href="https://parade.com/995147/parade/st-patricks-day-recipes/" class="footer-submenu-link">St. Patrick's Day Recipes</a></li>
<li class=""><a href="https://parade.com/1022051/parade/easter-recipes/" class="footer-submenu-link">Easter Dinner Ideas</a></li>
<li class=""><a href="https://parade.com/969844/parade/weight-watchers-recipes/" class="footer-submenu-link">WW Recipes</a></li>
<li class=""><a href="https://parade.com/pop-kitchen/" class="footer-submenu-link">Pop Kitchen</a></li>
<li class=""><a href="https://www.youtube.com/channel/UCH0nW7Z_xsKQmVL1rml36Vg" class="footer-submenu-link">Videos</a></li>
<li class=""><a href="https://parade.com/what-america-eats/" class="footer-submenu-link">What America Eats</a></li>
</ul>
</div>
</span><span class="footer-menu-group1">
<div class="categories">
<a href="https://parade.com/health/" class="">Wellness</a>
<ul class="footer-tab-up-submenu">
<li class=""><a href="https://parade.com/self-care/" class="footer-submenu-link">Self-Care</a></li>
<li class=""><a href="https://parade.com/healthy-now/" class="footer-submenu-link">Healthy Now</a></li>
<li class=""><a href="https://parade.com/mental-health/" class="footer-submenu-link">Mental Health</a></li>
<li class=""><a href="https://parade.com/caregiver-boot-camp/" class="footer-submenu-link">Caregiving</a></li>
<li class=""><a href="https://parade.com/covid-vaccine/" class="footer-submenu-link">COVID-19 Vaccine</a></li>
<li class=""><a href="https://parade.com/super-survivors/" class="footer-submenu-link">Cancer Survivors</a></li>
<li class=""><a href="https://parade.com/cold-and-flu/" class="footer-submenu-link">Cold and Flu</a></li>
<li class=""><a href="https://parade.com/986848/nancy_henderson/types-of-diets/" class="footer-submenu-link">Types of Diets</a></li>
<li class=""><a href="https://parade.com/969668/ericasweeney/benefits-of-meditation/" class="footer-submenu-link">Benefits of Meditation</a></li>
<li class=""><a href="https://parade.com/970149/ashleylauretta/best-workout-apps/" class="footer-submenu-link">Best Free Workout Apps</a></li>
<li class=""><a href="https://parade.com/1113631/korinmiller/best-stationary-bikes/" class="footer-submenu-link">Best Stationary Bike</a></li>
<li class=""><a href="https://parade.com/970087/lisamulcahy/keto-diet-food-list/" class="footer-submenu-link">Keto Approved Foods</a></li>
<li class=""><a href="https://parade.com/983137/ericasweeney/mediterranean-diet-food-list/" class="footer-submenu-link">Mediterranean Diet Food List</a></li>
<li class=""><a href="https://parade.com/922292/amberpetty/soursop-tea/" class="footer-submenu-link">Soursop Tea Benefits</a></li>
<li class=""><a href="https://parade.com/numbrix/" class="footer-submenu-link">Numbrix</a></li>
</ul>
</div>
</span><span class="footer-menu-group1">
<div class="categories">
<a href="https://parade.com/living/" class="">Life</a>
<ul class="footer-tab-up-submenu">
<li class=""><a href="https://parade.com/family/" class="footer-submenu-link">Family</a></li>
<li class=""><a href="https://parade.com/founders-side-hustlers/" class="footer-submenu-link">Founders & Side Hustlers</a></li>
<li class=""><a href="https://parade.com/heroes-helpers/" class="footer-submenu-link">Heroes & Helpers</a></li>
<li class=""><a href="https://parade.com/252644/viannguyen/15-of-martin-luther-king-jr-s-most-inspiring-motivational-quotes/" class="footer-submenu-link">MLK Quotes</a></li>
<li class=""><a href="https://parade.com/260134/linzlowe/15-inspiring-quotes-for-black-history-month-freedom-is-never-given/" class="footer-submenu-link">Black History Month Quotes</a></li>
<li class=""><a href="https://parade.com/975103/marynliles/international-womens-day-quotes/" class="footer-submenu-link">International Women's Day Quotes</a></li>
<li class=""><a href="https://parade.com/tag/jokes/" class="footer-submenu-link">Jokes</a></li>
<li class=""><a href="https://parade.com/1007652/kelseypelzer/irish-blessings/" class="footer-submenu-link">Irish Blessings</a></li>
<li class=""><a href="https://parade.com/1146456/kelseypelzer/when-is-lent/" class="footer-submenu-link">Lent 2021</a></li>
<li class=""><a href="https://parade.com/984978/kelseypelzer/april-fools-pranks/" class="footer-submenu-link">April Fools' Day Pranks</a></li>
<li class=""><a href="https://parade.com/1006821/marynliles/easter-quotes/" class="footer-submenu-link">Easter Quotes</a></li>
<li class=""><a href="https://parade.com/1012420/nicolepajer/best-online-games/" class="footer-submenu-link">Online Games</a></li>
<li class=""><a href="https://parade.com/1043064/marynliles/texting-games/" class="footer-submenu-link">Texting Games</a></li>
<li class=""><a href="https://parade.com/969021/marynliles/popular-baby-names/" class="footer-submenu-link">Popular Baby Names</a></li>
<li class=""><a href="https://parade.com/945400/kelseypelzer/unique-baby-names/" class="footer-submenu-link">Unique Baby Names</a></li>
<li class=""><a href="https://parade.com/1116818/marynliles/angel-names/" class="footer-submenu-link">Angel Names</a></li>
<li class=""><a href="https://parade.com/travel/" class="footer-submenu-link">Travel</a></li>
<li class=""><a href="https://parade.com/tag/trivia/" class="footer-submenu-link">Trivia</a></li>
<li class=""><a href="https://www.youtube.com/playlist?list=PLs2k2TJZZt8nqdCVKmv63rYA6pAqXsIIN" class="footer-submenu-link">Try the Trend</a></li>
<li class=""><a href="https://parade.com/parade-picks/" class="footer-submenu-link">Shopping, Deals & Freebies</a></li>
<li class=""><a href="https://parade.com/what-people-earn/" class="footer-submenu-link">What People Earn</a></li>
</ul>
</div>
</span><span class="footer-menu-group1">
<div class="categories">
<a href="https://parade.com/culture/" class="">Pop Culture</a>
<ul class="footer-tab-up-submenu">
<li class=""><a href="https://parade.com/celebrities/" class="footer-submenu-link">Celebs</a></li>
<li class=""><a href="https://parade.com/royal-family/" class="footer-submenu-link">Royals</a></li>
<li class=""><a href="https://parade.com/1004471/marynliles/royal-baby-names/" class="footer-submenu-link">Royal Baby Names</a></li>
</ul>
</div>
</span>
</div>
</div>
</div>
<div class="row-fluid last_row">
<div class="span12" data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="bottom" data-parade-views="true" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">
<p data-parade-type="promoarea" data-parade-location-types="promoarea" data-parade-location-ids="legal" data-parade-views="false" data-parade-touches="false" data-parade-clicks="false" data-parade-mouseovers="false">© 2021 AMG/Parade. All rights reserved.
</p>
<p><div class="ad-link-footer">
<div class="new-footer-legal">
Your use of this website constitutes and manifests your acceptance
of our <a href="/user-agreement/">User Agreement</a>,
<a href="/privacy-policy/">Privacy Policy</a>,
<a href="/cookie-policy/">Cookie Notification</a>,
and awareness of the <a href="/privacy-policy/#cpr">California Privacy Rights</a>.
Pursuant to U.S. Copyright law, as well as other applicable federal
and state laws, the content on this website may not be reproduced,
distributed, displayed, transmitted, cached, or otherwise used,
without the prior, express, and written permission of Athlon Media Group.
<a href="/privacy-policy/#thirdparty">Ad Choices</a>
</div>
</div></p>
<p class="gdpr">
<span>Do not sell my <a href="javascript:void(0)" class="amgmanageconsent" data-consent-model="ccpa">personal information</a>.</span>
<span>Manage your GDPR consents by <a href="javascript:void(0)" class="amgmanageconsent" data-consent-model="gdpr">clicking here.</a></span>
</p>
<div class="new-footer-link-container">
<ul class="new-footer-contacts">
<li><a href="http://www.athlonmediagroup.com/parade/" target="_blank">About Parade</a></li><li><a href="http://www.athlonmediagroup.com/contact/" target="_blank">Contact Us</a></li><li><a href="http://www.athlonmediagroup.com/parade" target="_blank">Media Kit</a></li><li><a href="https://parade.com/media-relations/" target="_blank">Media Relations</a></li><li><a href="https://parade.com/parade-contributors/" target="_blank">Our Contributors</a></li>
</ul>
</div>
<img src="https://ath-clients.s3.amazonaws.com/parade/logo/ParadeMedia_SolidBlueWht_Reg.svg" alt="Parade Media" class="parade-media" />
</div>
<div class="footer-ad" style="display:flex;width:100%;justify-content:center;background-color:#212121;">
<div style="display:inherit;flex-direction:column;padding:20px 0 30px;color:#fff;font-size:12px;">
advertisement
<a href="https://parade.com/healthy-now/">
<img src="https://s3.amazonaws.com/i.athcdn.com/assets/images/ads/20_Parade_HealthyNowBanner2.jpg" border="0">
</a>
</div>
</div>
</div>
</div>
</div>
<style type="text/css">

</style>
</footer>
<div class="ad-wrapper">
<div id='div-gpt-ad-ditto-background-5' class="ad-ditto-background">
<script type='text/javascript'>
            window.AdManager.displaySlot("ditto_background", "div-gpt-ad-ditto-background-5");
        </script>
</div>
</div>
<span id="parade-modal-dialog-newsletter" style="display:none;">
<span id="parade-modal-dialog-newsletter-general">
<div id="newsletter_container" class="standalone"><div class="signup_module standalone" data-parade-type="promoarea" data-parade-location-ids="newsletter" data-parade-newsletter-type="default" data-parade-newsletter-slug="parade">
<div class="signup_content">
 <header>
<span class="icon"><span class="symbol"></span></span>
<h4>Parade Daily</h4>
<div class="signup_text">
Celebrity interviews, recipes and health tips delivered to your&nbsp;inbox.
</div>
</header>
<form>
<fieldset>
<div class="input_group input_algnmnt">
<label>Email Address</label>
<input type="text" name="email" value="" placeholder="Email Address" data-parade-type="email">
<span class="submit_block">
<input class="has_newsletter single" type="submit" value="Sign Up">
<span class="loading_spinner">
<span class="bar bar_1"></span>
<span class="bar bar_2"></span>
<span class="bar bar_3"></span>
<span class="bar bar_4"></span>
<span class="bar bar_5"></span>
<span class="bar bar_6"></span>
<span class="bar bar_7"></span>
<span class="bar bar_8"></span>
<span class="bar bar_9"></span>
<span class="bar bar_10"></span>
<span class="bar bar_11"></span>
<span class="bar bar_12"></span>
</span>
</span>
<span class="error_message">
Please enter a valid email address.
</span>
</div>
<div class="note success">
Thanks for signing up! Please check your email to confirm your subscription.
</div>
</fieldset>
</form>
</div>
</div>
</div>
</span>
<span id="parade-modal-dialog-newsletter-food">
<div id="newsletter_container" class="standalone"><div class="signup_module standalone food" data-parade-type="promoarea" data-parade-location-ids="newsletter" data-parade-newsletter-type="channel" data-parade-newsletter-slug="food">
<div class="signup_content">
<header>
<span class="icon"><span class="symbol"></span></span>
<h4>Pop Kitchen Newsletter</h4>
<div class="signup_text">
Mouthwatering recipes, handy kitchen tips, and more delivered to your inbox
</div>
</header>
<form>
<fieldset>
<div class="input_group input_algnmnt">
<label>Email Address</label>
<input type="text" name="email" value="" placeholder="Email Address" data-parade-type="email">
<span class="submit_block">
<input class="has_newsletter single" type="submit" value="Sign Up">
<span class="loading_spinner">
<span class="bar bar_1"></span>
<span class="bar bar_2"></span>
<span class="bar bar_3"></span>
<span class="bar bar_4"></span>
<span class="bar bar_5"></span>
<span class="bar bar_6"></span>
<span class="bar bar_7"></span>
<span class="bar bar_8"></span>
<span class="bar bar_9"></span>
<span class="bar bar_10"></span>
<span class="bar bar_11"></span>
<span class="bar bar_12"></span>
</span>
</span>
<span class="error_message">
Please enter a valid email address.
</span>
</div>
<div class="note success">
Thanks for signing up! Please check your email to confirm your subscription.
</div>
</fieldset>
</form>
</div>
</div>
</div>
</span>
</span>
<span id="parade-modal-dialog-search" style="display:none;">
<span id="parade-modal-dialog-search-container">
<div id="search_container" class="standalone"><div class="search_module standalone" data-parade-type="promoarea" data-parade-location-ids="search">
<div class="search_content">
<div class="input_group">
<input type="text" name="search" value="" placeholder="Search" data-parade-type="search" class="input_group_search" style="
				display: block;
				padding: 8px;
				border: solid 1px #cacaca;
				margin: 0;
				-webkit-border-radius: 3px;
				-moz-border-radius: 3px;
				border-radius: 3px;
				float: left;
				width: 68.5%;
			">
<span class="submit_block" style="
				width: 25%;
				float: right;
			">
<input class="has_search single" type="submit" value="Search">
<span class="loading_spinner">
<span class="bar bar_1"></span>
<span class="bar bar_2"></span>
<span class="bar bar_3"></span>
<span class="bar bar_4"></span>
<span class="bar bar_5"></span>
<span class="bar bar_6"></span>
<span class="bar bar_7"></span>
<span class="bar bar_8"></span>
<span class="bar bar_9"></span>
<span class="bar bar_10"></span>
<span class="bar bar_11"></span>
<span class="bar bar_12"></span>
</span>
</span>
</div>
</div>
</div>
</div>
</span>
</span>
<script type="text/javascript">
(function(){var e=navigator.userAgent.match(/MSIE [67]\..*?(?!.*Trident\/[5-9])/);if(null!==e&&e.length>0){var t=document.getElementsByTagName("img"),n=document.getElementsByTagName("figure"),r=0,i=t.length,s;for(;r<i;r+=1){s=t[r];var o=s.getAttribute("data-parade-image");"undefined"!=typeof o&&"true"===s.getAttribute("data-parade-image-inlining")&&(s.src=s.getAttribute("data-parade-image"))}var r=0,i=n.length,s;for(;r<i;r+=1){s=t[r];if("true"===s.getAttribute("data-parade-background-image-inlining")){var o=s.getAttribute("data-parade-background-image");"undefined"!=typeof o&&(s.style["background-image"]="url("+s.getAttribute("data-parade-background-image")+")")}}}})();

window.parade = ( function( app ) {
	app.facebookAppId = "134158690266891";
    app.facebookAppNamespace = "amgparadecom";
    app.facebookCommentAppId = "134158690266891";
	return app;
} )( window.parade || {} );window.parade = ( function( app ) { app.refreshPolls = true; return app; } )( window.parade || {} );window.parade = ( function( app ) {
	app.endpoint = "https:\/\/parade.com\/wp-admin\/admin-ajax.php";
	app.post = {"ID":1039985,"post_author":687561,"post_date":"2020-10-01 15:15:30","post_date_gmt":"2020-10-01 19:15:30","post_content":"The <strong>best pick-up lines<\/strong>\u2014whether they're cheesy, funny pick-up lines that'll get someone laughing or clever pick-up lines that'll make you stand out\u2014will make breaking the ice and <a href=\"https:\/\/parade.com\/969981\/parade\/conversation-starters\/\" target=\"_blank\" rel=\"noopener noreferrer\">getting the conversation started<\/a> a little bit easier.\r\n\r\nPlus, using <a href=\"https:\/\/parade.com\/965742\/parade\/corny-jokes\/\" target=\"_blank\" rel=\"noopener noreferrer\">corny<\/a> pick-up lines shows off what a playful personality you have, too\u2014and who doesn't like that!\r\n\r\nSo whether you're looking for cute pick-up lines to tell a girl you like her or need some cheesy pick-up lines to text to a guy you're into, these 101 best funny pick up lines can help you get your flirt on.\r\n<h2>Best Pick Up Lines<\/h2>\r\n1. I hope you know CPR, because you just took my breath away!\r\n\r\n2. So, aside from taking my breath away, what do you do for a living?\r\n\r\n3. I ought to complain to Spotify for you not being named this week\u2019s hottest single.\r\n\r\n4. Are you a parking ticket? \u2018Cause you\u2019ve got \u2018fine\u2019 written all over you.\r\n\r\n5. Your eyes are like the ocean; I could swim in them all day.\r\n\r\n6. When I look in your eyes, I see a very kind soul.\r\n\r\n7. If you were a vegetable, you\u2019d be a \u2018cute-cumber.\u2019\r\n\r\n8. Do you happen to have a Band-Aid? \u2018Cause I scraped my knees falling for you.\r\n\r\n9. I never believed in love at first sight, but that was before I saw you.\r\n\r\n10. I didn\u2019t know what I wanted in a woman until I saw you.\r\n\r\n[image  id=\"1040103\" src=\"https:\/\/parade.com\/wp-content\/uploads\/2020\/05\/pick-up-lines-1.jpg\" class=\"paradeImage wp-media-selected size-100 aligncenter wp-image-1040103\" size=\"size-100\" link=\"none\" width=\"100%\" title=\"Clever pick up lines\" height=\"1080\" alt=\"\" caption=\"\"]\r\n\r\n11. I was wondering if you could tell me: If you\u2019re here, who\u2019s running Heaven?\r\n\r\n12. No wonder the sky is gray (or dark, if at night)\u2014all the color is in your eyes.\r\n\r\n13. You\u2019ve got everything I\u2019ve been searching for, and believe me\u2014I\u2019ve been looking a long time.\r\n\r\n14. You\u2019re like a fine wine. The more of you I drink in, the better I feel.\r\n\r\n15. You\u2019ve got a lot of beautiful curves, but your smile is absolutely my favorite.\r\n\r\n16. Are you as beautiful on the inside as you are on the outside?\r\n\r\n17. If being sexy was a crime, you\u2019d be guilty as charged.\r\n\r\n18. I was wondering if you\u2019re an artist because you were so good at drawing me in.\r\n\r\n19. It says in the Bible to only think about what\u2019s pure and lovely\u2026 So I\u2019ve been thinking about you all day long.\r\n\r\n20. Do you have a map? I just got lost in your eyes.\r\n<h2>Funny Pick Up Lines<\/h2>\r\n21. I\u2019d like to take you to the movies, but they don\u2019t let you bring in your own snacks.\r\n\r\n22. You know what you would look really beautiful in? My arms.\r\n\r\n23. I would never play hide and seek with you because someone like you is impossible to find.\r\n\r\n24. Are you a magician? It\u2019s the strangest thing, but every time I look at you, everyone else disappears.\r\n\r\n25. I think there\u2019s something wrong with my phone. Could you try calling it to see if it works?\r\n\r\n26. Hi, I just wanted to thank you for the gift. (pause) I\u2019ve been wearing this smile ever since you gave it to me.\r\n\r\n27. Are you an electrician? Because you\u2019re definitely lighting up my day\/night!\r\n\r\n28. I\u2019ve heard it said that kissing is the \u2018language of love.\u2019 Would you care to have a conversation with me about it sometime?\r\n\r\n29. I always thought happiness started with an \u2018h,\u2019 but it turns out mine starts with \u2018u.\u2019\r\n\r\n30. I believe in following my dreams. Can I have your Instagram?\r\n\r\n[image  id=\"1040106\" src=\"https:\/\/parade.com\/wp-content\/uploads\/2020\/05\/pick-up-lines-61.jpg\" class=\"paradeImage wp-media-selected size-100 aligncenter wp-image-1040106\" size=\"size-100\" link=\"none\" width=\"100%\" title=\"Funny pick up lines\" height=\"1080\" alt=\"\" caption=\"\"]\r\n\r\n31. Do you know what the Little Mermaid and I have in common? We both want to be part of your world.\r\n\r\n32. If you were a song, you\u2019d be the best track on the album.\r\n\r\n33. On a scale of 1 to America, how free are you tonight?\r\n\r\n34. You know, I always thought that Disneyland was the \u2018happiest place on Earth,\u2019 but that was before I got a chance to stand here next to you.\r\n\r\n35. Want to go outside and get some fresh air with me? You just took my breath away.\r\n\r\n36. If you were a taser, you\u2019d be set to \u2018stun.\u2019\r\n\r\n37. If you were a Transformer, you\u2019d be \u2018Optimus Fine.\u2019\r\n\r\n38. Is your name Google? Because you have everything I\u2019m searching for.\r\n\r\n39. Do you ever get tired from running through my thoughts all night?\r\n\r\n40. You know, they say that love is when you don\u2019t want to sleep because reality is better than your dreams. And after seeing you, I don\u2019t think I ever want to sleep again.\r\n<h2>Cheesy Pick Up Lines for Guys<\/h2>\r\n41. Your hand looks heavy\u2014can I hold it for you?\r\n\r\n42. Are you a time traveler? Because I absolutely see you in my future.\r\n\r\n43. Do you know what my shirt is made of? Boyfriend material.\r\n\r\n44. I thought this was a (bar\/restaurant\/etc.), but I must be in a museum because you\u2019re a piece of art.\r\n\r\n45. You know, your smile has been lighting up the room all night and I just had to come and say hello.\r\n\r\n46. Hi, I\u2019m (your name). Do you remember me? Oh, that\u2019s right\u2014we\u2019ve only met in my dreams.\r\n\r\n47. What does it feel like to be the most gorgeous girl in the room?\r\n\r\n48. I can\u2019t tell if that was an earthquake, or if you just seriously rocked my world.\r\n\r\n49. I just had to tell you, your beauty made me truly appreciate being able to see.\r\n\r\n50. If you were a fruit, you\u2019d be a \u2018fine-apple.\u2019\r\n\r\n[image  id=\"1040104\" src=\"https:\/\/parade.com\/wp-content\/uploads\/2020\/05\/pick-up-lines-21.jpg\" class=\"paradeImage wp-media-selected size-100 aligncenter wp-image-1040104\" size=\"size-100\" link=\"none\" width=\"100%\" title=\"Cute pick up line\" height=\"1080\" alt=\"\" caption=\"\"]\r\n\r\n51. I don\u2019t know your name, but I\u2019m sure it\u2019s as beautiful as you are. I\u2019m (your name).\r\n\r\n52. You are astoundingly gorgeous, but I can tell that\u2019s the least interesting thing about you. I\u2019d love to know more.\r\n\r\n53.\u00a0The sparkle in your eyes is so bright, the sun must be jealous.\r\n\r\n54. One night I looked up at the stars and thought, \u2018Wow, how beautiful.\u2019 But now that I\u2019m looking at you, nothing else can compare.\r\n\r\n55. If I had a nickel for every time I saw someone as beautiful as you, I\u2019d still only have five cents.\r\n\r\n56.\u00a0If beauty were time, you\u2019d be eternity.\r\n\r\n57. I think the only way you could possibly be more beautiful is if I got to know you.\r\n\r\n58. I don\u2019t know which is prettier today\u2014the weather, or your eyes.\r\n\r\n59. I swear someone stole the stars from the sky and put them in your eyes.\r\n\r\n60. In my opinion, there are three kinds of beautiful: Cute, pretty, and sexy. Somehow, you manage to be all three.\r\n\r\n[connatix]\r\n<h2>Cute Pick Up Lines for Girls<\/h2>\r\n61. I\u2019m not usually religious, but when I saw you, I knew you were the answer to my prayers.\r\n\r\n62. (Hold out your hand) Hey, I\u2019m going for a walk. Would you mind holding this for me?\r\n\r\n63. Do you believe in love at first sight, or should I try walking by again?\r\n\r\n64. I\u2019m really glad I just bought life insurance, because when I saw you, my heart stopped.\r\n\r\n65. I\u2019m not photographer, but I can definitely picture us together.\r\n\r\n66. Would you mind giving me a pinch? You\u2019re so cute, I must be dreaming.\r\n\r\n67. Wow, when God made you, he was seriously showing off.\r\n\r\n68. Excuse me, do you have the time? I just want to remember the exact minute I got a crush on you.\r\n\r\n69. Kiss me if I\u2019m wrong but, dinosaurs still exist, right?\r\n\r\n<span class=\"Apple-converted-space\">70.\u00a0If I were a cat, I\u2019d spend all nine of my lives with you.<\/span>\r\n\r\n[image  id=\"1040107\" src=\"https:\/\/parade.com\/wp-content\/uploads\/2020\/05\/pick-up-lines-81.jpg\" class=\"paradeImage wp-media-selected size-100 aligncenter wp-image-1040107\" size=\"size-100\" link=\"none\" width=\"100%\" title=\"Funny pick-up lines\" height=\"1080\" alt=\"\" caption=\"\"]\r\n\r\n71. You know, I had a pickup line ready to go, but you\u2019re so hot it just left my mind.\r\n\r\n72. When I text you goodnight later, what phone number should I use?\r\n\r\n73. I saw you walking by and I had to come say hello. I love your style. My name\u2019s (your name).\r\n\r\n74. I\u2019m not currently an organ donor, but I\u2019d be happy to give you my heart.\r\n\r\n75. I was going to say something really sweet about you, but when I saw you, I became speechless.\r\n\r\n76.You know, I believe that honesty is the best policy, so to be perfectly honest, you\u2019re the sexiest man I\u2019ve ever seen.\r\n\r\n77. I\u2019d say, \u2018God bless you,\u2019 but it looks like he already did.\r\n\r\n78. You must be a hell of a thief, because you managed to steal my heart from across the room.\r\n\r\n79. There must be something wrong with my eyes\u2014I can\u2019t seem to take them off of you.\r\n\r\n80. If you let me borrow a kiss, I promise I\u2019ll give it right back.\r\n<h2>Cute Pick Up Lines to Use at a Bar<\/h2>\r\n81. My friends bet me I couldn\u2019t talk to the prettiest girl in the bar. Want to use their money to buy some drinks?\r\n\r\n82. Trust me, I\u2019m not drunk; I\u2019m just intoxicated by you.\r\n\r\n83. I seem to have lost my number\u2014can I have yours?\r\n\r\n84. I was just trying to buy a drink here, but you\u2019re very distracting.\r\n\r\n85. I started reading\/watching an interesting book\/show last week, and I\u2019d love to discuss it with someone. Have you heard of it?\r\n\r\n86. You see my friend over there? S\/he wants to know if you think I\u2019m cute.\r\n\r\n87. I was going to call you beautiful, but then I realized I don\u2019t have your number yet.\r\n\r\n88. You: Are you good at math?\r\nThem: No (or Yes)\r\nYou: Me neither (or Me too). But the only number I care about is yours.\r\n\r\n89. I\u2019m surprised the restaurant\/bar\/etc. hasn\u2019t asked you to leave yet. You\u2019re so beautiful you\u2019re making all the other girls look bad.\r\n\r\n90. Excuse me, I don\u2019t mean to intrude, but you owe me a drink (pause), because when I saw you, I dropped mine.\r\n\r\n[image  id=\"1040108\" src=\"https:\/\/parade.com\/wp-content\/uploads\/2020\/05\/pick-up-lines-100.jpg\" class=\"paradeImage wp-media-selected size-100 aligncenter wp-image-1040108\" size=\"size-100\" link=\"none\" width=\"100%\" title=\"Cheesy pick-up lines\" height=\"1080\" alt=\"\" caption=\"\"]\r\n\r\n91. Are you any good at boxing? Because you look like a knockout.\r\n\r\n92. It\u2019s never easy meeting a complete stranger\u2014especially one as beautiful as you\u2014without being properly introduced. But can we try anyway?\r\n\r\n93. I wish I\u2019d paid more attention to science in high school, because you and I\u2019ve got chemistry and I want to know all about it.\r\n\r\n94. Hi, my name is (your name), but you can call me tonight or tomorrow.\r\n\r\n95. Do I know you? (pause) Oh, sorry, it\u2019s just that you look just like my next girlfriend.\r\n\r\n96. If I were to ask you out on a date, would your answer be the same as the answer to this question?\r\n\r\n97. Hey, do you mind if we take a picture together? I just want to show my mom what my next girlfriend looks like.\r\n\r\n98.\u00a0You look like you know how to have a good time. Been on any adventures lately?\r\n\r\n99. You know, I\u2019m actually terrible at flirting. How about you try to pick me up instead?\r\n\r\n100. Do you have a name, or can I just call you \u2018mine?\u2019\r\n\r\n101. I\u2019m not sure what it is yet, but something about you seems really interesting.\r\n\r\n<em>Check out:<\/em>\r\n\r\n<strong>250 <a href=\"https:\/\/parade.com\/968403\/parade\/questions-to-ask-a-guy\/\" target=\"_blank\" rel=\"noopener noreferrer\">Questions to Ask a Guy<\/a>\r\n250 <a href=\"https:\/\/parade.com\/966617\/parade\/never-have-i-ever-questions\/\" target=\"_blank\" rel=\"noopener noreferrer\">Never Have I Ever Questions<\/a>\r\n<\/strong><strong>250 \"<a href=\"https:\/\/parade.com\/964027\/parade\/would-you-rather-questions\/\" target=\"_blank\" rel=\"noopener noreferrer\">Would You Rather..?\" Questions<\/a><\/strong>\r\n<strong>250 <a href=\"https:\/\/parade.com\/966507\/parade\/truth-or-dare-questions\/\" target=\"_blank\" rel=\"noopener noreferrer\">Truth or Dare Questions<\/a><\/strong>","post_title":"101 Cheesy-But-Cute Pick Up Lines That'll Kick Your Flirting Game Into High Gear","post_excerpt":"","post_status":"publish","comment_status":"open","ping_status":"closed","post_name":"pick-up-lines","post_modified":"2020-12-10 11:42:04","post_modified_gmt":"2020-12-10 16:42:04","menu_order":0,"post_type":"post","post_mime_type":"","comment_count":"0","post_timestamp":1601565330000,"authorHandle":""};
    app.current = {"analytics":{"date":"20201001","primaryCategory":"entertainment"},"format":{"print":false,"single":true,"homepage":false,"featured_image":true},"type":{"homepage":false,"recipe":false,"gallery":false,"member":false,"tag":false,"tax":false,"attachment":false,"fullscreen":false,"channel":false,"section":false,"login":false,"register":false,"reset":false,"print":false,"newsletter":false,"search":false,"post":true,"freebie":false,"numbrix":false,"page":false},"slug":null,"taxonomyName":false,"tags":[{"display":"Cheesy Pick Up Lines","slug":"cheesy-pick-up-lines"},{"display":"Funny Pick Up Lines","slug":"funny-pick-up-lines"},{"display":"Pick Up Lines","slug":"pick-up-lines"}],"categories":[{"display":"Entertainment","slug":"entertainment"}],"member":{"active":false,"newsletter":false},"primary":{"channel":{"term_id":3,"name":"Entertainment","slug":"entertainment","term_group":0,"term_taxonomy_id":3,"taxonomy":"category","description":"Get the latest TV, movie, music, and celebrity news, exclusive interviews with your favorite stars, and behind-the-scenes celebrity videos and photos","parent":0,"count":29715,"filter":"raw","cat_ID":3,"category_count":29715,"category_description":"Get the latest TV, movie, music, and celebrity news, exclusive interviews with your favorite stars, and behind-the-scenes celebrity videos and photos","cat_name":"Entertainment","category_nicename":"entertainment","category_parent":0},"section":"none","display":{"term_id":3,"name":"Entertainment","slug":"entertainment","term_group":0,"term_taxonomy_id":3,"taxonomy":"category","description":"Get the latest TV, movie, music, and celebrity news, exclusive interviews with your favorite stars, and behind-the-scenes celebrity videos and photos","parent":0,"count":29715,"filter":"raw","cat_ID":3,"category_count":29715,"category_description":"Get the latest TV, movie, music, and celebrity news, exclusive interviews with your favorite stars, and behind-the-scenes celebrity videos and photos","cat_name":"Entertainment","category_nicename":"entertainment","category_parent":0},"member":687561,"format":"article"},"comments":{"walled":true,"disable_recent_comments":true},"copy":{"search":"Search Parade: Entertainment, Recipes, Health, Life, Holidays"}};
    app.newsletters = {"parade":{"type":"default","slug":"parade","copy":"<h4>Parade Daily<\/h4><div class=\"signup_text\">Celebrity interviews, recipes and health tips delivered to your&nbsp;inbox.<\/div>\n"},"food":{"type":"channel","slug":"food","copy":"<h4>Pop Kitchen Newsletter<\/h4><div class=\"signup_text\">Mouthwatering recipes, handy kitchen tips, and more delivered to your inbox.<\/div>\n"},"health":{"type":"channel","slug":"health","copy":"<h4>Healthy Now Newsletter<\/h4><div class=\"signup_text\">Get good vibes and health tips delivered right to your inbox!<\/div>\n"},"parade-picks":{"type":"subcategory","slug":"parade-picks","copy":"<h4>Pop Shop Newsletter<\/h4><div class=\"signup_text\">Get our favorite fabulous finds delivered right to your inbox!<\/div>\n"}};
    app.chartbeat = {"author":"marynliles:687561","section":"entertainment","loggedIn":false};
	return app;
} )( window.parade || {} );//var addthis_conf = { ver: 300 };
var addthis_product = 'wppssi-200';
var addthis_config = {
	pubid: "ra-52cd8afc148cded0",
	services_compact: 'print, email, more',
	data_ga_property: 'UA-15170730-18',
	data_ga_social : true,
	data_track_clickback: true,
	data_track_textcopy: true,
	data_track_addressbar: false,
	services_overlay:'facebook,twitter,pinterest_share',
	image_include: 'at_include'
};
var addthis_share = {
    'position' : 'top',
	url_transforms: {
	    clean: true,
	    referring_service : '{{code}}',
	    shorten: {
		twitter: 'bitly',
		facebook: 'bitly'
	    }
	},
	shorteners : {
	    bitly : {
		username: 'paradecondenastcom',
		apiKey: 'R_66f14bfd6671132aa3d6924a831839bf'
	    }
	},

};

function pd_callback(){if("undefined"==typeof window.parade.refreshPolls||!0!==window.parade.refreshPolls)return;var e=["728_top","728_bottom","300_top","300_bottom"],t=[];for(var n=0;n<e.length;n++){var r=e[n];window.AdManager&&window.AdManager.hasAd(r)&&t.push(window.AdManager.adInstances[r])}t.length>0&&window.AdManager&&window.AdManager.refreshAds(t)};

		</script>
<script type="text/javascript">

// GA stub in case consent is not granted
window.ga = function() {
    var stub = function() {
        if (typeof window.realGa === 'function') {
            console.info("Passing ga event through");
            window.realGa.apply(null, arguments);
            return;
        }
        console.info("Queing ga event pending consent");
        stub.cmd.push(arguments);
    };
    stub.cmd = [];
    stub.flushQueue = function() {
        console.info("Flushing ga queue");

        // shut down the queue
        stub.cmd.push = function(details) {
            window.realGa.apply(null, details);
        };

        while (stub.cmd.length > 0) {
            console.info("Applying queued event", stub.cmd[0]);
            window.realGa.apply(null, stub.cmd.shift());
        }
    };

    return stub;
}();

ConsentManager.registerVendorHandler("s26", function() {
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','realGa');

    ga('create', 'UA-15170730-18', 'auto', {'name': 'amgTracker', 'legacyCookieDomain': document.location.hostname});
    ga('amgTracker.require', 'displayfeatures');
    ga('amgTracker.require', 'linkid', 'linkid.js');

    /**
     * Set dimension vairables.
     * @note these will be sent and processed with the events other events that are triggered.
     * Map:
     *   dimension1 => member : scope = user
     *   dimension2 => signedin : scope = user
     *   dimension3 => format : scope = hit
     *   dimension4 => primary : scope = hit
     *   dimension5 => author : scope = hit
     */
    if (typeof window.parade !== "undefined" && typeof window.parade.current !== "undefined") {
        var customParams = {
            'customVarMember': '0',
            'customVarSignedIn': 'no',
            'customVarFormat': 'unknown',
            'customVarPrimary': 'unknown',
            'customVarAuthor': '0'
        };

        /** UID (Visitor) **/
        if (typeof window.parade.current.member.data !== 'undefined' && typeof window.parade.current.member.data.ID !== 'undefined') {
            customParams.customVarMember = window.parade.current.member.data.ID.toString();
        }

        /** User Type (Session) */
        if (typeof window.parade.current.member !== "undefined" && window.parade.current.member.active === true) {
            customParams.customVarSignedIn = 'yes';
            if (typeof window.parade.current.member.newsletter !== "undefined" && window.parade.current.member.newsletter === true) {
                customParams.customVarSignedIn = 'newsletter';
            }
        }

        /** Content Type (Format) */
        if (typeof window.parade.current.primary.format !== "undefined" && window.parade.current.primary.format !== null) {
            customParams.customVarFormat = window.parade.current.primary.format;
        }

        /** Primary Channel (Page) */
        if (typeof window.parade.current.primary.display !== "undefined" && window.parade.current.primary.display != null && typeof window.parade.current.primary.display.slug !== "undefined") {
            customParams.customVarPrimary = window.parade.current.primary.display.slug;
        }

        /** Primary Author (Page) */
        if (typeof window.parade.current.primary.member !== "undefined" && window.parade.current.primary.member !== null) {
            customParams.customVarAuthor = window.parade.current.primary.member.toString();
        }

        ga('amgTracker.set', 'dimension1', customParams.customVarMember);
        ga('amgTracker.set', 'dimension2', customParams.customVarSignedIn);
        ga('amgTracker.set', 'dimension3', customParams.customVarFormat);
    //    ga('amgTracker.set', 'dimension4', customParams.customVarPrimary);
        ga('amgTracker.set', 'dimension5', customParams.customVarAuthor);

        if (typeof window.parade.current.analytics !== "undefined") {
            if (typeof window.parade.current.analytics.primaryCategory !== "undefined") {
                ga('amgTracker.set', 'dimension4', window.parade.current.analytics.primaryCategory);
            }

            if (typeof window.parade.current.analytics.secondaryCategory !== "undefined") {
                ga('amgTracker.set', 'dimension6', window.parade.current.analytics.secondaryCategory);
            }

            if (typeof window.parade.current.analytics.date !== "undefined") {
                ga('amgTracker.set', 'dimension7', window.parade.current.analytics.date);
            }

            if (typeof window.parade.current.analytics.primaryPackage !== "undefined") {
                ga('amgTracker.set', 'dimension8', window.parade.current.analytics.primaryPackage);
            }
        }
    }

    ga('amgTracker.send', 'pageview');

    if (typeof ga.flushQueue === 'function') {
        ga.flushQueue();
    }
}, null, "GA tag add, custom dimensions");
</script>
<script>var AmgHeaderOps = (function(navContainer, incomingSettings) {
    //polyfill for element closest
    if (!Element.prototype.matches) {
        Element.prototype.matches = Element.prototype.msMatchesSelector || Element.prototype.webkitMatchesSelector;
    }
      
    if (!Element.prototype.closest) {
        Element.prototype.closest = function(s) {
            var el = this;
        
            do {
            if (el.matches(s)) return el;
            el = el.parentElement || el.parentNode;
            } while (el !== null && el.nodeType === 1);
            return null;
        };
    }

    if (window.NodeList && !NodeList.prototype.forEach) {
        NodeList.prototype.forEach = Array.prototype.forEach;
    }

    var mergeSettingsArray = function(defaults, incoming) {
        if (typeof incoming === "undefined") {
            return defaults;
        }

        var result = {};
        for ( var key in defaults ) {
            result[key] = (typeof incoming[key] === "undefined") ? defaults[key] : incoming[key]; 
        }
        return result;
    }

    var defaultSettings = {
        'desktopFormSelector' : ".desktop-display .search form",
        'desktopInputSelector' : ".desktop-display .search form input",
        'mobileFormSelector' : ".mobile-search form",
        'mobileInputSelector' : ".mobile-search form input",
        'searchButtonSelector' : ".action.action--search",
        'expandingMenuSelector' : ".right-nav a.action",

        // hamburger settings
        'hamburgerContainerSelector' : ".hamburger-container",
        "sideNavSelector" : ".nav-hidden",
        "navOverlaySelector" : ".nav-overlay",
        "hamburgerIndicatorSelector" : ".hamburger-indicator",
        "accordianMemberSelector" : ".accordion",

        // nav scroll settings
        "navFeatureSelector" : "#navigation-feature",
        "navMainSelector" : "#main-navigation",
        "navStickyClass" : "nav-down",
        "wpAdminClass" : "wp-admin-active",
        "headerHiddenPosition" : "-60px",
        "headerShownPosition" : 0,
        "stickyPadding" : 500
    };

    if (typeof navContainer === "undefined") {
        navContainer = window.document;
    }

    var settings = mergeSettingsArray(defaultSettings, incomingSettings);

    // search related variables
    var desktopSearchForm = navContainer.querySelector(settings.desktopFormSelector),
        desktopSearchInput= navContainer.querySelector(settings.desktopInputSelector),
        mobileSearchForm = navContainer.querySelector(settings.mobileFormSelector),
        mobileSearchInput = navContainer.querySelector(settings.mobileInputSelector),
        searchButtons = navContainer.querySelectorAll(settings.searchButtonSelector),
        expandingMenuButtons = navContainer.querySelectorAll(settings.expandingMenuSelector);

    var searchPlaceholderText = desktopSearchForm.getAttribute("placeholder") || "";

    // hamburger container variables
    var hamburgerContainers = document.querySelectorAll(settings.hamburgerContainerSelector),
        hamburgerIndicators = document.querySelectorAll(settings.hamburgerIndicatorSelector),
        sideNav = document.querySelector(settings.sideNavSelector),
        navOverlay = document.querySelector(settings.navOverlaySelector),
        bodyRef = document.querySelector('body'),
        htmlRef = document.querySelector('html');


    // nav scroll variables
    var prevScrollpos = window.pageYOffset,
        feature = document.querySelector(settings.navFeatureSelector),
        header = document.querySelector(settings.navMainSelector),
        _scrollHasStickyClass = false, // performance flag
        _scrollIsHidden = false, // performace flag
        currentScrollPos = window.pageYOffset, // used in navScroll, external for performace
        navOffset = 0, // used in navScroll, external for performance
        wpAdminBar,
        stickyOffset = (feature != null) ? feature.clientHeight : 0,
        navOffset = settings.headerShownPosition; //recalculated on the fly for mobile


    var toggleMenu = function (el) {
        var parent = el.closest('.nav-item');
        if (parent.classList.contains('active')) {
            closeMenuDropdown(el, parent);
        } else {
            openMenuDropdown(el, parent);
        }
    };

    var openMenuDropdown = function (actionBtn, parent) {
        parent = parent || actionBtn.closest('.nav-item');
        var target = document.querySelector("." + actionBtn.getAttribute("data-target"));

        if (target == null) { 
            // Not good, couldn't find the target.
            return;
        }

        var targetField = target.querySelector("input");

        target.classList.add('open');
        parent.classList.add('active');
        
        if (targetField !== null && typeof targetField.focus === "function") {
            targetField.focus();
        }

        closeOtherMenus(actionBtn, parent);
    };

    var closeMenuDropdown = function (actionBtn, parent) {
        parent = parent || actionBtn.closest('.nav-item');
        var target = document.querySelector('.' + actionBtn.getAttribute('data-target'));

        target.classList.remove('open');
        parent.classList.remove('active');
    };

    var closeOtherMenus = function (actionBtn, parent) {
        expandingMenuButtons.forEach(function(item) {
            if (item !== actionBtn) {
                closeMenuDropdown(actionBtn, parent);
                return;
            }
        });
    };

    var validateSearchInput = function ($input) {
        var isValid = true,
            searchText = $input.val();

        if (searchText === searchPlaceholderText) {
            isValid = false;
        } else if (searchText.length < 1) {
            isValid = false;
        }

        return isValid;
    };

    var hamburgerClickHandler = function(event) {
        event.preventDefault();
        
        if (isNavOpen()) {
            closeNav();
        } else {
            openNav();
        }
        return false;
    };

    var isNavOpen = function() {
        return (sideNav.classList.contains('closed') === false);
    }

    var openNav = function() {
        sideNav.classList.remove('closed');
        sideNav.classList.add("menu-open");
        navOverlay.classList.remove('hidden');
        bodyRef.classList.add('no-scroll');
        htmlRef.classList.add('no-scroll');
        hamburgerIndicators.forEach(function(hamburgerIndicator){ hamburgerIndicator.checked = true});
    };

    var closeNav = function () {
        sideNav.classList.add('closed');
        sideNav.classList.remove("menu-open");
        navOverlay.classList.add('hidden');
        bodyRef.classList.remove('no-scroll');
        htmlRef.classList.remove('no-scroll');
        hamburgerIndicators.forEach(function(hamburgerIndicator){ hamburgerIndicator.checked = false});
    };


    // this method is called on a per-frame basis, so it has some structural oddities for performance
    var navScroll = function () {
        if (prevScrollpos == window.pageYOffset) {
            return;
        }

        currentScrollPos = window.pageYOffset;

        if (window.pageYOffset >= stickyOffset || (feature == null && window.pageYOffset < 0)) {
            // Performance short circuit 
            if (!_scrollHasStickyClass) {
                // If we're past the start of the navbar, 
                // change the css to become a sticky nav bar at the top of the page
                header.classList.add(settings.navStickyClass);
                if (wpAdminBar !== null) {
                    // If the wp admin bar is active add a class to reposition the navigation
                    header.classList.add(settings.wpAdminClass);
                }
                
                _scrollHasStickyClass = true;
            }
            
        } else if (_scrollHasStickyClass) { // performance short circuit 
            // If we're above the start of the navbar, remove the sticky css class.
            header.classList.remove(settings.navStickyClass);
            header.classList.remove(settings.wpAdminClass);
            _scrollHasStickyClass = false;
        }

        if (prevScrollpos < currentScrollPos && currentScrollPos > (stickyOffset + settings.stickyPadding)) {
            if (!_scrollIsHidden) { // performance short circuit
                //while scrolling (going down), make the nav go away after past the feature position
                // if it is 500px past the nav start area (200px)
                header.style.transform = "translateY(" + settings.headerHiddenPosition + ")";
                _scrollIsHidden = true;
            }

        } else if (prevScrollpos >= currentScrollPos || currentScrollPos > stickyOffset || currentScrollPos < (stickyOffset + settings.stickyPadding)) {
            //while scrolling (going up), make the nav re-appear regardless of it's position.        
            navOffset = calculateNavOffset(currentScrollPos);
            header.style.transform = "translateY(" + navOffset + "px)";
            _scrollIsHidden = false;
        }

        prevScrollpos = currentScrollPos;
    };

    var calculateNavOffset = function(currentScrollPos) {
        if (!window.parade.is_phone 
            || wpAdminBar === null 
            || currentScrollPos >= wpAdminBar.clientHeight 
            || feature !== null) {
            return settings.headerShownPosition;
        }

        return wpAdminBar.clientHeight - currentScrollPos;
    }

    var initScrollMonitor = function() {
        // Performance Enhancement for onScroll with requestAnimationFrame
        var raf = window.requestAnimationFrame ||
            window.webkitRequestAnimationFrame ||
            window.mozRequestAnimationFrame ||
            window.msRequestAnimationFrame ||
            window.oRequestAnimationFrame;

        var lastScrollTop = window.scrollY;

        var loop = function() {
            if (lastScrollTop === window.scrollY) {
                raf(loop);
                return;
            }

            lastScrollTop = window.scrollY;

            // fire scroll function if scrolls vertically
            navScroll();
            raf(loop);
        }

        if (raf) {
            loop();
        };

        document.addEventListener("DOMContentLoaded", function() {
            // wp admin bar is constructed dynamically, wait for document load.
            wpAdminBar = document.getElementById("wpadminbar");
            if (wpAdminBar !== null && feature === null) {
                header.classList.add(settings.wpAdminClass);
            }
            if (wpAdminBar !== null && feature !== null && window.parade.is_phone) {
                stickyOffset = feature.clientHeight + wpAdminBar.clientHeight;
            }
            
            navScroll();
        });

    };


    // ACCORDION FUNCTION

    var initAccordians = function() {
        var topLevelNavItems;
        var elem = navContainer.querySelector(settings.accordianMemberSelector);

        // Create siblings helper method
        var getTopLevelNavItems = function (elem) {
            // Setup siblings array and get the first sibling
            var sibling = elem.parentNode.firstChild;
            var siblings = [];

            // Loop through each sibling and push to the array
            while (sibling) {
                if (sibling.nodeType === 1) {
                    siblings.push(sibling);
                }
                sibling = sibling.nextSibling
            }
            return siblings;

        };

        var handleAccordianClick = function (event) {
            this.parentNode.classList.toggle("active");
        };

        // Initialize accordion items
        var initializeAccordianItem = function (item) {
            item.firstElementChild.addEventListener('click', handleAccordianClick);
        };


        if (elem !== null) {  //double check the return if not found?  empty? null?
            topLevelNavItems = getTopLevelNavItems(elem);
            // Loops the the siblings array 
            for (var i = 0; i < topLevelNavItems.length; i++) {
                initializeAccordianItem(topLevelNavItems[i]);
            }
        }
    };

    var initMenuFunctionality = function() {
        searchButtons.forEach(function(searchBtn){
            if (typeof searchBtn.addEventListener !== "function") {
                return;
            }

            searchBtn.addEventListener("click", function (e) {
                e.preventDefault();
                e.stopPropagation();

                toggleMenu(this);
            });
        });

        desktopSearchForm.addEventListener("submit", function () {
            return validateSearchInput(desktopSearchInput);
        });

        mobileSearchForm.addEventListener("submit", function () {
            return validateSearchInput(mobileSearchInput);
        });

        var assignClickHandler = function (hamburgerContainer) {
            hamburgerContainer.addEventListener("click", hamburgerClickHandler);
            navOverlay.addEventListener("click", function(e,a,b) {
                e.preventDefault();
                if (isNavOpen()) {
                    closeNav();
                }
            });
        };

        hamburgerContainers.forEach(assignClickHandler);
    };

    return {
        'openNav': openNav,
        'closeNav': closeNav,
        'init' : function() {
            initMenuFunctionality();
            initAccordians();
            initScrollMonitor();
        }
    }


})();

AmgHeaderOps.init();
</script><script type='text/javascript'>
    var _sf_async_config = window._sf_async_config = (window._sf_async_config || {});
    /** CONFIGURATION START **/

    //Assign chartbeat section if available
    if (window.parade.chartbeat.section) {
        _sf_async_config.sections = window.parade.chartbeat.section;
    }
    //Assign chartbeat author if available
    if (window.parade.chartbeat.author) {
        _sf_async_config.authors = window.parade.chartbeat.author;
    }

    // Checks if user is logged in and tracks them accordingly
    var _cbq = window._cbq = (window._cbq || []);
    if (window.parade.chartbeat.loggedIn) {
        _cbq.push(['_acct', 'lgdin']);
    }
    else {
        _cbq.push(['_acct', 'anon']);
    }
    /** CONFIGURATION END **/

    (function() {
        function loadChartbeat() {
            window._sf_endpt = (new Date()).getTime();
            var e = document.createElement('script');
            e.setAttribute('language', 'javascript');
            e.setAttribute('type', 'text/javascript');
            e.setAttribute('src', '//static.chartbeat.com/js/chartbeat.js');
            document.body.appendChild(e);
        }

        window.ConsentManager.registerVendorHandler("s28", loadChartbeat, null, "Chartbeat add");
    })();
</script>

<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NQNX3LZ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script type='text/javascript'>
/* <![CDATA[ */
var rmp_frontend = {"admin_ajax":"https:\/\/parade.com\/wp-admin\/admin-ajax.php","postID":"1039985","noVotes":"No votes so far! Be the first to rate this post.","cookie":"You already voted! This vote will not be counted!","afterVote":"Thank you for rating this post!","notShowRating":"1","social":"1","feedback":"1","cookieDisable":"1","emptyFeedback":"Please insert your feedback in the box above!","hoverTexts":"1","preventAccidental":"1","grecaptcha":"1","siteKey":"","votingPriv":"1","loggedIn":"","positiveThreshold":"2","ajaxLoad":"2","nonce":"f3bef078b7"};
/* ]]> */
</script>
<script>window.jQuery || document.write('<script src="https://parade.com/wp-includes/js/jquery/jquery.js"><\/script>')</script>
<script type='text/javascript' src='https://parade.com/wp-content/plugins/rate-my-post/public/js/rate-my-post.js'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var EasyAzonPro_Localize_Links = {"ajaxAction":"easyazonpro_localize","ajaxUrl":"https:\/\/parade.com\/wp-admin\/admin-ajax.php"};
/* ]]> */
</script>
<script type='text/javascript' src='https://parade.com/wp-content/plugins/easyazon-pro/components/localization/links/resources/links.js'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var EasyAzonPro_Components_Popovers = {"ajaxUrl":"https:\/\/parade.com\/wp-admin\/admin-ajax.php","ajaxAction":"easyazon_get_popover_markup","loading":"Loading product data.","placement":"top","template":"<div class=\"popover easyazon-popover\"><div class=\"arrow\"><\/div><h3 class=\"popover-title\"><\/h3><div class=\"popover-content easyazon-popover-content\"><\/div><\/div>","timeout":"750"};
/* ]]> */
</script>
<script type='text/javascript' src='https://parade.com/wp-content/plugins/easyazon-pro/components/popovers/resources/popovers.js'></script>
<script type='text/javascript' defer="defer" async="1" src='https://parade.com/wp-content/plugins/amg_nativeai_analytics/assets/js/nativeai.js'></script>
<script type='text/javascript' src='https://parade.com/wp-includes/js/wp-embed.min.js'></script>
<script data-main="https://parade.com/wp-content/static/builds/main/article.min" data-version="8" src="https://parade.com/wp-content/static/builds/require/require-jquery.js" async="true" defer="true"></script>
</div>
</body>
</html>
"""
soup = BeautifulSoup(html_data, 'html.parser')

# get all p tags (only the pickup lines)
res = soup.find_all('p', {'class': None})
for r in res:
    string = r.getText()
    # to validate if it is pickupline (based from html; it always has number in front)
    if string[0:1].isnumeric():
        # the string will then be used to format it in javascript
        print(string)


