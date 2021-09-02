/**
 * 均衡调度JS
 *
 */

var flag = 0;
var dayTime= $("#endTime2").val();
var xiaoquname1 = "";
var city1 = "";
var xiaoquname2 = "";
var city2 = "";
var blanceId="";
var changjia = "";
var functid = "";
var day= $("#day").val();
var day1= $("#day1").val();
var city3 = "";

layui.config({
	//自定义模块存放的目录
	base: '/carrier/js/'
}).use('mymode',function(){

	var mymode = layui.mymode;
	mymode.tabSwitch();

    getPage("spotList","totalPage","currentpage","fenye");
    getPage("spotList","totalPage2","currentpage2","fenye2");
    getValue();
  	spotList(currentpage);
});

function getValue() {
	if(flag==0) {
		dayTime=$("#endTime2").val();
    	xiaoquname2 = $("#xiaoquname2").val();
    	city2 = $("#city2").val();
    	changjia = $("#changjia2").val();
    	functid = $("#functid2").val();
	}
	if(flag==1) {
    	city1 = $("#city1").val();
        xiaoquname1 = $("#xiaoquname1").val();
        blanceId=$("#blanceId").val();
        day= $("#day").val();
	}
	if (flag==2) {
		day1= $("#day1").val();
		city3 = $("#city3").val();
	}

}

function search(currentpage) {
	getValue();
	spotList(currentpage);
}

