!function(e){var t={};function n(r){if(t[r])return t[r].exports;var o=t[r]={i:r,l:!1,exports:{}};return e[r].call(o.exports,o,o.exports,n),o.l=!0,o.exports}n.m=e,n.c=t,n.d=function(e,t,r){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(n.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)n.d(r,o,function(t){return e[t]}.bind(null,o));return r},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s=175)}({175:function(e,t,n){n(176),e.exports=n(256)},176:function(e,t){if(function(e,t){var n=e.__forecast||(e.__forecast={});if(n.domain="https://forecast.lemonde.fr",!n.loaded){var r=t.createElement("script");r.async=!0,r.src="".concat(n.domain,"/sdk.js");var o=t.getElementsByTagName("script")[0];o.parentNode.insertBefore(r,o),n.loaded=!0}}(window,document),window.__forecast.config={services:{readingRate:{},widget:[{targetSelector:"#forecast_widget",type:"retargeting",template:"retargeting",passLead:!0,failovers:[{name:"most_read",versions:[{rate:90,template:"tops",options:{orderBy:"pageview",publishedSince:"2d",since:"1d",itemNumber:"3"}},{rate:10,template:"recommendations",options:{type:"weighted-top-articles",itemNumber:"3"}}]}]}]},contentSelector:".article__content"},window.lmd.user){var n=window.lmd.user;window.__forecast.user={id:n.id,isSubscriber:n.abo,subscriptionStartDate:n.beginDate,subscriptionEndDate:n.expiryDate}}},256:function(e,t,n){"use strict";function r(e){var t=e.detail,n=t.version;!1!==t.feedback||1!==n&&2!==n||window.__forecast.launchComment()}n.r(t);var o=n(29);(document.getElementsByClassName("meta__social").length>0&&window.addEventListener("socialShare",(function(e){window.__forecast&&e.detail&&"element-live"!==e.detail.position&&function(e,t){switch(t){case"fb":e.launchShareFacebook();break;case"tw":e.launchShareTwitter();break;case"mail":e.launchShareMail();break;default:e.launchShare()}}(window.__forecast,e.detail.socialType)})),Object(o.a)(window.lmd,"analytics","amplitude","pageType")&&"commentaires"===window.lmd.analytics.amplitude.pageType)&&function(e,t){e&&e.addEventListener("commentPost",r.bind(t))}(document.getElementById("comment-form"))},29:function(e,t,n){"use strict";function r(e){for(var t=!0,n=arguments.length,r=new Array(n>1?n-1:0),o=1;o<n;o++)r[o-1]=arguments[o];return r.reduce((function(e,n){return e&&void 0!==e[n]?e[n]:(t=!1,null)}),e),t}n.d(t,"a",(function(){return r}))}});
//# sourceMappingURL=forecast.bundle.js.map