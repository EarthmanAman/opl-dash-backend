(this.webpackJsonpopl_frontend=this.webpackJsonpopl_frontend||[]).push([[13],{282:function(e,r,t){"use strict";var n=t(18),a=t(69),_=t(68),s=t.n(_),o=t(0),T=t(72),c=t(3),O=["bsPrefix","className","as"],i=o.forwardRef((function(e,r){var t=e.bsPrefix,_=e.className,o=e.as,i=void 0===o?"div":o,l=Object(a.a)(e,O),u=Object(T.b)(t,"row"),E=Object(T.a)(),A="".concat(u,"-cols"),N=[];return E.forEach((function(e){var r,t=l[e];delete l[e],r=null!=t&&"object"===typeof t?t.cols:t;var n="xs"!==e?"-".concat(e):"";null!=r&&N.push("".concat(A).concat(n,"-").concat(r))})),Object(c.jsx)(i,Object(n.a)(Object(n.a)({ref:r},l),{},{className:s.a.apply(void 0,[_,u].concat(N))}))}));i.displayName="Row",r.a=i},418:function(e,r,t){"use strict";t.r(r);var n=t(60),a=t(12),_=t(13),s=t(14),o=t(15),T=t(61),c=t.n(T),O=t(0),i=t.n(O),l=t(409),u=t(282),E=t(283),A=t(414),N=t(410),C=t(25),d=t(2),p=(t(83),t(84),t(64)),D=t(71),P=t(413),b=t(3),j=function(e){Object(s.a)(t,e);var r=Object(o.a)(t);function t(){return Object(a.a)(this,t),r.apply(this,arguments)}return Object(_.a)(t,[{key:"render",value:function(){var e=this;return Object.keys(this.props.errors).map((function(r,t){return Object(b.jsxs)(P.a,{variant:"danger",children:[r,": ",e.props.errors[r][0]]},t)}))}}]),t}(i.a.Component),f=j,U=t(26),I=t(76),x=function(e){Object(s.a)(t,e);var r=Object(o.a)(t);function t(){var e;Object(a.a)(this,t);for(var _=arguments.length,s=new Array(_),o=0;o<_;o++)s[o]=arguments[o];return(e=r.call.apply(r,[this].concat(s))).state={spinner:!1,redirect:!1,redirect_depot:!1,email:"",password:"",show_error:!1,null_error:!1,loaded:!1},e.onSubmit=function(){var r=Object(n.a)(c.a.mark((function r(t){var n,a,_;return c.a.wrap((function(r){for(;;)switch(r.prev=r.next){case 0:return t.preventDefault(),r.next=3,e.props.GET_TOKEN_ERROR_REMOVE_ACTION();case 3:if(n=e.state,a=n.email,_=n.password,""!==a&&""!==_){r.next=8;break}e.setState({null_error:!0}),r.next=11;break;case 8:return e.setState({spinner:!0,show_error:!1}),r.next=11,e.props.GET_TOKEN_ACTION(a,_);case 11:case"end":return r.stop()}}),r)})));return function(e){return r.apply(this,arguments)}}(),e}return Object(_.a)(t,[{key:"render",value:function(){var e=this,r=this.state,t=(r.show_error,r.null_error),n=r.spinner;r.email;return this.state.redirect?Object(b.jsx)(d.a,{to:"/"}):this.state.redirect_depot?Object(b.jsx)(d.a,{to:"/depots"}):Object(b.jsx)(l.a,{children:Object(b.jsxs)(u.a,{className:"login-row",children:[n?Object(b.jsx)(U.a,{spinner:n}):null,Object(b.jsx)(E.a,{className:"login-row__logo-col",children:Object(b.jsx)("img",{src:"".concat(D.b,"/static/opl_logo.png"),alt:"logo"})}),Object(b.jsx)(E.a,{xs:7,className:"login-row__form-col",children:Object(b.jsxs)(A.a,{onSubmit:this.onSubmit,className:"login-form",children:[Object(b.jsxs)("div",{className:"login-form__title",children:[Object(b.jsx)("h3",{children:"Sign in To The Dashboard"}),Object(b.jsx)("p",{children:"Enter your email and password to sign in."})]}),null!==this.props.login_error&&void 0!==this.props.login_error?Object(b.jsx)(f,{errors:this.props.login_error}):null,t?Object(b.jsx)(f,{errors:{"":["Fields cannot be empty"]}}):null,Object(b.jsx)(A.a.Group,{className:"mb-3",controlId:"formBasicEmail",children:Object(b.jsx)(A.a.Control,{type:"text",placeholder:"Enter email",className:"login-form__input",onChange:function(r){return e.setState({email:r.target.value,show_error:!1,null_error:!1})}})}),Object(b.jsx)(A.a.Group,{className:"mb-3",controlId:"formBasicPassword",children:Object(b.jsx)(A.a.Control,{type:"password",placeholder:"Password",className:"login-form__input",onChange:function(r){return e.setState({password:r.target.value,show_error:!1,null_error:!1})}})}),Object(b.jsx)(N.a,{variant:"primary",type:"submit",className:"login-form__submit",children:"Submit"})]})})]})})}}]),t}(i.a.Component);x.getDerivedStateFromProps=function(){var e=Object(n.a)(c.a.mark((function e(r,t){var n,a,_,s,o,T,O,i,l,u;return c.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(n=r.login_error,a=r.token,_=r.product_list,s=r.depot_list,o=r.customer_list,T=new Date("30 Jan 2022"),O=new Date("30 Jan 2022"),i=new Date("30 Jan 2022"),l=new Date("30 Jan 2022"),"object"!==typeof r.login_error||null===n){e.next=10;break}t.show_error=!0,t.spinner=!1,e.next=57;break;case 10:if(void 0===_||void 0===s||void 0===o){e.next=16;break}!1===a.is_staff?t.redirect_depot=!0:void 0!==o&&(t.redirect=!0),t.show_error=!1,t.spinner=!1,e.next=57;break;case 16:if(void 0===a||null===a||!1!==t.loaded){e.next=57;break}return t.loaded=!0,u=Object(I.a)(O,-1),e.next=21,r.UPDATE_DASHBOARD_METRIC_ACTION(!0);case 21:return e.next=23,r.UPDATE_CURRENCY_TYPE_ACTION("Million");case 23:return e.next=25,r.UPDATE_SELECTION_DATES_ACTION({endDate:T,startDate:u});case 25:return e.next=27,r.UPDATE_DEPOT_MONTH_MONTH_ACTION(13);case 27:return e.next=29,r.UPDATE_DEPOT_MONTH_YEAR_ACTION(T.getFullYear());case 29:return e.next=31,r.UPDATE_DEPOT_PRODUCT_MONTH_MONTH_ACTION(13);case 31:return e.next=33,r.UPDATE_DEPOT_PRODUCT_MONTH_YEAR_ACTION(T.getFullYear());case 33:return e.next=35,r.UPDATE_DEPOT_CUSTOMER_YEAR_ACTION(T.getFullYear());case 35:return e.next=37,r.UPDATE_DEPOT_CUSTOMER_MONTH_ACTION(13);case 37:return e.next=39,r.UPDATE_DEPOT_ACTION(0);case 39:if(!a.is_staff){e.next=50;break}return e.next=42,r.UPDATE_SALES_DATE_ACTION({end_date:i,start_date:Object(I.a)(l,-1)});case 42:return e.next=44,r.UPDATE_PRODUCT_MONTH_YEAR_ACTION(T.getFullYear());case 44:return e.next=46,r.UPDATE_TOP_CUSTOMER_MONTH_ACTION(13);case 46:return e.next=48,r.UPDATE_TOP_CUSTOMER_YEAR_ACTION(T.getFullYear());case 48:return e.next=50,r.UPDATE_TOP_CUSTOMER_PRODUCT_ACTION("All");case 50:return e.next=52,r.GET_DEPOT_LIST_ACTION();case 52:return e.next=54,r.GET_PRODUCT_LIST_ACTION();case 54:return e.next=56,r.GET_CUSTOMER_LIST_ACTION();case 56:case 57:return e.abrupt("return",t);case 58:case"end":return e.stop()}}),e)})));return function(r,t){return e.apply(this,arguments)}}();var R={GET_TOKEN_ACTION:p.q,GET_TOKEN_ERROR_REMOVE_ACTION:p.r,GET_TOP_CUSTOMER_ACTION:p.s,GET_CUSTOMER_LIST_ACTION:p.e,GET_DEPOT_MONTH_ACTION:p.h,GET_DEPOT_LIST_ACTION:p.g,GET_PRODUCT_SERIES_ACTION:p.n,GET_PRODUCT_MONTH_ACTION:p.m,GET_PRODUCT_TOP_CUSTOMER_ACTION:p.o,GET_PRODUCT_LIST_ACTION:p.l,UPDATE_DASHBOARD_METRIC_ACTION:p.x,UPDATE_SELECTION_DATES_ACTION:p.O,UPDATE_CURRENCY_TYPE_ACTION:p.v,UPDATE_PRODUCT_MONTH_YEAR_ACTION:p.L,UPDATE_DEPOT_MONTH_MONTH_ACTION:p.D,UPDATE_DEPOT_MONTH_YEAR_ACTION:p.E,UPDATE_DEPOT_PRODUCT_MONTH_MONTH_ACTION:p.G,UPDATE_DEPOT_PRODUCT_MONTH_YEAR_ACTION:p.H,UPDATE_TOP_CUSTOMER_MONTH_ACTION:p.Q,UPDATE_TOP_CUSTOMER_PRODUCT_ACTION:p.R,UPDATE_TOP_CUSTOMER_YEAR_ACTION:p.S,UPDATE_DEPOT_CUSTOMER_MONTH_ACTION:p.A,UPDATE_DEPOT_CUSTOMER_YEAR_ACTION:p.B,UPDATE_SALES_DATE_ACTION:p.N,UPDATE_DEPOT_ACTION:p.y};r.default=Object(C.b)((function(e){return{token:e.auth_reducer.token,login_error:e.auth_reducer.login_error,depot_list:e.list_reducer.depot_list,product_list:e.list_reducer.product_list,customer_list:e.list_reducer.customer_list}}),R)(x)},76:function(e,r,t){"use strict";t.d(r,"a",(function(){return n})),t.d(r,"b",(function(){return a})),t.d(r,"c",(function(){return _}));var n=function(e,r){return e.setMonth(e.getMonth()+r),e},a=function(e){return"Million"===e?"m":"k"},_=function(e){return parseFloat(e.toString().match(/^-?\d+(?:\.\d{0,2})?/)[0])}}}]);
//# sourceMappingURL=13.138fc512.chunk.js.map