function spotList(currentpage){
    var json={};
    //实时负荷均衡
    if(flag==0){
    	json = {"pagesize":pagesize,"page":currentpage,"dayTime":dayTime,"xiaoquname":xiaoquname2,
    			"city":city2,"changjia":changjia,"functid":functid};
        $.ajax({
		  url: "./sameCover/interface/getLoadbalanceResult",
		  type:"post",
		  data:json,
		  dataType:"json",
		  async: false,
		  timeout:10000,
		  beforeSend:function(){
	        index = layer.load(1, {
	            shade: [0.1,'#000000'], //0.1透明度
	            offset:'300px'
	        });
		  },
		  complete: function () {
			layer.close(index);
		  },
		  success: function (data) {
			  var dataVal = data.value;
			  var html = "";
		      var statue = "";
		  	  for(var i=0; i < dataVal.length; i++){

			  	  html += "<tr style='text-align:left'>";
			  	  html += "<td >"+dataVal[i].changjia+"</td>";
			  	  html += "<td >"+dataVal[i].city+"</td>";
			  	  html += "<td >"+dataVal[i].functid+"</td>";
				  html += "<td title="+dataVal[i].xiaoqu_z+"><a href='javascript:void(0);' style='text-decoration : none;color: #009FD7;' data-toggle='modal' data-target='#myModal' onclick='queryByName(\""+dataVal[i].xiaoqu_z+"\",\""+ dataVal[i].updatetime+"\",\""+ dataVal[i].changjia+"\")' >"+dataVal[i].xiaoqu_z+"</a></td>";
			  	  html += "<td >"+dataVal[i].updatetime+"</td>";
			  	  html += "<td >"+dataVal[i].countday+"</td>";

			  	  var tim = dataVal[i].updatetime;
		   	 	  var arr1 = tim.split(" ");
		   	 	  var date1 = arr1[0];
		   	 	  var date2 = dataVal[i].day;
		   	 	  var count = ((date1.replace("-","").replace("-",""))-date2)+1;

			  	  html += "<td >"+dataVal[i].countback+"</td>";
			  	  html += "<td >"+dataVal[i].use_rate_z+"</td>";

			  	  if(dataVal[i].use_rate_z_t==null){
			  	  	html += "<td nowrap='nowrap'>"+"待评估"+"</td></tr>";
			  	  }else{
			  	  	html += "<td nowrap='nowrap'>"+dataVal[i].use_rate_z_t+"</td></tr>";
			  	  }

		      }
		      document.getElementById("totalPage2").innerHTML=data.total;
		      if(currentpage==1){
		   		document.getElementById("currentpage2").innerHTML=1;
		   	  }
		  	  $("#xiaoquList2").html(html);
		 },
		 error:function(data,textStatus){
		      layer.closeAll('loading');
		      if(textStatus=="timeout"){
                     layer.alert("加载超时，请重试",{icon: 5,offset:'300px'});
             }else{
		      		  layer.alert("系统异常，获取同覆盖数据失败！",{icon: 5,offset: "200px"});
		      }
		 }
	  });
    }

    //同覆盖均衡
    if(flag==1){
        json = {"pagesize":pagesize,"page":currentpage,
        "dayTime":day,"flag":null,"xiaoquname":xiaoquname1,
        "city":city1,"blanceId":blanceId,"changjia":null};
        $.ajax({
		  url: "./sameCover/interface/getSameCoverXiaoqu",
		  type:"post",
		  data:json,
		  dataType:"json",
		  async: false,
		  timeout:10000,
		  beforeSend:function(){
	        index = layer.load(1, {
	            shade: [0.1,'#000000'], //0.1透明度
	            offset:'300px'
	        });
		  },
		  complete: function () {
			layer.close(index);
		  },
		  success: function (data) {
			  var dataVal = data.value;
			  var html = "";
		      var statue = "";
		  	  for(var i=0; i < dataVal.length; i++){
			  	  html += "<tr style='text-align:left'>";
			  	  html += "<td>"+dataVal[i].city+"</td>";

			  	  html += "<td title="+dataVal[i].xiaoqu_z+"><a style='text-decoration : none;' href='javascript:void(0);' onclick='copyContent(this)'>"+dataVal[i].xiaoqu_z+"</a></td>";
			  	  html += "<td title="+dataVal[i].xiaoqu_sc+"><a style='text-decoration : none;' href='javascript:void(0);' onclick='copyContent(this)'>"+dataVal[i].xiaoqu_sc+"</a></td>";

			  	  html += "<td>"+dataVal[i].configure+"</td>";

			  	  html += "<td>"+trim(dataVal[i].use_rate_z)+"</td>";
				  html += "<td>"+trim(dataVal[i].use_rate_sc)+"</td>";

			  	  if(dataVal[i].isbalanced==1){
			  	  	html += "<td>"+"均衡"+"</td>";
			  	  }else if(dataVal[i].isbalanced==2){
			  	  	html += "<td>"+"不均衡"+"</td>";
			  	  }else{
			  	  	html += "<td>"+""+"</td>";
			  	  }

			  	  html += "<td title="+trim(dataVal[i].condit)+">"+trim(dataVal[i].condit)+"</td>";

                 html+="<td class='td-manage'><a class='btn btn-info btn-xs' onclick='query(\""+dataVal[i].xiaoqu_sc+"\",\""+dataVal[i].xiaoqu_z+"\",\""+dataVal[i].updatetime+"\",\""+dataVal[i].cgi_z+"\",\""+dataVal[i].cgi_sc+"\",\""+dataVal[i].changjias+"\")'>详情</a> <a class='btn btn-info btn-xs' onclick='queryHis(\""+dataVal[i].xiaoqu_sc+"\",\""+dataVal[i].xiaoqu_z+"\",\""+dataVal[i].updatetime+"\")'>归档</a></td></tr>";
		      }
		  	document.getElementById("totalPage").innerHTML=data.total;
		  	if(currentpage==1){
		   		document.getElementById("currentpage").innerHTML=1;
		   	 }
		  	  $("#xiaoquList").html(html);
		 },
		 error:function(data,textStatus) {
		     layer.closeAll('loading');
		     if (textStatus=="timeout") {
                 layer.alert("加载超时，请重试",{icon: 5,offset:'300px'});
             } else {
		      	layer.alert("系统异常，获取同覆盖数据失败！",{icon: 5,offset: "200px"});
		      }
		 }
	  });
    }

    if (flag==2) {

    	//实时负荷均衡
    	var countlogs = 0;
		var countxiaoqu = 0;
		var countadjust = 0;
		var countback = 0;
		var countsuccesslogs = 0;
		var countlimit = 0;
		var countyx = 0;
		console.log(path+"/sameCover/interface/countBalances");
    	$.ajax({
  		  url:path+"/sameCover/interface/countBalances",
  		  type:"post",
  		  data:{"day":day1,"city":city3},
  		  dataType:"json",
  		  async: false,
  		  success: function (data) {
  			  var dataVal = data.SamecoverDataCount;
  			  var dataValy = data.LoadbalanceDataCount_Y;//昨日实时负荷

  			  var unbalances = 0;
  			  var adjusteds = 0;
  			  var finished = 0;
  			  var alllogs = 0;
  			  var successlogs = 0;
  			  var unbalances_1 = 0;
  			  var samecoverxiaoqus = 0;
  			  var unbalances_one = 0;
  			  var samecoverxiaoqus_one = 0;
  			  var countyx_1 = 0;

  			  var unbalances_y = 0;
  			  var adjusteds_y = 0;
  			  var finished_y = 0;
  			  var alllogs_y = 0;
  			  var successlogs_y = 0;
  			  var unbalances_1_y = 0;
  			  var samecoverxiaoqus_y = 0;
  			  var unbalances_one_y = 0;
  			  var samecoverxiaoqus_one_y = 0;

  			  var beforeDay = getBeforeDay(day1);
  			  var unbalances_1_b = 0;

  			  if (dataVal != null && dataVal.length > 0) {
  				  for (var i=0; i < dataVal.length; i++) {
  					  if (dataVal[i].updatetime==day1) {
  						  unbalances += dataVal[i].unbalances;
  						  adjusteds += dataVal[i].adjusteds;
  						  finished += dataVal[i].finished;
  						  unbalances_1 += dataVal[i].unbalances_1;
  						  alllogs += dataVal[i].alllogs;
  						  successlogs += dataVal[i].successlogs;
  						  samecoverxiaoqus += dataVal[i].samecoverxiaoqus;
  						  unbalances_one += dataVal[i].unbalances_one;
  						  samecoverxiaoqus_one += dataVal[i].samecoverxiaoqus_one;
  						  countyx_1 += dataVal[i].countyx_1;
  					  } else if(dataVal[i].updatetime==beforeDay){
  						  unbalances_y += dataVal[i].unbalances;
						  adjusteds_y += dataVal[i].adjusteds;
						  finished_y += dataVal[i].finished;
						  unbalances_1_y += dataVal[i].unbalances_1;
						  alllogs_y += dataVal[i].alllogs;
						  successlogs_y += dataVal[i].successlogs;
						  samecoverxiaoqus_y += dataVal[i].samecoverxiaoqus;
						  unbalances_one_y += dataVal[i].unbalances_one;
						  samecoverxiaoqus_one_y += dataVal[i].samecoverxiaoqus_one;
  					  }else{
  						  unbalances_1_b += dataVal[i].unbalances_1
  					  }

  				  }
  			  }

  			  $("#unbalances").text(unbalances_one);
  			  if(samecoverxiaoqus_one==null || samecoverxiaoqus_one==0){
				  $("#zhanbi").text("0.00%");
			  }else{
				  $("#zhanbi").text((unbalances_one/samecoverxiaoqus_one * 100).toFixed(2)+ "%");
			  }

  			// 垂直面均衡优化
  			  $("#adjusteds").text(adjusteds);
  			  if(unbalances == 0){
  				  $("#unbalancesRate").text("0.00%");
  			  } else {
  				  $("#unbalancesRate").text((adjusteds/unbalances * 100).toFixed(2)+ "%");
  			  }

  			  /*if (unbalances_y == 0){
				  $("#unbalancesRate_y").text("0.00%");
			  } else {
				  $("#unbalancesRate_y").text((adjusteds_y/unbalances_y * 100).toFixed(2)+ "%");
			  }*/

  			  // 有效率
  			 var balancesRate_yx_y = countyx_1 / unbalances_1;
  			 if(unbalances_1 ==0 || countyx_1 == 0){
				  $("#balancesRate_yx_y").text("0.00%");
			  } else {
				  $("#balancesRate_yx_y").text((balancesRate_yx_y*100).toFixed(2)  + "%");
			  }

  			  /*闭环率*/
  			  var finishedRate = finished / unbalances_1_y;
  			  $("#finisheds").text(finished);
  			  if(unbalances_1_y ==0 || finished == 0){
  				  $("#finishedRate").text("0.00%");
  			  } else {
  				  $("#finishedRate").text((finishedRate*100).toFixed(2)  + "%");
  			  }

  			  var finishedRate_y = finished_y / unbalances_1_b;
			  $("#finisheds_y").text(finished_y);
			  if(unbalances_1_b ==0 || finished_y == 0){
				  $("#finishedRate_y").text("0.00%");
			  } else {
				  $("#finishedRate_y").text((finishedRate_y*100).toFixed(2)  + "%");
			  }

  			  //工参同覆盖统计
  			  $("#unbalances_y").text(unbalances_one_y);
  			  $("#adjusteds_y").text(adjusteds_y);

  			  $("#alllogs").text(alllogs);
  			  var daylogs_successRate = successlogs / alllogs;
  			  if(successlogs ==0 || alllogs == 0){
				  $("#daylogs_successRate").text("0.00%");
			  } else {
				  $("#daylogs_successRate").text((daylogs_successRate*100).toFixed(2)  + "%");
			  }

  			  $("#alllogs_y").text(alllogs_y);
  			  var daylogs_successRate_y = successlogs_y / alllogs_y;
  			  if(successlogs_y ==0 || alllogs_y == 0){
				  $("#daylogs_successRate_y").text("0.00%");
			  } else {
				  $("#daylogs_successRate_y").text((daylogs_successRate_y*100).toFixed(2)  + "%");
			  }

  			  //昨日实时负荷均衡
  			  var countlogs_y = 0;
  			  var countxiaoqu_y = 0;
  			  var countadjust_y = 0;
  			  var countback_y = 0;
  			  var countsuccesslogs_y = 0;
  			  var countlimit_y = 0;
  			  var countyx_y = 0;

  			  if (dataValy != null && dataValy.length > 0) {
	  				for (var i=0; i < dataValy.length; i++) {
	  					if (dataValy[i].updatetime==day1) {
	  						countlogs += dataValy[i].countlogs;
	  	  				  	countxiaoqu += dataValy[i].countxiaoqu;
	  	  				  	countadjust += dataValy[i].countadjust;
	  	  				  	countback += dataValy[i].countback;
	  	  				  	countsuccesslogs += dataValy[i].countsuccesslogs;
	  	  				  	countlimit += dataValy[i].countlimit;
	  	  				  	countyx += dataValy[i].countyx;
	  					} else {
	  						countlogs_y += dataValy[i].countlogs;
	  	  				  	countxiaoqu_y += dataValy[i].countxiaoqu;
	  	  				  	countadjust_y += dataValy[i].countadjust;
	  	  				  	countback_y += dataValy[i].countback;
	  	  				  	countsuccesslogs_y += dataValy[i].countsuccesslogs;
	  	  				  	countlimit_y += dataValy[i].countlimit;
	  	  				  	countyx_y += dataValy[i].countyx;
	  					}

	  				}


  				  $("#countxiaoqu_y").text(countxiaoqu_y);
  				  $("#countadjust_y").text(countadjust_y);

  				  $("#countback_y").text(countback_y);
  				  var countbackRate_y = countback_y / countadjust_y;
	    			  if(countback_y ==0 || countadjust_y == 0){
	  				  $("#countbackRate_y").text("0.00%");
	  			  } else {
	  				  $("#countbackRate_y").text((countbackRate_y*100).toFixed(2)  + "%");
	  			  }

    			  $("#countyx_y").text(countyx_y);
	    		  var countyxRate_y = countyx_y / countxiaoqu_y;
    			  if(countyx_y ==0 || countxiaoqu_y == 0){
    				  $("#countyxRate_y").text("0.00%");
	  			  } else {
	  				  $("#countyxRate_y").text((countyxRate_y*100).toFixed(2)  + "%");
	  			  }

    			  $("#countlogs_y").text(countlogs_y);
    			  var reallogs_successRate_y = countsuccesslogs_y / countlogs_y;
    			  if(countsuccesslogs_y ==0 || countlogs_y == 0){
    				  $("#reallogs_successRate_y").text("0.00%");
	  			  } else {
	  				  $("#reallogs_successRate_y").text((reallogs_successRate_y*100).toFixed(2)  + "%");
	  			  }

  			  } else {
  				  $("#countlogs_y").text("0");
  				  $("#countxiaoqu_y").text("0");
  				  $("#countback_y").text("0");
  				  $("#countbackRate_y").text("0");
  				  $("#countadjust_y").text("0");
  			  }

  		  },
  		  error: function (res) {

  		  }

    	});

    	if (today == day1) {
    		$.ajax({
    			url: path+"/sameCover/interface/loadbalanceDataCount",
    			type:"post",
    			data:{"city":city3},
    			dataType:"json",
    			async: false,
    			success: function (data) {
    				var dataVal1 = data.LoadbalanceDataCount;
    				if (dataVal1.length>0) {
    					for (var i=0; i < dataVal1.length; i++) {
    						countlogs += dataVal1[i].countlogs;
    						countxiaoqu += dataVal1[i].countxiaoqu;
    						countadjust += dataVal1[i].countadjust;
    						countback += dataVal1[i].countback;
    						countsuccesslogs += dataVal1[i].countsuccesslogs;
    						countlimit += dataVal1[i].countlimit;
    						countyx += dataVal1[i].countyx;
    					}
    				}

    			},
    			error: function (res) {

    			}

    		});

    	}

    	//水平面均衡优化
		$("#countxiaoqu").text(countxiaoqu);

		// 均衡执行情况
		$("#countadjust").text(countadjust);
		$("#countback").text(countback);
		var countbackRate = countback / countadjust;
		if(countback ==0 || countadjust == 0){
			$("#countbackRate").text("0.00%");
		} else {
			$("#countbackRate").text((countbackRate*100).toFixed(2)  + "%");
		}

		$("#countyx").text(countyx);
		var countyxRate = countyx / countxiaoqu;
		if(countyx ==0 || countxiaoqu == 0){
			$("#countyxRate").text("0.00%");
		} else {
			$("#countyxRate").text((countyxRate*100).toFixed(2)  + "%");
		}

		$("#countlogs").text(countlogs);
		var reallogs_successRate = countsuccesslogs / countlogs;
		if(countsuccesslogs ==0 || countlogs == 0){
			$("#reallogs_successRate").text("0.00%");
		} else {
			$("#reallogs_successRate").text((reallogs_successRate*100).toFixed(2)  + "%");
		}

	}

};

