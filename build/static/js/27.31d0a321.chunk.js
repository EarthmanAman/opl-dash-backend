(this.webpackJsonpopl_frontend=this.webpackJsonpopl_frontend||[]).push([[27,29],{169:function(e,t,r){"use strict";r.r(t);var s=r(62),n=r(12),a=r(13),c=r(14),o=r(15),l=r(63),i=r.n(l),u=r(0),d=r.n(u),p=r(132),j=r(25),b=r(84),m=r(140),h=r(191),_=r(133),O=r(429),x=(r(186),r(187),r(188),r(68)),f=r(435),v=r(436),C=r(97),S=r(266),g=r(26),T=(r(189),r(3)),y=function(e){Object(c.a)(r,e);var t=Object(o.a)(r);function r(){var e;Object(n.a)(this,r);for(var a=arguments.length,c=new Array(a),o=0;o<a;o++)c[o]=arguments[o];return(e=t.call.apply(t,[this].concat(c))).state={product:null,customer:null,truck:null,entry_no:null,order_no:null,lpo_no:null,depot:null,date:new Date,vol_obs:null,vol_20:null,selling_price:null,products:[],paid:!0,loading_date:null,amount_paid:null,seal_no:null,remarks:null,trucks:[],spinner:!1,success:!1,null_error:!1,show_error:!1,submit:!1},e.componentWillReceiveProps=function(){var t=Object(s.a)(i.a.mark((function t(r){return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:null!==r.sales_create_error?e.setState({spinner:!1,show_error:!0}):e.setState({spinner:!1,success:!0});case 1:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e.handleCustomerSelect=function(t){var r=e.props.customers[parseInt(t)];e.setState({customer:r.id,trucks:r.trucks})},e.onSubmit=function(){var t=Object(s.a)(i.a.mark((function t(r){var s,n,a,c,o,l,u,d,p,j,b,m,h,_,O,x,f,v,C,S,g;return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:for(r.preventDefault(),s=e.state,n=s.product,a=s.lpo_no,c=s.customer,o=s.truck,l=s.depot,u=s.entry_no,d=s.order_no,p=s.date,j=s.vol_obs,b=s.vol_20,m=s.selling_price,h=s.paid,_=s.loading_date,O=s.seal_no,x=s.amount_paid,f=s.remarks,v=[n,c,o,l,d,p,j,m],C=!1,S=0;S<v.length;S++)null!==v[S]&&""!==v[S]&&void 0!==v[S]||(C=!0);if(!C){t.next=9;break}e.setState({null_error:!0}),t.next=13;break;case 9:return e.setState({spinner:!0,submit:!0}),g=e.props.sales_date,t.next=13,e.props.SALES_CREATE_ACTION(g.start_date,g.end_date,n,a,c,o,l,u,d,p,j,b,m,h,_,O,x,f);case 13:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e}return Object(a.a)(r,[{key:"render",value:function(){var e=this,t=this.state,r=t.date,s=t.loading_date,n=t.trucks,a=this.props,c=a.depots,o=a.customers,l=a.products;return n=n.concat(this.props.truck_list),Object(T.jsxs)("div",{className:"upload-form",children:[this.state.spinner?Object(T.jsx)(g.a,{spinner:this.state.spinner}):null,Object(T.jsx)("h4",{className:"upload-title",children:"Fill the information"}),Object(T.jsx)("p",{style:{color:"brown",fontSize:12},children:"All field mark with * must be filled"}),this.state.success&&this.state.submit?Object(T.jsx)(f.a,{variant:"success",size:"sm",children:"Entry Created successful"}):null,this.state.null_error?Object(T.jsx)(f.a,{variant:"danger",size:"sm",children:"All the fields must be field"}):null,this.state.show_error?Object(T.jsx)(f.a,{variant:"danger",size:"sm",children:this.props.sales_create_error}):null,Object(T.jsxs)(v.a,{onSubmit:this.onSubmit,children:[Object(T.jsxs)(C.a,{style:{marginTop:0,height:"auto"},children:[Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsxs)(v.a.Label,{children:["Date ",Object(T.jsx)("span",{style:{color:"brown"},children:"*"})]}),Object(T.jsx)(v.a.Control,{type:"date",placeholder:"Date",size:"sm",value:r,onChange:function(t){return e.setState({date:t.target.value,submit:!1})}})]})}),Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Loading Date"}),Object(T.jsx)(v.a.Control,{type:"date",placeholder:"Date",size:"sm",value:s,onChange:function(t){return e.setState({submit:!1,loading_date:t.target.value})}})]})})]}),Object(T.jsxs)(C.a,{style:{marginTop:0,height:"auto"},children:[Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsxs)(v.a.Label,{children:["Depot ",Object(T.jsx)("span",{style:{color:"brown"},children:"*"})]}),Object(T.jsxs)(v.a.Select,{"aria-label":"Default select example",size:"sm",onChange:function(t){return e.setState({submit:!1,depot:t.target.value})},children:[Object(T.jsx)("option",{children:"Select"}),c.map((function(e,t){return Object(T.jsx)("option",{value:e.id,children:e.name})}))]})]})}),Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsxs)(v.a.Label,{children:["Customer ",Object(T.jsx)("span",{style:{color:"brown"},children:"*"})]}),Object(T.jsxs)(v.a.Select,{"aria-label":"Default select example",size:"sm",onChange:function(t){return e.handleCustomerSelect(t.target.value)},children:[Object(T.jsx)("option",{children:"Select"}),o.map((function(e,t){return Object(T.jsx)("option",{value:t,children:e.name})}))]})]})}),Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsxs)(v.a.Label,{children:["Truck ",Object(T.jsx)("span",{style:{color:"brown"},children:"*"})]}),Object(T.jsxs)(v.a.Select,{"aria-label":"Default select example",size:"sm",onChange:function(t){return e.setState({truck:t.target.value})},children:[Object(T.jsx)("option",{children:"Select"}),n.map((function(e){return Object(T.jsxs)("option",{value:e.id,children:[e.plate_no," - ",e.driver]})}))]})]})})]}),Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsxs)(v.a.Label,{children:["Product ",Object(T.jsx)("span",{style:{color:"brown"},children:"*"})]}),Object(T.jsxs)(v.a.Select,{"aria-label":"Default select example",size:"sm",onChange:function(t){return e.setState({product:t.target.value})},children:[Object(T.jsx)("option",{children:"Select"}),l.map((function(e){return Object(T.jsx)("option",{value:e.id,children:e.name})}))]})]}),Object(T.jsx)("h6",{className:"upload-form__details",children:"Details"}),Object(T.jsxs)(C.a,{style:{marginTop:0,height:"auto"},children:[Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsxs)(v.a.Label,{children:["Order No ",Object(T.jsx)("span",{style:{color:"brown"},children:"*"})]}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Order No",size:"sm",onChange:function(t){return e.setState({show_error:!1,order_no:t.target.value})}})]})}),Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Lpo no"}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Lpo no",size:"sm",onChange:function(t){return e.setState({lpo_no:t.target.value})}})]})})]}),Object(T.jsxs)(C.a,{style:{marginTop:0,height:"auto"},children:[Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Entry no"}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Entry No",size:"sm",onChange:function(t){return e.setState({entry_no:t.target.value})}})]})}),Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Seal no"}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Seal no",size:"sm",onChange:function(t){return e.setState({seal_no:t.target.value})}})]})})]}),Object(T.jsxs)(C.a,{style:{marginTop:0,height:"auto"},children:[Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsxs)(v.a.Label,{children:["Vol OBS ",Object(T.jsx)("span",{style:{color:"brown"},children:"*"})]}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Vol OBS",size:"sm",onChange:function(t){return e.setState({vol_obs:t.target.value})}})]})}),Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Vol@20"}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Vol@20",size:"sm",onChange:function(t){return e.setState({vol_20:t.target.value})}})]})})]}),Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsxs)(v.a.Label,{children:["Selling Price ",Object(T.jsx)("span",{style:{color:"brown"},children:"*"})]}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Selling price",size:"sm",onChange:function(t){return e.setState({selling_price:t.target.value})}})]}),Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Amount Paid"}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Amount Paid",size:"sm",onChange:function(t){return e.setState({amount_paid:t.target.value})}})]}),Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Paid"}),Object(T.jsxs)("div",{className:"mb-3",children:[Object(T.jsx)(v.a.Check,{inline:!0,label:"Yes",name:"group1",type:"radio",id:"inline-radio-1",onClick:function(){return e.setState({paid:!0})}}),Object(T.jsx)(v.a.Check,{inline:!0,label:"No",name:"group1",type:"radio",id:"inline-radio-2",onClick:function(){return e.setState({paid:!1})}})]},"inline-radio")]}),Object(T.jsxs)(v.a.Group,{className:"mb-3",controlId:"exampleForm.ControlTextarea1",children:[Object(T.jsx)(v.a.Label,{children:"Remarks"}),Object(T.jsx)(v.a.Control,{as:"textarea",rows:3,onChange:function(t){return e.setState({remarks:t.target.value})}})]}),Object(T.jsx)("div",{align:"center",children:Object(T.jsx)(O.a,{variant:"primary",type:"submit",children:"Upload"})})]})]})}}]),r}(d.a.Component),D={SALES_CREATE_ACTION:x.u},I=Object(j.b)((function(e){return{depots:e.list_reducer.depot_list?e.list_reducer.depot_list:[],products:e.list_reducer.product_list?e.list_reducer.product_list:[],customers:e.list_reducer.customer_list?e.list_reducer.customer_list:[],truck_list:e.list_reducer.truck_list?e.list_reducer.truck_list:[],sales_list:e.list_reducer.sales_list?e.list_reducer.sales_list:[],sales_date:e.update_reducer.sales_date,sales_create_error:e.list_reducer.sales_create_error}}),D)(y),N=r(30),k=function(e){Object(c.a)(r,e);var t=Object(o.a)(r);function r(){var e;Object(n.a)(this,r);for(var a=arguments.length,c=new Array(a),o=0;o<a;o++)c[o]=arguments[o];return(e=t.call.apply(t,[this].concat(c))).state={name:"",location:"",spinner:!1,success:!1,null_error:!1,show_errors:!1,customer_list:e.props.customer_list},e.onSubmit=function(){var t=Object(s.a)(i.a.mark((function t(r){var s,n,a;return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(r.preventDefault(),s=e.state,n=s.name,a=s.location,""!==n&&""!==a){t.next=6;break}e.setState({null_error:!0}),t.next=9;break;case 6:return e.setState({spinner:!0}),t.next=9,e.props.CUSTOMER_CREATE_ACTION(n,a);case 9:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e}return Object(a.a)(r,[{key:"render",value:function(){var e=this;return Object(T.jsxs)("div",{className:"upload-form",children:[this.state.spinner?Object(T.jsx)("div",{className:"spinner",children:Object(T.jsx)(N.b,{color:"#00BFFF",height:100,width:100,timeout:4e3,visible:this.state.spinner})}):null,Object(T.jsx)("h4",{children:"Create Customer"}),this.state.success?Object(T.jsx)(f.a,{variant:"success",size:"sm",children:"Customer created successful"}):null,this.state.null_error?Object(T.jsx)(f.a,{variant:"danger",size:"sm",children:"The fields cannot be empty"}):null,Object(T.jsxs)(v.a,{onSubmit:this.onSubmit,id:"sub",children:[Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Customer name"}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Name",size:"sm",value:this.state.name,onChange:function(t){return e.setState({name:t.target.value,success:!1,null_error:!1,show_errors:!1})}})]}),Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Code"}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Name",size:"sm",value:this.state.location,onChange:function(t){return e.setState({location:t.target.value,success:!1,null_error:!1,show_errors:!1})}})]}),Object(T.jsx)("div",{children:Object(T.jsx)(O.a,{variant:"primary",type:"submit",size:"sm",id:"add_customer",children:"Create"})})]})]})}}]),r}(d.a.Component);k.getDerivedStateFromProps=function(){var e=Object(s.a)(i.a.mark((function e(t,r){return i.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(void 0!==t.customer_list){e.next=4;break}return e.abrupt("return",null);case 4:(void 0===r.customer_list&&void 0!==t.customer_list||t.customer_list.length>r.customer_list.length)&&(r.spinner=!1,r.success=!0,r.null_error=!1);case 5:return r.customer_list=t.customer_list,e.abrupt("return",r);case 7:case"end":return e.stop()}}),e)})));return function(t,r){return e.apply(this,arguments)}}();var w={CUSTOMER_CREATE_ACTION:x.c},E=Object(j.b)((function(e){return{customer_list:e.list_reducer.customer_list}}),w)(k),A=function(e){Object(c.a)(r,e);var t=Object(o.a)(r);function r(){var e;Object(n.a)(this,r);for(var a=arguments.length,c=new Array(a),o=0;o<a;o++)c[o]=arguments[o];return(e=t.call.apply(t,[this].concat(c))).state={customer:null,depot:null,spinner:!1,success:!1,null_error:!1,show_errors:!1},e.handleCustomerSelect=function(t){e.setState({customer:t})},e.handleDepotSelect=function(t){e.setState({depot:t})},e.onSubmit=function(){var t=Object(s.a)(i.a.mark((function t(r){var s,n,a;return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(r.preventDefault(),s=e.state,n=s.depot,a=s.customer,null!==n&&null!==a){t.next=6;break}e.setState({null_error:!0}),t.next=9;break;case 6:return e.setState({spinner:!0}),t.next=9,e.props.ADD_CUSTOMER_ACTION(n,a);case 9:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e.componentDidMount=Object(s.a)(i.a.mark((function t(){return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,e.props.ADD_CUSTOMER_REMOVE_ACTION();case 2:case"end":return t.stop()}}),t)}))),e}return Object(a.a)(r,[{key:"render",value:function(){var e=this;return Object(T.jsxs)("div",{className:"upload-form",children:[this.state.spinner?Object(T.jsx)("div",{className:"spinner",children:Object(T.jsx)(N.b,{color:"#00BFFF",height:100,width:100,timeout:4e3,visible:this.state.spinner})}):null,Object(T.jsx)("h4",{children:"Add Customer"}),this.state.success?Object(T.jsx)(f.a,{variant:"success",size:"sm",children:"Customer Added successfull"}):null,this.state.null_error?Object(T.jsx)(f.a,{variant:"danger",size:"sm",children:"The fields cannot be empty"}):null,this.state.show_errors?Object(T.jsx)(f.a,{variant:"danger",children:"Something went wrong!"}):null,Object(T.jsxs)(v.a,{onSubmit:this.onSubmit,id:"sub",children:[Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Depot"}),Object(T.jsxs)(v.a.Select,{"aria-label":"Default select example",size:"sm",onChange:function(t){return e.handleDepotSelect(t.target.value)},children:[Object(T.jsx)("option",{children:"Select"}),this.props.depots.map((function(e,t){return Object(T.jsx)("option",{value:e.id,children:e.name})}))]})]}),Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Customer"}),Object(T.jsxs)(v.a.Select,{"aria-label":"Default select example",size:"sm",onChange:function(t){return e.handleCustomerSelect(t.target.value)},children:[Object(T.jsx)("option",{children:"Select"}),this.props.customers.map((function(e,t){return Object(T.jsx)("option",{value:e.id,children:e.name})}))]})]}),Object(T.jsx)("div",{children:Object(T.jsx)(O.a,{variant:"primary",type:"submit",size:"sm",id:"add_customer",children:"Add"})})]})]})}}]),r}(d.a.Component);A.getDerivedStateFromProps=function(e,t){return void 0!==e.add_customer&&("success"===e.add_customer.status?(t.spinner=!1,t.success=!0,t.null_error=!1):(t.spinner=!1,t.show_errors=!0)),t};var z={ADD_CUSTOMER_ACTION:x.a,ADD_CUSTOMER_REMOVE_ACTION:x.b},R=(Object(j.b)((function(e){return{customers:e.list_reducer.customer_list,depots:e.list_reducer.depot_list,add_customer:e.update_reducer.add_customer}}),z)(A),function(e){Object(c.a)(r,e);var t=Object(o.a)(r);function r(){var e;Object(n.a)(this,r);for(var a=arguments.length,c=new Array(a),o=0;o<a;o++)c[o]=arguments[o];return(e=t.call.apply(t,[this].concat(c))).state={file:null,spinner:!1,success:!1,show_error:!1,null_error:!1,depot:null},e.componentWillReceiveProps=function(){var t=Object(s.a)(i.a.mark((function t(r){return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:r.upload_excel_error?e.setState({show_error:!0,spinner:!1}):e.setState({spinner:!1,success:!0});case 1:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e.onSubmit=function(){var t=Object(s.a)(i.a.mark((function t(r){var s,n,a;return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(r.preventDefault(),s=e.state,n=s.file,a=s.depot,null!==n&&null!==a){t.next=6;break}e.setState({null_error:!0}),t.next=9;break;case 6:return e.setState({spinner:!0}),t.next=9,e.props.UPLOAD_EXCEL_ACTION(n,a);case 9:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e}return Object(a.a)(r,[{key:"render",value:function(){var e=this;return Object(T.jsxs)("div",{className:"upload-form",children:[this.state.spinner?Object(T.jsx)("div",{className:"spinner",children:Object(T.jsx)(N.b,{color:"#00BFFF",height:100,width:100,timeout:4e3,visible:this.state.spinner})}):null,Object(T.jsx)("h5",{children:"Upload File"}),this.state.success?Object(T.jsx)(f.a,{variant:"success",size:"sm",children:"File Uploaded successful"}):null,this.state.show_error?Object(T.jsx)(f.a,{variant:"danger",size:"sm",children:this.props.upload_excel_error.message}):null,this.state.null_error?Object(T.jsx)(f.a,{variant:"danger",size:"sm",children:"All the field must be filled"}):null,Object(T.jsxs)(v.a,{onSubmit:this.onSubmit,children:[Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Depot"}),Object(T.jsxs)(v.a.Select,{"aria-label":"Default select example",size:"sm",onChange:function(t){return e.setState({depot:t.target.value})},children:[Object(T.jsx)("option",{children:"Select"}),this.props.depot_list.map((function(e){return Object(T.jsx)("option",{value:e.id,children:e.name})}))]})]}),Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"File"}),Object(T.jsx)(v.a.Control,{type:"file",accept:".xlsx, .xls, .csv",placeholder:"File",size:"sm",onChange:function(t){return e.setState({file:t.target.files[0]})}})]}),Object(T.jsx)("div",{children:Object(T.jsx)(O.a,{variant:"primary",type:"submit",value:this.state.file,size:"sm",children:"Upload"})})]})]})}}]),r}(d.a.Component)),F={UPLOAD_EXCEL_ACTION:x.X},L=Object(j.b)((function(e){return{uploaded_excel:e.update_reducer.uploaded_excel,upload_excel_error:e.update_reducer.upload_excel_error,depot_list:e.list_reducer.depot_list}}),F)(R),P=r(79),U=function(e){Object(c.a)(r,e);var t=Object(o.a)(r);function r(){var e;Object(n.a)(this,r);for(var a=arguments.length,c=new Array(a),o=0;o<a;o++)c[o]=arguments[o];return(e=t.call.apply(t,[this].concat(c))).state={depot:null},e.onSubmit=function(){var t=Object(s.a)(i.a.mark((function t(r){var s;return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:r.preventDefault(),s=e.state.depot,window.open("".concat(P.b,"/depot/download/").concat(parseInt(s),"/"),"_blank");case 3:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e}return Object(a.a)(r,[{key:"render",value:function(){var e=this;return Object(T.jsxs)("div",{className:"upload-form",children:[Object(T.jsx)("h4",{children:"Download Template"}),Object(T.jsxs)(v.a,{onSubmit:this.onSubmit,children:[Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Depot"}),Object(T.jsxs)(v.a.Select,{"aria-label":"Default select example",size:"sm",onChange:function(t){return e.setState({depot:t.target.value})},children:[Object(T.jsx)("option",{children:"Select"}),this.props.depot_list.map((function(e){return Object(T.jsx)("option",{value:e.id,children:e.name})}))]})]}),Object(T.jsx)("div",{children:Object(T.jsx)(O.a,{variant:"primary",type:"submit",size:"sm",children:"Download"})})]})]})}}]),r}(d.a.Component),G=Object(j.b)((function(e){return{depot_list:e.list_reducer.depot_list}}),{})(U),M=function(e){Object(c.a)(r,e);var t=Object(o.a)(r);function r(){var e;Object(n.a)(this,r);for(var a=arguments.length,c=new Array(a),o=0;o<a;o++)c[o]=arguments[o];return(e=t.call.apply(t,[this].concat(c))).state={customer:null,customers:[],customer_index:null,plate_no:"",first_name:"",last_name:"",spinner:!1,success:!1,null_error:!1,show_errors:!1,customer_list:e.props.customer_list,truck_list:e.props.truck_list},e.handleCustomerSelect=function(t){try{var r=e.props.customers[t];e.setState({customer:r.id,customer_index:t})}catch(s){e.setState({customer:null})}},e.onSubmit=function(){var t=Object(s.a)(i.a.mark((function t(r){var s,n,a,c,o;return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(r.preventDefault(),s=e.state,n=s.customer,a=s.plate_no,c=s.first_name,o=s.last_name,""!==a&&""!=c&&""!=o){t.next=6;break}e.setState({null_error:!0}),t.next=11;break;case 6:return e.setState({spinner:!0,success:!1}),t.next=9,e.props.UPDATE_GET_TRUCK_LIST_ACTION();case 9:return t.next=11,e.props.TRUCK_CREATE_ACTION(n,a,c,o);case 11:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e}return Object(a.a)(r,[{key:"componentDidMount",value:function(){this.setState({success:!1})}},{key:"render",value:function(){var e=this;return Object(T.jsxs)("div",{className:"upload-form",children:[this.state.spinner?Object(T.jsx)("div",{className:"spinner",children:Object(T.jsx)(N.b,{color:"#00BFFF",height:100,width:100,timeout:4e3,visible:this.state.spinner})}):null,Object(T.jsx)("h4",{children:"Add Truck"}),this.state.success?Object(T.jsx)(f.a,{variant:"success",size:"sm",children:"Truck created successful"}):null,this.state.null_error?Object(T.jsx)(f.a,{variant:"danger",size:"sm",children:"The fields cannot be empty"}):null,Object(T.jsxs)(v.a,{onSubmit:this.onSubmit,id:"sub",children:[Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Customer"}),Object(T.jsxs)(v.a.Select,{"aria-label":"Default select example",size:"sm",onChange:function(t){return e.handleCustomerSelect(t.target.value)},children:[Object(T.jsx)("option",{children:"Select"}),this.props.customers.map((function(e,t){return Object(T.jsx)("option",{value:t,children:e.name})}))]})]}),Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Plate No"}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Name",size:"sm",value:this.state.plate_no,onChange:function(t){return e.setState({plate_no:t.target.value,success:!1,null_error:!1,show_errors:!1})}})]}),Object(T.jsx)("h6",{className:"upload-form__details",children:"Driver"}),Object(T.jsxs)(C.a,{children:[Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"First Name"}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Name",size:"sm",value:this.state.first_name,onChange:function(t){return e.setState({first_name:t.target.value,success:!1,null_error:!1,show_errors:!1})}})]})}),Object(T.jsx)(S.a,{children:Object(T.jsxs)(v.a.Group,{className:"mb-2",controlId:"exampleForm.ControlInput1",children:[Object(T.jsx)(v.a.Label,{children:"Last Name"}),Object(T.jsx)(v.a.Control,{type:"text",placeholder:"Name",size:"sm",value:this.state.last_name,onChange:function(t){return e.setState({last_name:t.target.value,success:!1,null_error:!1,show_errors:!1})}})]})})]}),Object(T.jsx)("div",{children:Object(T.jsx)(O.a,{variant:"primary",type:"submit",size:"sm",id:"add_customer",children:"Add"})})]})]})}}]),r}(d.a.Component);M.getDerivedStateFromProps=function(){var e=Object(s.a)(i.a.mark((function e(t,r){var s;return i.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return console.log(t.truck_create),!1===t.update_get_truck_list&&(r.spinner=!1,r.null_error=!1,r.show_errors=!1),void 0!==t.truck_create&&null!==t.truck_create&&t.truck_create.plate_no===r.plate_no&&(console.log("in if"),r.success=!0,null!==r.customer_index?((s=t.customers)[parseInt(r.customer_index)].trucks=[t.truck_create].concat(s[parseInt(r.customer_index)].trucks),t.UPDATE_GET_CUSTOMER_LIST_ACTION(s)):t.UPDATE_TRUCK_LIST_ACTION([t.truck_create].concat(t.truck_list)),r.plate_no="",r.first_name="",r.last_name=""),r.customers=t.customers,r.truck_list=t.truck_list,e.abrupt("return",r);case 6:case"end":return e.stop()}}),e)})));return function(t,r){return e.apply(this,arguments)}}();var B={TRUCK_CREATE_ACTION:x.v,UPDATE_GET_TRUCK_LIST_ACTION:x.M,UPDATE_GET_CUSTOMER_LIST_ACTION:x.K,UPDATE_TRUCK_LIST_ACTION:x.W},K=Object(j.b)((function(e){return{customers:e.list_reducer.customer_list,truck_list:e.list_reducer.truck_list,update_get_truck_list:e.list_reducer.update_get_truck_list,truck_create:e.list_reducer.truck_create}}),B)(M),V=function(e){Object(c.a)(r,e);var t=Object(o.a)(r);function r(){var e;Object(n.a)(this,r);for(var a=arguments.length,c=new Array(a),o=0;o<a;o++)c[o]=arguments[o];return(e=t.call.apply(t,[this].concat(c))).state={startDate:e.props.selection_dates.startDate,endDate:e.props.selection_dates.endDate,dashboard_metric:e.props.dashboard_metric,key:"selection",add_order:!1},e.handleMetricChange=function(){var t=Object(s.a)(i.a.mark((function t(r){return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if("revenue"!==r){t.next=5;break}return t.next=3,e.props.UPDATE_DASHBOARD_METRIC_ACTION(!0);case 3:t.next=7;break;case 5:return t.next=7,e.props.UPDATE_DASHBOARD_METRIC_ACTION(!1);case 7:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e.handleSelect=function(){var t=Object(s.a)(i.a.mark((function t(r){var s;return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return s=e.props.depot_list[parseInt(e.props.depot)].id,e.setState({startDate:r.selection.startDate,endDate:r.selection.endDate}),t.next=4,e.props.UPDATE_SELECTION_DATES_ACTION({startDate:r.selection.startDate,endDate:r.selection.endDate});case 4:return t.next=6,e.props.GET_PRODUCT_SERIES_ACTION(r.selection.startDate,r.selection.endDate);case 6:return t.next=8,e.props.UPDATE_PRODUCT_SERIES_ACTION();case 8:return t.next=10,e.props.GET_DEPOT_SERIES_ACTION(s,r.selection.startDate,r.selection.endDate);case 10:return t.next=12,e.props.GET_DEPOT_PRODUCT_SERIES_ACTION(s,r.selection.startDate,r.selection.endDate);case 12:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e.close=function(){e.setState({add_order:!1})},e}return Object(a.a)(r,[{key:"render",value:function(){var e=this;return Object(T.jsxs)("div",{className:"buttons",children:[Object(T.jsx)(p.a,{trigger:Object(T.jsx)(O.a,{className:"input-dates",size:"sm",children:Object(T.jsxs)("div",{className:"input-dates__input-display",children:[Object(T.jsx)("span",{children:Object(T.jsx)(b.b,{color:"#D04D30",size:18})}),this.state.startDate.toDateString()," - ",this.state.endDate.toDateString(),Object(T.jsx)("span",{children:Object(T.jsx)(b.e,{size:18})})]})}),position:"bottom",children:Object(T.jsx)(_.DateRangePicker,{onChange:this.handleSelect,showSelectionPreview:!0,moveRangeOnFirstSelection:!1,months:2,ranges:[this.state],direction:"horizontal",preventSnapRefocus:!0,calendarFocus:"backwards",className:"input-date__date-range"})}),Object(T.jsxs)("div",{className:"metrics",children:[Object(T.jsxs)(O.a,{variant:this.state.dashboard_metric?"info":"secondary",size:"sm",className:"metrics__add-button",style:{color:"black"},onClick:function(){return e.handleMetricChange("revenue")},children:[Object(T.jsx)(h.a,{color:"green",size:20}),"Revenue"]}),Object(T.jsxs)(O.a,{variant:!1===this.state.dashboard_metric?"info":"secondary",size:"sm",className:"metrics__add-button",style:{color:"black"},onClick:function(){return e.handleMetricChange("quantities")},children:[Object(T.jsx)(b.g,{color:"orange",size:20}),"Quantities"]})]}),Object(T.jsxs)("div",{className:"form",children:[Object(T.jsx)(p.a,{contentStyle:{width:300},trigger:Object(T.jsxs)(O.a,{variant:"secondary",size:"sm",className:"form__add-button",style:{color:"black"},children:[Object(T.jsx)(b.c,{color:"green",size:20}),"Template"]}),position:"bottom",children:Object(T.jsx)(G,{})}),Object(T.jsx)(p.a,{contentStyle:{width:300},trigger:Object(T.jsxs)(O.a,{variant:"secondary",size:"sm",className:"form__add-button",style:{color:"black"},children:[Object(T.jsx)(m.a,{color:"green",size:20}),"Upload"]}),position:"bottom center",children:Object(T.jsx)(L,{})}),Object(T.jsx)(p.a,{contentStyle:{width:300},trigger:Object(T.jsxs)(O.a,{variant:"info",size:"sm",className:"form__add-button",children:[Object(T.jsx)(b.h,{color:"#e9e7ec",size:20}),"Customer"]}),position:"bottom center",children:Object(T.jsx)(E,{})}),Object(T.jsx)(p.a,{contentStyle:{width:300},trigger:Object(T.jsxs)(O.a,{variant:"info",size:"sm",className:"form__add-button",children:[Object(T.jsx)(b.h,{color:"#e9e7ec",size:20}),"Truck"]}),position:"bottom center",children:Object(T.jsx)(K,{})}),Object(T.jsx)(p.a,{contentStyle:{width:700,minHeight:400},trigger:Object(T.jsxs)(O.a,{variant:"primary",size:"sm",className:"form__add-button",onClick:function(){return e.setState({add_order:!0})},children:[Object(T.jsx)(b.h,{color:"#e9e7ec",size:20}),"Add Order"]}),position:"left top",open:this.state.add_order,children:Object(T.jsx)(I,{close:this.close})})]})]})}}],[{key:"getDerivedStateFromProps",value:function(e,t){var r=e.selection_dates,s=e.dashboard_metric;return r.startDate,t.startDate=new Date("".concat(r.startDate)),t.endDate=new Date("".concat(r.endDate)),t.dashboard_metric=s,t}}]),r}(d.a.Component),H={UPDATE_DASHBOARD_METRIC_ACTION:x.y,UPDATE_SELECTION_DATES_ACTION:x.R,GET_PRODUCT_SERIES_ACTION:x.n,GET_DEPOT_SERIES_ACTION:x.k,GET_DEPOT_PRODUCT_SERIES_ACTION:x.j,UPDATE_PRODUCT_SERIES_ACTION:x.P};t.default=Object(j.b)((function(e){return{selection_dates:e.update_reducer.selection_dates,dashboard_metric:e.update_reducer.dashboard_metric,depot:e.update_reducer.depot,depot_list:e.list_reducer.depot_list}}),H)(V)},97:function(e,t,r){"use strict";var s=r(18),n=r(69),a=r(65),c=r.n(a),o=r(0),l=r(71),i=r(3),u=["bsPrefix","className","as"],d=o.forwardRef((function(e,t){var r=e.bsPrefix,a=e.className,o=e.as,d=void 0===o?"div":o,p=Object(n.a)(e,u),j=Object(l.b)(r,"row"),b=Object(l.a)(),m="".concat(j,"-cols"),h=[];return b.forEach((function(e){var t,r=p[e];delete p[e],t=null!=r&&"object"===typeof r?r.cols:r;var s="xs"!==e?"-".concat(e):"";null!=t&&h.push("".concat(m).concat(s,"-").concat(t))})),Object(i.jsx)(d,Object(s.a)(Object(s.a)({ref:t},p),{},{className:c.a.apply(void 0,[a,j].concat(h))}))}));d.displayName="Row",t.a=d}}]);
//# sourceMappingURL=27.31d0a321.chunk.js.map