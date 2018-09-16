/*************************************************************************/
/*******************       用户登录界面             ****************************/
/*************************************************************************/

$(function(){
	
	//是否记住密码选项
	$("#chooseRemind").on("click",function(){
		if($(this).hasClass("selected")){
			$(this).removeClass("selected");
			$(this).addClass("not_selected"); //此时不选中
		}else{
			$(this).removeClass("not_selected");//此时选中
			$(this).addClass("selected");
		}
	});
	
	/*登录框的提示部分*/
	
	//第一步，验证用户名
	var btn1=false;
	var btn2=false;
	var btn3=false;
	function userName(){
		$("#userAccount").siblings().remove("label");
		var $useraccount  = $("#userAccount").val();
		var $email        = /^([\.a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/;
		var $pattern      = /1[3|5|7|8|][0-9]{9}/;
		var $errorname    = $("<label>");
		$("#userAccount").after($errorname );
		if($useraccount==""){
			$errorname.html("请输入已验证的手机号或邮箱");
			btn1=false;
		}else if(!($pattern.test($useraccount)||$email.test($useraccount))){
			$errorname.html("请输入正确的手机号或邮箱");
			btn1=false;
		}else if(($pattern.test($useraccount)||$email.test($useraccount))){
			$("#userAccount").siblings().remove("label");
			btn1=true;
		}
	}
	
	$(".login_bar input").slice(0,3).blur(function(){
		userName();
	});
	
	function number1(){                   //为提交表单的验证错误信息做准备
		userName();
	}
	
	
	//第二步   密码不为空
	
	function passWord(){
		$("#password").siblings().remove("label");
		var $passWord   = $("#password").val();
		var $errorpw  = $("<label>");
		$("#password").after($errorpw );
		if($passWord==""){
			$errorpw.html("请输入密码");
			btn2=false;
		}else if($passWord!=""){
			$("#password").siblings().remove("label");
			btn2=true;
		}
	}
	
	$(".login_bar input").slice(1,3).blur(function(){
		if(btn1){
			passWord();
		}	
	});
	
	function number2(){
		if(btn1){
			passWord();
		}
	}
	//  第三步，生成并验证  验证码
	rdmNum();
	function rdmNum(){
		var a=Math.floor((Math.random())*10);
		var b=Math.floor((Math.random())*10);
		var c=Math.floor((Math.random())*10);
		var d=Math.floor((Math.random())*10);
		var $ramNum =(""+a+b+c+d);
		$("#rdm a").html($ramNum);
	}
	
	$("#rdm a").on("click",function(){
		rdmNum();
	});
	
	function randomNum(){
		$("#randomImg").siblings().remove("label");
		var $rpassword   = $("#randomImg").val();
		var $errorname  = $("<label>");
		$("#rdm").after($errorname );
		if($rpassword==""){                         //图片验证码的校验
			$errorname.html("请输入验证码");
			btn3=false;
		}else if($rpassword!=$("#rdm a").html()){
			$errorname.html("请输入正确的验证码");
			btn3=false;
		}
		else if($rpassword==$("#rdm a").html()){
			$("#randomImg").siblings().remove("label");
			btn3=true;
		}
	}
	
	$(".login_bar input").slice(2,3).blur(function(){
		if(btn1&&btn2){
			randomNum();
		}
	});
	function number3(){
		if(btn1&&btn2){
			randomNum();
		}
	}
	
	
	//第四步，登录魅力惠
	
	$("#visited").on("click",function(){
		if(btn1&&btn2&&btn3){
			if($("#chooseRemind").hasClass("selected")){
				setCookie({
					key   : "user",
					value :  $("#userAccount").val()+"||"+$("#password").val(),
					day   : 7,
					path  :"/"
				});
			}else if($("#chooseRemind").hasClass("not_selected")){//移出用户信息
			
				removeCookie("user","/");
			}
			alert("登录成功");
			return false;
		}else{
			number1();
			number2();
			number3();
			return false;
		}
	});
	
	
	//自动登录 用户
	var $info  =  getCookie("user");
	if($info){
		var $arrinfo  = $info.split("||");
		$("#userAccount").val($arrinfo[0]);
		$("#password").val($arrinfo[1]);
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
})
