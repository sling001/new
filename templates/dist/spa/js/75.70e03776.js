(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[75],{"71a3":function(t,e,a){"use strict";a.r(e);var o=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("q-page",{staticClass:"flex flex-top"},[[a("div",{staticClass:"q-pa-md"},[a("div",{staticClass:"q-gutter-y-md",staticStyle:{"max-width":"100%"}},[a("q-tabs",{model:{value:t.detaillink,callback:function(e){t.detaillink=e},expression:"detaillink"}},[a("transition",{attrs:{appear:"","enter-active-class":"animated zoomIn"}},[a("q-route-tab",{directives:[{name:"show",rawName:"v-show",value:"Admin"!==t.$q.localStorage.getItem("staff_type")&&"Manager"!==t.$q.localStorage.getItem("staff_type")&&"Supervisor"!==t.$q.localStorage.getItem("staff_type")&&"Inbound"!==t.$q.localStorage.getItem("staff_type")&&"Outbound"!==t.$q.localStorage.getItem("staff_type")&&"StockControl"!==t.$q.localStorage.getItem("staff_type")&&"Customer"!==t.$q.localStorage.getItem("staff_type"),expression:"$q.localStorage.getItem('staff_type') !== 'Admin' &&\n                               $q.localStorage.getItem('staff_type') !== 'Manager' &&\n                               $q.localStorage.getItem('staff_type') !== 'Supervisor' &&\n                               $q.localStorage.getItem('staff_type') !== 'Inbound' &&\n                               $q.localStorage.getItem('staff_type') !== 'Outbound' &&\n                               $q.localStorage.getItem('staff_type') !== 'StockControl' &&\n                               $q.localStorage.getItem('staff_type') !== 'Customer'\n                              "}],attrs:{name:"supplierasnlist",label:t.$t("inbound.asn"),icon:"img:statics/inbound/asn.png",to:"/supplierasn/supplierasnlist",exact:""}})],1),a("transition",{attrs:{appear:"","enter-active-class":"animated zoomIn"}},[a("q-route-tab",{directives:[{name:"show",rawName:"v-show",value:"Admin"!==t.$q.localStorage.getItem("staff_type")&&"Manager"!==t.$q.localStorage.getItem("staff_type")&&"Supervisor"!==t.$q.localStorage.getItem("staff_type")&&"Inbound"!==t.$q.localStorage.getItem("staff_type")&&"Outbound"!==t.$q.localStorage.getItem("staff_type")&&"StockControl"!==t.$q.localStorage.getItem("staff_type")&&"Customer"!==t.$q.localStorage.getItem("staff_type"),expression:"$q.localStorage.getItem('staff_type') !== 'Admin' &&\n                               $q.localStorage.getItem('staff_type') !== 'Manager' &&\n                               $q.localStorage.getItem('staff_type') !== 'Supervisor' &&\n                               $q.localStorage.getItem('staff_type') !== 'Inbound' &&\n                               $q.localStorage.getItem('staff_type') !== 'Outbound' &&\n                               $q.localStorage.getItem('staff_type') !== 'StockControl' &&\n                               $q.localStorage.getItem('staff_type') !== 'Customer'\n                              "}],attrs:{name:"supplierasnfinish",label:t.$t("inbound.asnfinish"),icon:"img:statics/inbound/asnfinish.png",to:"/supplierasn/supplierasnfinish",exact:""}})],1)],1)],1)])],a("div",{staticClass:"main-table"},[a("router-view")],1)],2)},s=[],n={name:"Pageinbound",data(){return{detaillink:"asn"}},methods:{}},l=n,r=a("42e1"),i=a("9989"),g=a("429b"),f=a("7867"),p=a("eebe"),c=a.n(p),m=Object(r["a"])(l,o,s,!1,null,null,null);e["default"]=m.exports;c()(m,"components",{QPage:i["a"],QTabs:g["a"],QRouteTab:f["a"]})}}]);