//导出
function exportXiaoqu(flag) {

	getValue();

  //同覆盖导出
  if(flag==1){
  	    window.location.href = "./sameCover/interface/exportSameCoverXiaoqu?dayTime="
  	    +dayTime + "&flag="+null + "&xiaoquname="+xiaoquname1+ "&blanceId="+blanceId + "&city="+city1;
   }

   //实时负荷工单导出
   if(flag==0){
  	    window.location.href = "./sameCover/interface/exportLoadXiaoqu?day="
  	    +dayTime + "&city="+city2 + "&xiaoqu_z="+xiaoquname2+ "&changjia="+changjia ;
   }

}

function import_bmd(flag) {
	var uploadFile = "";
	if(flag ==0){
		uploadFile = document.getElementById("uploadFile1").value;
	}else{
		uploadFile = document.getElementById("uploadFile2").value;
	}
	if (uploadFile == null || uploadFile == "") {
		alert("请选择要上传的Excel文件");
		return false;
	}
	var fileExtend = uploadFile.substring(uploadFile.lastIndexOf('.')).toLowerCase();
	if (fileExtend == ".xls" || fileExtend == ".xlsx") {
		saveRro(flag);
	}else{
		alert("文件格式需为'.xls' 或 '.xlsx'格式");
		return false;
	}
}

