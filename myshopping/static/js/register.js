$(function () {
    var error_pwd = false;
    var error_email = false;
    var error_phone = false;
    var error_checkpwd = false;
    $("#username").blur(function () {
        var len = $("#username").val().trim().length;
        if (len < 3 || len > 6) {
            $("#username").next().html("请输入3-6位长度的字符");
            return;
        }

        params = {"username":$("#username").val()};

        console.log(params);
        $.get("/user/check_name/",params,function (data) {
            console.log(data);
            if (data.msg1) {
                $("#username").next().html("用户名可用");

            }else {
                $("#username").next().html("用户名重复");
                $(".reg_form").prop("disabled", "disabled")
            }
        },"json")
    });

    $("#nickname").blur(function () {
        var len = $("#nickname").val().trim().length;
        if (len<=0) {
             $("#nickname").next().html("用户昵称不能为空");
             return;
        }

        params = {"nickname":$("#nickname").val()};

        console.log(params);

        $.get("/user/check_nickname/",params,function (data) {
            console.log(data);
            if (data.msg2) {
                $("#nickname").next().html("用户昵称可用");
            }
            else {
                $("#nickname").next().html("用户昵称重复");
                $(".reg_form").prop("disabled", "disabled")
            }
        },"json")
    });

    $("#password").blur(function () {
        check_password();
    });
    $("#confirmpwd").blur(function () {
        check_confirm_pwd();
    });
    $("#phone").blur(function () {
        check_phone();
    });
    $("#email").blur(function () {
        check_email();
    });

    function check_password() {
        var len = $("#password").val().trim().length;
        if (len<3){
            $("#password").next().html("密码不能小于三位");
            error_pwd = true;
        }
        else {
            $("#password").next().html("密码可用");
            error_pwd = false
        }
    }
    function check_confirm_pwd() {
        var pwd_ = $("#password").val().trim();
        var cpwd_ = $("#confirmpwd").val().trim();
        if(pwd_ != cpwd_) {
            $("#confirmpwd").next().html("两次密码输入不一致");
            $(".reg_form").prop("disabled", "disabled");
            error_checkpwd = true;
        }
        else {
            $("#confirmpwd").next().html("密码设置成功");
            $(".reg_form").removeAttr("disabled");
            error_checkpwd = false;
        }
    }
    function check_email() {
        var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
        if(re.test($('#email').val().trim()))
		{
			$('#email').next().html("邮箱可用");
			$(".change").removeAttr("disabled");
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确');
			$(".change").prop("disabled", "disabled");
			error_email = true;
		}
    }

    function check_phone() {
        var re = /^1[356789]\d{9}$/;
        if (re.test($("#phone").val().trim())){
			$('#phone').next().html("手机号可用");
			$(".change").removeAttr("disabled");
			error_phone = false;
        }
        else {
            $('#phone').next().html("手机号不存在");
            $(".change").prop("disabled", "disabled");
			error_phone = false;
        }
    }

    // $('#reg_form').submit(function() {
	// 	check_username();
	// 	check_nickname();
	// 	check_password();
	// 	check_confirm_pwd();
	// 	check_email();
	// 	check_phone();
    //
	// 	if(error_name == false && error_pwd == false && error_checkpwd == false && error_email == false && error_nickname == false && error_phone == false)
	// 	{
	// 		return true;
	// 	}
	// 	else
	// 	{
	// 		return false;
	// 	}

	// });
});