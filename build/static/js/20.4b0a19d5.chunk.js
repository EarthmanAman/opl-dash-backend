(this.webpackJsonpopl_frontend=this.webpackJsonpopl_frontend||[]).push([[20],{411:function(t,e,n){"use strict";n.r(e);var r=n(12),i=n(13),o=n(14),a=n(15),s=n(0),u=n.n(s),c=n(25),l=n(88),d=n.n(l),h=n(75),p=n(3),f=function(t){Object(o.a)(n,t);var e=Object(a.a)(n);function n(t){var i;return Object(r.a)(this,n),(i=e.call(this,t)).state={series:[],options:{chart:{type:"bar",height:350},title:{text:"Monthly Sale Comparison"},plotOptions:{bar:{horizontal:!1,columnWidth:"55%",endingShape:"rounded"}},dataLabels:{enabled:!1},stroke:{show:!0,width:2,colors:["transparent"]},xaxis:{title:{text:"Months"},categories:["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]},yaxis:{title:{text:i.props.dashboard_metric?"Kshs (Millions)":"Litres"}},fill:{opacity:1},tooltip:{y:{formatter:i.props.dashboard_metric?function(t){return"Kshs "+t+" Million"}:function(t){return t+" Litres"}}}}},i}return Object(i.a)(n,[{key:"render",value:function(){return Object(p.jsx)("div",{id:"chart",children:Object(p.jsx)(d.a,{options:this.state.options,series:this.state.series,type:"bar",height:350})})}}]),n}(u.a.Component);f.getDerivedStateFromProps=function(t,e){var n=void 0!==t.customer?function(t,e,n,r){if(void 0===t||null===t||t===[])return null;var i=t.filter((function(t){return t.year===parseInt(n)})),o=new Array(12).fill(0);for(var a in t=i.length>0?i[0].months:[]){var s=t[a];o[s.date__month-1]="Million"===r?Object(h.c)((e?s.sum:s.quantity)/1e7):Object(h.c)((e?s.sum:s.quantity)/1e3)}return o}(t.customer,t.dashboard_metric,t.customer_year,t.currency_type):null,r=[{name:t.dashboard_metric?"Revenue":"Quantity",data:null===n?[]:n}];return e.series=r,e.options.yaxis.title.text=t.dashboard_metric?"Customer Revenue":"Customer Quantity",e};e.default=Object(c.b)((function(t){return{}}),{})(f)},75:function(t,e,n){"use strict";n.d(e,"a",(function(){return r})),n.d(e,"b",(function(){return i})),n.d(e,"c",(function(){return o}));var r=function(t,e){return t.setMonth(t.getMonth()+e),t},i=function(t){return"Million"===t?"m":"k"},o=function(t){return parseFloat(t.toString().match(/^-?\d+(?:\.\d{0,2})?/)[0])}}}]);
//# sourceMappingURL=20.4b0a19d5.chunk.js.map