function saveRro(flag) {
  if(flag==0){
	$("#form1").ajaxSubmit(function(data) {
	// 对表单进行提交后进行的操作，相当于ajax提交表单的success
		if(data=="success"){
			layer.msg("导入成功！",{icon: 1});
		}else if(data=="false"){
			layer.msg("您没有导入任何数据！",{icon: 1});
		}else{
			layer.msg("导入失败，请联系管理员！",{icon: 5});
		}
	});
	$("#sure1").attr("data-dismiss","modal");
  }
  else{
	$("#form2").ajaxSubmit(function(data) {
	// 对表单进行提交后进行的操作，相当于ajax提交表单的success
		if(data=="success"){
			layer.msg("导入成功！",{icon: 1});
		}else if(data=="false"){
			layer.msg("您没有导入任何数据！",{icon: 1});
		}else{
			layer.msg("导入失败，请联系管理员！",{icon: 5});
		}
	});
	$("#sure2").attr("data-dismiss","modal");
  }
	return false; // 返回false，阻止跳转
}

function queryByName(xiaoquname,updatetime,changjia){
	sessionStorage.setItem('changjia',changjia);
	sessionStorage.setItem('xiaoquname',xiaoquname);
	sessionStorage.setItem('updatetime',updatetime);
	sessionStorage.setItem('xiaoqu_l','');
	x_admin_show('优化日志',path+'/view/scheduleva/opt_log.jsp');
}

 //查询日志
 function query(xiaoqu_sc,xiaoqu_z,updatetime,cgi1,cgi2,changjia) {
	 sessionStorage.setItem('xiaoqu_sc',xiaoqu_sc);
	 sessionStorage.setItem('xiaoqu_z',xiaoqu_z);
	 sessionStorage.setItem('updatetime',updatetime);
	 sessionStorage.setItem('cgi1',cgi1);
	 sessionStorage.setItem('cgi2',cgi2);
	 sessionStorage.setItem('changjia',changjia);
	 sessionStorage.setItem('flag','0');
	 if(changjia=='中兴-中兴'){
    	 x_admin_show('优化详情',path+'/view/scheduleva/dailyBalance_log.jsp');
	 } else if(changjia=='华为-华为'){
    	 x_admin_show('优化详情',path+'/view/scheduleva/dailyBalance_log_hw.jsp');
	 } else if(changjia=='爱立信-爱立信'){
    	 x_admin_show('优化详情',path+'/view/scheduleva/dailyBalance_log_ericsson.jsp');
	 } else if(changjia=='诺西-诺西'){
    	 x_admin_show('优化详情',path+'/view/scheduleva/dailyBalance_log_nokia.jsp');
	 } else {
		 x_admin_show('优化详情',path+'/view/scheduleva/dailyBalance_log_other.jsp');
	 }
 }

 //查询流程参数
 function queryHis(xiaoqu_sc,xiaoqu_z,updatetime){
 	sessionStorage.setItem('xiaoqu_sc',xiaoqu_sc);
 	sessionStorage.setItem('xiaoqu_z',xiaoqu_z);
 	sessionStorage.setItem('updatetime',updatetime);
 	x_admin_show('日志归档',path+'/view/scheduleva/dailyBalance_guidang.jsp');
 }

 function getSameCoverXiaoquOne(){
 	x_admin_show('同覆盖扇区',path+'/view/scheduleva/same_cover_xiaoqu_one.jsp');
 }

 function getLog(){
	x_admin_show('同覆盖均衡日志',path+'/view/scheduleva/dailyBalance_allLog.jsp');
 }

 function getLoadLog(){
	x_admin_show('负荷均衡日志',path+'/view/scheduleva/loadLog_guidang.jsp');
 }

 function getLoadXiaoquOne() {
	 	x_admin_show('负荷均衡邻区对',path+'/view/scheduleva/load_xiaoqu_one.jsp');
	 }

 function onMouseOver1(){
	layer.tips("同覆盖小区定义：<br/>两小区经纬度距离差在50米以内，方向角差值在±15°之内（从方位角0度开始顺时针"
			+ "选择第一个小区，若同时存在多个小区，则根据F1→F2→D1→D2→D3→FDD900→FDD1800，"
			+ "从优先级自高到低依次作为基准小区，其余小区若方位角与该小区差距在15度以内，则纳入第一个同覆盖扇区；"
			+ "随后顺时针选择第二个小区，若已有同覆盖扇区，则不再考虑，否则作为第二个基准小区，以此类推）；" ,'#notes1', {
	  tips: [2, '#3595CC'],
	  time: 0,
	  area: ['33%','23%']
	});
 }

 function onMouseOver2(){
	layer.tips("不均衡判定规则：<br/>将同覆盖小区划分为D频段、F频段、D/F、TDD/FDD1800频段组，若该频段组不均衡，则该扇区不均衡；<br/>"
			+ "（1）D频段内：利用率最高小区无线利用率超过50%，且与最低的小区之间差值超过20%时，不均衡；<br/>"
			+ "（2）F频段内：利用高最高小区无线利用率超过50%，且F1高出F2超30%或F2高出F1超10%，不均衡；<br/>"
			+ "（3）D/F：D或F频段的利用率超50%，且差值超过20%，不均衡；<br/>"
			+ "（4）TDD/FDD1800：FDD1800小区利用率超70%或TDD小区利用率超50%，且FDD高出TDD超20%或TDD高出FDD，不均衡；" ,'#notes2', {
	  tips: [2, '#3595CC'],
	  time: 0,
	  area: ['37%','27%']
	});
 }

 function onMouseOut(){
	layer.closeAll();
 }

 function getNowFormatDate(t) {
    var date = new Date();
    var seperator1 = "-";
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var strDate = date.getDate()-t;
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
    }
    var currentdate = year + seperator1 + month + seperator1 + strDate;
    return currentdate;
}

 function exportSameCoverXiaoqu() {
	xiaoquname1 = $("#xiaoquname1").val();
	city1 = $("#city1").val();
	blanceId= $("#blanceId").val();
	day= $("#day").val();
    window.location.href = "./sameCover/interface/exportSameCoverXiaoqu?xiaoqu_z="+xiaoquname1+ "&isbalanced="+blanceId + "&city="+city1 + "&day="+day;
 }
 //获取到指定一天的前一天
 function getBeforeDay(day){
     var yesterday=new Date();
     yesterday.setTime(new Date(day).getTime()-1000*60*60*24)
     var strYear=yesterday.getFullYear();
     var strDay=yesterday.getDate();
     var strMonth=yesterday.getMonth()+1;
     if(strMonth<10){
         strMonth="0"+strMonth;
      }
     if(strDay<10){
    	 strDay="0"+strDay;
     }
     var strYesterday=strYear+"-"+strMonth+"-"+strDay;
     return strYesterday;

 }
