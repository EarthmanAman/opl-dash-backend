(this.webpackJsonpopl_frontend=this.webpackJsonpopl_frontend||[]).push([[11],{1:function(t,e,n){"use strict";n.d(e,"o",(function(){return r})),n.d(e,"p",(function(){return u})),n.d(e,"q",(function(){return o})),n.d(e,"X",(function(){return a})),n.d(e,"r",(function(){return c})),n.d(e,"Q",(function(){return _})),n.d(e,"c",(function(){return d})),n.d(e,"I",(function(){return s})),n.d(e,"s",(function(){return i})),n.d(e,"U",(function(){return p})),n.d(e,"K",(function(){return T})),n.d(e,"b",(function(){return l})),n.d(e,"a",(function(){return E})),n.d(e,"t",(function(){return O})),n.d(e,"e",(function(){return f})),n.d(e,"f",(function(){return P})),n.d(e,"B",(function(){return D})),n.d(e,"g",(function(){return y})),n.d(e,"E",(function(){return U})),n.d(e,"i",(function(){return j})),n.d(e,"H",(function(){return b})),n.d(e,"h",(function(){return R})),n.d(e,"d",(function(){return h})),n.d(e,"y",(function(){return m})),n.d(e,"l",(function(){return S})),n.d(e,"N",(function(){return A})),n.d(e,"k",(function(){return C})),n.d(e,"L",(function(){return M})),n.d(e,"m",(function(){return x})),n.d(e,"j",(function(){return g})),n.d(e,"n",(function(){return G})),n.d(e,"J",(function(){return v})),n.d(e,"V",(function(){return L})),n.d(e,"W",(function(){return N})),n.d(e,"P",(function(){return I})),n.d(e,"w",(function(){return H})),n.d(e,"M",(function(){return k})),n.d(e,"u",(function(){return w})),n.d(e,"D",(function(){return F})),n.d(e,"C",(function(){return K})),n.d(e,"G",(function(){return Y})),n.d(e,"F",(function(){return z})),n.d(e,"x",(function(){return B})),n.d(e,"T",(function(){return J})),n.d(e,"R",(function(){return X})),n.d(e,"S",(function(){return V})),n.d(e,"A",(function(){return q})),n.d(e,"z",(function(){return Q})),n.d(e,"O",(function(){return W})),n.d(e,"v",(function(){return Z}));var r="GET_TOKEN",u="GET_TOKEN_ERROR",o="GET_TOKEN_ERROR_REMOVE",a="USER_LOGGED_OUT",c="GET_TOP_CUSTOMER",_="UPDATE_TOP_CUSTOMER",d="GET_CUSTOMER_LIST",s="UPDATE_GET_CUSTOMER_LIST",i="GET_TRUCK_LIST",p="GET_TRUCK_LIST",T="UPDATE_GET_TRUCK_LIST",l="GET_CUSTOMER_DETAIL",E="ADD_CUSTOMER",O="TRUCK_CREATE",f="GET_DEPOT_LIST",P="GET_DEPOT_MONTH",D="UPDATE_DEPOT_MONTH",y="GET_DEPOT_PRODUCT_MONTH",U="UPDATE_DEPOT_PRODUCT_MONTH",j="GET_DEPOT_SERIES",b="UPDATE_DEPOT_SERIES",R="GET_DEPOT_PRODUCT_SERIES",h="GET_DEPOT_CUSTOMER",m="UPDATE_DEPOT_CUSTOMER",S="GET_PRODUCT_SERIES",A="UPDATE_PRODUCT_SERIES",C="GET_PRODUCT_MONTH",M="UPDATE_PRODUCT_MONTH",x="GET_PRODUCT_TOP_CUSTOMER",g="GET_PRODUCT_LIST",G="GET_SALES_LIST",v="UPDATE_GET_SALES_LIST",L="UPLOAD_EXCEL",N="UPLOAD_EXCEL_ERROR",I="UPDATE_SELECTION_DATES",H="UPDATE_DASHBOARD_METRIC",k="UPDATE_PRODUCT_MONTH_YEAR",w="UPDATE_CURRENCY_TYPE",F="UPDATE_DEPOT_MONTH_YEAR",K="UPDATE_DEPOT_MONTH_MONTH",Y="UPDATE_DEPOT_PRODUCT_MONTH_YEAR",z="UPDATE_DEPOT_PRODUCT_MONTH_MONTH",B="UPDATE_DEPOT",J="UPDATE_TOP_CUSTOMER_YEAR",X="UPDATE_TOP_CUSTOMER_MONTH",V="UPDATE_TOP_CUSTOMER_PRODUCT",q="UPDATE_DEPOT_CUSTOMER_YEAR",Q="UPDATE_DEPOT_CUSTOMER_MONTH",W="UPDATE_SALES_DATE",Z="UPDATE_CUSTOMER_YEAR"},26:function(t,e,n){"use strict";var r=n(12),u=n(13),o=n(14),a=n(15),c=n(0),_=n.n(c),d=n(30),s=n(3),i=function(t){Object(o.a)(n,t);var e=Object(a.a)(n);function n(){return Object(r.a)(this,n),e.apply(this,arguments)}return Object(u.a)(n,[{key:"render",value:function(){return Object(s.jsx)("div",{className:"spinner",children:Object(s.jsx)(d.a,{ariaLabel:"Please wait as we log you in ...",color:"#00BFFF",height:100,width:100,timeout:4e3,visible:this.props.spinner})})}}]),n}(_.a.Component);e.a=i},33:function(t,e,n){"use strict";n.d(e,"a",(function(){return D}));var r=n(8),u=n(23),o=n(41),a=n(17),c=n.n(a),_=n(1),d=function(t,e){return Object.assign({},t,e)},s=function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},e=arguments.length>1?arguments[1]:void 0;switch(e.type){case _.o:return d(t,{token:e.payload,login_error:null});case _.p:case _.q:return d(t,{login_error:e.payload});default:return t}},i=function(t,e){return Object.assign({},t,e)},p=function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},e=arguments.length>1?arguments[1]:void 0;switch(e.type){case _.r:return i(t,{top_customer:e.payload,update_top_customer:!1});case _.Q:return i(t,{update_top_customer:e.payload});case _.c:case _.I:return i(t,{customer_list:e.payload,update_get_truck_list:!1});case _.s:return i(t,{truck_list:e.payload,update_get_truck_list:!1});case _.t:return i(t,{truck_create:e.payload});case _.U:return i(t,{truck_list:e.payload,update_get_truck_list:!1});case _.K:return i(t,{update_get_truck_list:!0});case _.b:return i(t,{customer_detail:e.payload});case _.e:return i(t,{depot_list:e.payload});case _.f:return i(t,{depot_month:e.payload,update_depot_month:!1});case _.B:return i(t,{update_depot_month:!0});case _.h:return i(t,{depot_product_series:e.payload,update_product_series:!1});case _.d:return i(t,{depot_customer:e.payload,update_depot_customer:!1});case _.y:return i(t,{update_depot_customer:!0});case _.g:return i(t,{depot_product_month:e.payload,update_depot_product_month:!1});case _.E:return i(t,{update_depot_product_month:!0});case _.i:return i(t,{depot_series:e.payload,update_product_series:!1,update_depot_series:!1});case _.H:return i(t,{update_depot_series:!0});case _.l:return i(t,{product_series:e.payload,update_product_series:!1});case _.N:return i(t,{update_product_series:!0});case _.k:return i(t,{product_month:e.payload,update_product_month:!1});case _.L:return i(t,{update_product_month:!0});case _.m:return i(t,{product_top_customer:e.payload,update_top_customer:!1});case _.j:return i(t,{product_list:e.payload});case _.n:return i(t,{sales_list:e.payload,update_get_sales_list:!1});case _.J:return i(t,{update_get_sales_list:!0});default:return t}},T=function(t,e){return Object.assign({},t,e)},l=function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},e=arguments.length>1?arguments[1]:void 0;switch(e.type){case _.a:return T(t,{add_customer:e.payload});case _.w:return T(t,{dashboard_metric:e.payload});case _.v:return T(t,{customer_year:e.payload});case _.P:return T(t,{selection_dates:e.payload});case _.u:return T(t,{currency_type:e.payload});case _.M:return T(t,{product_month_year:e.payload});case _.C:return T(t,{depot_month_month:e.payload});case _.D:return T(t,{depot_month_year:e.payload});case _.G:return T(t,{depot_product_month_year:e.payload});case _.F:return T(t,{depot_product_month_month:e.payload});case _.x:return T(t,{depot:e.payload});case _.z:return T(t,{depot_customer_month:e.payload});case _.A:return T(t,{depot_customer_year:e.payload});case _.R:return T(t,{top_customer_month:e.payload});case _.T:return T(t,{top_customer_year:e.payload});case _.S:return T(t,{top_customer_product:e.payload});case _.O:return T(t,{sales_date:e.payload});case _.V:return T(t,{uploaded_excel:e.payload,upload_excel_error:null});case _.W:return T(t,{upload_excel_error:e.payload});default:return t}},E=Object(r.b)({auth_reducer:s,list_reducer:p,update_reducer:l}),O=function(t,e){return e.type===_.X&&(c.a.removeItem("persist:root"),t=void 0),E(t,e)},f={key:"root",storage:c.a},P=Object(u.a)(f,O),D=Object(r.c)(P,Object(r.a)(o.a));Object(u.b)(D)},48:function(t,e,n){},58:function(t,e,n){},59:function(t,e,n){"use strict";n.r(e);var r=n(0),u=n.n(r),o=n(34),a=n.n(o),c=(n(48),n(25)),_=n(12),d=n(13),s=n(14),i=n(15),p=n(29),T=n(2),l=n(26),E=n(3),O=Object(r.lazy)((function(){return Promise.all([n.e(0),n.e(1),n.e(16)]).then(n.bind(null,427))})),f=Object(r.lazy)((function(){return Promise.all([n.e(0),n.e(5),n.e(1),n.e(19)]).then(n.bind(null,430))})),P=Object(r.lazy)((function(){return Promise.all([n.e(0),n.e(5),n.e(1),n.e(18)]).then(n.bind(null,431))})),D=Object(r.lazy)((function(){return Promise.all([n.e(0),n.e(5),n.e(1),n.e(28)]).then(n.bind(null,432))})),y=Object(r.lazy)((function(){return Promise.all([n.e(0),n.e(5),n.e(1),n.e(17)]).then(n.bind(null,433))})),U=function(t){Object(s.a)(n,t);var e=Object(i.a)(n);function n(){return Object(_.a)(this,n),e.apply(this,arguments)}return Object(d.a)(n,[{key:"render",value:function(){return Object(E.jsx)(p.a,{children:Object(E.jsx)(r.Suspense,{fallback:Object(E.jsx)(l.a,{spinner:!0}),children:Object(E.jsxs)(T.d,{children:[Object(E.jsx)(T.b,{path:"/login",exact:!0,element:Object(E.jsx)(O,{})}),Object(E.jsx)(T.b,{path:"/",exact:!0,element:Object(E.jsx)(f,{})}),Object(E.jsx)(T.b,{path:"/sale",exact:!0,element:Object(E.jsx)(D,{})}),Object(E.jsx)(T.b,{path:"/depots",exact:!0,element:Object(E.jsx)(P,{})}),Object(E.jsx)(T.b,{path:"/customers",exact:!0,element:Object(E.jsx)(y,{})})]})})})}}]),n}(u.a.Component),j=U,b=n(33);n(58);var R=function(){return Object(E.jsx)(c.a,{store:b.a,children:Object(E.jsx)(j,{})})},h=function(t){t&&t instanceof Function&&n.e(34).then(n.bind(null,434)).then((function(e){var n=e.getCLS,r=e.getFID,u=e.getFCP,o=e.getLCP,a=e.getTTFB;n(t),r(t),u(t),o(t),a(t)}))};a.a.createRoot(document.getElementById("root")).render(Object(E.jsx)(u.a.StrictMode,{children:Object(E.jsx)(R,{})})),h()}},[[59,12,13]]]);
//# sourceMappingURL=main.3d7ba472.chunk.js.map