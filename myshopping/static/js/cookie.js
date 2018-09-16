// 封装添加/修改cookie的函数
function setCookie(oParam) {
	var
		name  = oParam.key,
		value = oParam.value,
		iDay  = oParam.day,
		path  = oParam.path;

	if(!name) {
		console.error('您必须要传入cookie的key！');
		return false;
	}
	var oDate = new Date();
	oDate.setDate(oDate.getDate() + iDay);
	document.cookie = name + '=' + encodeURIComponent(value) + ';expires= ' + oDate + ' ;path=' + path;
}
// 封装获取cookie的函数
function getCookie(key) {
	var aCookie = document.cookie.split('; ');
	for(var i= 0; i < aCookie.length; i++) {
		var aTemp = aCookie[i].split('=');
		if(aTemp[0] === key) {
			return decodeURIComponent(aTemp[1]);
		}
	}
}
// 删除cookie的函数
function removeCookie(key, path) {
	setCookie({key: key, value: '', day: -1, path: path});
}



